---
title: Connection Types
layout: default
parent: MMS Dyna Devices Master Programmer's Manual
nav_order: 3
---

# Connection Types
Connection Types

**Table 2** on page **36** includes a list of connection types available for
each device. The following subsections provide details developers will need to
communicate with the device using each connection type.

## How to Use USB Connections (USB Only)

These USB devices conform to the USB specification revision 1.1. They also
conform to the Human Interface Device (HID) class specification version 1.1.
This document assumes the audience is familiar with USB HID class
specifications, which are available at [**www.usb.org**](http://www.usb.org).
MagTek strongly recommends becoming familiar with that standard before trying to
communicate with the device directly via USB.

These devices are full-speed, high-powered USB devices that draw power from the
USB bus they are connected to. They enter and wake up from Suspend mode when
directed to do so by the USB host. They do not support remote wakeup.

When connecting via USB, MMS devices connect to the USB host as a
**vendor-defined** Human Interface Device. MMS devices identify themselves to
the host with MagTek’s vendor ID **0x0801**. DynaFlex products report as Product
ID (PID) **0x2020**, DynaProx products report as Product ID (PID) **0x2023 and
DynaFlex II Go report as Product ID (PID) 0x2024**.

Details for exchanging messages with the device are provided in the sections
that follow.

### About USB Reports, Usages, Usage Pages, and Usage IDs

All USB HID devices send and receive data using **Reports**. Each report may
contain several sections, called **Usages**, each of which has its own unique
four-byte (32-bit) identifier. The two most significant bytes of a usage are
called the **usage page**, and the two least significant bytes are called the
**usage ID**. Vendor-defined HID device usages must have a usage page in the
range **0xFF00 - 0xFFFF**, and it is common practice for related usage IDs share
the same usage page. For these reasons, all usages for MMS devices use
vendor-defined usage page **0xFF00**, **Magnetic Stripe Reader**.

HID reports used by the host can be divided into two types:

-   **Output Reports**, which the host uses to send messages (such as commands)
    to the device.
-   **Input Reports**, which the device uses to send messages (such as responses
    and unsolicited notifications) to the host.

For information about using output reports to send command messages to / receive
response messages from the device, see section **2.1.3 How to Send Command
Requests Using the USB Connection**. For information about receiving unsolicited
data from the device, see section **2.1.4 How to Receive Data Using the USB
Connection (HID Only)**.

### How to Connect to a Device Using the USB Connection

The steps for a host to connect to the device using the USB connector are the
same as connecting to any USB HID device, and are platform specific. The general
steps regardless of platform are as follows:

-   Enumerate the USB devices connected to the host.
-   Locate the desired device by PID.
-   Open the USB connection.
-   Read the report descriptor.
-   Begin listening for incoming reports, and sending data using outgoing
    reports.

### How to Send Command Requests Using the USB Connection

MMS communication between the host and the device consists of **Messages**,
which are independent of connection type and are documented in section **2.7**.
This section focuses specifically on how to use the device’s USB HID connection
to transmit a **Command** to the host by composing and sending a **Request
Message**, then listening for and interpreting the corresponding **Response
Message**.

When the device is connected to the host via USB, the host sends one or more
**Output Reports** to the device to send the requests for commands, and listens
/ waits for the device to send one or more **Input Reports** containing a
response (see section **2.1.1**). All reports use Usage Page **0xFF00**, Usage
ID **0x20**, and no Report ID (which some platform libraries present to the
calling software as Report ID 0x00).

The host may send Output Reports by using either the default **Control** pipe or
the Interrupt OUT pipe using a blocking call to the platform’s USB libraries.
The device ACKs all Output Reports immediately. Upon detecting the ACK for the
last Output Report in the message stream, the host software can immediately
begin listening for one or more follow-up Input Reports containing the device’s
response.

Some messages defined in section **2.7** may exceed the maximum packet length
allowed by USB HID. For this reason, MMS implements a packetizing scheme the
host must use when it composes Output Reports to send commands, and when it
decomposes Input Reports to receive responses. The host should follow this
general sequence to send a request and receive a response:

1.  Choose the command to invoke from section **6 Commands**.
2.  Construct the command request message using the **Request** table in the
    command documentation. For a deeper explanation of the contents of request
    tables, see section **2.7**.
3.  .
4.  Determine the complete length of the command request message.
5.  Examine the device’s **Report Descriptor** to determine what payload length
    the device expects for an Output Report (operating system libraries may
    refer to this length as the “Report Length” or “Report Count”). MMS devices
    using USB HID generally use a payload length of 64 bytes.
    1.  If the message length fits the **Single Packet** payload length of 62
        bytes, wrap the message in the Single Packet format shown in **Table
        4**.
    2.  If the message length does not fit the Single Packet payload length,
        wrap the message in the format of a single **Multi-Packet Head**,
        followed by zero or more **Multi-Packet Middles** as necessary, followed
        by one **Multi-Packet Tail**, as shown in **Table 5**, **Table 6**, and
        **Table 7**. If necessary, the host can cancel in the middle of a
        Multi-Packet message using the **Multi-Packet Cancel** packet shown in
        **Table 8**.
6.  For each packet, send an Output Report to the device, and wait for the
    device to ACK the output report USB packet. Upon ACK, either send the next
    packet in the sequence (if any), or begin listening for an Input Report
    containing the device’s response message [see section **2.1.4 How to Receive
    Data Using the USB Connection (HID Only)**]. If an ACK does not arrive, time
    out and assume the command needs to be started again.
7.  Strip wrappers off the device’s response in exactly the same way you
    constructed the command (using either Single Packet format or Multi-Packet
    format), and recompose the response message. Be sure to assemble the packets
    in the correct order using **Packet Number**, and to truncate the padding
    based on **Message Length** or **Remaining Message Length**.
8.  Parse the final response message using the Response table in the
    documentation for the command.

Table 4 - Single Packet Format

| Byte Offset | Field Name         | Field Value                          |
|-------------|--------------------|--------------------------------------|
| 0           | Packet Type        | 0x00 = Single Packet                 |
| 1           | Message Length     | Message length, denoted as **N**     |
| 2..N+1      | Message            | Message exactly from section **2.7** |
| N+2..63     | Padding, if needed | 0x00                                 |

Table 5 - Multi-Packet Head Format

| Byte Offset | Field Name     | Field Value                                                                                                      |
|-------------|----------------|------------------------------------------------------------------------------------------------------------------|
| 0           | Packet Type    | 0x01 = Multi-packet Head                                                                                         |
| 1..4        | Message Length | Total message length before decomposing into packets, denoted as **N**. If 62 or less, use Single Packet Format. |
| 5..63       | Message Part   | First 59 bytes of message from section **2.7**                                                                   |

Table 6 - Multi-Packet Middle Format

| Byte Offset | Field Name    | Field Value                                                                              |
|-------------|---------------|------------------------------------------------------------------------------------------|
| 0           | Packet Type   | 0x02 = Multi-Packet Middle                                                               |
| 1..2        | Packet Number | 0x0001 = First Multi-Packet Middle 0x0002 = Second Multi-Packet Middle Etc. up to 0xFFFF |
| 3..63       | Message Part  | Next 61 bytes of message from section **2.7**                                            |

Table 7 - Multi-Packet Tail Format

| Byte Offset | Field Name               | Field Value                                                                                       |
|-------------|--------------------------|---------------------------------------------------------------------------------------------------|
| 0           | Packet Type              | 0x03 = Multi-Packet Tail                                                                          |
| 1           | Remaining Message Length | Number of bytes of the message that are being transmitted in this final packet, denoted as **n**. |
| 2..n+1      | Message Part             | Final n bytes of message exactly as described in section **2.7**                                  |
| n+2..63     | Padding, if needed       | 0x00                                                                                              |

Table 8 - Multi-Packet Cancel Format

| Byte Offset | Field Name        | Field Value                |
|-------------|-------------------|----------------------------|
| 0           | Packet Type       | 0x04 = Multi-Packet Cancel |
| 1..2        | Reason for Cancel | 0x0000 = General           |
| 3..63       | Padding           | 0x00                       |

### How to Receive Data Using the USB Connection (HID Only)

MMS devices use the same mechanism to send **Response** messages to host
commands and to send unsolicited **Notifications** to the host when events
occur, such as device state changes or user interactions.

When the device communicates with the host as a vendor-defined HID device, it
sends messages to the host via an Input Report, which it sends to the host using
the **USB Interrupt IN** pipe. Per the USB HID standard, the host polls the
device on a regular Polling Interval to see if the device has input reports
available to send. If the device does not, it responds to the host’s poll with a
USB NAK.

The host software should always be listening for **Input Reports** from the
device containing notification messages and command response messages.
Assembling and parsing the incoming message is the same in both cases, but
notification messages, which are generally unpredictable, need to be routed to
different handlers than responses, which are generally anticipated after sending
a command. All input reports use Usage Page **0xFF00**, Usage ID **0x20**.
Because MMS devices only implement one input report, the input report they send
to the host does not include an Input Report ID (which some operating system
libraries present to the calling software as Input Report ID 0x00), in
accordance with the USB HID specification.

Some response and notification messages defined in section **2.7** may exceed
the maximum packet length allowed by USB HID. If the message can’t fit into one
packet, the device sends multiple packets, each containing partial message data
using the same message packet structures described in section **2.1.3**, **Table
4**, **Table 5**, **Table 6**, **Table 7**, **Table 8**.

Upon receiving an input report, the host can determine the size of message
packet Input Reports by looking at the HID report descriptor. The host can
locate a specific data element in the report by finding the corresponding Usage
and interpreting its contents as binary data. Because MMS devices use a single
usage to hold the Input Report contents, unlike devices that divide the Input
Report contents into length-delimited Usages, the host software can hard-code
its method of finding the packet data; it is not necessary for the host software
to examine the Report Descriptor for information about separate data elements’
offsets upon receiving a packet.

The host should follow this general sequence to process incoming Input Reports:

1.  Register a listener with the operating system USB library to have the
    relevant Input Reports routed to the host software for processing.
2.  When an Input Report arrives, knowing from section **2.1.1** that the device
    uses **Usage Page 0xFF00**, and knowing the desired data is found in the
    usage with **Usage ID 0x0020**, call the platform’s USB SDK to retrieve the
    data from **Usage 0xFF000020** in the input report.
3.  Interpret the blob of data according to tables in section **2.1.3** to
    determine whether the incoming message is in single packet format or
    multi-packet format. If it is using multi-packet format:
    1.  Continue buffering the message and processing incoming packets until the
        last packet of the message arrives.
    2.  Assemble the full message. Be sure to assemble the packets in the
        correct order using the Packet Number, and to truncate the padding based
        on **Message Length** or **Remaining Message Length**.
4.  Determine the message type and message ID and parse it according to the
    corresponding Response table or Notification table in section **2.7**.
5.  Route the fully composed message to the appropriate handler.

## How to Use Wireless LAN (WLAN) Connections (WLAN Only)

### About Wireless LAN (WLAN) Connections

This section provides information about developing software for a host to
communicate via a TCP/IP network with MMS products connected to a wireless LAN
access point. In this arrangement, the host and device exchange messages as
peers using the bidirectional **WebSocket** protocol. For details about the
WebSocket Protocol, formally **IETF RFC 6455**, see
<https://tools.ietf.org/html/rfc6455> and <http://websocket.org>.

For information about SDKs and sample code that can wrap the protocol and speed
up development, see section **1.4 About SDKs and Sample Code**.

### How to Connect to a Device Using the Wireless LAN (WLAN) Connection

Before the device and host can communicate using the wireless LAN (WLAN)
connection, the device must first be configured to connect to a WLAN access
point. For details about configuring the device, see the device’s **Installation
and Operation Manual** or supporting documentation included with the device.

After the device has been successfully configured for WLAN communication,
whenever the device powers on or resets, it attempts to connect to the
configured access point. If it is configured to use DHCP, it contacts a DHCP
server to acquire a dynamic IP address and register its Hostname to the DNS
server, otherwise it uses its configured static IP address. It then opens a
WebSocket server listener port, and waits for a host to establish a connection
using a WebSocket handshake. If any notification events occur before the host
completes the handshake and establishes a connection, the device does not send
the corresponding notifications, and it does not buffer while it waits for a
host to establish a connection.

If you wish to test the device’s network connection before writing any code, you
may choose to use the echo tool at <https://www.websocket.org/echo.html>, which
allows a WebSocket capable browser to connect directly to a local IP address and
port to perform a simple echo operation.

To connect to the device, the host software must follow these steps:

1.  Know the WebSocket connection / handshake parameters:
    1.  /host/ is the device’s IP address or IP name (if DNS is in use). By
        default, when using DHCP, the device registers its Hostname as its IP
        name. Suggest using the Hostname df-device serial number to keep each
        server unique. See the serial number label on the back of the device.
    2.  /port/ is the port the device’s WebSocket server is listening on. Per
        the WebSocket standard, if the host does not specify a port, the
        connection assumes the default (port 80 for non-secure WebSocket, port
        443 for secure WebSocket). For these devices, use the default port.
    3.  /resource name/, /protocols/, and /extensions/ are not required because
        the device only communicates with a single host and uses binary
        WebSocket frames.
    4.  /origin/ is not required per the WebSocket standard, because the host
        software is not a web browser.
    5.  /secure/ is recommended .
2.  As a WebSocket server, the device can be configured to accept up to four
    client connections at a time.
3.  Establish a connection using a standard WebSocket handshake.
4.  Leave the connection open to listen for incoming WebSocket messages as
    binary WebSocket frames.
5.  The device will automatically disconnect from the client at the end of a
    session. See **Command 0x1F03 - Extend Session (Session Management Only)**
    for more details.
6.  Spawn a process to send a WebSocket **ping** across the connection on a
    reasonable interval (such as 5 seconds) to make sure the connection is still
    alive. Note that WebSocket protocol keeps ping / pong and binary message
    traffic separate, so there is not a risk of collision between MMS messages
    and a ping. Upon detecting the connection is no longer functioning (such as
    during power interruptions, wireless interference or out-of-range, network
    outage, etc.), take appropriate action such as:
    1.  Resetting the state of all host-side operations in process
    2.  Reporting the connection state and recommended troubleshooting
        procedures to the operator
    3.  Attempting to re-establish the connection

### How to Send Commands Using the Wireless LAN (WLAN) Connection

To send a command to the device using the WLAN connection:

1.  Make sure there is an open WebSocket connection. See section **2.2.2 How to
    Connect to a Device Using the Wireless LAN (**WLAN) Connection for details.
2.  Choose the command to invoke from section **6 Commands**.
3.  Construct the command request message using the **Request** table in the
    command documentation. For a deeper explanation of the contents of request
    tables, see section **2.7**.
4.  Transmit the full command request using the binary WebSocket message type
    (binary frames).
5.  Listen for the device’s response, which will also come in as a binary
    WebSocket message type.
6.  Make sure the incoming message is the expected response, not an asynchronous
    notification.
7.  Parse the final response message using the Response table in the
    documentation for the command.

### How to Receive Data Using the Wireless LAN (WLAN) Connection

MMS devices use the same mechanism to send **Response** messages to host
commands and to send unsolicited **Notifications** to the host when events
occur, such as device state changes or user interactions.

The host software should always be listening for notification messages, and
should listen for command response messages after sending a command. Receiving
the incoming message is the same in both cases, but notification messages, which
are generally unpredictable, need to be routed to different handlers than
responses, which are generally anticipated after sending a command.

The host should follow this general sequence to process notification messages
incoming via WebSocket protocol:

1.  Make sure there is an open WebSocket connection. See section **2.2.2 How to
    Connect to a Device Using the Wireless LAN (**WLAN) Connection for details.
2.  After a WebSocket message arrives, determine the message type and message ID
    and route / parse it according to the corresponding Response table or
    Notification table in section **2.7**.

## How to Use Ethernet Connections (Ethernet Only, MAGTEK INTERNAL ONLY FOR NOW)

### About Ethernet Connections

### How to Connect to a Device Using the Ethernet Connection

### How to Send Commands Using the Ethernet Connection

### How to Receive Data Using the Ethernet Connection

## How to Use Bluetooth® LE Connections (Bluetooth® LE Only)

This section provides information about developing software for a Bluetooth®
LE-capable host that needs to communicate with the device using Bluetooth® Low
Energy (Bluetooth® LE). The device acts as a Bluetooth® LE server/peripheral,
and the host acts as a client/central.

### About GATT Characteristics

Messages are exchanged with the device using a service named “DynaFlex”. The
UUID for this service is 0c ba 14 b7 ff 24 47 b0 be 09 26 44 05 38 53 0c in big
endian order. This service contains the following characteristics.

Messages are sent to the device using a characteristic named “Message From
Host”. The UUID for this service is 47 f0 5f fa 59 09 49 69 bc 57 25 0d 47 e8 74
e5 in big endian order. This characteristic supports the Write Request Attribute
PDU Method. The value of this characteristic has a variable length. The maximum
length is 244 bytes. The host must have performed secure connections pairing
with the device before the device will allow it to write to this characteristic.

Messages are sent to the host using a characteristic named “Message To Host”.
The UUID for this service is fe d4 91 18 c7 e2 4a 61 9e d5 e6 dd 65 c3 07 1b in
big endian order. This characteristic only supports the Handle Value
Notification Attribute PDU Method. The value of this characteristic has a
variable length. The maximum length is 244 bytes. The host must have secure
connections pairing with the device before the device will send notifications on
this characteristic. The host must also enable notifications to be sent from
this characteristic before the device will start sending messages on it.

Messages are exchanged with these characteristics using the DynaFlex Bluetooth®
LE protocol. This protocol is described in the next section.

### DynaFlex Bluetooth® LE protocol

This protocol was designed to meet the following goals.

1.  Exchange messages with the device.
2.  Maximize throughput.
3.  Allow the side receiving a message to detect if a message is partially or
    completely dropped.

Bluetooth® LE attribute protocol transmits data in protocol data units (PDUs).
The maximum size of a PDU is determined by the maximum transmission unit (MTU)
agreed on between the host and the device. The MTU is typically set to the
minimum of the host and device’s ATT_MTU size. DynaFlex’s ATT_MTU size is 247
bytes. Most host’s ATT_MTU sizes are larger than 247 bytes, so the MTU size
agreed on between most hosts and DynaFlex’s is 247 bytes. Since application
messages can be much larger than 247 bytes, application messages need to be able
to be sent using multiple PDUs. Note that the minimum ATT_MTU allowed for all
hosts and devices is 23 bytes. To maximize throughput, all messages should be
sent using the maximum MTU size possible. This protocol allows large application
messages to be sent using multiple PDUs. The protocol format for sending and
receiving messages is the same for both the host and device. The only difference
is the characteristic used. Since the attribute opcode and attribute handle use
3 bytes of the MTU size the attribute value length for the message from host and
message to host characteristics is limited to 247 - 3 = 244 bytes.

When a PDU is received in the application layer, it is guaranteed to be correct
since Bluetooth® LE does error detection and retries in the lower layers.
However, PDUs can be completely dropped if the device goes out of range of the
host or bad interference occurs. So host applications should be written with
appropriate error detection and handling to account for these potential drops.

The following is the definition of each byte of a characteristic’s value for the
DynaFlex Bluetooth® LE protocol:

The first byte of the characteristic value is the message counter for every PDU.
The message counter should be zero for the first message sent after every new
BLE connection is established and should increase by one after sending every
message. If its’ value is 0xff before it increments, it should have a value of
zero after incrementing. All PDUs of a single message should have the same value
for the message counter. The side receiving the message can use this counter to
help detect if some PDUs of a message or if an entire message is dropped. The
message counter for the message from host direction should be completely
independent from the message counter for the message to host direction.

The second byte of the characteristic value is the PDU counter for every PDU.
The PDU counter should be zero for the first PDU of a message sent and should
increase by one after sending every PDU of that message. If its’ value is 0xff
before it increments, it should have a value of one instead of zero after
incrementing. This is because the value of zero is reserved to always be used
for the first PDU of a message. If the device receives a PDU counter of zero
while it is still expecting more PDUs for an existing message, it shall discard
any message that it is currently receiving and start receiving the new message.
The first PDU of a message has a different protocol format than the remaining
PDUs. The side receiving the message shall use this counter to help detect if
some PDUs of a message are dropped. The PDU counter for the message from host
direction should be completely independent from the PDU counter for the message
to host direction.

If the PDU counter is zero indicating that this is the first PDU of a message,
then the following paragraphs define the remaining bytes of the PDU, otherwise
the remaining bytes of the PDU starting with the third byte contain the next
portion of the application message.

If the PDU counter is zero indicating that this is the first PDU of a message,
then the third byte of the PDU contains the protocol control byte (PCB). The
protocol control byte is reserved and should always be set to zero. This byte
may be used in the future to extend the protocol.

If the PDU counter is zero indicating that this is the first PDU of a message,
then the fourth, fifth, sixth and seventh byte of the PDU contain the message
length in big endian order. This is the length of the entire message not just
the portion contained in the current PDU. The receiver of the message shall use
this value to determine when it has received all the PDUs of a message.

If the PDU counter is zero indicating that this is the first PDU of a message,
the remaining bytes of the PDU starting with the eighth byte contain the first
portion of the application message. If the entire application message fits into
one PDU then it contains all the application message.

The following is an example of sending two application messages in a row where
the first 9-byte message fits into a single PDU and the second 512-byte message
requires 3 PDUs.

| Message Counter | PDU Counter | PCB | Message Length | Message Portion |
|-----------------|-------------|-----|----------------|-----------------|
| 00              | 00          | 00  | 00 00 00 09    | 9 bytes         |

| Message Counter | PDU Counter | PCB | Message Length          | Message Portion |
|-----------------|-------------|-----|-------------------------|-----------------|
| 01              | 00          | 00  | 00 00 02 00 (512 bytes) | 237 bytes       |

| Message Counter | PDU Counter | Message Portion |
|-----------------|-------------|-----------------|
| 01              | 01          | 242 bytes       |

| Message Counter | PDU Counter | Message Portion |
|-----------------|-------------|-----------------|
| 01              | 02          | 33 bytes        |

Protocol implementation recommendations:

1.  To optimize throughput, split large messages into the minimum number of PDUs
    by making all PDUs the agreed upon MTU size long (ideally 247 bytes) except
    for possibly the last PDU.
2.  Implement error detection that as a minimum detects and discards incomplete
    messages.
3.  If the device detects an incomplete message, it should be able to continue
    to receive new complete messages.
4.  Use the message counter, PDU counter and message length fields to detect
    incomplete messages.
5.  When receiving a multiple PDU message and expecting more PDUs, if the next
    PDU has a PDU counter of zero discard the previous message and start
    receiving the new one.
6.  When looking for the first PDU of a message, if a PDU arrives that does not
    have a PDU counter of zero discard it.
7.  If the message counter advances by more than one between two messages,
    assume a message has been dropped. The device should ignore this situation.
    The host can ignore this situation too or implement error handling of its
    choice.

## How to Use RS-232/UART Connections (SLIP Only)

To connect the host to the device using a serial connection such as RS-232 UART,
configure the host’s serial port to use 115200 Baud, 8 Bit, No-parity,1 Stop
bit, and No flow control.

When using these connections, the host and device use SLIP format to send and
receive MMS messages. For details, see section **2.6 How to Use SLIP Format
(SLIP Only)**. The host software should always be ready to receive notification
messages and command response messages from the device.

(BCR Only) When using the UART interface and the device is configured to be
enable user action event notifications using **Property 1.2.7.1.2.1 User Event
Notification Controls Enable**, the device cannot determine if it is connected
to a host or not, therefore the device will continue reading barcode data even
when not connected to a host.

## How to Use SLIP Format (SLIP Only)

For connection types that do not include error detection and correction, such as
serial protocols, which provides a means for the host and device to
re-synchronize in the case of connection errors by watching for specifically
reserved frame delimiters marking the start and end of a message. The MMS SLIP
wrapper is defined in **Table 9**.

All messages start with SLIP’s frame delimiter **C0**, and must consider SLIP
escape sequences that deal with occurrences of C0 inside the SLIP data frame:

-   If an outbound message contains the byte value **C0**, software should
    encode it into SLIP as **DB DC**.
-   If an inbound message contains the byte sequence **DB DC**, software should
    decode it to **C0**.
-   If an outbound message contains the byte value **DB**, software should
    encode it into SLIP as **DB DD**.
-   If an inbound message contains the byte sequence **DB DD**, software should
    decode it to **DB**.

**Message Info** indicates the direction of the message (such as **Direction
Host to Device** for **Commands**, **Direction Device to Host** for
**Notifications**). If the host has sent the device a command that exceeds the
device’s incoming message buffer capacity, the device responds with a brief
message indicating **Hardware Capability Exceeded**, and populates **Length of
MMS Message** with the maximum possible message length the device can process,
followed by a zero length **MMS Message** and the closing **SLIP Frame
Delimiter**.

For general information about messages, see section **2.7**.

For specific messages, see sections **6 Commands** and **7 Notifications**.

Table 9 - MMS SLIP Wrapper

| Offset     | Value                                                                                                            |
|------------|------------------------------------------------------------------------------------------------------------------|
| Byte 0     | SLIP Frame Delimiter = 0xC0                                                                                      |
| Byte 1     | Message Info 0x00 = Direction Host to Device 0x02 = Direction Device to Host 0x03 = Hardware Capability Exceeded |
| Bytes 2..5 | Length of MMS Message Use big endian order                                                                       |
| Bytes 6..n | MMS Message                                                                                                      |
| Byte n+1   | SLIP Frame Delimiter = 0xC0                                                                                      |

For further reference, see the definition of the SLIP format in Part D, Section
3 of **Specification of the Bluetooth® System, Host Controller Interface, Volume
4**, which is available at
<https://www.bluetooth.org/Technical/Specifications/adopted.htm>. Note the
reference to bluetooth.org is intentional, and the specification does indeed
apply to other device connection types.

## How to Use Apple iAP2 Connections (iAP2 Only)

This section provides information about developing an iOS app that interfaces
with the device via the USB connector using iPod Accessory Protocol (iAP2). For
sample code and other supporting materials, see **1000007353 MAGTEK UNIVERSAL
SDK FOR MMS DEVICES ( iOS )**, available from MagTek.

To develop host software for an iOS host that connects to the device, you must
know the following device properties, which are specified by the purchaser when
ordering, and loaded by the manufacturer:

-   Apple iAP2 AppBundleID, also known as the SDK Protocol, usually in the form
    of a reverse DNS string unique to the host software developer or the device
    purchaser.

The host software should initiate a connection to the device using the iOS SDK’s
**ExternalAccessory** Framework (for sample code, see Apple’s **EADemo** app).
Upon establishing the connection, the host can begin exchanging data with the
device.