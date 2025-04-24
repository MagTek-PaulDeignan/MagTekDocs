---
title: Design Intent (MAGTEK INTERNAL ONLY)
layout: home
parent: Configuration
nav_order: 240
---

## Design Intent (MAGTEK INTERNAL ONLY)

The main body of this document describes MMS from a customer’s point of
view. However, when MagTek firmware engineers need to make decisions
about extending or modifying the standard, there are additional factors
that are important to the design that are not important to customers.
For example, although the first release of MMS includes four Message
Types, it may become necessary in the future to add another one, and in
that case, the design intent behind the existing Message Type numbers
becomes an important consideration, because dependent software may make
assumptions that rely on certain “invisible rules” being consistently
followed. This section collects the design factors to consider.

#