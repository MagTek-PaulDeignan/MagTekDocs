---
title: Configurations
layout: home
parent: DynaFlex Family Programmer's Manual
has_children: true
nav_order: 8
---
## Configuration

### About Configuration

The device provides two mechanisms for the host to retrieve information
about the device and to configure / customize device behavior:

- **Properties** are smaller configuration values (generally up to 255
  bytes and often significantly smaller). The device stores properties
  in a hierarchical tree, where each property has its own unique ID
  (sometimes referred to as an Object Identifier or OID) that identifies
  its position in the tree. The host can set and get properties using
  the commands in Command Group 0xD1nn - Settings and Information. For
  further information about OIDs, see **Appendix A Object IDs (OIDs) and
  ITU-T X660**.


- **Files** are larger configuration values, which include custom
  graphics files and large configuration data blobs such as EMV terminal
  and application settings. Each file has a unique identifier more akin
  to a file path in a file system. The host can set and get files using
  the commands in **Command Group 0xD8nn - File Operations**.

This section focuses on **properties**, which the host can either read
from the device to retrieve device information (such as its PCI hardware
ID, serial number, firmware revision numbers, etc.), or write to the
device to change device behavior, or to store values for future
reference.

Property unique IDs represent a tree structure, where each property is
at the “leaf” level of the tree. Some operations allow the host to work
with entire groups of properties (branches or even the trunk containing
all its leaves) by using a property number representing a higher level
of the tree.

Each property (a “leaf” in the tree) is described in a subsection below,
including whether it can be written to, how it is secured, how to
construct or interpret its value(s), and how it affects device behavior.

To reflect this hierarchy, this section of the document groups settings
by major categories that correspond to the tree structure, which roughly
breaks down into overall property **type**, **module**, and
**submodule**.


