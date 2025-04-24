---
title: Command Group 0x10nn - Transactions
layout: home
parent: Commands
nav_order: 1
---

## Command Group 0x10nn - Transactions

---

- [Command Group 0x10nn - Transactions](#command-group-0x10nn---transactions)
    - [Command 0x1001 - Start Transaction](#command-0x1001---start-transaction)
    - [Command 0x1002 - Continue Transaction (MAGTEK INTERNAL ONLY FOR NOW)](#command-0x1002---continue-transaction-magtek-internal-only-for-now)
    - [Command 0x1003 - Finalize (MAGTEK INTERNAL ONLY FOR NOW)](#command-0x1003---finalize-magtek-internal-only-for-now)
    - [Command 0x1004 - Resume Transaction](#command-0x1004---resume-transaction)
    - [Command 0x1008 - Cancel Transaction](#command-0x1008---cancel-transaction)
    - [Command 0x1009 - Close / Clear Transaction (MAGTEK INTERNAL ONLY FOR NOW)](#command-0x1009---close--clear-transaction-magtek-internal-only-for-now)
    - [Command 0x1014 - Get Transaction Status (MAGTEK INTERNAL ONLY FOR NOW)](#command-0x1014---get-transaction-status-magtek-internal-only-for-now)
    - [Command 0x1041 - Set Payment Parameters (MAGTEK INTERNAL ONLY FOR NOW)](#command-0x1041---set-payment-parameters-magtek-internal-only-for-now)
    - [Command 0x1042 - Get Payment Parameters (MAGTEK INTERNAL ONLY FOR NOW)](#command-0x1042---get-payment-parameters-magtek-internal-only-for-now)

---


#### Command 0x1001 - Start Transaction

The host uses this command to start a payment transaction.

The sequence of events for transactions with card readers enabled is
roughly as follows.

**(MCE Only)** The sequence for Manual Entry Mode is provided further
below.

1)  If the device is configured to enable user action event
    notifications using **Property 1.2.7.1.2.1 User Event Notification
    Controls Enable**, the cardholder may present a card or payment
    device before the host calls this command, and the device sends
    **Notification 0x1001 - Device Information Update** to the host to
    indicate it should call this command to start a transaction.

    1)  **(MSR Only)** In the case where the cardholder has swiped
        before the transaction started, the device temporarily stores
        the card swipe data for the period of time specified by
        **Property 1.2.7.1.2.2 User Event Notification MSR Data Timeout
        (MSR Only)** to make it available during the transaction. Later
        in this sequence, when the device would ordinarily prompt the
        cardholder to swipe, insert, or tap, the device briefly displays
        the same cardholder prompt, then automatically proceeds with the
        transaction using the temporarily stored card data. The
        cardholder does not have to swipe again.

    2)  **(EMV Contact Only \| EMV Contactless Only)** In the case where
        the cardholder has inserted or tapped before the transaction
        started, the host should call this command as quickly as
        possible while the card is still in the slot, or while the card
        or contactless payment device is still within tap range. The
        device does not begin contact or contactless reads until after
        the host invokes this command and does not store any data from
        the cardholder action event before the transaction is in
        process.

2)  The host composes a command request in the format below, and sends
    it to the device. It may cancel the transaction in process by
    calling **Command 0x1008 - Cancel Transaction**.

3)  The device sends a response in the format below, and waits for the
    cardholder to present payment using one of the enabled payment
    technologies.

4)  **(BCR Only)** If the cardholder scans a barcode, the device sends
    **Notification 0x0101 - Transaction Information Update** to report
    Barcode / Barcode Event / Type / Data Attached with the barcode data
    attached and terminates the transaction.

5)  After the cardholder presents payment, the device sends
    **Notification 0x0101 - Transaction Information Update** to report
    the payment technology being used / **Card Event**.

6)  **(MSR Only)** If **Property 1.2.1.1.1.1 Device-Driven Fallback
    Behavior (MSR Only)** is configured so the device automatically
    performs fallback operations, it performs them at this time
    following roughly the same sequence of steps as host-driven fallback
    described below. Device-driven fallback occurs at this point in the
    sequence within one iteration of this command, whereas host-driven
    fallback requires the host to re-send this command for each retry
    attempt.

7)  **(EMV Contact Only)** If the cardholder has inserted a chip card
    and there is more than one application the device and card mutually
    support:

    1)  **(Display Only)** The device prompts the cardholder to select
        the application to use.

    2)  **(No Display Only)** The device sends **Notification 0x1803 -
        User Interface Host Action Request** to report **Cardholder
        Selection Request**/ **Notification Payload** to prompt the
        cardholder to select the application to use. The host should
        respond by showing the prompt, receiving input from the
        cardholder, and calling **Command 0x1802 - Report Cardholder
        Selection** to report the selection result to the device.

8)  The device sends **Notification 0x0101 - Transaction Information
    Update** to report the payment technology being used / **Data Update
    / ARQC Update / Data Attached**.

9)  If the host specified **Quick Chip Transaction Flow** in the
    **Transaction Flow** parameter:

    1)  The device immediately constructs its own internal ARPC
        Response, with tag 8A set to ‘Z3’ to coordinate the transaction
        with the card or other payment method, and sends the host
        **Notification 0x0105 - Transaction Operation Complete** to
        report the payment technology being used / **Kernel Outcome** /
        **Quick Chip Deferred** /outcome detail. A Transaction Option
        parameter can be set to display on amount or not.

    2)  **(Display Only)** The device shows the message **REMOVE CARD**
        to notify the cardholder the card can be removed.

    3)  **(No Display only)** The device sends the host **Notification
        0x1803 - User Interface Host Action Request** to report
        **Display**/**Display Message**/**Data Attached** with message
        **REMOVE CARD** to notify the cardholder the card can be
        removed.

    4)  The host should then process the ARQC Message data, including
        replacing the default amount with the final transaction amount,
        and should coordinate with the transaction processor to retrieve
        a final transaction result. Because in this case the device is
        not involved in determining the final transaction result, it
        does not send a notification to the host to show **APPROVED** or
        **DECLINED**.

        1)  **(Display Only)** Instead, the host should call **Command
            0x1803 - Display Message (Display Only)** to show an
            appropriate message to the cardholder, such as **APPROVED**
            or **DECLINED**, based on the final transaction result.

        2)  **(No Display Only)** Instead, the host should use its local
            display to show an appropriate message to the cardholder,
            such as **APPROVED** or **DECLINED**, based on the final
            transaction result.

10) If the host specified **EMV Transaction Flow** in the **Transaction
    Flow** parameter:

    1)  The host processes the ARQC Message data and uses it to
        coordinate with the transaction processor to receive an ARPC
        Response, which it processes and sends to the device using
        **Command 0x1004 - Resume Transaction**.

    2)  The device waits for the period of time specified in **Property
        1.1.1.1.1.5 ARPC Receive Timeout**. If an ARPC timeout occurs,
        the device sends the ARQC again based on the setting in
        **Property 1.1.1.1.1.6 ARPC Retry Attempts**.

    3)  **(EMV Contact Only)** If the cardholder inserted a contact chip
        card, the device communicates with the card to determine whether
        to approve or decline the transaction.

    4)  The device sends the host **Notification 0x0105 - Transaction
        Operation Complete** to report the payment technology being used
        / **Kernel Outcome** / **Approved** or **Declined** /outcome.

    5)  **(Display Only)** The device shows **APPROVED** or **DECLINED**
        to notify the cardholder of the transaction result.

    6)  **(No Display Only)** The device sends the host **Notification
        0x1803 - User Interface Host Action Request** to report
        **Display**/**Display Message**/**Data Attached** with message
        **APPROVED** or **DECLINED** to notify the cardholder of the
        transaction result.

11) **(Touch Only)** If the card requires a signature, and if **Property
    1.2.1.1.2.1 Signature Capture Control** is set to **Device-driven
    Signature Capture**, and if the **Signature Capture Control (MSR
    Only)** command parameter does not apply to the current transaction,
    the device prompts the cardholder to sign.

12) The device sends **Notification 0x0101 - Transaction Information
    Update** to report the payment technology used / **Data Update /
    Batch Data / Data Attached**. **(Touch Only)** Depending on the
    setting in **Property 1.2.1.1.2.2 Include Signature Data in EMV
    Batch Data (Touch Only)**, the device includes any acquired
    signature data with the batch data.

13) The device sends **Notification 0x0105 - Transaction Operation
    Complete** to report the payment technology used / **Outcome** / the
    final result of the transaction.

14) **(MSR Only)** If **Property 1.2.1.1.1.1 Device-Driven Fallback
    Behavior (MSR Only)** is configured so the device does not perform
    fallback operations, and if the solution design requires payment
    brand fallback logic, the host may use the contents of the
    notifications above to implement fallback flow according to the
    following rules, which mimic the automatic fallback behaviors the
    device implements during a single invocation of this command. The
    primary difference is that the host must keep track of its own final
    **Fallback Indicator** instead of receiving it from the device in
    the **EMV ARQC Type**:

    1)  If the transaction was successful and the notification indicates
        Payment Technology is **EMV Contact** or **EMV Contactless**,
        there is no need to perform fallback-related operations.

    2)  If the transaction was successful and the notification indicates
        Payment Technology is **Magnetic Stripe Reader**, the host
        should check the contents of the **Card Type** tag DFDF52 in the
        **EMV ARQC Type** from the notification. Per payment brand
        fallback rules:

        1)  If **Card Type** is NOT **MSR Financial and Contact Chip
            Card (ICC)**, the host may continue with the current
            transaction attempt using the magnetic stripe data. There is
            no need to perform fallback-related operations.

        2)  If **Card Type** is **MSR Financial and Contact Chip Card
            (ICC)**, and the host has restarted the same transaction
            because a previous attempt failed with the notification
            indicating **MSR Fallback**, the chip card and the device
            communicated during the previous invocation of this command,
            and determined they are not compatible. The host may
            continue the current transaction using the magnetic stripe
            data.

        3)  If **Card Type** is **MSR Financial and Contact Chip Card
            (ICC)** and the host has NOT restarted the same transaction
            three times and failed with the notification indicating
            **Technical Fallback**, the card has a chip the cardholder
            should use so the transaction will be more secure. The host
            should guide the cardholder to use the chip card interface
            by sending **Command 0x1803 - Display Message** to direct
            the device to display **USE CHIP READER**, then repeat
            **Command 0x1001 - Start Transaction** and arm the device
            with the contact interface enabled. The host may opt to also
            arm the contactless interface.

        4)  If **Card Type** is **MSR Financial and Contact Chip Card
            (ICC)** and the host has restarted the same transaction
            three times and failed with the notification indicating
            **Technical Fallback**, the host may continue the current
            transaction using the magnetic stripe data.

    3)  If the transaction has failed and the notification indicates
        Payment Technology is **None**, something went wrong at the very
        beginning of the transaction (for example, the host canceled),
        and the host may simply end all attempts at performing the
        transaction, or it may opt to repeat the original transaction
        with the same payment technologies enabled.

    4)  If the transaction has failed and the notification indicates
        Payment Technology is **EMV Contact**, the host should examine
        the contents of the notification. Per payment brand fallback
        rules:

        1)  If the notification indicates **MSR Fallback**, the chip
            card and the device have communicated and have determined
            they are not compatible. The host should guide the
            cardholder to use the magnetic stripe interface by sending
            **Command 0x1803 - Display Message** to direct the device to
            display **USE MAGSTRIPE**, then repeat **Command 0x1001 -
            Start Transaction** and arm the device with the Magnetic
            Stripe Reader interface enabled. The host may opt to also
            arm the contactless interface.

        2)  If the host has NOT restarted the same transaction three
            times and failed with the notification indicating a
            **Technical Fallback**, the host should guide the cardholder
            to re-insert the chip card by sending **Command 0x1803 -
            Display Message** to direct the device to display **TRY
            AGAIN**, then repeat **Command 0x1001 - Start Transaction**
            and arm the device with the contact interface enabled. The
            host may opt to also arm the contactless interface.

        3)  If the host has restarted the same transaction three times
            and failed with the notification reporting **Technical
            Fallback**, the host should guide the cardholder to use the
            magnetic stripe reader by sending **Command 0x1803 - Display
            Message** to direct the device to display **USE MAGSTRIPE**,
            then repeat **Command 0x1001 - Start Transaction** and arm
            the device with the Magnetic Stripe Reader interface
            enabled. The host may opt to also arm the contactless
            interface.

15) (Touch Only) If **Property 1.2.1.1.2.1 Signature Capture Control**
    is set to **Host-driven Signature Capture** and the card requires a
    signature, the host should perform host-driven signature capture at
    this time. The device waits for the time period specified by
    **1.2.1.1.2.3 Signature Timing Window (Touch Only)**, providing a
    time window for the host to end the transaction by sending **Command
    0x1801 - Request Cardholder Signature**. At the end of that time
    window, if the host has not called that command, the device returns
    to the idle state.

16) **(EMV Contactless Only)** For NFC Tag, the flow is as follows:

<!-- -->

1)  Use Start Transaction command with the NFC enabled in Contactless
    Reader Mode

2)  If an NFC Tag is Detected

    1.  the terminal will send a notification that identifies the NFC
        card type, see **Notification 0x0101 - Transaction Information
        Update**

    2.  the terminal will send another notification with the UID as a
        payload, see **Table 298 - Notification Payload for Data Update,
        ARQC Update (Quick Chip), Data Attached**. If a card is
        configured with a random ID, its value will be changed every
        time the card gets detected. The host is responsible to retrieve
        the real UID.

3)  No ARQC or BATCH data will be sent

4)  The host application can continue interfacing with the NFC tag by
    sending pass-through commands

5)  When an NFC Tag gets out of the field, the terminal sends
    **Notification 0x0105 – 20 05 00 00 (PICC, NFC Tag, Tag Removed,
    Reserved)** indicating that the Tag has been removed.

<!-- -->

17) **(MCE Only)** For manual card entry, the sequence of events is as
    follows:

<!-- -->

1)  The host composes a command request in the format below with
    **Manual Entry Mode** parameters defined and other reader modes
    empty and sends it to the device. The host may cancel the
    transaction in process by calling **Command 0x1008 - Cancel
    Transaction**.

2)  The device presents a sequence of pages based on the setting of
    **Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.**.

3)  The device creates Track 1 and 2 data based on the entered values.

4)  The device sends instances of **Notification 0x0101 - Transaction
    Information Update** to report each of the following:

    1.  Manual Card Entry, Card Event, Data Entered, Reserved

    2.  Manual Card Entry, Data Update, ARQC Update, Data Attached

    3.  Manual Card Entry, Data Update, Batch Update, Data Attached

<!-- -->

5)  The device sends **Notification 0x0105 - Transaction Operation
    Complete** to report **Manual Card Entry, Transaction Completed,
    Reserved, Reserved**.

<!-- -->

18) Tip Feature **(Touch Only)**

<u>Tip Operation Use Case Mode 1A</u>

1)  Use Tag A4 for Tip and Tax Options

2)  Use Byte 1 of Tag 81 under A4 to specify Tip mode

    1.  0x01 = Use % mode

    2.  0x02 = Use Amount mode

3)  Bytes 2 through 31 of Tag 81 specifies the % or \$ value to show for
    Buttons 1 thru 6. There is a button mode to control whether the
    button is going to show \$/%, CUSTOM, NO TIP, or is disabled.

4)  Tag 82 is the Tax Amount to Display

5)  DF5D = Tip Amount, DF5E = Tax Amount are used for reporting back to
    the host application.

6)  If available, tags DF5D and DF5E will be sent in the ARQC Data, see
    **Table 18 - EMV ARQC (DynaPro Format) Type** .

7)  The value of Tag 9F02 provided in command 0x1001 will be updated by
    the Device by adding TIP and TAX before passing that value to the
    kernels.

8)  See **Tip & Tax Display Limits (Touch Only)** for display
    limitations.

<u>Tip Operation Use Case Mode 1B</u>

1)  If **Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event
    Control(Touch Only)** is Enabled, and there is a socket connection
    with the host, the device will show the **START SALE** button.

2)  When the cardholder touches the **START SALE** button, the device
    will automatically start a transaction by asking cardholder to enter
    the transaction amount. The device will show the **CUSTOM AMOUN**T
    screen. Press **ENTER** to set transaction amount. The Start
    Transaction parameters are taken from the settings of these
    properties

    1.  **Property 1.1.1.1.2.2 Tip Mode(Touch Only)**

    2.  Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button
        Press

    3.  **Property 1.1.1.1.3.2 Reader Options (Touch Only)**

    4.  **Property 1.1.1.1.3.3 Transaction Options (Touch Only)**

3)  The Device automatically sends a Notification – Transaction
    Information Update that a transaction has started, **Table 297 -
    Notification Detail Codes**.

4)  If the **CANCEL** button is touched, the device automatically sends
    a Notification – Transaction Information Update that a transaction
    is canceled, **Table 297 - Notification Detail Codes**.

5)  After amount is entered, device checks **Property 1.1.1.1.2.2 Tip
    Mode(Touch Only)** to determine if TIP mode is enabled, as well as
    the TIP parameters. The Device will show the **TIP SCREEN** or
    **CUSTOM AMT** screen per cardholder selection. Press **SUBMIT** to
    set TIP amount.

6)  The device checks **Property 1.1.1.1.2.3 Tax Rate (Touch Only**) to
    determine if taxes need to be calculated. If enabled, device
    calculates the Taxes per the tax rate specified in the property.

7)  If tax function is enabled, the device checks **Property 1.1.1.1.2.4
    Display Tax or Surcharge (Touch Only)** to determine how to show the
    label, tax or surcharge in the **SUMMARY SCREEN**

8)  Tax is only calculated on the amount entered, excluding TIP.

9)  Total Amount = Amount + Tip + Tax Total Amount is the value that
    will be used for Tag 9F02 of the transaction flow.

10) See **Tip & Tax Display Limits (Touch Only)** for display
    limitations.

<!-- -->

19) Audio Transducer Beep Flow:

<!-- -->

1)  Upon NFC tag detection, notify HOST

2)  Host sends 0x1001 to Start Transaction

3)  After NFC is activated - No Beep

4)  Host goes thru several Pass-Through commands to R/W NFC

5)  A parameter will be added to the Pass-Through command API to
    indicate if this is the last command

6)  If this is the last command, Device -\> Single Beep to indicate CARD
    CAN BE REMOVED. Turn-Off RF to shut down-card.

7)  If an error condition is detected, the device will end session,
    double-beep, Turn-Off RF to shut down the card.

<!-- -->

20) Command 0x1001 – Start a Payment Transaction with an option to show
    functional button Right **(Display Only)**

The host uses this command to start a payment transaction with an option
to display a **Present a Card** page and a green functional button Right
(e.g. Service Request button).

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image4.png"
style="width:3.375in;height:2.5625in"
alt="A close-up of a card reader Description automatically generated" /><img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image5.png"
style="width:2.55208in;height:3.375in"
alt="A white paper with black text Description automatically generated" />

When the cardholder presses the **Service Request** button, the device
will send a notification, show **PLEASE WAIT** and await the next
command from the host.

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image6.png"
style="width:3.47361in;height:2.64028in"
alt="A white background with black text AI-generated content may be incorrect." />

The host uses **Command 0x1001** to start a payment transaction. If the
battery charge is five percent or less, a response is returned
indicating that the command has not been executed. See **Table 70 -
Response Example for Command 0x1001 – Start Transaction Command not
executed due to Battery Charge State**.

Table 68 - Request Data for Command 0x1001 - Start Transaction

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
<td colspan="6">1001 = <strong>Command 0x1001 - Start
Transaction</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td>Reserved</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Transaction Timeout, in seconds</p>
<p>This parameter defines how long the device waits for the cardholder
to take action on any cardholder input, for example, when waiting for
the cardholder to present payment after the host starts the
transaction.</p>
<ul>
<li><p>0x00 = No timeout</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>var</td>
<td><p>Reader Options</p>
<p>The parameters inside this TLV data object allow the host to enable
and disable the various payment method interfaces.</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td><p>Magnetic Stripe Reader Mode (MSR Only)</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = EMV</p></li>
<li><p>0x80 = Non-EMV (disables other readers) (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x01</td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Contact Reader Mode (EMV Contact Only)</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = EMV</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x01</td>
</tr>
<tr>
<td>/83</td>
<td>01</td>
<td><p>Contactless Reader Mode (EMV Contactless Only)</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = EMV</p></li>
<li><p>0x02 = NFC</p></li>
<li><p>0x03 = EMV and NFC</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x01</td>
</tr>
<tr>
<td>/84</td>
<td>03</td>
<td><p>Manual Entry Mode (Touch Only)</p>
<p>Populate this parameter to enable manual card entry. When using this
feature, all other Reader Mode parameters must be set to
<strong>Disabled</strong>.</p>
<p>Byte 1 Card Number Valid Format</p>
<ul>
<li><p>0x00 = PAN min 8, max 21 digits</p></li>
</ul>
<p>Byte 2 User Interface Sequence</p>
<ul>
<li><p>0x00 = Based on the setting of <strong>Property 1.2.1.1.4.5
MIFARE Plus AES_Key1.</strong></p></li>
</ul>
<p>Byte 3 Beeper Feedback</p>
<ul>
<li><p>0x00 = On keypress sound disabled</p></li>
<li><p>0x01 = On keypress sound enabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>02</td>
<td><p>Barcode Reader Mode (BCR Only)</p>
<p>Populate this parameter to enable the device’s barcode reader. This
feature can be enabled alongside all other reader modes except Manual
Entry Mode.</p>
<p>Byte 1 Barcode Reader Enable</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = Enabled</p></li>
</ul>
<p>Byte 2 Encrypt Non-EMV Barcode Data</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = Enabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x0000</td>
</tr>
<tr>
<td>/86</td>
<td>01</td>
<td><p>PIN Block Format (Touch Only)</p>
<ul>
<li><p>0x00 = ISO Format 0</p></li>
<li><p>0x03 = ISO Format 3</p></li>
<li><p>0x04 = ISO Format 4</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>A4</td>
<td>var</td>
<td>Tip and Tax Options</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>1F</td>
<td><p>Byte 1 Tip Mode</p>
<p>0x00 – Disable Tip Mode</p>
<p>0x01 – Show Tip GUI immediately using % value</p>
<p>0x02 – Show Tip GUI immediately using $ amount</p>
<p>0x11 - Enable Read Channel(s), with +Tip Button, %value</p>
<p>0x12 - Enable Read Channel(s), with +Tip Button, $ Amount</p>
<p>For Tip Modes 0x01 and 0x02, the Tip GUI is shown immediately with
selected read channels disabled. They get enabled after the Tip
information are entered.</p>
<p>For Tip Modes 0x11 and 0x12, the read channels are enabled and “+Tip”
button is shown. If no tip is desired, just present the card. If “+Tip”
button is selected, read channels are first disabled, then show the Tip
GUI.</p>
<p>Byte 2, Display Mode for Button1</p>
<p>0 - % or Amount</p>
<p>1 – Display Custom</p>
<p>2 – Display NO TIP</p>
<p>3 – Disabled (An OID controls whether the button is blank, grayed out
or not showing, see <strong>Property 1.1.1.1.2.5 Disabled Tip Button
Display Mode (Touch Only)</strong>)</p>
<p>Bytes 3 to 6 Value in % or Amount for Button 1, if applicable</p>
<p>Byte 7, Display Mode for Button 2 (See Byte 2 for Details)</p>
<p>Bytes 8 to 11 Value in % or Amount for Button 2, if applicable</p>
<p>Byte 12, Display Mode for Button 3 (See Byte 2 for Details)</p>
<p>Bytes 13 to 16 Value in % or Amount for Button 3, if applicable</p>
<p>Byte 17, Display Mode for Button 4 (See Byte 2 for Details)</p>
<p>Bytes 18 to 21 Value in % or Amount for Button 4, if applicable</p>
<p>Byte 22, Display Mode for Button 5 (See Byte 2 for Details)</p>
<p>Bytes 23 to 26 Value in % or Amount for Button 5, if applicable</p>
<p>Byte 27, Display Mode for Button 6 (See Byte 2 for Details)</p>
<p>Bytes 28 to 31 Value in % or Amount for Button 6, if applicable</p>
<p><strong>See Property 1.1.1.1.2.2 Tip Mode(Touch Only) for a suggested
default value</strong></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>06</td>
<td><p>Tax or Surcharge Amount to Display</p>
<p>See <strong>Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch
Only)</strong> to configure display Tax or Surcharge</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>02</td>
<td><p>Transaction Options</p>
<p>This parameter is a bitmask (ORed bits) that sets various device
behaviors that change the transaction flow or the way the device reports
transaction results, as follows:</p>
<p>Byte 1 Apple VAS Mode (<strong>Apple / Google VAS Only, set to 0 if
not supported</strong>)</p>
<p>Bits 0, 1</p>
<ul>
<li><p>0x00 = <strong>Apple/Google VAS Support
Disabled</strong></p></li>
<li><p>0x01 = <strong>VAS App OR Payment Mode (Single Mode)</strong>.
The<br />
device reads only Apple/Google VAS data from a tapped<br />
smartphone, or reads EMV payment data from a tapped<br />
card. When the device sends ARQC to conclude the<br />
transaction, it only includes either EMV payment data in<br />
container FC for cards, or includes VAS data in container<br />
FE for smartphones</p></li>
<li><p>0x02 = <strong>VAS App and Payment Mode (Dual Mode)</strong>.
The<br />
device reads both Apple/Google VAS data and EMV payment data<br />
from a tapped smartphone, or reads EMV payment data<br />
from a tapped card. When device sends ARQC to the host<br />
to conclude the transaction, it includes EMV payment data<br />
in container FC and includes VAS data, if available, in<br />
container FE</p></li>
<li><p>0x03 = <strong>VAS App Only Mode (VAS Mode)</strong>. The
device<br />
reads only Apple/Google VAS data from a tapped smartphone, and<br />
does not read data from a tapped card. If the tapped<br />
smartphone does not support VAS, the device does not<br />
detect or read from the smartphone. When the device send<br />
ARQC to conclude the transaction, it includes VAS data in<br />
container FE and does not include EMV payment data in<br />
container FC</p></li>
<li><p>0x04 = <strong>Payment Only Mode (Payment Mode)</strong>.
The<br />
device operates the same as EMV mode (01). It reads only<br />
EMV payment data from a tapped smartphone or a tapped<br />
card. When the device sends ARQC to conclude the<br />
transaction, it includes EMV payment data in container FC<br />
and does not include VAS data in container FE.</p></li>
</ul>
<p>Bits 4, 5, 6 Wallet Mode</p>
<p>4 -Apple</p>
<p>5 - Google</p>
<p>6 - Reserved</p>
<ul>
<li><p>0x000 = Wallet Support Disabled</p></li>
<li><p>0x001 = Apple VAS Enable</p></li>
</ul>
<ul>
<li><p>0x002 = Google VAS Enabled</p></li>
<li><p>0x003 = –Apple and Google VAS Enabled</p></li>
</ul>
<p>Bit 7 Apple VAS Protocol Mode<br />
o Value 0 – URL VAS Protocol<br />
o Value 1 – FULL VAS Protocol</p>
<p>Byte 2 Transaction Flow Control</p>
<ul>
<li><p>Bit 0 Transaction Flow</p>
<ul>
<li><p>Value 1 = Quick Chip Transaction Flow</p></li>
<li><p>Value 0 = EMV Transaction Flow</p></li>
</ul></li>
</ul>
<ul>
<li><p>Bit 1 Response Format</p>
<ul>
<li><p>Value 1 = DynaPro Response Format. For sending ARQC data and
batch data, the device uses <strong>EMV ARQC (DynaPro Format)
Type</strong> and <strong>EMV Batch Data (DynaPro Format)
Type</strong>.</p></li>
<li><p>Value 0 = Reserved.</p></li>
</ul></li>
<li><p>Bit 2 Signature Capture Control (MSR Only).</p>
<ul>
<li><p>Value 1 = Skip Signature Capture On Service Code. The device
skips signature capture during an MSR-only transaction if the card’s
service code indicates it is a chip card.</p></li>
<li><p>Value 0 = Do Not Skip Signature Capture.</p></li>
</ul></li>
<li><p>Bit 3 Display Amount for Quick Chip Transaction Flow</p>
<ul>
<li><p>Value 1 = Display Amount</p></li>
<li><p>Value 0 = Do not Display Amount</p></li>
</ul></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x0003</td>
</tr>
<tr>
<td>86</td>
<td>var</td>
<td><p>Transaction TLV</p>
<p>This is a list of self-contained TLV data objects that defines the
basic parameters for the transaction. It may contain any of the
following tags in the formats defined in the <em><strong>EMV
4.3</strong></em> specification or payment brand specifications, but at
minimum it must contain 9C and 9F02, plus 9F03 if the transaction
includes cash back. This parameter is optional for Manual Card Entry; to
show a transaction amount when using Manual Card Entry, include 9F02 and
5F2A:</p>
<ul>
<li><p>9C Transaction Type</p></li>
<li><p>9F02 Amount Authorized. If the <strong>Transaction Flow</strong>
parameter specifies <strong>Quick Chip Transaction Flow</strong>, the
host must specify a non-zero amount.</p></li>
<li><p>9F03 Amount Other</p></li>
<li><p>9F7C Merchant Custom Data</p></li>
<li><p>5F2A Transaction Currency Code</p></li>
<li><p>5F36 Transaction Currency Exponent</p></li>
<li><p>9F53 Transaction Category Code</p></li>
<li><p>9F15 Merchant Category Code</p></li>
<li><p>9F16 Merchant ID</p></li>
</ul></td>
<td>B</td>
<td>R/O</td>
<td></td>
</tr>
<tr>
<td>A8</td>
<td>00</td>
<td><p>(MAGTEK INTERNAL ONLY FOR NOW)</p>
<p>Tag Lists</p></td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>8A</td>
<td></td>
<td><p>(MAGTEK INTERNAL ONLY FOR NOW)</p>
<p>Notification Options</p>
<ul>
<li><p>??</p></li>
</ul></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>AC</td>
<td>var</td>
<td>User Interface Options</td>
<td>T</td>
<td>O</td>
<td>null</td>
</tr>
<tr>
<td>/81</td>
<td>00</td>
<td><p>Suppress Thank You Message</p>
<p>By default, devices with a display signal the end of a transaction by
briefly showing “THANK YOU,” then “WELCOME.” The host can include this
parameter to direct the device to suppress the “THANK YOU” message
during this transaction.</p></td>
<td>T</td>
<td>O</td>
<td>null</td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Override Final Transaction Message</p>
<p>By default, devices with a display signal the end of a transaction by
returning to the idle page and showing “WELCOME.” The host can include
this parameter to direct the device to show a different message, chosen
from the list of available Display String IDs in section <strong>4.3
Display Strings</strong>. This option completely overrides the device’s
idle page behavior until the next transaction, power cycle, or other
similar state change.</p></td>
<td>B</td>
<td>O</td>
<td>null</td>
</tr>
<tr>
<td>/83</td>
<td>02</td>
<td><p>Functional button Right option.</p>
<p>String ID = Enable the present card page with a green functional
button Right – label with a String ID associates with a configured
String message. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings.</strong> This button can fit about 15 characters. When user
presses this button, device sends notification to the host to indicate
the present card functional button Right is pressed. See
<strong>Notification 0x1803 - User Interface Host Action
Request</strong></p>
<p>If host wants to disable this button, do not include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td>null</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 69 - Response Data for Command 0x1001 - Start Transaction

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1001 = **Command 0x1001 - Start Transaction** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 10 01 82 04 80 02 03 16 |

Table 70 - Response Example for Command 0x1001 – Start Transaction
Command not executed due to Battery Charge State

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 71 - Request Example (MSR, Contact, and Contactless Only)

| Example (Hex) |
|----|
| AA 00 81 04 01 00 10 01 84 3D 10 01 82 01 3C A3 09 81 01 01 82 01 01 83 01 01 84 02 00 03 86 27 9C 01 00 9F 02 06 00 00 00 00 01 00 9F 03 06 00 00 00 00 00 00 5F 2A 02 08 40 5F 36 01 02 9F 15 02 00 00 9F 53 01 00 |

| Example (Hex) |
|----|
| AA 00 81 04 01 00 10 01 84 3D 10 01 82 01 3C A3 09 81 01 00 82 01 00 83 01 01 84 02 00 03 86 27 9C 01 00 9F 02 06 00 00 00 00 01 00 9F 03 06 00 00 00 00 00 00 5F 2A 02 08 40 5F 36 01 02 9F 15 02 00 00 9F 53 01 00 |

Table 72 - Request Example (Contactless Only)

Table 73 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 10 01 82 04 01 00 00 00 |

#### Command 0x1002 - Continue Transaction (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use in operations where **Command 0x1001 - Start
Transaction** must suspend for some reason, e.g., waiting for an ARPC
response, waiting for a host-driven application selection, etc.

#### Command 0x1003 - Finalize (MAGTEK INTERNAL ONLY FOR NOW)

#### Command 0x1004 - Resume Transaction

The host uses this command to provide the device with additional /
modified data to resume a transaction that is currently paused.

Table 74 - Request Data for Command 0x1004 - Resume Transaction

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
<td colspan="6">Beginning of any wrappers, at minimum including Request
Message found on page <a href="#request-message">23</a></td>
</tr>
<tr>
<td colspan="6">1004 = <strong>Command 0x1004 - Resume
Transaction</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Resume Code</p>
<p>Indicates the pause state the transaction will resume from:</p>
<ul>
<li><p>0x00 = Waiting for ARPC</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td>Reserved</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>ARPC Data</p>
<p>This contains an <strong>EMV ARPC Type</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>var</td>
<td><p>Transaction TLV Update</p>
<p>Not applicable when Resume Code = <strong>Waiting for
ARPC</strong></p></td>
<td>B</td>
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

Table 75 - Response Data for Command 0x1004 - Resume Transaction

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1004 = **Command 0x1004 - Resume Transaction** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 76 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 00 10 04 84 21 10 04 81 01 00 82 01 78 84 17 FF 74 14 DF DF 25 08 99 26 90 E1 16 12 07 10 FA 06 70 04 8A 02 30 30 |

Table 77 - Response Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 82 06 10 04 82 04 00 00 00 00 84 02 10 04 |

#### Command 0x1008 - Cancel Transaction

The host can use this command to cancel a transaction in progress that
it initiated using **Command 0x1001 - Start Transaction**.

The sequence of events is as follows:

1)  The host has already called **Command 0x1001 - Start Transaction**
    and the transaction is still in process.

2)  The host constructs the command request in the format below.

3)  The host sends the command request to the device.

4)  The device sends a response in the format below to the host.

    1)  If the transaction is in a state where it can not be canceled,
        the device’s response returns operation status detail **Failed,
        Device State Issue, Cannot Cancel**.

    2)  If there is no transaction in progress, the device’s response
        returns operation status detail codes **Failed, Device State
        Issue, No Transaction**.

5)  If the device successfully cancels the transaction, the device’s
    response returns operation status detail **All Good, Requested
    Operation Was Successful**, shows **CANCELED** on the display (if
    any), and returns to the idle state.

Table 78 - Request Data for Command 0x1008 - Cancel Transaction

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| 1008 = **Command 0x1008 - Cancel Transaction** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 79 - Response Data for Command 0x1008 - Cancel Transaction

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1008 = **Command 0x1008 - Cancel Transaction** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 80 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 13 10 08 84 02 10 08 |

Table 81 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 13 10 08 82 04 00 00 00 00 |

#### Command 0x1009 - Close / Clear Transaction (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

#### Command 0x1014 - Get Transaction Status (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

#### Command 0x1041 - Set Payment Parameters (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave. MAC.

#### Command 0x1042 - Get Payment Parameters (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.