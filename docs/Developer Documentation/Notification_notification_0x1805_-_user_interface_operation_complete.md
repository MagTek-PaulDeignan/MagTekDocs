---
title: Notification 0x1805 - User Interface Operation Complete
layout: home
parent: Notifications
nav_order: 22
---

## Notification 0x1805 - User Interface Operation Complete

This notification reports information about progress and state changes
that occur during interaction with the User Interface modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 339**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 339 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>UI</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Module <strong>0x01 Touchscreen</strong> contains UI
notification detail codes that are specific to the touchscreen module
(Touch Only)</p>
<ul>
<li><p>Reason 0x01 = Signature Capture</p></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td><p>Touchscreen, Signature Capture, Success, Data Available (Touch
Only)</p>
<p>In this case, the device includes the File ID as defined in
<strong>Table 340</strong> in the <strong>Additional Detail</strong>
portion of the <strong>Notification Message</strong>. The host should
use this File ID and call <a href="#_Command_0xD821_-"><strong>Command
0xD825 – Start Get File from Device</strong></a>.</p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>02</td>
<td>01</td>
<td>Touchscreen, Signature Capture, Operation Failed, Timeout (Touch
Only)</td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>02</td>
<td>02</td>
<td>Touchscreen, Signature Capture, Operation Failed, Hardware Not
Available (Touch Only)</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x02 Display</strong> contains UI
notification detail codes that are specific to the display module
(Display Only).</p>
<ul>
<li><p>Reason 0x01 = Display Message Request</p></li>
<li><p>Reason 0x02 = Cardholder Selection Request</p></li>
<li><p>Reason 0x03 = Online PIN Request (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
</ul></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Display, Display Message, Timed Out, Reserved</p>
<p>The device has finished displaying a message requested by the host
using <strong>Command 0x1803 - Display Message</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x04 Barcode Reader</strong> contains
notification detail codes that are specific to the barcode reader
module.</p>
<ul>
<li><p>Reason 0x03 = Read Barcode Result</p></li>
</ul></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>01</td>
<td>00</td>
<td><p>Barcode Reader, Read Barcode Result, Success, Unidentified
Type</p>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
If the data is encrypted, the data is in the format described in
<strong>Table 341</strong>. Data that is not encrypted is in the format
described in <strong>Table 342</strong>.</p></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>01</td>
<td>01</td>
<td><p>Barcode Reader, Read Barcode Result, Success, MagTek Blob
Type</p>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
MagTek Blob data is always encrypted. The data is in the format
described in <strong>Table 341</strong>.</p></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>01</td>
<td>02</td>
<td><p>Barcode Reader, Read Barcode Result, Success, EMV Type</p>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
EMV barcode data is always encrypted. The data is in the format
described in <strong>Table 341.</strong></p></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>02</td>
<td>01</td>
<td>Barcode Reader, Read Barcode Result, Operation Failed, Timeout</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x05 Buzzer</strong> contains
notification detail codes that are specific to the buzzer module.</p>
<ul>
<li><p>Reason 0x04 = Buzzer Result</p></li>
</ul></td>
</tr>
<tr>
<td>05</td>
<td>04</td>
<td>01</td>
<td>00</td>
<td>Buzzer, Buzzer Result, Operation Success, Reserve</td>
</tr>
<tr>
<td>05</td>
<td>04</td>
<td>02</td>
<td>00</td>
<td>Buzzer, Buzzer Result, Operation Fail, Reserve</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x06 Card Emulation</strong> contains
notification detail codes that are specific to card emulation.</p>
<ul>
<li><p>Reason 0x05 = Card Emulation Result</p></li>
</ul></td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>01</td>
<td>00</td>
<td>Card Emulation, Card Emulation Result, Operation Success,
Reserve</td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>02</td>
<td>01</td>
<td>Card Emulation, Card Emulation Result, Operation Fail, Timeout</td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>02</td>
<td>03</td>
<td>Card Emulation, Card Emulation Result, Operation Fail, Cancel</td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>02</td>
<td>04</td>
<td>Card Emulation, Card Emulation Result, Operation Fail, Error</td>
</tr>
</tbody>
</table>

Table 340 - Additional Detail for Touchscreen, Signature Capture,
Success, Data Available (Touch Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 83 | 04 | File ID from ­Table 196 | B | R |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 341 - Notification Payload for Barcode Reader, Read Barcode
Result, Success (Encrypted Data Attached)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1805 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Data KSN</strong> parameter
and the <strong>Encrypted Data Encryption Type</strong> parameter to
read its contents. The format of the decrypted data is shown in
<strong>Table 342</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF50</td>
<td>var</td>
<td>Encrypted Data KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF51</td>
<td>01</td>
<td><p>Encrypted Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 342 - Notification Payload for Barcode Reader, Read Barcode
Result, Success (Unencrypted Data)

| Tag   | Len | Value / Description    | Typ | Req | Default |
|-------|-----|------------------------|-----|-----|---------|
| FC    | var | Barcode Data Container | T   | R   |         |
| /DF74 | var | Barcode Data           | B   | O   |         |

**Table 343 – Default User Interface String IDs and Strings**

| Display String ID | Display String               |
|-------------------|------------------------------|
| 0x0000            | “ ”                          |
| 0x0001            | “Thank You”                  |
| 0x0002            | “Hello”                      |
| 0x0003            | “Please Select”              |
| 0x0004            | “Touch Screen To Continue”   |
| 0x0005            | “Cancel”                     |
| 0x0006            | “Select a Transaction”       |
| 0x0007            | “Deposit”                    |
| 0x0008            | “Withdrawal”                 |
| 0x0009            | “Choose PIN”                 |
| 0x000A            | “Change PIN”                 |
| 0x000B            | “Balance”                    |
| 0x000C            | “Cash Advance”               |
| 0x000D            | “Authenticate Me”            |
| 0x000E            | “Transfer”                   |
| 0x000F            | “Make Payment”               |
| 0x0010            | “On Sale”                    |
| 0x0011            | “Discount”                   |
| 0x0012            | “Clearance”                  |
| 0x0013            | “\$5.00 /5 Mins.”            |
| 0x0014            | “\$6.00 /7 Mins.”            |
| 0x0015            | “\$7.00 /9 Mins.”            |
| 0x0016            | “\$8.00 /15 Mins.”           |
| 0x0017            | “Call Attendant”             |
| 0x0018            | “Print Receipt”              |
| 0x0019            | “Email Receipt”              |
| 0x001A            | “Text Receipt”               |
| 0x001B            | “Please Select An Amount”    |
| 0x001C            | “Please Select A Tip Amount” |
| 0x001D            | “Menu Selection 1”           |
| 0x001E            | “Menu Selection 2”           |
| 0x001F            | “Menu Selection 3”           |
| 0x0020            | “Menu Selection 4”           |
| 0x0021            | “Service Request”            |
| 0x0022            | “Show More”                  |
| 0x0023            | “Options”                    |
| 0x0024            | “What is the issue?”         |
| 0x0025            | “Exit”                       |
| 0x0026            | “No Hot Water”               |
| 0x0027            | “Doesn't Spin”               |
| 0x0028            | “Water Leakage”              |
| 0x0029            | “No Heat”                    |
| 0x002A            | “Please select a Machine”    |
| 0x002B            | “Pump 1”                     |
| 0x002C            | “Pump 2”                     |
| 0x002D            | “Pump 3”                     |
| 0x002E            | “Pump 4”                     |
| 0x002F            | “A1”                         |
| 0x0030            | “A2”                         |
| 0x0031            | “A3”                         |
| 0x0032            | “A4”                         |
| 0x0033            | “B1”                         |
| 0x0034            | “B2”                         |
| 0x0035            | “B3”                         |
| 0x0036            | “B4”                         |
| 0x0037            | “C1”                         |
| 0x0038            | “C2”                         |
| 0x0039            | “C3”                         |
| 0x003A            | “C4”                         |
| 0x003B            | “\$5.50 – Cake”              |
| 0x003C            | “\$5.00 – Muffin”            |
| 0x003D            | “\$6.50 – Croissant”         |
| 0x003E            | “\$4.50 – Danish”            |
| 0x003F            | “Req. QR Code”               |
| 0x0040            | “Scan QR Code”               |
| 0x0041            | “Scan NFC”                   |
| 0x0042            | “Call Server”                |
| 0x0043            | “Request Bill”               |
| 0x0044            | “Approve”                    |
| 0x0045            | “Reject”                     |
| 0x0046            | “Verify SMS”                 |
| 0x0047            | “Verify Email”               |
| 0x0048            | “English”                    |
| 0x0049            | “Spanish”                    |
| 0x0080            | “Hola”                       |
| 0x0081            | “Por Favor Seleccione”       |
| 0x0082            | “Toca Para Continuar”        |
| 0x0083            | “Cancelar”                   |
| 0x0084            | “Seleccione Una Transaccion” |
| 0x0085            | “Deposito”                   |
| 0x0086            | “Retiro”                     |
| 0x0087            | “Elija PIN”                  |
| 0x0088            | “Cambiar PIN”                |
| 0x0089            | “Adelanto En Efectivo”       |
| 0x008A            | “Autenticarme”               |
| 0x008B            | “Verificar SMS”              |
| 0x008C            | “Confirmar”                  |
| 0x008D            | “Mostrar Mas”                |
| 0x008E            | “Opciones”                   |
| 0x008F            | “Salida”                     |
| 0x0090            | “Transferir”                 |
| 0x0091            | “Realizar Pago”              |
| 0x0092            | “En Venta”                   |
| 0x0093            | “Descuento”                  |
| 0x0094            | “Autorizacion”               |
| 0x0095            | “Operador De Llamada”        |
| 0x0096            | “Imprimir Recibo”            |
| 0x0097            | “Correo Electronico”         |
| 0x0098            | “Recibo De Texto”            |
| 0x0099            | “Seleccione Una Cantidad”    |
| 0x009A            | “Anadir Un Consejo”          |
| 0x009B            | “Requerido Codigo QR”        |
| 0x009C            | “Escanear Codigo QR”         |
| 0x009D            | “Escanear NFC”               |
| 0x009E            | “Servidor De Llamadas”       |
| 0x009F            | “Solicitar Factura”          |
| 0x00A0            | “Aprobar”                    |
| 0x00A1            | “Rechazar”                   |
| 0x00A2            | “Gracias”                    |
| 0x00A3            | “Ingles”                     |
| 0x00A4            | “Espanol”                    |

String ID value can be from 0x0000 to 0x012B, and String length maximum
is 30 characters. This default configured Strings can be changed and
uploaded to the device. See **4.29 UI Configuration File Type**