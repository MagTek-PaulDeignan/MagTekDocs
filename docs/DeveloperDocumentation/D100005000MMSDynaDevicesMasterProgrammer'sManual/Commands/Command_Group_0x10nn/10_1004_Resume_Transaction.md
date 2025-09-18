---
title: 0x1004 — Resume Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 4
---

# 0x1004 — Resume Transaction

Resumes a paused EMV transaction by providing the issuer/host decision (for example, ARPC) and any additional TLVs required to complete the flow.

---

## Sequence of Events

**Preconditions**
- A transaction was initiated with **0x1001 — Start Transaction** and reached a state where the device requires host/issuer input (e.g., online authorization path).
- The device has indicated a pause and is waiting for the host to resume.
- For **EMV Contact**, the ICC may still be present. For **Contactless**, the kernel context is retained briefly.

**Steps**
1. Host collects authorization data from the prior device response/notification.
2. Host performs online authorization and obtains decision and, if applicable, ARPC and issuer scripts.
3. Host constructs **0x1004** with TLVs:
   - `81` — Resume Code (e.g., `00` = waiting for ARPC).
   - `84` — ARPC Data (container that includes ARPC type and data).
   - `8A` — Authorization Response Code.
   - `86` — Transaction TLV Update (optional; issuer scripts/overrides).
4. Host sends **0x1004** to the device.
5. Device validates the TLVs (lengths, ARC/ARPC consistency).
6. **EMV Contact path**: performs EXTERNAL AUTHENTICATE; executes issuer scripts (71/72) if present; evaluates CVM/risk.
7. **EMV Contactless path**: applies decision and ARPC at the CTLS kernel layer; generates required AC per brand rules.
8. Device determines the final outcome (e.g., TC or AAC) and updates prompts (for ICC, may require **Remove Card**).
9. Device returns the 0x1004 response and any result TLVs.
10. Host finalizes tender (receipt, clearing).

**Error/Recovery**
- `69 85`: No resumable transaction → **0x1009 → (optional) 0x1014 → 0x1001**.
- `6A 80`: Invalid data → correct TLVs (ARC/ARPC mismatch) and reissue 0x1004.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| MSR (Swipe)           | ❌       | ❌              | ❌       | ❌             |
| EMV Contact           | ✅       | ✅              | ❌       | ✅             |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅             |
| MCE (Manual)          | ❌       | ❌              | ❌       | ❌             |

---

## Command Syntax

| Field   | Length | Value  | Description          |
|---------|--------|--------|----------------------|
| Command | 2      | 0x1004 | Resume Transaction   |
| TLVs    | var.   | —      | See Request TLVs     |

### Request TLVs

| Tag | Len | Field                           | Req | Notes                                       |
|----:|:---:|---------------------------------|:---:|---------------------------------------------|
| 81  | 01  | Resume Code                     | R   | `00` = host decision/ARPC present           |
| 84  | var | ARPC Data (includes ARPC Type)  | R   | Container for ARPC and related data         |
| 8A  | 02  | Authorization Response Code     | R   | e.g., `30 30` approve, `31 30` decline      |
| 86  | var | Transaction TLV Update          | O   | Issuer script(s) / TLV override if required |

---

## Examples — Full APDUs (Hex)

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 01 00 10 04 84 21 10 04 81 01 00 82 01 78 84 17 FF 74 14 DF DF 25 08 99 26 90 E1 16 12 07 10 FA 06 70 04 8A 02 30 30 |

### Response
| Example (Hex) |
|---------------|
| AA 00 81 04 82 06 10 04 82 04 00 00 00 00 84 02 10 04 |

---

## Error Conditions

| SW1SW2 | Meaning                                            |
|--------|-----------------------------------------------------|
| 9000   | Success                                             |
| 6985   | Conditions not satisfied (no resumable transaction) |
| 6A80   | Invalid data (malformed/mismatched TLVs)            |
| 6F00   | Unknown error                                       |

---

## Notes
- Ensure `8A` (ARC) matches the issuer decision implied by the ARPC container.
- Preserve order of issuer script tags if present (71 before 72).
- Do not interleave **0x1008 — Cancel** or a new **0x1001** while 0x1004 is in flight.
