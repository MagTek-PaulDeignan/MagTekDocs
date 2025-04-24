---
title: Command Group 0x1Fnn - Device Control
layout: home
parent: Commands
nav_order: 4
---

## Command Group 0x1Fnn - Device Control

---

- [Command Group 0x1Fnn - Device Control](#command-group-0x1fnn---device-control)
    - [Command 0x1F01 - Reset Device](#command-0x1f01---reset-device)
    - [Command 0x1F02 - Set Notification Subscriptions](#command-0x1f02---set-notification-subscriptions)
    - [Command 0x1F03 - Extend Session (Session Management Only)](#command-0x1f03---extend-session-session-management-only)
    - [Command 0x1F04 – Terminate Bluetooth® LE Connection (Bluetooth® LE Only)](#command-0x1f04-–-terminate-bluetooth®-le-connection-bluetooth®-le-only)
    - [Command 0x1F05 – Erase All Bluetooth® LE Bonds (Bluetooth® LE Only)](#command-0x1f05-–-erase-all-bluetooth®-le-bonds-bluetooth®-le-only)

---


#### Command 0x1F01 - Reset Device

The host uses this command to reset the device.

The sequence of events is as follows:

1)  The host constructs the command request for **Command 0x1F01 - Reset
    Device** in the format below.

2)  The host sends the command request to the device.

3)  The device sends a response in the format below to the host.

4)  The device starts an automatic reset within 500ms.

Table 152 - Request Data for Command 0x1F01 - Reset Device

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
<td colspan="6">1F01 = <strong>Command 0x1F01 - Reset
Device</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Power Off Option</p>
<ul>
<li><p>0x00 = Reset</p></li>
<li><p>0x01 = Power Off</p></li>
</ul>
<p>Power off only works while a device is running on its battery. If a
device is powered off while it is powered by USB, the device will
immediately turn back on.</p></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 153 - Response Data for Command 0x1F01 - Reset Device

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1F01 = **Command 0x1F01 - Reset Device** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 154 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 12 1F 01 84 02 1F 01 |

Table 155 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 12 1F 01 82 04 00 00 00 00 |

#### Command 0x1F02 - Set Notification Subscriptions

The host uses this command to specify which notifications the device
should send on each of its available interfaces. By default, the device
sends notifications to the host on all interfaces.

The sequence of events is as follows:

1)  The host constructs the command request in the format below.

2)  The host sends the command request to the device.

3)  The device sends a response in the format below to the host.

4)  The device immediately begins routing notifications per the request.

5)  If the device restarts or loses power, the device resets its
    notification subscriptions to defaults, and the host must call this
    command again to change them.

Table 156 - Request Data for Command 0x1F02 - Set Notification
Subscriptions

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
<td colspan="6">1F02 = <strong>Command 0x1F02 - Set Notification
Subscriptions</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Subscribe</p>
<ul>
<li><p>0x00 = Unsubscribe</p></li>
<li><p>0x01 = Subscribe</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x01</td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Notifications Affected</p>
<ul>
<li><p>0x00 = Only subscribe or unsubscribe to notification messages in
the Notification Message ID List parameter</p></li>
<li><p>0x01 = Subscribe or unsubscribe to all notifications</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x01</td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td><p>Notification Message ID List</p>
<p>List of two-byte Notification Message IDs (MSB first) from section
<strong>7 Notifications</strong> to be subscribed / unsubscribed by this
command. For example, to subscribe to <strong>Notification 0x0105 -
Transaction Operation Complete</strong> on the interface being used to
send this command, the host would include 0x0105 as two bytes in the
list. The device ignores any Notification Message IDs in the list that
do not exist.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>A4</td>
<td>var</td>
<td><p>Interfaces</p>
<p>List of interfaces this command should change the subscription
settings for. If the host does not specify any interfaces here, the
command applies only to the interface the host is using to send the
command.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/81</td>
<td>00</td>
<td>Apply changes to the USB interface</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>00</td>
<td>Apply changes to the WLAN interface</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>00</td>
<td>Apply changes to the Bluetooth® LE interface</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/84</td>
<td>00</td>
<td>Apply changes to the UART interface</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 157 - Response Data for Command 0x1F02 - Set Notification
Subscriptions

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1F02 = **Command 0x1F02 - Set Notification Subscriptions** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 158 - Request Example

| Example (Hex)               |
|-----------------------------|
| AA00 810401551F02 8402 1F02 |

Table 159 - Response Example

| Example (Hex)                            |
|------------------------------------------|
| AA00 810482551F02 820400000000 8402 1F02 |

#### Command 0x1F03 - Extend Session (Session Management Only)

The host can use this command to extend a session for open protocol
interfaces, such as the WLAN interface, which require session management
to meet PCI requirements.

The sequence of events is as follows:

1)  The host establishes a session with the device on a given interface.
    For the WLAN interface, a session starts when the host establishes a
    TLS websocket connection with the device.

2)  The device starts a countdown timer for a 30 minute session timeout
    period.

3)  Five minutes before the session timeout period expires, the device
    starts repeatedly (every minute) sending **Notification 0x1001 -
    Device Information Update** to report **Session Management / Session
    Expiring Soon**.

4)  The host may extend the session multiple times, until the device
    automatically resets to meet PCI’s 24 hour self-test requirement, by
    sending any command request using the same interface before the
    timeout occurs. Upon receiving the command, the device resets the
    session countdown timer to 30 minutes. This helps prevent the
    session from expiring while the host is actively using the device,
    including when the device is performing a transaction. If the host
    wants to extend the session but does not need to send another
    command, it may follow these steps at any time during the session:

    1)  The host constructs the command request in the format below.

    2)  The host sends the command request to the device.

    3)  The device sends a response in the format below to the host.

    4)  The device resets the session countdown timer to 30 minutes.

5)  When the session expires, the device closes the websocket
    connection.

For the WLAN interface, if the device is configured to allow connections
to more than one client at the same time with **Property 1.2.2.1.1.A
Maximum Client Connections** and more than one client is connected, then
the following applies. There is always only a single session and it
applies to all clients. There is not a separate session for each client.
The session starts when the first client connects. Only one client needs
to send a command on its connection to extend the session. The other
clients do not need to send any commands. When the session expires, all
clients will be disconnected.

Table 160 - Request Data for Command 0x1F03 - Extend Session (Session
Management Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| 1F03 = **Command 0x1F03 - Extend Session (Session Management Only)** |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 161 - Response Data for Command 0x1F03 - Extend Session (Session
Management Only)Extend Session

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1F03 = **Command 0x1F03 - Extend Session (Session Management Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 162 - Request Example

| Example (Hex)               |
|-----------------------------|
| AA00 810401551F03 8402 1F03 |

Table 163 - Response Example

| Example (Hex)                            |
|------------------------------------------|
| AA00 810482551F03 820400000000 8402 1F03 |

#### Command 0x1F04 – Terminate Bluetooth® LE Connection (Bluetooth® LE Only)

The host can use this command to terminate a Bluetooth® LE connection.
The host may also be able to terminate a Bluetooth® LE connection
directly without using this command.

The sequence of events is as follows:

1)  The host constructs the command request for **Device in** the format
    below.

2)  The host sends the command request to the device.

3)  The device sends a response in the format below to the host.

4)  The device terminates the Bluetooth® LE connection within around
    500ms.

Table 164 - Request Data for Command 0x1F04 – Terminate Bluetooth® LE
Connection

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| 1F04 = **Command 0x1F04 – Terminate Bluetooth® LE Connection** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 165 - Response Data for Command 0x1F04 – Terminate Bluetooth® LE
Connection

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1F04 = **Command 0x1F04 – Terminate Bluetooth® LE Connection** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 166 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 55 1F 04 84 02 1F 04 |

Table 167 - Response Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 82 55 1F 04 82 04 00 00 00 00 84 02 1F 04 |

#### Command 0x1F05 – Erase All Bluetooth® LE Bonds (Bluetooth® LE Only)

The host can use this command to erase all Bluetooth® LE bonds. The user
should then forget the device and re-pair the device on any host that it
was previously paired with if that host needs to communicate with the
device again.

The sequence of events is as follows:

1)  The host constructs the command request for **Command 0x1F01 - Reset
    Device** in the format below.

2)  The host sends the command request to the device.

3)  The device sends a response in the format below to the host.

4)  The device erases all Bluetooth® LE bonds within around 500ms.

Table 168 - Request Data for Command 0x1F05 – Erase All Bluetooth® LE
Bonds

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| 1F05 = **Command 0x1F05 – Erase All Bluetooth® LE Bonds** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 169 - Response Data for Command 0x1F05 – Erase All Bluetooth® LE
Bonds

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1F05 = **Command 0x1F05 – Erase All Bluetooth® LE Bonds** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 170 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 55 1F 05 84 02 1F 05 |

Table 171 - Response Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 82 55 1F 05 82 04 00 00 00 00 84 02 1F 05 |