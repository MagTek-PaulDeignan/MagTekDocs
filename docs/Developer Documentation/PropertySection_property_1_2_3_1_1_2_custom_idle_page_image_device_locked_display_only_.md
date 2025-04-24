---
title: Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display Only)
layout: home
parent: Configuration
nav_order: 119
---

## Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display Only)

Table 886- Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked
(Display Only)

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
<td>1.2.3.1.1.2 / 0x010203010102</td>
</tr>
<tr>
<td>Name</td>
<td>Custom Idle Page Image Device Locked</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set which custom image it
displays when idle and locked. If the selected image does not exist, the
device falls back to showing text. This property does not take effect
instantly; it takes effect the next time the device transitions to idle
(for example, after a transaction or after resetting). See
<strong>Device Lock Feature</strong> for more information.</p>
<ul>
<li><p>0x00 = Show text “Welcome” “Device is Locked”</p></li>
<li><p>0x01 = Show custom image 1</p></li>
<li><p>0x02 = Show custom image 2</p></li>
<li><p>0x03 = Show custom image 3</p></li>
<li><p>0x04 = Show custom image 4</p></li>
</ul>
<p>To use this feature, the host must first load an image into the
selected slot using <strong>Command 0xD812 - Start Send File to Device
(Unsecured)</strong>. Images must be BMP format, 160KB or smaller with
no compression, maximum 320px by 240px, with color depth 16 color, 256
color, 16-bit color, 24-bit color. Images smaller than the maximum size
are centered on the display. Note images at full screen size must be
16-bit color or lower to meet the size requirement.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any number</td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 887 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02030101 8902 C200 |

Table 888 - Get Response Example

| Example (Hex) |
|----|
| AA00 81 04 8255D101 82 04 00000000 84 820010 D101 85 01 01 87 04 02030101 89 03 C2 01 00 |

Table 889 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02030101 8903 C201 00 |

Table 890 - Set Response Example

| Example (Hex) |
|----|
| AA00 81 04 8255D111 82 04 00000000 84 820010 D111 85 01 01 87 04 02030101 89 03 C2 01 00 |

##