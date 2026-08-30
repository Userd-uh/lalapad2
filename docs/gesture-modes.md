# 2F / 3F gesture modes (Issue #3)

Each half has four independent build-time settings in its `.conf`:
`CONFIG_INPUT_IQS9151_{2,3}F_{HORIZONTAL,VERTICAL}_MODE`.
Values: `0 = Disabled`, `1 = Scroll`, `2 = Action`.

The editor saves these settings with **Save All**. Rebuild and flash both
halves to apply mode changes. Mode settings are not transferred by Studio RPC,
NVS runtime configuration, or split setting synchronization.

Action bindings use the normal Studio keymap RPC after upgrading the firmware.
2F and 3F bindings are independent for each direction, side, and layer.
The old 68 positions retain their indices; 8 new 3F positions are appended:

| Gesture | Left | Right |
| --- | --- | --- |
| 2F right / left / up / down | 58 / 59 / 60 / 61 | 63 / 64 / 65 / 66 |
| 3F right / left / up / down | 68 / 69 / 70 / 71 | 72 / 73 / 74 / 75 |

New 3F defaults copy the previous directional bindings, including mouse-layer
bindings. Tap and pinch positions are unchanged. 3F Scroll sends direct relative
wheel events; 2F smoothing/inertia integration is intentionally not included.

## Upgrade and verification

1. Before flashing, load/export the current MCU keymap and back up local config.
2. Save the desired modes and bindings, then build this firmware with the pinned
   driver revision. Flash the matching left and right builds.
3. Reconnect and load from MCU. Confirm 76 positions per layer before writing
   Action changes by RPC. The editor refuses a 76-position write to old firmware.
4. Existing Studio-saved settings may override compiled defaults. Inspect the
   loaded bindings and restore the intended mappings from your backup as needed.
   Do not reset stored settings automatically; a reset can discard other settings.
5. On real hardware, check each side, both finger counts, both axes, and all three
   modes. Confirm Action occurs once, Scroll is continuous, and Disabled emits
   no directional event. Check staged 3→2→1→0 release, tap, pinch, pointer, and
   2F scroll/inertia for regressions. Physical feel and sensor behavior remain
   hardware acceptance checks, not claims established by a successful build.
