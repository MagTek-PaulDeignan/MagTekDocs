---
title: Security
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 5
---

  - [About Message Authentication Codes (MAC)](#about-message-authentication-codes-mac)
    - [MACs for EMV Data](#macs-for-emv-data)
  - [About Key Serial Numbers (KSNs)](#about-key-serial-numbers-ksns)
  - [About Encryption and Decryption](#about-encryption-and-decryption)
  - [How to Determine the Key](#how-to-determine-the-key)
  - [How to Decrypt Data](#how-to-decrypt-data)
  - [24 Hour Automatic Reset PCI Requirement](#24-hour-automatic-reset-pci-requirement)
  - [Device Lock Feature](#device-lock-feature)

---


## Security

### About Message Authentication Codes (MAC)

“MAC” is an abbreviation of Message Authentication Code, which is a
string of bytes included in a message that can be used to provide
reasonable assurance that the message originated from a trusted source
and has not been modified.

#### MACs for EMV Data

This section describes how to calculate MACs for EMV ARQC and EMV Batch
Data.

The key and variant used to calculate the MAC is determined by how the
**DUKPT Key Mapping** is mapped, this can be set-up for TDES or AES
mode.

The key used to calculate the MAC is normally the same key used to
encrypt the encrypted data included as part of the same data structure.
For TDES MAC, the key variant is always ***Message Authentication,
Request or Both Ways***. For AES MAC, this can be AES-128 or AES-256,
the valid usages are: 0x08=MAC Generate, 0x0A=MAC Generate/Verify.

For TDES MAC:

ANSI X9.24-3-2017

The MAC operations follow the CBC procedure described in ISO 16609
Section C.4 using padding method 1 defined in ISO 9797 section 6.1.1.

For AES CMAC:

NIST Special Publication 800-38B

Section 6.2 MAC Generation

The data structure for both EMV ARQC and EMV Batch Data has the
following format related to MACing:

AAAA /\* 2-byte MSB message length excluding padding and CBC-MAC \*/

F9\<len\> /\* container for MAC structure and generic data \*/

DFDF54(MAC KSN)\<len\>\<val\>

DFDF55(MAC Encryption Type)\<len\>\<val\>

DFDF25(IFD Serial Number)\<len\>\<val\>

\<Nested TLV data objects specific to the message\>

\<Padding to force the 2-byte MSB message length plus F9 plus padding to
be a multiple of 8 bytes\>

\<Four byte CBC-MAC of all data starting with the 2-byte MSB message
length and ending with the last byte of padding (if any)\>

### About Key Serial Numbers (KSNs)

The device can use two different types of keys: Triple Data Encryption
Standard (TDES) DUKPT Keys and AES DUKPT Keys. The Key Serial Number
(KSN) format is slightly different depending on which type of key is
injected into the key slot that is being used by the operation being
performed or the data being passed.

When the device and host are using TDES keys, the Key Serial Number
(KSN) is an 80-bit value. The rightmost 21 bits are the current value of
the encryption counter associated with that key. The leftmost 59 bits
are the **Initial KSN** for that key, which is specified during key
injection and is a combination of the **Key Set ID** that identifies the
Base Derivation Key (BDK) injected into the device during manufacture,
and the device’s serial number (DSN); how those two values are combined
into the 59 bit Initial KSN is defined by a convention the customer
defines when architecting the solution, with support from MagTek. For
example, one common scheme is to concatenate a 7 hex digit (28 bit) Key
Set ID, a 7 hex digit (28 bit) Device Serial Number, and a 3 bit
**Initial Key Load Counter** the injecting host increments each time the
same key is re-loaded into the device. In these cases, the key can be
referenced by an 8-digit MagTek part number (“key ID”) consisting of the
7 hex digit Key Set ID plus a trailing “0.”

### About Encryption and Decryption

Some data exchanged between the device and the host is encrypted. This
includes parts of the **EMV ARQC Type** and the **EMV Batch Data Type**.
To decrypt this data, the host must first determine what key to use,
then decrypt the data. The following sections explain each of those
steps in detail.

### How to Determine the Key

When the device and the host are using TDES DUKPT key and the device is
encrypting data, the host software must do the following to generate a
key (the “derived key”) to use for decryption:

1)  **Determine the value of the Initial Key loaded into the device**.
    The lookup methods the host software uses depend on the overall
    solution architecture, and are outside the scope of this document.
    However, most solutions do this in one of two ways, both of which
    use the Initial Key Serial Number that arrives with the encrypted
    data:

    1)  Look up the value of the Base Derivation Key using the Initial
        KSN portion of the current KSN as an index value, then use TDES
        DUKPT algorithms to calculate the value of the Initial Key; or

    2)  Look up the value of the Initial Key directly, using the Initial
        KSN portion of the current KSN as an index value.

2)  **Derive the current key**. Apply TDES DUKPT algorithms to the
    Initial Key value and the encryption counter portion of the KSN that
    arrives with the encrypted data.

3)  **Determine which variant of the current key the device used to
    encrypt**. The variants are defined in ***ANS X9.24-1:2009 Annex
    A***, which programmers of host software must be familiar with.
    Which variant the host should use depends on the type of data the
    host is decrypting. The encrypted portions of EMV ARQC and EMV Batch
    Data both use the *Data Encryption, Request or Both Ways* variant.

4)  Use the variant algorithm with the current key to calculate that
    variant.

5)  Decrypt the data according to the steps in section **5.5 How to
    Decrypt Data**.

### How to Decrypt Data

For EMV ARQC and EMV Batch Data, the device begins by TDES encrypting
the first 8 bytes of clear text data. The 8-byte result of this
encryption is placed in an encrypted data buffer. The process continues
using the TDES CBC (Cipher Block Chaining) method with the encrypted 8
bytes XORed with the next 8 bytes of clear text. That result is placed
in next 8 bytes of the encrypted data buffer, and the device continues
until all clear text bytes have been encrypted. If the final block of
clear text contains fewer than 8 bytes, the device pads the end of the
block to make 8 bytes. After the final clear text block is XORed with
the prior 8 bytes of encrypted data, the device encrypts it and places
it in the encrypted data value. No Initial Vector is used in the
process.

The host must decrypt the data in 8 byte blocks, ignoring any final
unused bytes in the last block. When a value consists of more than one
block, the host should use the CBC method to decrypt the data by
following these steps:

1)  Start decryption on the last block of 8 bytes (call it block N)
    using the key.

2)  XOR the result of the decryption with the next-last block of 8 bytes
    (block N-1).

3)  Repeat until reaching the first block.

4)  Do not XOR the first block with anything.

5)  Concatenate all blocks.

6)  Determine the expected length of the decrypted data. For EMV ARQC
    and EMV Batch Data this information is included as part of the
    unencrypted data structure.

7)  Truncate the end of the decrypted data block to the expected data
    length, which discards the padding at the end.

### 24 Hour Automatic Reset PCI Requirement

Due to Payment Card Industry (PCI) certification requirements, the
device must automatically reset at least once every 24 hours. This is
required for security purposes, so that the device can reinitialize
memory and perform a self-test. Host software developers and potentially
end users should be aware of this.

By default, the device will automatically reset 23 hours after it boots
up and it will attempt to send a warning notification message to the
host 3 minutes before the reset occurs.

The default behavior is adjustable. See the following for more
information.

**Property 1.2.7.1.1.4 Auto Reset Configuration**

**Property 1.2.7.1.1.3 Device Reset Will Occur Soon Notification
Control**

Device Reset Will Occur Soon notification in **Notification 0x1001 -
Device Information Update**

One way the host software could handle receiving a device reset will
occur notification would be as follows.

1)  Cancel any operation that is in process like a transaction if it is
    unlikely to end before the reset.

2)  Optionally send **Command 0x1F01 - Reset Device** instead of waiting
    for the automatic reset to occur.

3)  Re-connect with the device and re-start any operation that was in
    process.

### Device Lock Feature

The purpose of locking a device is to disable most of the device’s
functionality for use cases that need this extra layer of security. When
a device is locked, it will reject all commands except for a few. This
locks the majority of the device’s functionality. Use of the device lock
feature is optional. It is not required by PCI.

The device lock state can be either unlocked or locked. The device lock
state can be retrieved by getting a property.

The device lock state can be changed by setting a secure property or it
can be changed with a command that requires knowledge of the device lock
passcode.

The device can be configured to always have the device lock state set to
locked after a reset or power cycle by setting a property.

If the device has a display and the device is locked, the welcome screen
will display “WELCOME” “Device is Locked”. This screen can be
customized.

The device lock passcode can be changed by setting a secure property or
it can be changed with a command that requires knowledge of the current
device lock passcode.

The following commands and properties can be used to manage the device
lock feature:

**Command 0xEF06 – Change Device Lock State**

**Command 0xEF07 – Change Device Lock Passcode**

**Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR
NOW)**

**Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display
Only)**

**Property 1.2.5.2.1.1 Device Lock State**

**Property 1.2.5.2.1.2 Device Lock State After Reset**

**Property 1.2.5.2.1.3 Device Lock Passcode**

Only the following commands are allowed when the device lock state is
set to locked:

**Command 0x1F01 - Reset Device**

**Command 0x1F03 - Extend Session (Session Management Only)**

**Command 0x1F04 – Terminate Bluetooth® LE Connection (Bluetooth® LE
Only)**

**Command 0xD101 - Get Property**

**Command 0xD112 - Set Property (Secured)**

**Command 0xDF01 - Echo**

**Command 0xE001 - Get Challenge**

**Command 0xEF06 – Change Device Lock State**

**Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR
NOW)**

**Command 0xEF11 - Get Key Info**

**Command 0xEEEE - Send Secured Command to Device**

