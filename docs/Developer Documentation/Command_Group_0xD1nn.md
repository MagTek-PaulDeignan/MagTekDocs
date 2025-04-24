---
title: Command Group 0xD1nn - Settings and Information
layout: home
parent: Commands
nav_order: 6
---

## Command Group 0xD1nn - Settings and Information

---

- [Command Group 0xD1nn - Settings and Information](#command-group-0xd1nn---settings-and-information)
    - [Command 0xD101 - Get Property](#command-0xd101---get-property)
    - [Command 0xD111 - Set Property (Unsecured)](#command-0xd111---set-property-unsecured)
    - [Command 0xD112 - Set Property (Secured)](#command-0xd112---set-property-secured)
    - [Command 0xD201 - Reset Properties to Defaults (MAGTEK INTERNAL ONLY FOR NOW)](#command-0xd201---reset-properties-to-defaults-magtek-internal-only-for-now)

---


#### Command 0xD101 - Get Property

The host uses this command to get information about the device or its
configuration / settings.

Each data element representing device information or device
configuration is part of a tree of values and is uniquely identified by
an Object Identifier (also known as an Object ID or OID) as defined in
***ITU-T X.660 \| ISO/IEC 9834-1***, which can be found by searching for
**X.660** in the publications on [www.itu.int](http://www.itu.int). This
document refers to these data elements collectively as **Properties**.
The list of all properties and their corresponding OIDs and other
characteristics is provided in section **8 Configuration**.

This command can be used in multiple ways. For simplicity, this document
describes one possible way that does not require detailed knowledge of
the ***X.660*** specification.

To get a property, the sequence of events is as follows:

1)  The host determines which property or tree branch of properties it
    wants to get from the device (see section **8 Configuration**).

2)  The host composes the command request in the format below, and sends
    it to the device.

3)  The device sends a response. If the request succeeded, the response
    includes the value(s) of the requested property or properties. If it
    did not succeed, the device returns a failure response with no
    command-specific parameters.

Table 180 - Request Data for Command 0xD101 - Get Property

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">D101 = <strong>Command 0xD101 - Get
Property</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Company ID</p>
<p>This value is the root of the “long form” of the Property OID, and is
the same for all MagTek devices. Leave this parameter empty and use the
default.</p></td>
<td>B</td>
<td>O</td>
<td>2B 06 01 04 01 F6 09</td>
</tr>
<tr>
<td>82</td>
<td>03</td>
<td><p>Device Family ID</p>
<p>This value is the second portion of the “long form” of the Property
OID, and is the same for all similar MagTek devices within the same
product family. Unless you have a specific use case that uses this
parameter, leave this parameter empty and use the default otherwise your
software may not work with multiple products.</p>
<p>Byte 1 Platform</p>
<ul>
<li><p>0x02 = Apollo Platform</p></li>
</ul>
<p>Byte 2 Product</p>
<ul>
<li><p>0x01 = DynaFlex, 0x02 = DynaProx, 0x03 = DynaFlex II PED, 0x04 =
DynaFlex II, 0x05 = DynaFlex II Go</p></li>
</ul>
<p>Byte 3 Device Variant</p>
<ul>
<li><p>0x00 = Standard</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>Product dependent</td>
</tr>
<tr>
<td>85</td>
<td>01</td>
<td><p>Property Type</p>
<p>This parameter contains the first number of the Property OID as
documented in section <strong>8 Configuration</strong>.</p>
<ul>
<li><p>0x01 = Device Settings</p></li>
<li><p>0x02 = Device Information</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>87</td>
<td>var</td>
<td><p>Property OID Tree Prefix</p>
<p>This optional parameter contains subsequent numbers of the Property’s
OID as documented in section <strong>8 Configuration</strong>, but can
not include the final number.</p>
<p>This can also be populated with fewer numbers from the OID, in which
case the remaining numbers of the OID of the Property or set of
Properties you wish to retrieve must be included in the <strong>Property
OID Remainder</strong>.</p>
<p>For simplicity, populate this with the 2<sup>nd</sup> through the
second-to-last number in the property’s OID.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>Property OID Remainder</p>
<p>This contains the remaining numbers of the Property’s OID, BER TLV
encoded per <em><strong>X.660</strong></em> section <em><strong>8 Basic
encoding rules</strong></em>. For details about TLV encoding an OID. To
request a set of properties in a branch of the Property OID structure,
the host should pass a partial Property OID, and the device returns the
value of all properties from the specified tree level downward.</p>
<p>For simplicity, include all numbers except the final number of the
property’s OID in <strong>Property Type</strong> and <strong>Property
OID Tree Prefix</strong>, and include the final number of the OID OR
0xC0 here, then append constant byte 0x00. These two bytes represent a
single empty BER TLV primitive data object.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 181 - Response Data for Command 0xD101 - Get Property

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">D101 = <strong>Command 0xD101 - Get
Property</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Company ID</p>
<p>This contains the Company ID the host included in the request
message. If this parameter is not included in the request, the response
does not include it.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>82</td>
<td>03</td>
<td><p>Device Family ID</p>
<p>This contains the Device Family ID the host included in the request
message. If this parameter is not included in the request, the response
does not include it.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>85</td>
<td>01</td>
<td><p>Property Type</p>
<p>This contains the Property Type the host included in the request
message.</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>87</td>
<td>var</td>
<td><p>Property OID Tree Prefix</p>
<p>This contains the Property OID Tree Prefix the host included in the
request message. If this parameter is not included in the request, the
response does not include it.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>Property OID Remainder</p>
<p>This contains the same TLV-encoded portion of the OID the host
included in the Property OID Remainder of the request message, with leaf
nodes populated with actual values. If the host requested a set of
properties in a branch of the Property OID structure, this contains the
set of requested branches, including branch OIDs, leaf node IDs, and
values.</p>
<p>If the host follows the “for simplicity” recommendation in the
request message to request a single property, it can retrieve the value
of the requested property by stripping off the first few bytes, which
represent the TLV-encoded last number in the OID and the length of the
property’s value, as follows; the remaining bytes are the value of the
property:</p>
<ul>
<li><p>If the second byte is 7F or less, strip off the first two
bytes.</p></li>
<li><p>If the second byte is 81, strip off the first three
bytes.</p></li>
<li><p>If the second byte is 82, strip off the first four
bytes.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 182 - Request Example

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
<td><p>Get <strong>Property 1.2.7.1.1.1 Device Reset Occurred
Notification Control</strong> using “simple” form:</p>
<p>AA00 8104 0155D101 840F D101 8501 01 8704 02070101 8902 C100</p></td>
</tr>
</tbody>
</table>

Table 183 - Response Example

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
<td><p>Get <strong>Property 1.2.7.1.1.1 Device Reset Occurred
Notification Control</strong> using “simple” form:</p>
<p>AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070101
8903 C101 00</p></td>
</tr>
</tbody>
</table>

Table 184 - Request Example

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
<td><p>Get <strong>Property 1.2.7.1.1.1 Device Reset Occurred
Notification Control</strong> using longer Property OID Remainder:</p>
<p>AA00 8104 0155D101 8411 D101 8501 01 890A E208 E706 E104 E102
C100</p></td>
</tr>
</tbody>
</table>

Table 185 - Response Example

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
<td><p>Get <strong>Property 1.2.7.1.1.1 Device Reset Occurred
Notification Control</strong> using longer Property OID Remainder:</p>
<p>AA00 8104 8255D101 8204 00000000 84820012 D101 8501 01 890B E209 E707
E105 E103 C101 00</p></td>
</tr>
</tbody>
</table>

Table 186 - Request Example

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
<td><p>Get <strong>Property Subgroup 2.1.2.2.nn Core Firmware
Information</strong> using “simple” form:</p>
<p>AA00 8104 0155D101 840D D101 8501 02 8702 0102 8902 C200</p></td>
</tr>
</tbody>
</table>

Table 187 - Response Example

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
<td><p>Get <strong>Property Subgroup 2.1.2.2.nn Core Firmware
Information</strong> using “simple” form:</p>
<p>AA00 81 04 8255D101 82 04 00000000 84 820056 D101 85 01 02 87 02 0102
89 820049 E2 820045 E1 820004 C1 00 C2 00 E2 820039 C1 0D
44796E61466C65782050726F00 C2 13 313030303030373138332D41352D5043490000
C3 00 C4 0B 3130303030303731383300 C5 00 C6 02 FF00</p></td>
</tr>
</tbody>
</table>

#### Command 0xD111 - Set Property (Unsecured)

| <img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image19.png"
style="width:1.63in;height:0.3in"
alt="A black and white sign with letters AI-generated content may be incorrect." /> |
|----|
| Properties are stored in flash memory, which inherently has a limited number of read-write cycles before it begins to wear. For this reason, MagTek recommends setting properties as few times as possible over the lifecycle of the device. |

The host uses this command to set device configuration / settings that
do not require security. For setting properties that require security
see **Command 0xD112 - Set Property (Secured)**.

Each data element representing device configuration is part of a tree of
values and is uniquely identified by an Object Identifier (also known as
an Object ID or OID) as defined in ***ITU-T X.660 \| ISO/IEC 9834-1***,
which can be found by searching for **X.660** in the publications on
[www.itu.int](http://www.itu.int). This document refers to these data
elements collectively as **Properties**. The list of all properties and
their corresponding OIDs and other characteristics is provided in
section **8 Configuration**.

This command can be used in multiple ways. For simplicity, this document
describes one possible way that does not require detailed knowledge of
the ***X.660*** specification.

To set a property, the sequence of events is as follows:

1)  The host determines which property it wants to set and the value it
    wants to set in the device (see section **8 Configuration**).

2)  The host composes a command request in the format below, and sends
    it to the device.

3)  The device sends a response in the format below. If the request
    succeeded, the response payload is identical to the request payload.
    If it did not succeed, the device returns a failure response with no
    command-specific parameters.

Table 188 - Request Data for Command 0xD111 - Set Property (Unsecured)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">D111 = <strong>Command 0xD111 - Set Property
(Unsecured)</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Company ID</p>
<p>This value is the root of the “long form” of the Property OID, and is
the same for all MagTek devices. Leave this parameter empty and use the
default.</p></td>
<td>B</td>
<td>O</td>
<td>2B 06 01 04 01 F6 09</td>
</tr>
<tr>
<td>82</td>
<td>03</td>
<td><p>Device Family ID</p>
<p>This value is the second portion of the “long form” of the Property
OID, and is the same for all similar MagTek devices within the same
product family. Unless you have a specific use case that uses this
parameter, leave this parameter empty and use the default otherwise your
software may not work with multiple products.</p>
<p>Byte 1 Platform</p>
<p>0x02 = Apollo Platform</p>
<p>Byte 2 Product</p>
<ul>
<li><p>0x01 = DynaFlex, 0x02 = DynaProx, 0x03 = DynaFlex II PED, 0x04 =
DynaFlex II, 0x05 = DynaFlex II Go</p></li>
</ul>
<p>Byte 3 Device Variant</p>
<ul>
<li><p>0x00 = Standard</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>Product dependent</td>
</tr>
<tr>
<td>85</td>
<td>01</td>
<td><p>Property Type</p>
<p>This parameter contains the first number of the Property OID as
documented in section <strong>8 Configuration</strong>.</p>
<ul>
<li><p>0x01 = Device Settings</p></li>
<li><p>0x02 = Device Information</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>87</td>
<td>var</td>
<td><p>Property OID Tree Prefix</p>
<p>This optional parameter contains subsequent numbers of the Property’s
OID as documented in section <strong>8 Configuration</strong>, but can
not include the final number. For simplicity, populate this with the
2<sup>nd</sup> through the second-to-last number in the property’s
OID.</p>
<p>This can also be populated with fewer numbers from the OID, in which
case the remaining numbers of the OID must be included in the
<strong>Property OID Remainder</strong>.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>Property OID Remainder</p>
<p>This contains the remaining numbers of the Property’s OID, BER TLV
encoded per <em><strong>X.660</strong></em> section <em><strong>8 Basic
encoding rules</strong></em>. For details about TLV encoding an OID.</p>
<p>For simplicity, include all numbers except the final number of the
property’s OID in <strong>Property Type</strong> and <strong>Property
OID Tree Prefix</strong>, and include the final number of the OID OR
0xC0 here, then append a length corresponding one of the following, then
append the value to set the property to:</p>
<ul>
<li><p>If the length of the value you are setting is 0x7F or shorter,
include one byte equal to the length of the value.</p></li>
<li><p>If the length of the value you are setting is greater than 0x7F
but less than 0xFFFF, append 82, then two bytes equal to the length of
the value.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 189 - Response Data for Command 0xD111 - Set Property (Unsecured)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">D111 = <strong>Command 0xD111 - Set Property
(Unsecured)</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Company ID</p>
<p>This contains the Company ID the host included in the request
message. If this parameter is not included in the request, the response
does not include it.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>82</td>
<td>03</td>
<td><p>Device Family ID</p>
<p>This contains the Device Family ID the host included in the request
message. If this parameter is not included in the request, the response
does not include it.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>85</td>
<td>01</td>
<td><p>Property Type</p>
<p>This contains the Property Type the host included in the request
message.</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>87</td>
<td>var</td>
<td><p>Property OID Tree Prefix</p>
<p>This contains the Property OID Tree Prefix the host included in the
request message. If this parameter is not included in the request, the
response does not include it.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>Property OID Remainder</p>
<p>This contains the same TLV-encoded portion of the OID the host
included in the Property OID Remainder of the request message.</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Table 190 - Request Example

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
<td><p>Set <strong>Property 1.2.7.1.1.1 Device Reset Occurred
Notification Control</strong></p>
<p>AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 07 01 01 89 03
C1 01 00</p></td>
</tr>
</tbody>
</table>

Table 191 - Response Example

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
<td><p>Set <strong>Property 1.2.7.1.1.1 Device Reset Occurred
Notification Control</strong></p>
<p>AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01
87 04 02 07 01 01 89 03 C1 01 00</p></td>
</tr>
</tbody>
</table>

#### Command 0xD112 - Set Property (Secured)

| <img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image19.png"
style="width:1.63in;height:0.3in"
alt="A black and white sign with letters Description automatically generated" /> |
|----|
| Properties are stored in flash memory, which inherently has a limited number of read-write cycles before it begins to wear. For this reason, MagTek recommends setting properties as few times as possible over the lifecycle of the device. |

The host uses this command to set device configuration / settings
securely. Properties that require security should specify that they do
in their documentation. This command can also be used for properties
that do not require security.

The details, request data and response data of this command are
identical to what is documented in **Command 0xD111 - Set Property
(Unsecured),** however, the command must be structured and sent
according to what is documented in sequence of events 1-5 of **Command
0xD811 - Start Send File to Device (Secured)**.

#### Command 0xD201 - Reset Properties to Defaults (MAGTEK INTERNAL ONLY FOR NOW)

The host uses this command to reset the device’s Command 0xD201 - Reset
Properties to Defaults (MAGTEK INTERNAL ONLY FOR NOW) Properties to
their default values. It does not reset configuration values that are
set using **Command 0xD111 - Set Property (Unsecured)** or **Command
0xD112 - Set Property (Secured)**.

The sequence of events is as follows:

1)  The host composes a command request in the format below and sends it
    to the device.

2)  The device resets all properties to the default values specified by
    the command.

3)  The device sends a response in the format below.

4)  The device automatically resets and applies the new settings.

<table>
<caption><p>Table 192 - Request Data for Command 0xD201</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a>.</td>
</tr>
<tr>
<td colspan="6">D201= Command 0xD112 - Set Property (Secured)</td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Default Values to Use</p>
<ul>
<li><p>0x01 = Use Firmware Defaults (see section
<strong>8</strong>)</p></li>
<li><p>Other Values = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| D201= Command 0xD112 - Set Property (Secured) |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 193 - Response Data for Command 0xD201

Table 194 - Request Example

| Example (Hex)                      |
|------------------------------------|
| AA00 81040101D201 8405 D201 810101 |

Table 195 - Response Example

| Example (Hex)                  |
|--------------------------------|
| AA00 81048201D201 820400000000 |