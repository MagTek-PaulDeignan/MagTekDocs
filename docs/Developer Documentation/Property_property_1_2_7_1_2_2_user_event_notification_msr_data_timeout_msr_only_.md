---
title: Property 1.2.7.1.2.2 User Event Notification MSR Data Timeout (MSR Only)
layout: home
parent: Configuration
nav_order: 135
---

## Property 1.2.7.1.2.2 User Event Notification MSR Data Timeout (MSR Only)

---

- [Property 1.2.7.1.2.2 User Event Notification MSR Data Timeout (MSR Only)](#property-127122-user-event-notification-msr-data-timeout-msr-only)

---


Table 955 - Property 1.2.7.1.2.2 User Event Notification MSR Data
Timeout (MSR Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Bit Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.2.2 / 0x010207010202</td>
</tr>
<tr>
<td>Name</td>
<td>User Event Notification MSR Data Timeout</td>
</tr>
<tr>
<td>Description</td>
<td><p>This parameter defines the number of seconds the device waits for
the host to take action (by sending <strong>Command 0x1001 - Start
Transaction)</strong> after the device sends <strong>Notification 0x1001
- Device Information Update</strong> to report a User Event / Card
Swiped event. After this period of time passes, the device erases the
buffered card data from memory.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
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
<td><ul>
<li><p>0x00 = Invalid value. (will be converted to 0x02 in the
firmware)</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
</tr>
<tr>
<td>Default</td>
<td>0x02 (2 seconds)</td>
</tr>
</tbody>
</table>

Table 956 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104 010CD101 841A D101 8107 2B06010401F609 8501 01 890A E208E706E104E202C200 |

Table 957 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 820CD101 8204 00000000 8482001B D101 8107 2B06010401F609 8501 01 890B E209E707E105E203C2 0102 |

Table 958 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104 010DD111 841B D111 8107 2B06010401F609 8501 01 890B E209E707E105E203C2 0102 |

Table 959 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 820DD111 8204 00000000 8482001B D111 8107 2B06010401F609 8501 01 890B E209E707E105E203C2 0102 |

##