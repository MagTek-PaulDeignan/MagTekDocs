---
title: 0x1102 — MIFARE DESFire (Type 4)
layout: home
parent: 0x11nn – NFC/MIFARE Pass Through
nav_order: 3
---

# 0x1102 — Pass Through Command for MIFARE DESFire (Type 4)

After a DESFire (Light/EV1/EV2/EV3) tag is activated, use this command to issue **native DESFire** commands (e.g., `GET_VERSION`, `SELECT`, `AUTH`, file ops) and receive responses. The device maintains a **30‑second timeout** to accommodate multi‑step exchanges.

---

## Sequence of Events

**Preconditions**
- DESFire tag is activated and in RF field.
- Host has any required keys/auth data if secure messaging is used.

**Steps**
1. Construct **0x1102** with the native DESFire command APDU in `81`; set `82/83` as needed.
2. Send **0x1102** to the device.
3. Device forwards to the tag; gathers the response (including additional frames if required by the instruction).
4. Device returns a response with status and NFC/MIFARE data container.
5. Repeat as necessary for multi‑stage operations until complete.

**Error/Recovery**
- If a frame/CRC/security error occurs, rebuild the DESFire command with correct CMAC/ENC and retry within the timeout.

---

## Command Syntax

| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1102  | DESFire pass‑through |
| TLVs    | var.   | —       | See Request/Response TLVs |

### Request TLVs
| Tag | Len | Field / Meaning | Req |
|----:|:---:|------------------|:---:|
| 81  | var | **Command to Send** (native DESFire APDU/frames) | R |
| 82  | 01  | **Encryption Control** — 00: none, 01: encrypted | O |
| 83  | 01  | **Flow Control** — 00: expect more, FF: last | R |

### Response TLVs
| Tag | Len | Field / Meaning | Req |
|----:|:---:|------------------|:---:|
| 81  | 01  | **Tag Response Code** — 00: success, 01: failed | R |
| 82  | var | **Encryption Control** (mirrors request) | O |
| 84  | var | **NFC/MIFARE Data Container** (encrypted or plain) | R |

**Encrypted Data (84 payload)**: `/DFDF59`, `/DFDF50`, `/DFDF51`  
**Unencrypted Data (84 payload)**: `FC` container with optional `/DF7A`

---

## Examples — Full APDUs (Hex)

### Request — GET_VERSION
| Example (Hex) |
|---------------|
| AA 00 81 04 01 13 11 02 84 0F 11 02 81 05 90 60 00 00 00 82 01 00 83 01 00 |

### Response — GET_VERSION
| Example (Hex) |
|---------------|
| AA 00 81 04 82 13 11 02 82 04 01 00 00 00 84 14 11 02 81 02 91 AF 82 0C FC 0A DF 7A 07 04 08 01 30 00 13 05 |

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
- DESFire native `GET_VERSION` appears here as `90 60 00 00 00` within TLV `81`. Honor the 30‑second timeout for multi‑shot exchanges.
