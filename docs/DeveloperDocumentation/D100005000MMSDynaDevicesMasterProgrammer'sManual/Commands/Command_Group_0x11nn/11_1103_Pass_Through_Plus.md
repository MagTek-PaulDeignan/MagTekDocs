---
title: 0x1103 — MIFARE Plus (Type 2)
layout: home
parent: 0x11nn – NFC/MIFARE Pass Through
nav_order: 4
---

# 0x1103 — Pass Through Command for MIFARE Plus (Type 2)

Pass‑through access for **MIFARE Plus** (Type 2). Supports read/write/value operations and security‑level transitions per the NXP specification.

---

## Sequence of Events

**Preconditions**
- MIFARE Plus tag is activated and in RF field.
- Host has appropriate keys and knows the target security level.

**Steps**
1. Construct **0x1103** with native MIFARE Plus command bytes in `81`; set `82` (encryption) and `83` (last/continue).
2. Send **0x1103** to the device.
3. Device forwards to the tag and collects the response.
4. Device returns a response with status and NFC/MIFARE data container.
5. Repeat for further operations as needed.

**Error/Recovery**
- On access/auth failures, correct keys or state and retry. For chained value ops, preserve ordering and timing.

---

## Command Syntax

| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1103  | MIFARE Plus pass‑through |
| TLVs    | var.   | —       | See Request/Response TLVs |

### Request TLVs
| Tag | Len | Field / Meaning                | Req | Notes |
|----:|:---:|--------------------------------|:---:|-------|
| 81  | var | Command to Send (native Plus)  | R   |       |
| 82  | 01  | Encryption Control             | O   | 00=none, 01=encrypted |
| 83  | 01  | Flow Control                   | R   | 00=more, FF=last |

### Response TLVs
| Tag | Len | Field / Meaning                 | Req | Notes |
|----:|:---:|---------------------------------|:---:|-------|
| 81  | 01  | Tag Response Code (00=ok,01=fail) | R   |       |
| 82  | var | Encryption Control                | O   | Mirrors request |
| 84  | var | NFC/MIFARE Data Container         | R   | Encrypted/Plain |

**Encrypted Data (inside 84)**: `/DFDF59` (Encrypted Data), `/DFDF50` (KSN), `/DFDF51` (Type)  
**Unencrypted Data (inside 84)**: `FC` (NFC Data Container) with optional `/DF7A` (NFC Data)

---

## Examples
> The Rev 103 source does not publish wrapper‑level APDUs for **0x1103**. If you want to include internal captures, I can insert them verbatim.

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
- Follow NXP Plus security‑level rules; set the last‑command flag (`83=FF`) when completing a command chain before a level transition.
