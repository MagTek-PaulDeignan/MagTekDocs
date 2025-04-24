---
title: Battery Charge Status
layout: home
parent: Configuration
nav_order: 255
---

## Battery Charge Status

As mentioned in **Appendix G Physical Button (DynaFlex Only)**, there is
only one physical button on DynaFlex devices. Pressing and holding this
button until the device beeps six times then releasing it causes the
LEDs on the front of the device to display the current charge state of
the battery. The LEDs will return to their previous state after three
seconds.

| Battery Level | Transactions and Firmware Update Allowed | LED Color | LEDs On When Button is Pressed |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 100% - 90% | Yes | Green | 4 LEDs |  |  |  |  |
| 89% - 70% | Yes | Green | 3 LEDs |  |  |  |  |
| 69% - 50% | Yes | Green | 2 LEDs |  |  |  |  |
| 49% - 20% | Yes | Amber | 1 LED |  |  |  |  |
| 19% - 6% | Yes | Red | 1 LED |  |  |  |  |
| 5% - 0% | No | Red | 1 LED |  |  |  |  |

Table 1213 - Battery Charged Example

The DynaFlex II Go has only green LEDs. Instead of lighting the first
LED in amber, it will slowly flash the first LED. Instead of Red, the
first LED will flash quickly.