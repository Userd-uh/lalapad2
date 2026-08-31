"""Read-only diagnostic v2 metrics. Does not infer physical finger contact.

Usage: python tools/analyze_gesture_log.py capture.log
Time metrics hold the last reported state until the next frame; event mode and
physical placement/release mean these are estimates, not sensor accuracy scores.
"""
import argparse
import itertools
import json
import math
import re
import statistics
from pathlib import Path

ANSI = re.compile(r"\x1b\[[0-9;]*m")
RECORD = re.compile(r"\b(GRAW|GF|GIN|GPRE|GSTEP|GOUT|GCFG|GCFGV|GCFGF) seq=(\d+) (.*)")
FIELDS = re.compile(r"(\w+)=([^\s]+)")
EXPECTED = {"GRAW", "GIN", "GPRE", "GSTEP", "GOUT"} | {f"GF{i}" for i in range(1, 8)}


def fields(text):
    def value(s):
        if "," in s:
            return [value(x) for x in s.split(",")]
        try:
            return int(s, 16 if s.startswith("0x") else 10)
        except ValueError:
            return s
    return {k: value(v) for k, v in FIELDS.findall(text)}


def parse(text):
    frames, issues = {}, []
    for number, line in enumerate(text.splitlines(), 1):
        line = ANSI.sub("", line)
        match = RECORD.search(line)
        if not match:
            if re.search(r"\b(?:GIN|GF|GRAW) seq=|messages dropped", line):
                issues.append(f"unparsed/dropped record at line {number}")
            continue
        kind, seq, tail = match.groups()
        seq, data = int(seq), fields(tail)
        if kind == "GF":
            kind += str(data.get("slot", "?"))
        frame = frames.setdefault(seq, {"seq": seq, "line": number, "records": {}})
        if kind in frame["records"]:
            issues.append(f"duplicate {kind} seq={seq} (possible reset/concatenation)")
        frame["records"][kind] = data
    if not frames:
        issues.append("no diagnostic frames")
    previous = None
    for frame in frames.values():
        seq, records = frame["seq"], frame["records"]
        missing = EXPECTED - records.keys()
        if missing:
            issues.append(f"seq={seq} missing {','.join(sorted(missing))}")
        if not {"fc", "t"} <= records.get("GIN", {}).keys() or "tp" not in records.get("GRAW", {}):
            issues.append(f"seq={seq} malformed frame header")
            continue
        if records["GIN"]["fc"] != records["GRAW"]["tp"] & 15:
            issues.append(f"seq={seq} count/raw mismatch")
        for slot in range(1, 8):
            finger = records.get(f"GF{slot}", {})
            if not {"xy", "strength", "area", "confidence"} <= finger.keys():
                issues.append(f"seq={seq} malformed slot {slot}")
            elif finger["confidence"] != (records["GRAW"]["tp"] >> (7 + slot)) & 1:
                issues.append(f"seq={seq} confidence/raw mismatch slot {slot}")
        if previous:
            if seq != previous["seq"] + 1:
                issues.append(f"sequence gap {previous['seq']}->{seq}")
            if records["GIN"]["t"] < previous["records"]["GIN"]["t"]:
                issues.append(f"device clock reversed at seq={seq}")
        previous = frame
    return list(frames.values()), issues


def frame_count(frame):
    return frame["records"]["GIN"]["fc"]


def time_ms(frame):
    return frame["records"]["GIN"]["t"]


def summarize_trial(frames, index, ended):
    contact = [f for f in frames if frame_count(f) > 0]
    duration = time_ms(frames[-1]) - time_ms(frames[0])
    held_three = first_three_held = longest_three = current_three = 0
    first_window = min(3000, duration)
    for first, second in zip(frames, frames[1:]):
        dt = time_ms(second) - time_ms(first)
        if frame_count(first) == 3:
            held_three += dt
            current_three += dt
            longest_three = max(longest_three, current_three)
            first_three_held += max(0, min(time_ms(second), time_ms(frames[0]) + 3000) - time_ms(first))
        else:
            current_three = 0
    counts = [frame_count(f) for f in frames]
    runs = [key for key, _ in itertools.groupby(counts)]
    slots, distances = {}, []
    for slot in range(1, 8):
        active = [f["records"][f"GF{slot}"] for f in contact
                  if f["records"][f"GF{slot}"]["area"] > 0
                  and 65535 not in f["records"][f"GF{slot}"]["xy"]]
        if active:
            slots[str(slot)] = {
                "observed_frames": len(active),
                "area_min_max": [min(s["area"] for s in active), max(s["area"] for s in active)],
                "strength_min_max": [min(s["strength"] for s in active), max(s["strength"] for s in active)],
                "confidence_zero_frames": sum(s["confidence"] == 0 for s in active),
            }
    for frame in contact:
        positions = [frame["records"][f"GF{i}"]["xy"] for i in range(1, 8)
                     if frame["records"][f"GF{i}"]["area"] > 0
                     and 65535 not in frame["records"][f"GF{i}"]["xy"]]
        if frame_count(frame) == 3 and len(positions) == 3:
            distances.append(min(math.dist(a, b) for a, b in itertools.combinations(positions, 2)))
    return {
        "trial": index, "first_seq": frames[0]["seq"], "last_seq": frames[-1]["seq"],
        "contact_start_record_observed": "GCFG" in frames[0]["records"],
        "full_release_observed": ended, "duration_ms": duration,
        "contact_frames": len(contact), "fc3_frames": counts.count(3),
        "fc3_frame_fraction": counts.count(3) / len(contact),
        "fc3_reported_time_ms_estimate": held_three,
        "fc3_reported_time_fraction_estimate": held_three / duration if duration else None,
        "longest_fc3_ms_estimate": longest_three,
        "first_3s_fc3_time_fraction_estimate": first_three_held / first_window if first_window else None,
        "count_runs_including_release": runs,
        "three_two_one_runs_including_release": sum(runs[i:i+3] == [3, 2, 1] for i in range(len(runs)-2)),
        "saturation_frames": sum(bool(f["records"]["GRAW"]["tp"] & 128) for f in contact),
        "too_many_frames": sum(bool(f["records"]["GRAW"]["tp"] & 32) for f in contact),
        "slots": slots,
        "fc3_min_pair_distance_coordinate_units": {
            "frames": len(distances), "min": min(distances), "median": statistics.median(distances),
            "max": max(distances),
        } if distances else None,
    }


def analyze(text):
    frames, issues = parse(text)
    snapshots = [{"seq": f["seq"], **f["records"]["GCFG"],
                  "values": f["records"].get("GCFGV"), "filters": f["records"].get("GCFGF")}
                 for f in frames if "GCFG" in f["records"]]
    result = {"frames": len(frames), "quality_issues": issues, "boot_snapshots": snapshots, "trials": []}
    if issues:
        return result  # Never compute apparently precise ratios across missing records.
    current = []
    for frame in frames:
        if frame_count(frame) > 0 or current:
            current.append(frame)
        if frame_count(frame) == 0 and current:
            result["trials"].append(summarize_trial(current, len(result["trials"]) + 1, True))
            current = []
    if current:
        result["trials"].append(summarize_trial(current, len(result["trials"]) + 1, False))
    result["completed_trials"] = sum(t["full_release_observed"] for t in result["trials"])
    result["caution"] = "Contact phases inferred from sensor count, not physical contact. Placement/release included; time is last-state-hold estimate. First 3s is not independently verified stationary. Distances are coordinate units, not mm."
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.log.read_text(encoding="utf-8-sig")), ensure_ascii=False, indent=2))
