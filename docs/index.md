---
title: Overview
layout: home
parent: 
nav_order: 1
---
# MagTek Docs

Welcome to the **MagTek Docs** developer documentation portal. This site consolidates technical resources for developers and integrators working with MagTek’s secure payment hardware. Whether you are installing a device, integrating with SDKs, or programming against the MagTek Messaging (MMS) or V5 Schemas , you’ll find structured documentation here.

## How to Use This Portal

*   **New users** — start with [Setup & Devices](/setup/) for installation and operation manuals.
    
*   **Developers and system integrators** — consult the [Web Docs](/web-docs/) for the authoritative MMS and V5 programming specifications. Web Docs include atomic references (commands, properties, notifications) and links to legacy PDF manuals.
    
*   **Application teams** — refer to the [SDK Guides](/sdks/) for sample code and platform-specific integration.
    

## Documentation Families

**🔧 Installation & Operation Manuals**  
Step-by-step setup and usage guides for each device family. Covers hardware installation, environment requirements, and daily operation.

**📘 Programmer’s Manuals**  
Authoritative MMS specifications for each device family.

*   **Scope:** command groups (e.g., 0x10nn, 0x11nn), configuration properties, notifications/response formats, and device-specific behavior.
    
*   **Formats:**
    
    *   **Legacy PDF (“Master Manual”)** — comprehensive, single-volume reference.
        
    *   **Web Docs (atomic)** — each command, property, and notification is an individual, linkable page for faster search and cross-reference.
        

During the transition, some families may offer both; **Web Docs** are the primary source.

**💻 SDK Guides & Sample Code**  
Integration resources for .NET, Java, iOS, Android, macOS, and Windows. Includes sample projects and platform-specific notes to accelerate development.

updated 12/19/2025

```javascript
await setMQTTSubTopic();
  await setMQTTPubTopic();
  mt_UI.LogData(`Done - Saving MQTT Configuration`);
  mt_UI.LogData("");
```

| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| --- | --- | --- | --- | --- |
| Cell 1-1 | Cell 1-2 | Cell 1-3 | Cell 1-4 | Cell 1-5 |
| Cell 2-1 | Cell 2-2 | Cell 2-3 | Cell 2-4 | Cell 2-5 |

```javascript
 if (cmds.status.ok){
     await parseCommands('Updating Device', cmds.data);
   }
   else
  {
```