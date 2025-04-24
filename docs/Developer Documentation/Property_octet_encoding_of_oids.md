---
title: Octet Encoding of OIDs
layout: home
parent: Configuration
nav_order: 238
---

## Octet Encoding of OIDs

---

- [Octet Encoding of OIDs](#octet-encoding-of-oids)

---


In addition to human-readable ***ASN.1*** value notation and encoding
forms above, OIDs can be encoded as binary values (octets) as follows
(per ***X.660*** section ***8.19 Encoding of an object identifier
value***):

1)  Start with the numerical form (for example, MagTek’s arc
    **1.3.6.1.4.1.15113** from section **A.1**).

2)  Multiply the primary value of the first node in the OID by 40
    decimal (e.g., 1\*40=40) and add it to the primary value of the
    second node. The sum is used as the first byte (e.g., 43 decimal =
    **0x2B**) of the octet form. The first two nodes receive this
    special treatment because their possible value ranges are expected
    to remain very small indefinitely.

3)  The next bytes in the octet encoded form are simply equal to each
    primary value in the OID sequence, unless the primary value is
    greater than 128 decimal (0x80). For primary values greater than
    0x80, additional encoding rules apply that are not necessary to
    detail here, because for simplicity MagTek selects OID primary
    values that are equal to 0x79 or less (and in many cases, 0x30 or
    less); In addition, TLV encoding places additional restrictions on
    selection of OID, in that if the OID is to be used directly as a tag
    in a TLV data object, it must not be greater than 0x1F (see section
    **3.2.1.1 About TLV Encoding**). The only portion of MagTek’s arc
    that is subject to these additional encoding rules is the primary
    value **15113** at the end, which encodes to **0xF609** hex (per the
    rules not detailed here, see ***X.660*** for details). The full arc
    **1.3.6.1.4.1.15113** therefore encodes to **0x2B 06 01 04 01
    F609**.

#