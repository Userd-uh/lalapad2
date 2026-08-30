from pathlib import Path
import re


CONFIG_PATH = Path(__file__).parents[1] / "config" / "lalapadgen2.conf"
RIGHT_CONFIG_PATH = Path(__file__).parents[1] / "config" / "boards" / "shields" / "lalapadgen2" / "lalapadgen2_right.conf"
BUILD_PATH = Path(__file__).parents[1] / "build.yaml"
WEST_PATH = Path(__file__).parents[1] / "config" / "west.yml"
KEYMAP_PATH = Path(__file__).parents[1] / "config" / "lalapadgen2.keymap"
DEBUG_DRIVER_REVISION = "ea0b07b9e85319bb1461545ab3d8cacda9d7c5a5"


def test_two_finger_horizontal_navigation_is_enabled_without_hwheel():
    config_lines = set()
    for path in (CONFIG_PATH, RIGHT_CONFIG_PATH):
        config_lines.update(
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )

    assert "CONFIG_INPUT_IQS9151_2F_HORIZONTAL_NAV=y" in config_lines
    assert "CONFIG_INPUT_IQS9151_SCROLL_X_ENABLE=n" in config_lines
    assert "CONFIG_INPUT_IQS9151_2F_NAV_SWIPE_THRESHOLD=200" in config_lines
    assert "CONFIG_INPUT_IQS9151_2F_HORIZONTAL_NAV=n" not in config_lines
    assert "CONFIG_INPUT_IQS9151_SCROLL_X_ENABLE=y" not in config_lines


def test_right_firmware_exposes_two_finger_navigation_debug_logs():
    config = RIGHT_CONFIG_PATH.read_text(encoding="utf-8")
    build = BUILD_PATH.read_text(encoding="utf-8")
    west = WEST_PATH.read_text(encoding="utf-8")

    assert "CONFIG_ZMK_USB_LOGGING=y" in config
    assert "CONFIG_INPUT_LOG_LEVEL_DBG=y" in config
    assert "CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS=3000" in config
    assert "shield: lalapadgen2_right rgbled_adapter\n    snippet: zmk-usb-logging" in build
    assert f"revision: {DEBUG_DRIVER_REVISION}" in west


def test_navigation_positions_emit_mouse_buttons_on_active_mouse_layer():
    keymap = KEYMAP_PATH.read_text(encoding="utf-8")
    mouse_layer = re.search(r"mouse_layer\s*\{.*?bindings\s*=\s*<(.*?)>;", keymap, re.DOTALL)

    assert mouse_layer is not None
    assert re.search(
        r"&kp LA\(LEFT\)\s+&kp LA\(RIGHT\)(?:\s+&to 0){3}\s+&mkp MB4\s+&mkp MB5",
        mouse_layer.group(1),
    )
