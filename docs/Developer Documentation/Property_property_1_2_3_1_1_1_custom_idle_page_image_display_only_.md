---
title: Property 1.2.3.1.1.1 Custom Idle Page Image (Display Only)
layout: home
parent: Configuration
nav_order: 118
---

## Property 1.2.3.1.1.1 Custom Idle Page Image (Display Only)

---

- [Property 1.2.3.1.1.1 Custom Idle Page Image (Display Only)](#property-123111-custom-idle-page-image-display-only)

---


Table 881- Property 1.2.3.1.1.1 Custom Idle Page Image (Display Only)

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
<td>1.2.3.1.1.1 / 0x010203010101</td>
</tr>
<tr>
<td>Name</td>
<td>Custom Idle Page Image</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set which custom image it
displays when idle. If the selected image does not exist, the device
falls back to showing text. This property does not take effect
instantly; it takes effect the next time the device transitions to idle
(for example, after a transaction or after resetting).</p>
<ul>
<li><p>0x00 = Show text “Welcome”</p></li>
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

Table 882 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E1 02 C1 00 |

Table 883 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E1 03 C1 01 03 |

Table 884 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E1 03 C1 01 03 |

Table 885 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E1 03 C1 01 03 |

##