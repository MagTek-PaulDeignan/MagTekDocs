---
title: 0x1100 — NTAG / MIFARE Ultralight (Type 2)
layout: home
parent: 0x11nn – NFC/MIFARE Pass Through
nav_order: 1
---

# 0x1100 — Pass Through Command for NTAG / MIFARE Ultralight (Type 2)

After a Type 2 tag is activated, the host uses this command to issue native **NTAG/Ultralight** operations (e.g., `GET_VERSION`, `READ`, `FAST_READ`, `WRITE`, `AUTHENTICATE`) and receive the tag's response via the device.

---

## Sequence of Events

**Preconditions**
- Contactless reader is active and a Type 2 tag (NTAG/Ultralight) has been activated.
- If read-protection is enabled on the tag (e.g., address `0x00`), host must use the correct key or the device will fail to access protected areas.

**Steps**
1. Construct **0x1100** with the desired native command in TLV `81` and set `82/83` as needed.
2. Send **0x1100** to the device.
3. The device forwards the command to the tag and collects the response.
4. The device returns a response to **0x1100** containing any encrypted/un‑encrypted NFC data container.
5. If `83` indicates more commands are expected, repeat from step 1 until the last command is sent.

**Error/Recovery**
- For failures (`81` in response ≠ success), verify opcode/parameters and any authentication steps; retry as appropriate.

---

## Command Syntax

| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1100  | Type 2 pass‑through |
| TLVs    | var.   | —       | See Request/Response TLVs |

### Request TLVs
| Tag | Len | Field / Meaning                         | Req | Notes                          |
|----:|:---:|-----------------------------------------|:---:|--------------------------------|
| 81  | var | Command to Send (opcode + parameters)   | R   | Native NTAG/Ultralight command |
| 82  | 01  | Encryption Control                      | O   | 00 = none, 01 = encrypted      |
| 83  | 01  | Flow Control                            | R   | 00 = more, FF = last           |

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

### Request — GET_VERSION
| Example (Hex) |
|---------------|
| AA 00 81 04 01 39 11 00 84 0B 11 00 81 01 60 82 01 00 83 01 00 |

### Response — GET_VERSION
| Example (Hex) |
|---------------|
| AA 00 81 04 82 39 11 00 82 04 01 00 00 00 84 14 11 00 81 01 00 82 0D FC 0B DF 7A 08 01 02 03 04 05 06 07 08 |

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
- Use `GET_VERSION (0x60)` before feature‑sensitive operations to branch logic by tag type.
- For protected reads, authenticate first to avoid device‑level failures. 
