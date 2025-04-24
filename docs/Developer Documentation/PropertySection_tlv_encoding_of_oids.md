---
title: TLV Encoding of OIDs
layout: home
parent: Configuration
nav_order: 239
---

## TLV Encoding of OIDs

The primary method of encoding OIDs, as specified in ***X.660*** section
***8 Basic encoding rules***, is BER Tag-Length-Value (TLV) format. A
TLV-encoded OID is a set of nested TLV data objects, where:

- The **tag** of each TLV data object equals the primary value of the
  node it represents in the OID sequence, encoded according to the BER
  TLV tag number rules; the assigned primary values in this standard are
  all **private** (11nnnnnn), the bottom level value / leaf of any OID
  arc is encoded as **primitive** (nn0nnnnn), and the levels above it
  are encoded as **composed** (nn1nnnnn). This information makes it
  possible to use the bit definitions for **Tag** in section **3.2.1
  Tag-Length-Value (TLV) Encoding** as a reference to encode each level
  of the OID as a tag. Generally the primary values in this standard are
  selected to be less than 0x1F, and so do not require multi-byte tags.

- The **length** of each TLV data object, like all TLV data objects, is
  equal to the length of its value.

- The **value** of each TLV data object is equal to a nested TLV data
  object containing all subsequent nodes in the OID sequence, so
  TLV-encoded OIDs must be built from the bottom up. The primitive value
  in the bottom node of a TLV-encoded OID is the set of actual values
  contained by that OID (e.g., string, byte\[s\], and so on), or in the
  case of requests where the value is (by definition) not known to the
  requester, the length is **0x00**.

For example, the process of TLV encoding the OID in a request to
retrieve the contents of **OID 3.5.7.9** with 9 being a leaf node looks
like this (all values are hexadecimal unless otherwise noted):

1)  First, realize OID 3.5.7.9 is to be interpreted as a nested set of
    containers. Node 3 contains node 5, which contains node 7, which
    contains node 9. Although node 9 presumably contains one or more
    values, the entity making the request for its contents, by
    definition, does not know the contents when composing the request,
    so in this example, node 9 is treated like an “empty bucket.” In the
    corresponding response, node 9 would include its actual contents.

2)  Because TLV is built from the inside out (bottom up), start the
    encoding process with the node at the end which has a primary value
    equal to 9. Like all OIDs in this standard it is **private**, and
    because it is a leaf node at the bottom / end of the OID tree and
    therefore does not contain any further nested TLV data objects, it
    is **primitive**: 0x09 primary value OR 0b11000000 private OR
    0b00000000 primitive = **C9**. As explained above, in this case it
    is an empty bucket, so its length is **00**. Its TLV encoding is
    **C9 00**.

3)  Up one level to the node with primary value equal to 7, it is also
    **private**, but unlike the previous level it contains a nested TLV
    data object (C9 00 from above) so it is **constructed** instead of
    primitive: 0x07 primary value OR 0b11000000 private OR 0b00100000
    constructed = **E7**. It has contents C9 00 so length is **02**. Its
    TLV encoding is **E7 02 C9 00**.

4)  Up one level to the node with primary value 5, it is **private** and
    contains TLV data object E7 02 C9 00 from above, so it is
    **constructed**: 0x05 primary value OR 0b11000000 private OR
    0b00100000 constructed = **E5**. It has contents E7 02 C9 00 so
    length is **04**. Its TLV encoding is **E5 04 E7 02 C9 00**.

5)  Up to the root with primary value 3, it is **private** and
    **constructed** so tag is **E3**, value is the TLV data object from
    above, so length is equal to that object’s length **06**. Its
    encoding is **E3 06 E5 04 E7 02 C9 00**, which is the final encoding
    of whole “empty bucket” OID **3.5.7.9**.

#