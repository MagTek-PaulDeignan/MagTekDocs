---
title: 0x1001 — Start Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 1
---

# 0x1001 — Start Transaction

The host uses this command to start a payment transaction.

---

## Sequence of Events
1. If [Property 1.2.7.1.2.1 – User Event Notification Controls Enable](../Properties/#property-1-2-7-1-2-1) is enabled,  
   the cardholder may present a card before the host calls this command.  
   In that case, the device sends [Notification 0x1001 – Device Information Update](../Notifications/#notification-0x1001),  
   prompting the host to start a transaction.
2. **MSR Only**: Swiped data is temporarily stored per [Property 1.2.7.1.2.2 – User Event Notification MSR Data Timeout](../Properties/#property-1-2-7-1-2-2).
3. The host issues **0x1001 — Start Transaction**.
4. The device guides the cardholder through MSR, EMV Contact, Contactless, or Manual Entry (MCE).
5. The device returns transaction data and status.

---

## Applicability Matrix
| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|------------------------|----------|-----------------|----------|----------------|
| MSR (Swipe)           | ✅       | ✅              | ❌       | ✅              |
| EMV Contact           | ✅       | ✅              | ❌       | ✅              |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅              |
| MCE (Manual)          | ✅       | ✅              | ❌       | ❌              |
| Barcode Reader        | ✅       | ✅              | ✅       | ✅              |

---

## Command Syntax
| Field   | Length | Value   | Description       |
|---------|--------|---------|-------------------|
| Command | 2      | 0x1001  | Start Transaction |
| TLVs    | var.   | –       | Transaction data  |

---

### Required TLVs
| Tag    | Name                       | Description                                |
|--------|----------------------------|--------------------------------------------|
| DFDF4D | Transaction Control Flags  | Controls available interfaces and flow     |
| RAAT   | Reader Action/Access Type *(MagTek Internal Only)* | Specifies reader action |

---

### Parameter Table
| Parameter | Type     | Description                                                   |
|-----------|----------|---------------------------------------------------------------|
| DFDF4D    | Bitfield | Defines which card technologies are enabled.                  |
| RAAT      | Internal | Reserved for MagTek internal use.                             |

---

## Examples
*(Examples identical to your provided structure: MSR, EMV, CTLS, MCE — with request/response/payloads.)*
