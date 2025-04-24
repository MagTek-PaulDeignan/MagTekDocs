---
title: About OIDs
layout: home
parent: Configuration
nav_order: 237
---

## About OIDs

For modular management of device functions, information, and settings,
this standard makes extensive use of Object Identifiers (also known as
Object IDs or OIDs) as defined in ***ITU-T X.660 \| ISO/IEC 9834-1***,
which can be found by searching for **X.660** in the publications on
[www.itu.int](http://www.itu.int).

OIDs are identifiers for any generic data element, and are managed by
standards bodies to be globally unique (much like web domains, IP
addresses, and Media Access Control MAC addresses). They are managed by
using a tree structure consisting of **nodes**, where the tree structure
is defined and controlled by a hierarchy of subordinate **Registration
Authorities**, each with their authority delegated by a Registration
Authority one level higher in the tree, starting with the root nodes
managed by ITU-T and ISO. The ***X.660*** standard for OIDs is
harmonized with the data representation standard of ***ASN.1*** via that
standard’s OBJECT IDENTIFIER and OID-IRI types. Every node is assigned a
**primary integer value** (or primary value for short) which serves to
uniquely identify the node, and may be assigned secondary identifiers
(such as strings) for human readability.

MagTek is the Registration Authority for the OID tree beginning at
**{iso(1) identified-organization(3) dod(6) internet(1) private(4)
enterprise(1) MagTek(15113)}** (using **value notation** of the
***ASN.1*** OBJECT IDENTIFIER type). The branch can also be represented
in numerical shorthand as **1.3.6.1.4.1.15113**, which is the
**encoding** form of the ***ASN.1*** OBJECT IDENTIFIER type.

Per ***X.660***, OIDs can be encoded in **constructed** form or
**primitive** form. The primitive form is a sequence of octets (bytes)
and is summarized in section **A.2 Octet Encoding of OIDs**. The
constructed form is a TLV data object and is summarized in section **A.3
TLV Encoding of OIDs**.

In many cases, the MagTek implementation of OID-based message elements
allows the host to specify an optional **Company ID** and **Tree
prefix** alongside a **Relative OID**, where the full OID is a
concatenation of the company ID, followed by the tree prefix, followed
by the relative OID. If a message does not include the optional company
ID or tree prefix, company ID is assumed to be the MagTek arc above, and
the tree prefix is assumed to be a reasonable sequence of additional
nodes based on the purpose and scope of the message.

##