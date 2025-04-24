---
title: Property 2.1.2.6.1.1 Firmware Git and Build information (MAGTEK INTERNAL ONLY)
layout: home
parent: Configuration
nav_order: 204
---

## Property 2.1.2.6.1.1 Firmware Git and Build information (MAGTEK INTERNAL ONLY)

---

- [Property 2.1.2.6.1.1 Firmware Git and Build information (MAGTEK INTERNAL ONLY)](#property-212611-firmware-git-and-build-information-magtek-internal-only)

---


Table 1130 - Property 2.1.2.6.1.1 Firmware Git and Build information
(MAGTEK INTERNAL ONLY)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.6.1.1 / 0x020102060101</td>
</tr>
<tr>
<td>Name</td>
<td>Firmware Git and Build information</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its firmware Git and
build information. Git bash command “git describe --long --dirty
--always” is used to return information about each repository “MAIN”,
“SDK”, “EXT” and “AMADIS” in the same order followed by the date and
time the firmware was built as a null terminated string.</p>
<p>An example of the string returned is
“MAIN[PCI-A3-20200929-61-g46efa1a-dirty]_SDK[PCI-A2-NO-LCD-20200930-2-g6b69d7f]_EXT[PCI-A3-20200929-14-g370c7f0]_AMADIS[PCI-A2-NO-LCD-20200930-4-g5957fb6]_[2020-11-17][14:48:03]”
where:</p>
<ul>
<li><p>“MAIN” means the main repository</p></li>
<li><p>“PCI-A3-20200929” is the last tag found in this
repository</p></li>
<li><p>“61” means there have been 61 commits made since this
tag</p></li>
<li><p>“g46efa1a” means the hash of the latest commit starts with
46efa1a</p></li>
<li><p>“dirty” means that the repository has uncommitted changes made
since the last commit</p></li>
<li><p>“[2020-11-17][14:48:03]” is the date and time the firmware was
built.</p></li>
</ul></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Compile time dependent</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>Compile time dependent</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1131 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020601 8902 C100 |

Table 1132 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104 8255D101 8204 00000000 848200C4 D101 8501 02 8704
01020601 898200B5 C18200B1
4D41494E5B5043492D41332D32303230303932392D36312D67343665666131612D64697274795D5F53444B5B5043492D41322D4E4F2D4C43442D32303230303933302D322D67366236396437665D5F4558545B5043492D41332D32303230303932392D31342D67333730633766305D5F414D414449535B5043492D41322D4E4F2D4C43442D32303230303933302D342D67353935376662365D5F5B323032302D31312D31375D5B31343A34383A30335D00</p>
<p>Text value:
MAIN[PCI-A3-20200929-61-g46efa1a-dirty]_SDK[PCI-A2-NO-LCD-20200930-2-g6b69d7f]_EXT[PCI-A3-20200929-14-g370c7f0]_AMADIS[PCI-A2-NO-LCD-20200930-4-g5957fb6]_[2020-11-17][14:48:03]</p></td>
</tr>
</tbody>
</table>

#