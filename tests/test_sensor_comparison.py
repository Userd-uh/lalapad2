import importlib.util
from pathlib import Path

ROOT = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location("gesture_analysis", ROOT / "tools/analyze_gesture_log.py")
analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analysis)


def frame(seq, t, count, saturation=False, snapshot=False):
    records = []
    if snapshot:
        records += [f"GCFG seq={seq} version=2 source=boot rc=0",
                    f"GCFGV seq={seq} settings=0x28 rx=12 tx=13 max=3 split=2 confidence=20",
                    f"GCFGF seq={seq} res=2457,3072 bottom=30 top=511 beta=20 stationary=5 jitter=2"]
    tp = 0x7f00 | count | (128 if saturation else 0)
    records += [f"GRAW seq={seq} info=0x0300 tp=0x{tp:04x}"]
    for i in range(1, 8):
        xy = f"{100*i},{200*i}" if i <= count else "65535,65535"
        records += [f"GF seq={seq} slot={i} xy={xy} strength=500 area={5 if i <= count else 0} confidence=1"]
    records += [f"GIN seq={seq} t={t} fc={count} f1v=1 f1=100,200 f2v=1 f2=200,400",
                f"GPRE seq={seq} a3=1 m3=0 last3=1 sum3=0,0",
                f"GSTEP seq={seq} step2=0,0 step3=0,0 a3=1 m3=0 last3=1 sum3=0,0",
                f"GOUT seq={seq} started=0 active=0 scroll=0,0 ended=0"]
    return "\n".join("[00:00:01] \x1b[0m<inf> iqs9151: " + r + "\x1b[0m" for r in records) + "\n"


def test_trials_time_weighting_release_and_distances():
    text = frame(1, 100, 3, snapshot=True) + frame(2, 120, 2, True) + frame(3, 150, 1) + frame(4, 160, 0)
    text += frame(5, 300, 3, snapshot=True) + frame(6, 330, 0)
    result = analysis.analyze(text)
    assert result["quality_issues"] == []
    assert result["completed_trials"] == 2
    trial = result["trials"][0]
    assert trial["fc3_frames"] == 1 and trial["contact_frames"] == 3
    assert trial["fc3_reported_time_ms_estimate"] == 20
    assert trial["duration_ms"] == 60
    assert trial["three_two_one_runs_including_release"] == 1
    assert trial["saturation_frames"] == 1
    assert trial["fc3_min_pair_distance_coordinate_units"]["frames"] == 1
    assert trial["contact_start_record_observed"]
    assert len(result["boot_snapshots"]) == 2  # GCFGF must not be parsed as GF!
    assert result["boot_snapshots"][0]["values"]["split"] == 2


def test_gap_or_incomplete_data_does_not_produce_ratios():
    for text in (frame(1, 10, 3) + frame(3, 30, 0),
                 frame(1, 10, 3).replace("GF seq=1 slot=7", "BROKEN seq=1 slot=7"),
                 frame(1, 10, 3) * 2, ""):
        result = analysis.analyze(text)
        assert result["quality_issues"]
        assert result["trials"] == []


def test_unreleased_contact_is_not_a_completed_trial():
    result = analysis.analyze(frame(1, 10, 3) + frame(2, 30, 2))
    assert result["completed_trials"] == 0
    assert not result["trials"][0]["full_release_observed"]


def test_no_mm_conversion_and_first_3s_time_is_clipped():
    result = analysis.analyze(frame(1, 0, 3) + frame(2, 4000, 1) + frame(3, 5000, 0))
    trial = result["trials"][0]
    assert trial["first_3s_fc3_time_fraction_estimate"] == 1
    assert trial["fc3_reported_time_fraction_estimate"] == .8
    assert "not mm" in result["caution"]


def test_variants_change_only_split_factor_and_remain_diagnostic_only():
    matrix = (ROOT / "build-diagnostics.yaml").read_text()
    assert matrix.count("shield: lalapadgen2_left rgbled_adapter") == 3
    assert "lalapadgen2_left-split-3-baseline" in matrix
    assert "diagnostic-split" not in (ROOT / "build.yaml").read_text()
    for value in (2, 4):
        config = ROOT / f"config/diagnostic-split-{value}.conf"
        active = [line for line in config.read_text().splitlines() if line and not line.startswith("#")]
        assert active == [f"CONFIG_INPUT_IQS9151_DIAGNOSTIC_SPLIT_FACTOR={value}"]
        assert f"lalapadgen2_left-split-{value}" in matrix


def test_inertia_diagnostic_build_is_left_split3_only():
    matrix = (ROOT / "build-inertia-diagnostics.yaml").read_text()
    assert matrix.count("shield:") == 1
    assert "shield: lalapadgen2_left rgbled_adapter" in matrix
    assert "artifact-name: lalapadgen2_left-split-3-inertia-diagnostics" in matrix
    assert "diagnostic-split-" not in matrix
    assert "config/gesture-diagnostics.conf" in matrix
    assert "inertia-diagnostics" not in (ROOT / "build.yaml").read_text()
