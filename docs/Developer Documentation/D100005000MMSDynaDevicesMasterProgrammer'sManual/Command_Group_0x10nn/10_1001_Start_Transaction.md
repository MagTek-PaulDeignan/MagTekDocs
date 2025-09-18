---
title: 0x1001 — Start Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 1
---

# 0x1001 — Start Transaction

Start a card-present transaction. The host sends TLVs with amount, currency, and type, plus entry options; the device drives MSR/ICC/CTLS UI and returns TLVs with SW1SW2.

---

## When to Use
- Beginning any payment that requires cardholder interaction.
- Preparing reader for specific entry modes (set `DF01`).

## Preconditions
- Device is **Idle** (no active transaction). Required parameters loaded. Sufficient power.

## Postconditions
- Device remains engaged until completion, cancel, or error. On success, result TLVs are returned.

## Sequence
```
Host SEND 0x1001  →  Device prompts/reads  →  Response TLVs (EMV/MSR)
```

---

## MSR — Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 23 9F 02 06 00 00 00 00 50 00 9A 03 25 09 18 9C 01 00 5F 2A 02 08 40 5F 36 01 02 DF 01 01 01 DF 02 02 00 3C |

## MSR — Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 1B 57 13 99 99 99 99 99 99 99 D2 51 22 01 12 34 56 78 9F 5A 08 99 99 99 99 99 99 99 90 00 |

---

## Contactless EMV — Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 23 9F 02 06 00 00 00 00 25 00 9A 03 25 09 18 9C 01 00 5F 2A 02 08 40 5F 36 01 02 DF 01 01 04 DF 02 02 00 1E |

## Contactless EMV — Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 1F 9F 27 01 40 9F 26 08 11 22 33 44 55 66 77 88 9F 10 07 06 01 12 03 A0 B0 01 9F 34 03 1E 03 00 90 00 |

---

## Contact (ICC, fallbacks allowed) — Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 1F 9F 02 06 00 00 00 01 00 00 9A 03 25 09 18 9C 01 00 5F 2A 02 08 40 DF 01 01 07 DF 02 02 00 3C |

## Contact (ICC) — Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 25 9F 27 01 40 9F 26 08 AA BB CC DD EE FF 00 11 9F 10 07 06 01 12 03 A0 B0 02 9F 36 02 00 2A 9F 37 04 12 34 56 78 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` conditions not satisfied (wrong state/interface)
- `6A 80` invalid data (bad TLV set)
- `6F 00` unknown

## Notes & Gotchas
- Choose one entry mode for fastest UX; use fallbacks only if required.
- Mask `5A` / `57` in logs; never store cryptograms unencrypted.
- Do not issue another `0x1001` until completion or **0x1008 Cancel**.
