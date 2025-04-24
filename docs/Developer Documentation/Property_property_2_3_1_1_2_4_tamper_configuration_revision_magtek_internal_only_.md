---
title: Property 2.3.1.1.2.4 Tamper Configuration Revision (MAGTEK INTERNAL ONLY)
layout: home
parent: Configuration
nav_order: 228
---

## Property 2.3.1.1.2.4 Tamper Configuration Revision (MAGTEK INTERNAL ONLY)

---

- [Property 2.3.1.1.2.4 Tamper Configuration Revision (MAGTEK INTERNAL ONLY)](#property-231124-tamper-configuration-revision-magtek-internal-only)

---


Table 1181 - Property 2.3.1.1.2.4 Tamper Configuration Revision (MAGTEK
INTERNAL ONLY)

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
<td>2.3.1.1.2.4 / 0x020301010204</td>
</tr>
<tr>
<td>Name</td>
<td>Tamper Configuration Revision</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report which tamper
configuration its security systems are currently using. Tampers are
configured and locked for security the first time a host calls
<strong>Command 0xF016 - Activate Device Security (MAGTEK INTERNAL
ONLY)</strong>, and the device determines and sets this property based
on the firmware version installed in the device at that time.</p>
<p>This property exists because the host can not determine which tamper
configuration the device is currently using by examining the currently
installed firmware version; if a host activates the device’s security
systems while the device is loaded with firmware that uses an earlier
tamper configuration, installing firmware that supports a newer tamper
configuration does not change the tamper configuration until an operator
resets the device’s security systems.</p>
<p>To reset the device’s security systems and change the tamper
configuration, an operator must first reset this property to <strong>Not
Configured</strong> by disconnecting all tamper-related power from the
device. For example, disconnect USB power, the rechargeable battery, and
the coin cell battery, which requires physical access to the inside of
the device. This process clears and unlocks the tamper configuration.
The host must then call <strong>Command 0xF016 - Activate Device
Security (MAGTEK INTERNAL ONLY)</strong> to activate the device’s
security systems again.</p></td>
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
<td><p>0x00 = Not Configured</p>
<p>0x01 = Original Configuration</p>
<p>0x02 = Coin Cell Current Optimized</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1182 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C400 |

Table 1183 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C401 02 |

#