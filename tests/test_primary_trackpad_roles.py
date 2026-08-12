from pathlib import Path


SHIELD_DIR = Path(__file__).parents[1] / "config" / "boards" / "shields" / "lalapadgen2"


def test_right_primary_uses_local_right_and_remote_left_listeners():
    overlay = (SHIELD_DIR / "lalapadgen2_right.overlay").read_text(encoding="utf-8")
    assert '&trackpad_listener_R {' in overlay
    assert '&trackpad_listener_L {' in overlay
    assert 'device = <&iqs9151>;' in overlay
    assert '&trackpad_split_R {' not in overlay


def test_left_peripheral_forwards_its_local_trackpad_input():
    overlay = (SHIELD_DIR / "lalapadgen2_left.overlay").read_text(encoding="utf-8")
    assert '&trackpad_split_L {' in overlay
    assert 'input = <&iqs9151>;' in overlay
    assert '&trackpad_split_R {' in overlay
    assert 'status = "disabled";' in overlay
    assert '&trackpad_listener_L {' not in overlay
