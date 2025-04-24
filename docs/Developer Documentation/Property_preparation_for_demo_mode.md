---
title: Preparation for Demo Mode
layout: home
parent: Configuration
nav_order: 243
---

## Preparation for Demo Mode

---

- [Preparation for Demo Mode](#preparation-for-demo-mode)

---


To use the contactless reader, contactless events must be enabled.
Writing 03000000 to OID 1.2.7.1.2.1 will the enable events for the
contactless reader. See [**Property 1.2.7.1.2.1 User Event Notification
Controls
Enable**](#property-1.2.7.1.2.1-user-event-notification-controls-enable)
for more information.

The device must be powered using a USB charger to enter Demo Mode. Demo
Mode will not start when the device is powered from a USB host or when
running from the battery.

If an image is to be displayed in place of the prompt, download the
image to the fourth image file (02000003). See [**Command 0xD812 - Start
Send File to Device
(Unsecured)**](#command-0xd812---start-send-file-to-device-unsecured)
for more information.