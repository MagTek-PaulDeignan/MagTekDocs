---
title: 0x10nn – Transactions
layout: home
parent: Commands
nav_order: 1
---

# 0x10nn – Transactions

Developer-ready command set for card-present transactions. Each page includes **When to Use**, **Preconditions**, **Sequence**, **Full Request/Response APDUs**, **Status/Errors**, and **Notes & Gotchas**.

---

## Flow Overview
```
0x1001 Start
   ├─► 0x1004 Resume / 0x1002 Continue (as required)
   ├─► 0x1003 Finalize or 0x1008 Cancel
   └─► 0x1009 Close/Clear for recovery; 0x1014 Get Status if uncertain
```
