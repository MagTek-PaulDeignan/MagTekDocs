---
title: Property 1.1.2.2.1.2 ISO/ABA Masking Character
layout: home
parent: Configuration
nav_order: 36
---

## Property 1.1.2.2.1.2 ISO/ABA Masking Character

Table 506 - Property 1.1.2.2.1.2 ISO/ABA Masking Character

| Property Description |  |
|----|----|
| Property OID | 1.1.2.2.1.2 / 0x010102020102 |
| Name | ISO/ABA Masking Character |
| Description | The device uses this property to determine what character it should use when sending masked ISO/ABA track data. If the **Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction** is enabled, the masked portions of the track will always be masked with ‘0’. For more information about masking, see the information at the bottom of this section. |
| Securing Key | None |
| Min. Len (b) | 0x00 |
| Max. Len (b) | 0x01 |
| Data Type | Character |
| Valid Values | Any ASCII character |
| Default | ‘0’ |

Table 507 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 17 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C2 00 |

Table 508 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 17 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C2 01 2A |

Table 509 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C2 01 30 |

Table 510 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0F D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C2 01 30 |

When the device sends masked track data, it replaces some characters in
the track data with a specified mask character. The specific characters
the device masks depends on the card encode type. The device only
selectively masks data that came from ISO/ABA cards (Financial Cards
with ***ISO/IEC 7813*** Format code B); it sends data from all other
card types entirely unmasked.

The device masks all fields from ISO/ABA cards except a number of
configurable leading and trailing characters of the PAN. See **Property
1.1.2.2.1.3 PAN Number of Leading Unmasked Characters** and **Property
1.1.2.2.1.4 PAN Number of Trailing Unmasked Characters**.

For chip card transactions, masked track 2 data is contained in TLV data
object DFDF4D. For magnetic stripe transactions, masked track 1, 2 and 3
data is contained in TLV data objects DFDF31, DFDF33 and DFDF35,
respectively.

**Table 511** **below** provides an example of data from tracks 1, 2,
and 3 of an ISO/ABA card after it has been decrypted or if the device
has sent it in the clear. **Table 512** shows the same data as it might
appear with a specific set of masking rules applied.

Table 511 - Sample ISO/ABA Track Data, Clear Text / Decrypted

| Sample ISO/ABA Track Data, Clear Text / Decrypted |  |
|----|----|
| Track 1 | %B6011000995500000^ TEST CARD ^15121015432112345678? |
| Track 2 | ;6011000995500000=15121015432112345678? |
| Track 3 | ;6011000995500000=15121015432112345678333333333333333333333? |

Table 512 - Sample ISO/ABA Track Data, Masked

| Sample ISO/ABA Track Data, Masked |  |
|----|----|
| Track 1 | %B6011000020000000^0000000000^00000000000000000000? |
| Track 2 | ;6011000020000000=00000000000000000000? |
| Track 3 | ;6011000020000000=00000000000000000000000000000000000000000? |

##