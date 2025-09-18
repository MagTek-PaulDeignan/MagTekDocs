---
title: 0x1101 — MIFARE Classic/MINI/Plus SL1 (Type 2)
layout: home
parent: 0x11nn – NFC/MIFARE Pass Through
nav_order: 2
---

# 0x1101 — Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2

After activation of a Type 2 tag in Classic/MINI/Plus SL1 mode, the host uses this command to issue native **MIFARE Classic** operations (e.g., `AUTH`, `READ`, `WRITE`, value operations) and receive the tag's response via the device.

---

## Sequence of Events

**Preconditions**
- Type 2 tag with Classic/MINI/Plus SL1 is activated and in RF field.
- Correct key (A/B) is available for the target sector/block if access‑controlled.

**Steps**
1. Construct **0x1101** with the native command bytes in `81` and set `82/83` to indicate encryption and whether this is the last command.
2. Send **0x1101** to the device.
3. Device forwards the command to the tag and collects the response.
4. Device returns a response with status and the NFC/MIFARE data container.
5. Repeat with additional commands if needed until `83` indicates last command.

**Error/Recovery**
- If authentication fails or the tag returns **NAK/0xFF**, correct the key and retry. For chained operations (e.g., value ops), maintain command order and timing.

---

## Command Syntax

| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1101  | Classic/MINI/Plus SL1 pass‑through |
| TLVs    | var.   | —       | See Request/Response TLVs |

### Request TLVs
| Tag | Len | Field / Meaning                       | Req | Notes |
|----:|:---:|---------------------------------------|:---:|-------|
| 81  | var | Command to Send (native Classic bytes)| R   |       |
| 82  | 01  | Encryption Control                    | O   | 00=none, 01=encrypted |
| 83  | 01  | Flow Control                          | R   | 00=more, FF=last |

### Response TLVs
| Tag | Len | Field / Meaning                 | Req | Notes |
|----:|:---:|---------------------------------|:---:|-------|
| 81  | 01  | Tag Response Code (00=ok,01=fail) | R   |       |
| 82  | var | Encryption Control                | O   | Mirrors request |
| 84  | var | NFC/MIFARE Data Container         | R   | Encrypted/Plain |

**Encrypted Data (inside 84)**: `/DFDF59` (Encrypted Data), `/DFDF50` (KSN), `/DFDF51` (Type)  
**Unencrypted Data (inside 84)**: `FC` (NFC Data Container) with optional `/DF7A` (NFC Data)

---

## Examples — Full APDUs (Hex)

### Request — Example (AUTH/READ path)
| Example (Hex) |
|---------------|
| AA 00 81 04 01 19 11 01 84 15 11 01 81 0B 30 00 00 00 00 FF FF FF FF FF FF 82 01 00 83 01 00 |

### Response — Example
| Example (Hex) |
|---------------|
| AA 00 81 04 82 19 11 01 82 04 01 00 00 00 84 1C 11 01 81 01 00 82 15 FC 13 DF 7A 10 A4 FB 0D 3E 6C 08 04 00 03 0D C0 90 EE BF BB 1D |

---

## Error Conditions
| SW1SW2 | Meaning |
|--------|---------|
| 9000   | Success |
| 6A80   | Invalid data |
| 6985   | Conditions not satisfied |
| 6F00   | Unknown error |

---

## Notes
- For **MIFARE Plus EV1/EV2/SE/X at SL1**, ensure you send the **last‑command marker (`83=FF`)** before switching security states or you may receive a device‑level error beep.
