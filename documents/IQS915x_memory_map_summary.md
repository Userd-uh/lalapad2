# IQS9150/IQS9151 I2C Memory Map Summary

This document extracts Section 15 (“I2C Memory Map - Register Descriptions”) and Appendix A (A.1–A.28) from the IQS9150/IQS9151 datasheet to provide a compact, high-visibility reference for driver development.

## Memory Map Overview (Section 15)

|Category|Address|Length|Access|Description|Notes|
| - | - | - | - | - | - |
|Version Information|0x1000–0x1013|20|Read Only|Product Information|Appendix A.1|
|Device Data|0x1014|2|Read Only|Relative X|Section 7.2.2|
|Device Data|0x1016|2|Read Only|Relative Y||
|Device Data|0x1018|2|Read Only|Gesture X|Section 8.1 and 8.3|
|Device Data|0x101A|2|Read Only|Gesture Y||
|Device Data|0x101C|2|Read Only|Single Finger Gestures|Appendix A.2|
|Device Data|0x101E|2|Read Only|Two-Finger Gestures|Appendix A.3|
|Device Data|0x1020|2|Read Only|Info Flags|Appendix A.4|
|Device Data|0x1022|2|Read Only|Trackpad Flags|Appendix A.5|
|Device Data|0x1024|2|Read Only|Finger 1 X-Coordinate|Section 7.2.3|
|Device Data|0x1026|2|Read Only|Finger 1 Y-Coordinate||
|Device Data|0x1028|2|Read Only|Finger 1 Touch Strength|Section 7.2.4|
|Device Data|0x102A|2|Read Only|Finger 1 Area|Section 7.2.5|
|Device Data|0x102C–0x1053|40|Read Only|Finger 2–6 Data (X/Y/Touch Strength/Area)|Repeats Finger 1 structure|
|Device Data|0x1054|2|Read Only|Finger 7 X-Coordinate|Section 7.2.3|
|Device Data|0x1056|2|Read Only|Finger 7 Y-Coordinate||
|Device Data|0x1058|2|Read Only|Finger 7 Touch Strength|Section 7.2.4|
|Device Data|0x105A|2|Read Only|Finger 7 Area|Section 7.2.5|
|Channel Data|0x105C|88|Read Only|Touch Status|Appendix A.28|
|Channel Data|0x10B4|2|Read Only|ALP Channel Count|Section 5.4.2|
|Channel Data|0x10B6|2|Read Only|ALP Channel LTA|Section 5.5.2|
|Channel Data|0x10B8|26|Read Only|ALP Individual Counts|Appendix A.6|
|Channel Data|0x10D2|88|Read Only|Snap Status|Appendix A.28|
|Channel Data|0x112A|2|Read Only|Button Output|Appendix A.7|
|Channel Data|0x112C|32|Read Only|Slider Output|Appendix A.8|
|Channel Data|0x114C|16|Read Only|Wheel Output|Appendix A.9|
|Trackpad Configuration|0x115C|26|Read-Write|ALP ATI Compensation|Appendix A.10|
|Trackpad Configuration|0x1176|1|Read-Write|I2C Update Key|Section 12.2|
|Trackpad Configuration|0x1177|1|Read-Write|I2C Slave Address||
|Trackpad Configuration|0x1178|1|Read-Write|Settings Minor Version|Section 11.1|
|Trackpad Configuration|0x1179|1|Read-Write|Settings Major Version||
|Trackpad Configuration|0x117A|2|Read-Write|Trackpad ATI Multiplier/Dividers (Global)|Appendix A.11|
|Trackpad Configuration|0x117C|26|Read-Write|ALP ATI Multiplier/Dividers|Appendix A.11|
|Trackpad Configuration|0x1196|2|Read-Write|Trackpad ATI Target|Section 5.7.1|
|Trackpad Configuration|0x1198|2|Read-Write|ALP ATI Target|Section 5.7.2|
|Trackpad Configuration|0x119A|2|Read-Write|ALP ATI Base Target||
|Trackpad Configuration|0x119C|2|Read-Write|Trackpad Negative Delta Re-ATI Value|Section 5.8|
|Trackpad Configuration|0x119E|2|Read-Write|Trackpad Positive Delta Re-ATI Value||
|Trackpad Configuration|0x11A0|1|Read-Write|Trackpad Reference Drift Limit||
|Trackpad Configuration|0x11A1|1|Read-Write|ALP LTA Drift Limit||
|Device Configuration|0x11A2|2|Read-Write|Active Mode Sampling Period (ms)|Section 6.1|
|Device Configuration|0x11A4|2|Read-Write|Idle-Touch Mode Sampling Period (ms)||
|Device Configuration|0x11A6|2|Read-Write|Idle Mode Sampling Period (ms)||
|Device Configuration|0x11A8|2|Read-Write|LP1 Mode Sampling Period (ms)||
|Device Configuration|0x11AA|2|Read-Write|LP2 Mode Sampling Period (ms)||
|Device Configuration|0x11AC|2|Read-Write|Stationary Touch Timeout (s)|Section 6.2|
|Device Configuration|0x11AE|2|Read-Write|Idle-Touch Mode Timeout (s)||
|Device Configuration|0x11B0|2|Read-Write|Idle Mode Timeout (s)||
|Device Configuration|0x11B2|2|Read-Write|LP1 Mode Timeout (s)||
|Device Configuration|0x11B4|2|Read-Write|Active to Idle Mode Timeout (ms)||
|Device Configuration|0x11B6|1|Read-Write|Re-ATI Retry Time (s)|Section 5.8.3|
|Device Configuration|0x11B7|1|Read-Write|Reference Update Time (s)|Section 5.5.1|
|Device Configuration|0x11B8|2|Read-Write|I2C Timeout (ms)|Section 12.6|
|Device Configuration|0x11BA|1|Read-Write|Snap Timeout|Section 5.6.2|
|Device Configuration|0x11BB|1|Read-Write|Reserved (0x00)||
|Device Configuration|0x11BC|2|Read-Write|System Control|Appendix A.12|
|Device Configuration|0x11BE|2|Read-Write|Config Settings|Appendix A.13|
|Device Configuration|0x11C0|2|Read-Write|Other Settings|Appendix A.14|
|Device Configuration|0x11C2|4|Read-Write|ALP Setup|Appendix A.15|
|Device Configuration|0x11C6|6|Read-Write|ALP Tx Enable|Appendix A.16|
|Device Configuration|0x11CC|1|Read-Write|Touch Set Threshold Multiplier|Section 5.6.1|
|Device Configuration|0x11CD|1|Read-Write|Touch Clear Threshold Multiplier||
|Device Configuration|0x11CE|1|Read-Write|ALP Output Threshold (Delta)|Section 5.6.3|
|Device Configuration|0x11CF|1|Read-Write|ALP Auto-Prox Threshold (Delta)||
|Device Configuration|0x11D0|1|Read-Write|ALP Set Debounce|Section 5.6.4|
|Device Configuration|0x11D1|1|Read-Write|ALP Clear Debounce||
|Device Configuration|0x11D2|1|Read-Write|Snap Set Threshold (Delta)|Section 5.6.2|
|Device Configuration|0x11D3|1|Read-Write|Snap Clear Threshold (Delta)||
|Device Configuration|0x11D4|1|Read-Write|ALP Count Filter Beta - LP1 Mode|Section 5.4.2 / 5.5.2|
|Device Configuration|0x11D5|1|Read-Write|ALP LTA Filter Beta - LP1 Mode||
|Device Configuration|0x11D6|1|Read-Write|ALP Count Filter Beta - LP2 Mode||
|Device Configuration|0x11D7|1|Read-Write|ALP LTA Filter Beta - LP2 Mode||
|Device Configuration|0x11D8|3|Read-Write|Trackpad Conversion Frequency|Appendix A.17|
|Device Configuration|0x11DB|3|Read-Write|ALP Conversion Frequency|Appendix A.17|
|Device Configuration|0x11DE|2|Read-Write|Trackpad Hardware Settings|Appendix A.18|
|Device Configuration|0x11E0|2|Read-Write|ALP Hardware Settings|Appendix A.18|
|Trackpad Configuration|0x11E2|1|Read-Write|Trackpad Settings|Appendix A.19|
|Trackpad Configuration|0x11E3|1|Read-Write|Total Rxs|Section 7.1.1|
|Trackpad Configuration|0x11E4|1|Read-Write|Total Txs||
|Trackpad Configuration|0x11E5|1|Read-Write|Max Multi-Touches|Section 7.3|
|Trackpad Configuration|0x11E6|2|Read-Write|X Resolution|Section 7.4|
|Trackpad Configuration|0x11E8|2|Read-Write|Y Resolution||
|Trackpad Configuration|0x11EA|2|Read-Write|XY Dynamic Filter Bottom Speed|Section 7.8|
|Trackpad Configuration|0x11EC|2|Read-Write|XY Dynamic Filter Top Speed||
|Trackpad Configuration|0x11EE|1|Read-Write|XY Dynamic Filter Bottom Beta||
|Trackpad Configuration|0x11EF|1|Read-Write|XY Static Filter Beta||
|Trackpad Configuration|0x11F0|1|Read-Write|Stationary Touch Movement Threshold|Section 7.5|
|Trackpad Configuration|0x11F1|1|Read-Write|Finger Split Factor|Section 7.6|
|Trackpad Configuration|0x11F2|1|Read-Write|X Trim Value|Section 7.9|
|Trackpad Configuration|0x11F3|1|Read-Write|Y Trim Value||
|Trackpad Configuration|0x11F4|1|Read-Write|Jitter Filter Delta Threshold|Section 7.8.2|
|Trackpad Configuration|0x11F5|1|Read-Write|Finger Confidence Threshold|Section 7.10|
|Gesture Configuration|0x11F6|2|Read-Write|Single Finger Gesture Enable|Appendix A.20|
|Gesture Configuration|0x11F8|2|Read-Write|Two-Finger Gesture Enable|Appendix A.21|
|Gesture Configuration|0x11FA|2|Read-Write|Tap Time (ms)|Section 8.1|
|Gesture Configuration|0x11FC|2|Read-Write|Air Time (ms)||
|Gesture Configuration|0x11FE|2|Read-Write|Tap Distance (pixels)||
|Gesture Configuration|0x1200|2|Read-Write|Hold Time (ms)|Section 8.2|
|Gesture Configuration|0x1202|2|Read-Write|Swipe Time (ms)|Section 8.3|
|Gesture Configuration|0x1204|2|Read-Write|Swipe Initial X-Distance (pixels)||
|Gesture Configuration|0x1206|2|Read-Write|Swipe Initial Y-Distance (pixels)||
|Gesture Configuration|0x1208|2|Read-Write|Swipe Consecutive X-Distance (pixels)||
|Gesture Configuration|0x120A|2|Read-Write|Swipe Consecutive Y-Distance (pixels)||
|Gesture Configuration|0x120C|1|Read-Write|Swipe Angle (64tan(deg))||
|Gesture Configuration|0x120D|1|Read-Write|Scroll Angle (64tan(deg))|Section 8.6|
|Gesture Configuration|0x120E|2|Read-Write|Zoom Initial Distance|Section 8.7|
|Gesture Configuration|0x1210|2|Read-Write|Zoom Consecutive Distance||
|Gesture Configuration|0x1212|2|Read-Write|Scroll Initial Distance|Section 8.6|
|Gesture Configuration|0x1214|2|Read-Write|Scroll Consecutive Distance||
|Gesture Configuration|0x1216|2|Read-Write|Palm Gesture Threshold|Section 8.4|
|Trackpad Electrode & Channel Configuration|0x1218|46|Read-Write|RxTx Mapping|Appendix A.22|
|Trackpad Electrode & Channel Configuration|0x1246|88|Read-Write|Trackpad Channel Disable|Appendix A.28|
|Trackpad Electrode & Channel Configuration|0x129E|88|Read-Write|Trackpad Snap Channel Enable|Appendix A.28|
|Trackpad Electrode & Channel Configuration|0x12F6|506|Read-Write|Individual Touch Threshold Adjustments|Appendix A.23|
|Virtual Sensor Configuration|0x14F0|2|Read-Write|Number Of Virtual Sensors Enabled|Appendix A.24|
|Virtual Button Configuration|0x14F2|2|Read-Write|Button 0 Top-Left X|Section 9.3|
|Virtual Button Configuration|0x14F4|2|Read-Write|Button 0 Top-Left Y||
|Virtual Button Configuration|0x14F6|2|Read-Write|Button 0 Bottom-Right X||
|Virtual Button Configuration|0x14F8|2|Read-Write|Button 0 Bottom-Right Y||
|Virtual Button Configuration|0x14FA–0x1568|112|Read-Write|Button 1–14 Coordinates|Same field order as Button 0|
|Virtual Button Configuration|0x156A|2|Read-Write|Button 15 Top-Left X|Section 9.3|
|Virtual Button Configuration|0x156C|2|Read-Write|Button 15 Top-Left Y||
|Virtual Button Configuration|0x156E|2|Read-Write|Button 15 Bottom-Right X||
|Virtual Button Configuration|0x1570|2|Read-Write|Button 15 Bottom-Right Y||
|Virtual Slider Configuration|0x1572|2|Read-Write|Slider Deadzone|Section 9.4.1|
|Virtual Slider Configuration|0x1574|2|Read-Write|Slider 0 Top-Left X|Section 9.4|
|Virtual Slider Configuration|0x1576|2|Read-Write|Slider 0 Top-Left Y||
|Virtual Slider Configuration|0x1578|2|Read-Write|Slider 0 Bottom-Right X||
|Virtual Slider Configuration|0x157A|2|Read-Write|Slider 0 Bottom-Right Y||
|Virtual Slider Configuration|0x157C|2|Read-Write|Slider 0 Resolution||
|Virtual Slider Configuration|0x157E–0x15B8|60|Read-Write|Slider 1–6 Definitions|Same field order as Slider 0|
|Virtual Slider Configuration|0x15BA|2|Read-Write|Slider 7 Top-Left X|Section 9.4|
|Virtual Slider Configuration|0x15BC|2|Read-Write|Slider 7 Top-Left Y||
|Virtual Slider Configuration|0x15BE|2|Read-Write|Slider 7 Bottom-Right X||
|Virtual Slider Configuration|0x15C0|2|Read-Write|Slider 7 Bottom-Right Y||
|Virtual Slider Configuration|0x15C2|2|Read-Write|Slider 7 Resolution||
|Virtual Wheel Configuration|0x15C4|2|Read-Write|Wheel 0 Centre X|Section 9.5|
|Virtual Wheel Configuration|0x15C6|2|Read-Write|Wheel 0 Centre Y||
|Virtual Wheel Configuration|0x15C8|2|Read-Write|Wheel 0 Inner Radius||
|Virtual Wheel Configuration|0x15CA|2|Read-Write|Wheel 0 Outer Radius||
|Virtual Wheel Configuration|0x15CC|2|Read-Write|Wheel 0 Resolution||
|Virtual Wheel Configuration|0x15CE–0x15E0|20|Read-Write|Wheel 1–2 Definitions|Same field order as Wheel 0|
|Virtual Wheel Configuration|0x15E2|2|Read-Write|Wheel 3 Centre X|Section 9.5|
|Virtual Wheel Configuration|0x15E4|2|Read-Write|Wheel 3 Centre Y||
|Virtual Wheel Configuration|0x15E6|2|Read-Write|Wheel 3 Inner Radius||
|Virtual Wheel Configuration|0x15E8|2|Read-Write|Wheel 3 Outer Radius||
|Virtual Wheel Configuration|0x15EA|2|Read-Write|Wheel 3 Resolution||
|Engineering Configuration|0x2000|2|Read-Write|Engineering Configuration|Appendix A.25|
|Engineering Configuration|0x2002|1|Read-Write|Main Oscillator Step Up||
|Engineering Configuration|0x2003|1|Read-Write|Main Oscillator Step Down||
|Engineering Configuration|0x2004|2|Read-Write|Main Oscillator Step Threshold||
|Trackpad Channel Information|0xA000|1012|Read Only|Trackpad Count Values|Appendix A.27|
|Trackpad Channel Information|0xB000|1012|Read Only|Trackpad Reference Values||
|Trackpad Channel Information|0xC000|1012|Read Only|Trackpad Delta Values||
|Trackpad Channel Information|0xD000|1012|Read Only|Trackpad ATI Compensation Values|Appendix A.26|
|Trackpad Channel Information|0xE000|6|Read Only|Unique Identifier||

## Appendix Extracts (A.1–A.28)

### A.1 Product Information (0x1000–0x1013)

|Address|Length|Description|IQS9150|IQS9151|
| - | - | - | - | - |
|0x1000|2|Product Number|0x076A|0x09BC|
|0x1002|2|Product Major Version|0x0001|0x0001|
|0x1004|2|Product Minor Version|0x0002|0x0000|
|0x1006|4|Product SHA|-|-|
|0x100A|2|Library Number|0x037D|-|
|0x100C|2|Library Major Version|0x0001|-|
|0x100E|2|Library Minor Version|0x0000|-|
|0x1010|4|Library SHA|-|-|

### A.2 Single Finger Gestures (0x101C)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Swipe and Hold Y-|Swipe and Hold Y+|Swipe and Hold X-|Swipe and Hold X+|Swipe Y-|Swipe Y+|Swipe X-|Swipe X+|

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Reserved|||Palm Gesture|Press-and-Hold|Triple Tap|Double Tap|Single Tap|||

- Bits 15–8: Swipe and Hold / Swipe directions (0: no gesture, 1: gesture occurred).
- Bit 4: Palm Gesture (0: none, 1: occurred).
- Bit 3: Press-and-Hold (0: none, 1: occurred).
- Bit 2: Triple Tap (0: none, 1: occurred).
- Bit 1: Double Tap (0: none, 1: occurred).
- Bit 0: Single Tap (0: none, 1: occurred).

### A.3 Two Finger Gestures (0x101E)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Reserved|||||||||

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Horizontal Scroll|Vertical Scroll|Zoom Out|Zoom In|Press-and-Hold|Triple Tap|Double Tap|Single Tap|

- Bits 7–0 flag gesture occurrences (0: none, 1: occurred); bits 15–8 are unused.

### A.4 Info Flags (0x1020)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Snap Toggled|Switch Toggled|TP Touch Toggled|ALP Prox Toggled|Global Snap|Switch Pressed|Global TP Touch|ALP Prox Status|

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Show Reset|ALP Re-ATI Occurred|ALP ATI Error|Re-ATI Occurred|ATI Error|Charging Mode (bit2–0)|||

- Bits 15–8: status toggles and global flags (0: not set, 1: set).
- Bit 7: Show Reset (1 = reset occurred and not yet acknowledged).
- Bits 6–3: Re-ATI status/errors.
- Bits 2–0: Charging Mode (000 Active, 001 Idle-Touch, 010 Idle, 011 LP1, 100 LP2).

### A.5 Trackpad Flags (0x1022)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Reserved|Finger 7 Confidence|Finger 6 Confidence|Finger 5 Confidence|Finger 4 Confidence|Finger 3 Confidence|Finger 2 Confidence|Finger 1 Confidence|

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Saturation|Main Osc Stepped|Too Many Fingers|Movement Detected|Number of Fingers (bit3–0)||||

- Bits 14–8: Finger Confidence (0: not confident, 1: confident).
- Bit 7: Saturation (0: none, 1: detected).
- Bit 6: Main Osc Stepped (0: not adjusted, 1: adjusted).
- Bit 5: Too Many Fingers (0: within max, 1: exceeds max).
- Bit 4: Movement Detected (0: none or stationary, 1: movement).
- Bits 3–0: Number of Fingers (0–7).

### A.6 ALP Individual Counts (0x10B8)

|Address|Bit 15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
|0x10B8|ALP Counts Rx0 and/or Rx13|||||||||||||||||
|0x10BA|ALP Counts Rx1 and/or Rx14|||||||||||||||||
|0x10BC|ALP Counts Rx2 and/or Rx15|||||||||||||||||
|0x10BE|ALP Counts Rx3 and/or Rx16|||||||||||||||||
|0x10C0|ALP Counts Rx4 and/or Rx17|||||||||||||||||
|0x10C2|ALP Counts Rx5 and/or Rx18|||||||||||||||||
|0x10C4|ALP Counts Rx6 and/or Rx19|||||||||||||||||
|0x10C6|ALP Counts Rx7 and/or Rx20|||||||||||||||||
|0x10C8|ALP Counts Rx8 and/or Rx21|||||||||||||||||
|0x10CA|ALP Counts Rx9 and/or Rx22|||||||||||||||||
|0x10CC|ALP Counts Rx10 and/or Rx23|||||||||||||||||
|0x10CE|ALP Counts Rx11 and/or Rx24|||||||||||||||||
|0x10D0|ALP Counts Rx12 and/or Rx25|||||||||||||||||

### A.7 Button Output (0x112A)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Button 15|Button 14|Button 13|Button 12|Button 11|Button 10|Button 9|Button 8|

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Button 7|Button 6|Button 5|Button 4|Button 3|Button 2|Button 1|Button 0|

- Bits reflect virtual button state (0: not pressed, 1: pressed).

### A.8 Slider Output (0x112C)

|Address|Length|Description|
| - | - | - |
|0x112C|2|Slider 0 output for Finger 1|
|0x112E|2|Slider 0 output for Finger 2|
|0x1130|2|Slider 1 output for Finger 1|
|0x1132|2|Slider 1 output for Finger 2|
|0x1134|2|Slider 2 output for Finger 1|
|0x1136|2|Slider 2 output for Finger 2|
|0x1138|2|Slider 3 output for Finger 1|
|0x113A|2|Slider 3 output for Finger 2|
|0x113C|2|Slider 4 output for Finger 1|
|0x113E|2|Slider 4 output for Finger 2|
|0x1140|2|Slider 5 output for Finger 1|
|0x1142|2|Slider 5 output for Finger 2|
|0x1144|2|Slider 6 output for Finger 1|
|0x1146|2|Slider 6 output for Finger 2|
|0x1148|2|Slider 7 output for Finger 1|
|0x114A|2|Slider 7 output for Finger 2|

### A.9 Wheel Output (0x114C)

|Address|Length|Description|
| - | - | - |
|0x114C|2|Wheel 0 output for Finger 1|
|0x114E|2|Wheel 0 output for Finger 2|
|0x1150|2|Wheel 1 output for Finger 1|
|0x1152|2|Wheel 1 output for Finger 2|
|0x1154|2|Wheel 2 output for Finger 1|
|0x1156|2|Wheel 2 output for Finger 2|
|0x1158|2|Wheel 3 output for Finger 1|
|0x115A|2|Wheel 3 output for Finger 2|

### A.10 ALP ATI Compensation (0x115C)

|Address|Bit 15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
|0x115C||Rx0 and/or Rx13||||||||||||||||
|0x115E||Rx1 and/or Rx14||||||||||||||||
|0x1160||Rx2 and/or Rx15||||||||||||||||
|0x1162||Rx3 and/or Rx16||||||||||||||||
|0x1164||Rx4 and/or Rx17||||||||||||||||
|0x1166||Rx5 and/or Rx18||||||||||||||||
|0x1168||Rx6 and/or Rx19||||||||||||||||
|0x116A||Rx7 and/or Rx20||||||||||||||||
|0x116C||Rx8 and/or Rx21||||||||||||||||
|0x116E||Rx9 and/or Rx22||||||||||||||||
|0x1170||Rx10 and/or Rx23|||||||||||||||
|0x1172||Rx11 and/or Rx24|||||||||||||||
|0x1174||Rx12 and/or Rx25|||||||||||||||

- Bit 15: unused.
- Bits 14–10: ALP Compensation Divider.
- Bits 9–0: ALP Compensation.

### A.11 Trackpad and ALP Multipliers / Divider (0x117A / 0x117C)

|Address|Bit 15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
|0x117A|Trackpad||||||||||||||||
|0x117C|ALP Rx0 + Rx13||||||||||||||||
|0x117E|ALP Rx1 + Rx14||||||||||||||||
|0x1180|ALP Rx2 + Rx15||||||||||||||||
|0x1182|ALP Rx3 + Rx16||||||||||||||||
|0x1184|ALP Rx4 + Rx17||||||||||||||||
|0x1186|ALP Rx5 + Rx18||||||||||||||||
|0x1188|ALP Rx6 + Rx19||||||||||||||||
|0x118A|ALP Rx7 + Rx20||||||||||||||||
|0x118C|ALP Rx8 + Rx21||||||||||||||||
|0x118E|ALP Rx9 + Rx22||||||||||||||||
|0x1190|ALP Rx10 + Rx23||||||||||||||||
|0x1192|ALP Rx11 + Rx24||||||||||||||||
|0x1194|ALP Rx12 + Rx25||||||||||||||||

- Bits 15–14: Fine Multiplier (2-bit, 1–2, recommended 1).
- Bits 13–9: Fine Divider (5-bit, 1–21, recommended >6).
- Bits 8–5: Coarse Multiplier (4-bit, 1–15; use GUI-recommended sets).
- Bits 4–0: Coarse Divider (5-bit, 1–31; use GUI-recommended sets).

### A.12 System Control (0x11BC)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Tx Short Test|Reserved|||Suspend|Reserved|SW Reset|Reserved|||

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Ack Reset|ALP Re-ATI|TP Re-ATI|ALP Reseed|TP Reseed|Mode Select|||

- Bit 15: Tx Short Test (0 normal, 1 enable short test).
- Bit 11: Suspend (0 none, 1 suspend after comms window).
- Bit 9: SW Reset (0 none, 1 reset after comms window).
- Bit 7: Ack Reset (0 none, 1 clear *Show Reset*).
- Bit 6: ALP Re-ATI (queue ALP re-ATI).
- Bit 5: TP Re-ATI (queue trackpad re-ATI).
- Bit 4: ALP Reseed (queue ALP reseed).
- Bit 3: TP Reseed (queue trackpad reseed).
- Bits 2–0: Mode Select (000 Active, 001 Idle-Touch, 010 Idle, 011 LP1, 100 LP2; manual mode only).

### A.13 Configuration Settings (0x11BE)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Snap Event Enable|Switch Event Enable|TP Touch Event Enable|ALP Event Enable|Re-ATI Event Enable|TP Event Enable|Gesture Event Enable|Event Mode|

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Manual Control|Terminate Comms Window|Sleep During Conversions|Force Comms Method|ALP Re-ATI Enable|TP Re-ATI Enable|ALP ATI Mode|Sleep Option|

- Bits 15–8 enable event sources and event mode.
- Bit 7: Manual Control (0 auto, 1 host manual).
- Bit 6: Terminate Comms Window (0 stop ends comms, 1 issue command + stop).
- Bit 5: Sleep During Conversions (0 normal, 1 sleep).
- Bit 4: Force Comms Method (0 allow clock stretching, 1 request comms window).
- Bit 3: ALP Re-ATI Enable (0 disabled, 1 enabled).
- Bit 2: TP Re-ATI Enable (0 disabled, 1 enabled).
- Bit 1: ALP ATI Mode (0 compensation only, 1 full ATI).
- Bit 0: Sleep Option (0 deep sleep, 1 light sleep).

### A.14 Other Settings (0x11C0)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Switch Enable|Switch Polarity|Prox Oscillator Adjustment||Reserved|||||

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Main Oscillator Selection||LP2 Auto-Prox Enable|LP1 Auto-Prox Enable|LP2 Auto-Prox Cycles||LP1 Auto-Prox Cycles|||||

- Bit 15: Switch Enable (0 disabled, 1 enabled).
- Bit 14: Switch Polarity (0 active-low, 1 active-high).
- Bits 13–12: Prox Oscillator Adjustment (00 nominal 16 MHz; 01 −10% / −20%; 10 −20% / −30%; 11 −30% / −40% depending on main osc).
- Bits 7–6: Main Oscillator Selection (00 14 MHz, 01 20 MHz, 10 24 MHz).
- Bit 5: LP2 Auto-Prox Enable (0 disabled, 1 enabled).
- Bit 4: LP1 Auto-Prox Enable (0 disabled, 1 enabled).
- Bits 3–2: LP2 Auto-Prox Cycles (00 16, 01 32, 10 64, 11 256).
- Bits 1–0: LP1 Auto-Prox Cycles (00 16, 01 32, 10 64, 11 256).

### A.15 ALP Setup (0x11C2)

- Bit 31: ALP Enable (0 disabled, 1 enabled).
- Bit 30: ALP Count Filter Enable (0 unfiltered, 1 filtered).
- Bit 29: ALP Sensing Method (0 self-cap, 1 mutual-cap).
- Bit 28: Active Tx Shield Enable (0 unused electrodes grounded, 1 ALP Txs mimic Rx).
- Bits 27–26: Reserved.
- Bits 25–0: Rx Enable mask (0 disabled, 1 enabled; Rx24–25 bits not applicable to IQS9151 and should be 0).

### A.16 ALP Tx Enable (0x11C6)

- Bits 47–46: Reserved; bit 44 also reserved (keep 0).
- Bits 45, 43–0: Tx Enable mask (0 disabled, 1 enabled; Tx24–43 bits not applicable to IQS9151 and should be 0).

### A.17 Trackpad and ALP Conversion Frequency (0x11D8, 0x11DB)

|Address|Length|Description|
| - | - | - |
|0x11D8|1|Trackpad Fraction Value|
|0x11D9|1|Trackpad Period1 Value|
|0x11DA|1|Trackpad Period2 Value|
|0x11DB|1|ALP Fraction Value|
|0x11DC|1|ALP Period1 Value|
|0x11DD|1|ALP Period2 Value|

|Conversion Frequency (MHz)|Fraction Value|Period1 Value|Period2 Value|
| - | :-: | :-: | :-: |
|0.25|4|31|31|
|0.50|8|15|15|
|0.75|12|9|10|
|1.00|16|7|7|
|1.25|20|5|5|
|1.50|24|4|4|
|1.75|28|3|4|
|2.00|32|3|3|
|2.25|36|2|3|
|2.50|40|2|2|
|2.75|44|1|2|
|3.00|48|1|2|
|3.25|52|1|1|
|3.50|56|1|1|
|4.00|64|1|1|

### A.18 Trackpad and ALP Hardware Settings (0x11DE, 0x11E0)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Initial Cycle Delay||SH Bias|||Count Upper Limit||||||

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Cs Discharge Voltage|RF Filters|NM Out Static|NM In Static|Global SH Offset|||||

- Bits 15–14: Initial Cycle Delay (00 16, 01 32, 10 64, 11 256).
- Bits 13–11: SH Bias (000 5 A, 001 10 A, 010 15 A, 011 20 A, 100 15 A, 101 20 A, 110 25 A, 111 30 A).
- Bits 10–8: Count Upper Limit (000 383, 001 511, 010 767, 011 1023, 100 2047).
- Bit 7: Cs Discharge Voltage (0 discharge to 0 V, 1 discharge to 0.5 V).
- Bit 6: RF Filters (0 disabled, 1 enabled).
- Bit 5: NM Out Static (0 disabled, 1 enabled).
- Bit 4: NM In Static (0 disabled, 1 enabled).
- Bits 3–0: Global SH Offset (0000 0 mV, 0001 −2 mV, …, 1111 +14 mV).

### A.19 Trackpad Settings (0x11E2)

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Reserved|Area Filter Disable|Jitter Filter|IIR Static|IIR Filter|Switch XY Axis|Flip Y|Flip X|

- Bit 6: Area Filter Disable (0 enabled, 1 disabled).
- Bit 5: Jitter Filter (0 disabled, 1 enabled).
- Bit 4: IIR Static (0 dynamic damping, 1 fixed).
- Bit 3: IIR Filter (0 disabled, 1 enabled).
- Bit 2: Switch XY Axis (0 RX=X/Tx=Y, 1 swap).
- Bit 1: Flip Y (0 default, 1 invert).
- Bit 0: Flip X (0 default, 1 invert).

### A.20 Single Finger Gesture Enable (0x11F6)

Same bit layout as A.2; bits enable (1) or disable (0) each gesture.

### A.21 Two Finger Gesture Enable (0x11F8)

Same bit layout as A.3; bits enable (1) or disable (0) each gesture (bits 7–0), bits 15–8 unused.

### A.22 RxTx Mapping (0x1218)

|Address|Length|Description|
| - | - | - |
|0x1218–0x1244|1 each|RxTx Mapping 0–44|
|0x1245|1|Reserved (0x00)|

- Byte 44–0 map trackpad Rx/Tx assignments; value 0x2C must not be written.

### A.23 Individual Touch Threshold Adjustments (0x12F6)

- Addresses 0x12F6–0x14EF (506 bytes): CH0–CH505 Touch Threshold Adjustment (signed 8-bit).
- Values offset the Touch Threshold Multiplier (e.g., 0x00:+0, 0x01:+1, …, 0x7F:+127, 0x80:−128, …, 0xFF:−1).

### A.24 Number Of Virtual Sensors Enabled (0x14F0)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Number of Wheels||||Number of Sliders||||

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Number of Buttons|||||||||

- Bits 15–12: number of virtual wheels; bits 11–8: number of virtual sliders; bits 7–0: number of virtual buttons.

### A.25 Engineering Configuration (0x2000)

|Bit|15|14|13|12|11|10|9|8|
| - | - | - | - | - | - | - | - | - |
|Description|Reserved|||||Main Osc Status||Reserved|

|Bit|7|6|5|4|3|2|1|0|
| - | - | - | - | - | - | - | - | - |
|Description|Reserved|||||||Main Osc Stepping Enable|

- Bit 0 enables main oscillator stepping; bits 15–11 and 8–1 are unused; bits 10–9 report main oscillator status.

### A.26 Trackpad ATI Compensation (0xD000)

- Addresses 0xD000 onward (2 bytes per channel): bits 14–10 Trackpad Compensation Divider, bits 9–0 Trackpad Compensation; bit 15 unused.

### A.27 Count / Delta / Reference Data

- 2 bytes per channel, packed as Count/Delta/ReferenceValue\[Row/Tx][Column/Rx].
- For a 26 Rx × 19 Tx pad (example table), bytes X..X+987 cover Tx0/Rx0 through Tx18/Rx25.
- For smaller pads, data pack densely according to *Total Rxs*; e.g., 4 Rx × 2 Tx uses bytes X..X+15.

### A.28 Individual Channel Status / Config Bit Definitions

- Status/config words are organized in 32-bit rows (Row0..Row21) with bits mapping to columns (Col0..Col25).
- Channel meaning by bit value:
  - Touch Status: 0 no touch, 1 touch present.
  - Snap Status: 0 no snap, 1 snap present.
  - Channel Disable: 0 enabled, 1 disabled.
  - Snap Enable: 0 snap disabled, 1 snap enabled.

