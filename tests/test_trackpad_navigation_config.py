from pathlib import Path


CONFIG_PATH = Path(__file__).parents[1] / "config" / "lalapadgen2.conf"


def test_two_finger_horizontal_navigation_is_enabled_without_hwheel():
    config_lines = {
        line.strip()
        for line in CONFIG_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }

    assert "CONFIG_INPUT_IQS9151_2F_HORIZONTAL_NAV=y" in config_lines
    assert "CONFIG_INPUT_IQS9151_SCROLL_X_ENABLE=n" in config_lines
    assert "CONFIG_INPUT_IQS9151_2F_NAV_SWIPE_THRESHOLD=200" in config_lines
