---
title: 0x1008 — Cancel Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 5
---

# 0x1008 — Cancel Transaction

Cancels the in-progress transaction and returns the device to Idle.

---

## Sequence of Events

**Preconditions**
- A transaction is active or paused.

**Steps**
1. Host issues **0x1008 — Cancel Transaction**.
2. Device aborts active reader/kernel activity and clears prompts.
3. For **EMV Contact**, device may display **Remove Card** and wait for ICC removal.
4. Device returns a response and transitions to Idle.

**Error/Recovery**
- If the device does not report Idle after cancel, issue **0x1009 — Close/Clear**, then restart with **0x1001**.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| MSR (Swipe)           | ✅       | ✅              | ✅       | ✅             |
| EMV Contact           | ✅       | ✅              | ❌       | ✅             |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅             |
| MCE (Manual)          | ✅       | ✅              | ❌       | ❌             |

---

## Command Syntax

| Field   | Length | Value  | Description            |
|---------|--------|--------|------------------------|
| Command | 2      | 0x1008 | Cancel Transaction     |
| TLVs    | var.   | —      | None required          |

---

## Examples — Full APDUs (Hex)

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 01 13 10 08 84 02 10 08 |

### Response
| Example (Hex) |
|---------------|
| AA 00 81 04 82 13 10 08 82 04 00 00 00 00 |

---

## Error Conditions

| SW1SW2 | Meaning                          |
|--------|-----------------------------------|
| 9000   | Success                           |
| 6985   | No transaction in progress        |
| 6F00   | Unknown error                     |

---

## Notes
- Send **0x1008** once and wait for its response before issuing a new **0x1001**.
