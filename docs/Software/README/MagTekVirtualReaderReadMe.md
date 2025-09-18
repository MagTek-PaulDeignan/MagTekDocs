---
title: Read Me
layout: home
parent: MagTekVirtual Reader
nav_order: 
---

# MagTekVirtualReader iOS SDK Code & Integration Guide



Accept contactless in-person payments on iPhone using Tap to Pay on iPhone with the [Magensa Payment Protection Gateway](https://www.magtek.com/product/mppg-services) (MPPG). This repository includes a sample app and integration notes to help you get running quickly.

Table of contents
=================
- [MagTekVirtualReader iOS SDK Code \& Integration Guide](#magtekvirtualreader-ios-sdk-code--integration-guide)
- [Table of contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Run and Test](#run-and-test)
  - [Best Practices](#best-practices)
  - [Terms and Conditions](#terms-and-conditions)
  - [License](#license)

## Requirements
- iOS: 17.4+
- Devices: iPhone models that support Tap to Pay on iPhone (physical device required; simulator is not supported)
- Xcode: 15+ (recommend latest stable)
- Account: A Magensa account (username & password)

ℹ️ If your app targets iOS versions < 17.4, you can still compile, but Tap to Pay flows will be runtime-gated to supported OS/device versions.

## Installation
- Download the latest MagTek VirtualReader SDK
- Drag the framework into your Xcode project and set Embed & Sign.
- For Action select “Copy files to destination”.
- For Target select your application.

- Add the ProximityReader.framework

## Configuration
The high level flow of the sample app is outlined below.

- Initialize MagTekT2PConfig with username, password and tokenURL:
```javascript
let magTekT2PConfig = MagTekT2PConfig(userName: username, password: password, url: tokenURL, readerID: "")
```

- Initialize MagTekT2PCardReader with configuration.
```javascript
let magTekVirtualCardReader = MagTekVirtualCardReader(config: magTekT2PConfig)
```

- After initialization is complete perform a check to verify the device supports Tap To Pay (T2P). Only enable T2P UI and functionality if the device supports T2P. T2P is not supported on iPads or older iOS devices.
```javascript
if magTekVirtualCardReader.isTapToPaySupported() {
    // Enable T2P UI in application.
}
```

- In order to process payments you must initialize a valid session. This is a simplified version of the code in the sample app:
```javascript
override func preparePaymentCardReaderSession() {
    let myevents = magTekVirtualCardReader?.getPaymentCardReaderEvents()
    
    Task {
        if let events = myevents {
            for await event in events {
                // Handle event in the app
                DispatchQueue.main.async {
                    // Perform UI Updates
                }
            }
        }
    }
    
    Task {
        guard let reader = self.magTekVirtualCardReader else {
            throw NSError(domain: "ReaderError", code: -1, userInfo: [NSLocalizedDescriptionKey: "Reader not available"])
        }
        
        do {
            let token = try await magTekVirtualCardReader?.fetchPaymentCardReaderTokenFromMagensaPSP(self.magTekT2PConfig)
            _ = try await reader.prepareCardReaderSessionWithToken(token!)
            
            DispatchQueue.main.async {
                // Perform UI updates
            }
        } catch {
            await handlePaymentCardReaderError(error)
        }
    }
}
```

- If there are no session initialization errors you are ready to perform payment transactions. Before making a payment request verify the session is active. In the sample code this is done via the magTekT2PViewModel:
```javascript
if mtViewModel.isCardReaderSessionActive {
    mtViewModel.pay(magTekT2PViewModel.amountDecimal)
} else {
    Task {
        await mtViewModel.processTapToPayTransaction(mtViewModel.amountDecimal)
    }
}
```

## Run and Test
- Connect a physical iPhone to your Mac.
- Open the sample app target and Build & Run.
- Enter your Magensa username & password on the login screen.
- Enter a test amount and choose Tap to Pay.
- Follow on-device prompts to complete a contactless transaction.

You’ll see success/failure states and basic logging in the sample UI.

## Best Practices
- Do not hardcode Magensa credentials or store them in UserDefaults. There are many well known [vulnerabilities](https://www.security.com/threat-intelligence/exposing-danger-within-hardcoded-cloud-credentials-popular-mobile-apps).
- Use Keychain for tokens/secrets.
- Error handling: Show user-friendly errors; capture SDK diagnostics in development builds only.

## Terms and Conditions
[Terms and Conditions](https://www.magtek.com/about/policy?tab=terms)

## License
[License](https://www.magtek.com/about/policy?tab=software)

