---
title: Property 2.1.2.5.6.7 Available Access Points
layout: home
parent: Configuration
nav_order: 202
---

## Property 2.1.2.5.6.7 Available Access Points

---

- [Property 2.1.2.5.6.7 Available Access Points](#property-212567-available-access-points)

---


Table 1126 - Property 2.1.2.5.6.7 Available Access Points

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.7 / 0x020102050607 |
| Name | Available Access Points |
| Description | The device uses this property to report a list of available access points. The access points are in a list of tags starting with 0xA0 and incrementing. The list can contain up to 20 access points. Each access point contains two tags. Tag 0x80 contains the access point’s SSID. The SSID is a text string of 1 to 32 characters. Tag 0x81 is the RSSI for the access point. The RSSI is a signed binary number between -30 and -90. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 740 |
| Data Type | Binary |
| Valid Values | See **Table 8.5-146 – Access Point Payload Detail** |
| Default | None |

Table 1127 – Access Point Payload Detail

| Tag | Len | Value / Description                       | Typ | Req | Default |
|-----|-----|-------------------------------------------|-----|-----|---------|
| A0  | var | Access Point Container 1                  | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |
| A1  | var | Access Point Container 2                  | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |
| A2  | var | Access Point Container 3                  | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |
| …   |     |                                           |     |     |         |
| Ax  | var | Access Point Container x+1                | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |

Table 1128 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C700 |

Table 1129 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048206D101 820400000000 84820065 D101 81072B06010401F609 850102 8955E153E251E54FE64DC74B A00E80094D79416363657373318102FFC7 A10F800A4D7957694669535349448102FFA9 A22580204449524543542D46442D4850204465736B4A65742033363330207365726965738102FFA6 |

#