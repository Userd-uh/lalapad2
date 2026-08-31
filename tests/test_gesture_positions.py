import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_append_only_layout_and_keymap():
    layout = json.loads((ROOT / 'config/lalapadgen2.json').read_text())['layouts']['default_layout']['layout']
    dtsi = (ROOT / 'config/boards/shields/lalapadgen2/lalapadgen2.dtsi').read_text()
    physical = (ROOT / 'config/boards/shields/lalapadgen2/lalapadgen2-layouts.dtsi').read_text()
    matrix = re.search(r'map\s*=\s*<(.*?)>;', dtsi, re.S).group(1)
    coordinates = [(int(a), int(b)) for a, b in re.findall(r'RC\((\d+),\s*(\d+)\)', matrix)]
    assert len(layout) == len(coordinates) == physical.count('&key_physical_attrs') == 76
    assert len(set(coordinates)) == 76
    assert [(k['row'], k['col']) for k in layout] == coordinates
    keymap = (ROOT / 'config/lalapadgen2.keymap').read_text()
    layers = re.findall(r'\w+_layer\s*\{.*?bindings\s*=\s*<(.*?)>;', keymap, re.S)
    assert len(layers) == 5
    for layer in layers:
        bindings = [b.strip() for b in re.findall(r'&[^&]+', layer)]
        assert len(bindings) == 76
        assert bindings[68:] == [bindings[i] for i in [58,59,60,61,63,64,65,66]]


def test_independent_action_positions_and_preserved_taps():
    dtsi = (ROOT / 'config/boards/shields/lalapadgen2/lalapadgen2.dtsi').read_text()
    positions = dict((name, int(value)) for name, value in re.findall(r'#define\s+(POS_TP_\w+)\s+(\d+)', dtsi))
    actions = [value for name, value in positions.items() if 'SWIPE' in name]
    assert len(actions) == len(set(actions)) == 16
    assert positions['POS_TP_LCLK_L'] == 52
    assert positions['POS_TP_MCLK_R'] == 57
    assert positions['POS_TP_PINCH_L'] == 62
    assert positions['POS_TP_PINCH_R'] == 67
