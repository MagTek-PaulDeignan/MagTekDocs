---
title: Qwantum Multi-factor Authentication™ Service
layout: home
parent: Web Docs
---

# Access Control & MFA API Documentation

This documentation covers the `AccessControlController` and `MFAController` endpoints. These APIs manage Users, Tokens, Devices, and Transactions within the Qwantum profile ecosystem.

## General Configuration

### Request Headers

| Header | Description | Required |
| :--- | :--- | :--- |
| `QwantumProfile` | Selects the DB collection context (e.g., `DBAuth`, `DBToken`). | Required |

### Universal Usage Notes
* **Authentication:** Most endpoints return `200 OK` on success. Errors are returned via `ExternalError.Response`.
* **Token Lookups:** Provide `Name` or `TokenName`. If the value starts with `Q002|`, it is automatically decrypted.
* **Delivery Channels:** Use the `Using` parameter to switch between `"SMS"` (default) and `"email"`.
* **Time Formats:** `AllowedTimes` follows the format: `DayIndex-StartTime-EndTime` (e.g., `1-08:00:00-17:00:00` for Monday).

---

## User Management
Endpoints for managing user accounts, profiles, and administrative locks.

### Create User
**POST** `api/QMFA/Admin/User/Create`
* **Purpose:** Create a new user account and initialize credentials.
* **Parameters:** `Username` (Req), `Firstname`, `Lastname`, `Email`, `SMSNumber`, `Password`, `MaxInvalidAttempts` (Default: 5).
* **Side Effects:** If `Password` is omitted, the system triggers `ResetPassword` to generate and send one.

### Read User
**POST** `api/QMFA/Admin/User/Read`
* **Purpose:** Retrieve full profile details for a specific user.
* **Parameters:** `Username` (Req).

### Update User
**POST** `api/QMFA/Admin/User/Update`
* **Purpose:** Update specific user attributes or claims.
* **Parameters:** `Username` (Req), `Firstname`, `Lastname`, `Email`, `SMSNumber`, `AccountStatus`, `IsLocked`, `Claims` (via `apiRequest.Claims`).

### Delete User
**POST** `api/QMFA/Admin/User/Delete`
* **Purpose:** Permanently remove a user from the system.
* **Parameters:** `Username` (Req).

### User Status (Lock/Unlock)
**POST** `api/QMFA/Admin/User/Lock` | `api/QMFA/Admin/User/Unlock`
* **Purpose:** Administratively enable or disable user access.
* **Behavior:** Unlocking also resets `InvalidAuthAttempts` to 0.

---

## Token Management
Endpoints for creating and managing access tokens, including specialized Apple/Google Wallet (VAS) passes.

### Create Token
**POST** `api/QMFA/Admin/Token/Create`
* **Purpose:** Generate a new access token for an owner.
* **Key Parameters:** `OwnerID` (Req), `TokenName`, `TokenPrefix`, `ExpDate`, `MaxUses`.
* **TOTP Setup:** If `SetupTOTP` is `"true"`, it triggers a TOTP reset and delivery.

### Redeem Token
**POST** `api/QMFA/Authorize/Token/Redeem`
* **Purpose:** Validate and use a token.
* **Key Behavior:** Increments usage count and enforces `AllowedTimes`. Sensitive fields like `TOTPSecret` are stripped from the response.

### Create VAS/Wallet Token
**POST** `api/QMFA/Admin/Token/VAS/Create`
* **Purpose:** Create Apple VAS / Wallet-optimized tokens (PKPass).
* **Key Parameters:** `Username` (Req), `PKUseNFC`, `QRDarkColor`, `QRLogo`, `PKPassAttach`.
* **Delivery:** Can deliver via SMS, email, or by injecting the base64 data directly into the user's `Claims`.

---

## Authentication & MFA
Endpoints for verifying identity via Password, OTC, TOTP, and HID hardware.

### One-Time Code (OTC)
**POST** `api/QMFA/Authorize/User/OTC/Send` | `api/QMFA/Authorize/User/OTC/Verify`
* **Purpose:** Request and verify a short-lived numeric code.
* **Configuration:** `OTCLength`, `OTCFormat`, `OTCDuration`.

### TOTP (Authenticator App)
**POST** `api/QMFA/Authorize/User/TOTP/Verify` | `api/QMFA/Admin/User/TOTP/Reset`
* **Purpose:** Manage and verify Time-based One-Time Passwords.
* **Tolerance:** Default window is 5 minutes (`TOTPTimeTolerance`).

### Password Management
**POST** `api/QMFA/Authorize/User/Password/Verify` | `api/QMFA/Authorize/User/Password/Update`
* **Purpose:** Standard credential verification and self-service updates.

### HID Tag Verification
**POST** `api/QMFA/Authorize/HID/Verify`
* **Purpose:** Verify physical HID hardware tags.
* **Parameters:** `tagID` (Req), `tac` (Tag Authentication Code).

---

## Device Management
Endpoints for managing hardware "Access Devices" (readers).

### Create/Read Device
**POST** `api/QMFA/Admin/Device/Create` | `api/QMFA/Admin/Device/Read`
* **Purpose:** Manage records of physical hardware readers.
* **Parameters:** `DeviceName` (Req), `Description`, `Type`.

### List Devices
**POST** `api/QMFA/Admin/Device/List`
* **Purpose:** Returns a list of all registered access devices.

---

## Transaction Management
Endpoints for creating and redeeming transient, short-lived transaction tokens.

### Create Transaction
**POST** `api/QMFA/Authorize/Transaction/Create`
* **Purpose:** Create a GUID-based transaction and notify a recipient.
* **Default Expiry:** 600 seconds (10 minutes).

### Redeem Transaction
**POST** `api/QMFA/Authorize/Transaction/Redeem`
* **Purpose:** Complete a transaction and record the outcome.
* **Parameters:** `TransactionToken`, `RedemptionStatus`, `RedemptionReason`.

---

## Example Request
All POST requests should wrap parameters in an `InputParameters` object.

```json
{
  "InputParameters": {
    "TokenName": "Q002|ENCRYPTED_DATA_HERE",
    "Using": "email",
    "Template": "TokenOTCSend",
    "OTCLength": "6"
  },
  "Claims": {
    "role": "admin",
    "department": "IT"
  }
}
```


API endpoint documentation for `QMFA`. Each section shows route, method, function name, purpose, InputParameters (KVPs read), defaults and required flags, key behaviors and side effects.

Header note
- Header: `QwantumProfile` — optional. When present it selects DB collection names (`DBAuth`, `DBToken`, `DBAccessToken`, `DBAccessDevice`).

Usage note
- For token lookups provide either `Name` or `TokenName`. If the value starts with `Q002|` the controller calls `Utils.MagensaDecryptTokenAsync`.
- Most endpoints return 200 OK on success and use `ExternalError.Response(...)` on error.
- `AllowedTimes` format expected by `IsAuthorizedNow`: comma-separated segments `DayIndex-StartTime-EndTime`, e.g. `1-08:00:00-17:00:00,2-08:00:00-17:00:00` (Mon/Tue).

Endpoints

---

### POST `api/QMFA/Authorize/Token/Redeem
- Purpose: Redeem a token, increment `NumUsesCount`, enforce rules and return token DTO with sensitive fields nulled.
- InputParameters (KVPs):
  - `Name` (string) or `TokenName` (string) — required. `Q002|` decrypt handled.
- Behavior:
  - Validates token and owner, checks `Enabled`, `IsExpired`, `AllowedTimes`, `NumUsesMax`.
  - Persists incremented use count (`DBAccessToken.Replace`).
  - Returned DTO clears `OTC` and `TOTPSecret`.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid name, token not found, not authorized time, token disabled/expired, account errors.

---

### POST `api/QMFA/Admin/Token/Read`
- Purpose: Return token details.
- InputParameters:
  - `Name` or `TokenName` — required. `Q002|` decrypt handled.
- Behavior: Finds token and returns `AccessTokenDTO`.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid name, token not found.

---

### POST `api/QMFA/Admin/Token/List`
- Purpose: Search tokens.
- InputParameters:
  - `Search` (string) — optional (empty string accepted).
  - `SearchType` (string) — optional, default `"Equals"` (examples: `"Equals"`, `"startswith"`).
- Behavior: Calls `DBAccessToken.List(name, searchType)` and returns list DTO.
- Responses:
  - 200: list of `AccessTokenDTO`
  - Errors: token not found (per DB behavior).

---

### POST `api/QMFA/Admin/Token/ListByOwner`
- Purpose: List tokens for a given owner.
- InputParameters:
  - `Search` (string) — required (owner name).
  - `SearchType` — present but unused by implementation.
- Behavior: Calls `DBAccessToken.ListbyOwner(Search)` and returns token DTO list.
- Responses:
  - 200: list of `AccessTokenDTO`
  - Errors: invalid name, token not found.

---

### POST `api/QMFA/Admin/Token/Create`
- Purpose: Create a new token for a user; optionally set up TOTP.
- InputParameters:
  - `Name` or `TokenName` — optional; if omitted the server builds `{TokenPrefix}{GUID}`.
  - `TokenPrefix` (string) — optional.
  - `OwnerID` (string) — required.
  - `Data`, `TokenType`, `Description`, `ActionType`, `AllowedTimes`, `AuthorizedDeviceList` — optional.
  - `MaxUses` — optional (string/int), default `"0"`.
  - `ExpDate` — optional, default = UTC.Now + 365 days.
  - `SetupTOTP` — optional (`"false"` default). If true:
    - `Template` (string) — default `"SetupTokenTOTP"`.
    - `Using` — controls delivery (`"SMS"` or `"email"`), plus `TemplateData`, `IssuerName`, `From`, `Subject`, `DisplayName` used inside `ResetTOTP`.
- Behavior:
  - Validates owner exists, creates `AccessTokenType`, inserts, optionally calls `ResetTOTP`.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: user not found, create failed.

---

### POST `api/QMFA/Admin/Token/Update`
- Purpose: Update token attributes.
- InputParameters:
  - `Name` or `TokenName` — required.
  - Optional: `Data`, `Description`, `TokenType`, `OwnerID`, `ExpDate`, `NumUsesMax`, `Enabled`, `AllowedTimes`, `ActionType`.
  - `Claims` may be provided in `apiRequest.Claims` to replace token claims.
- Behavior: Loads token, applies provided fields, `DBAccessToken.Upsert`.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid name, token not found.

---

### POST `api/QMFA/Admin/Token/Delete`
- Purpose: Delete a token.
- InputParameters:
  - `Name` or `TokenName` — required. `Q002|` decrypt handled.
- Behavior: Deletes token via `DBAccessToken.Delete`.
- Responses:
  - 200: delete result (boolean or object per DB impl)
  - Errors: invalid name, token not found.

---

### POST `api/QMFA/Admin/Device/Read`
- Purpose: Read an access device (token reader).
- InputParameters:
  - `Name` or `DeviceName` — required.
- Behavior: Returns `AccessDeviceType`.
- Responses:
  - 200: `AccessDeviceType`
  - Errors: invalid name, device not found.

---

### POST `api/QMFA/Admin/Device/List`
- Purpose: List or search devices.
- InputParameters:
  - `Search` — optional.
  - `SearchType` — optional, default `"Equals"`.
- Behavior: If `Search` empty returns `DBAccessDevice.List()`, else `List(name, searchType)`.
- Responses:
  - 200: list of `AccessDeviceType`.

---

### POST `api/QMFA/Admin/Device/Create`
- Purpose: Create device record.
- InputParameters:
  - `Name` or `DeviceName` — required.
  - `Description`, `Type` — optional.
  - `Enabled` — optional, default `"true"`.
  - Claims passed via `apiRequest.Claims` are copied into `DeviceInfo.Claims`.
- Behavior: Inserts device and seeds an empty `PublishTo` entry.
- Responses:
  - 200: created `AccessDeviceType`
  - Errors: invalid name, create failed.

---

### POST `api/QMFA/Admin/Device/Update`
- Purpose: Intended to update a device — currently a stub.
- Behavior: Returns `Ok(true)`. Implementation required to accept KVPs and perform upsert.
- Responses:
  - 200: `true` (stub)

---

### POST `api/QMFA/Admin/Device/Delete`
- Purpose: Delete a device.
- InputParameters:
  - `Name` or `DeviceName` — required.
- Behavior: Deletes device and returns the deleted `AccessDeviceType`.
- Responses:
  - 200: deleted `AccessDeviceType`
  - Errors: invalid name, device not found.

---

### POST `api/QMFA/Authorize/Token/OTC/Send`
- Purpose: Generate and send OTC to token owner via SMS or email.
- InputParameters:
  - `TokenName` — required.
  - `Using` — optional, default `"SMS"`; `"email"` uses `SendTOTCEmail`.
  - OTC-generation parameters passed into `SendTOTCEmail` / `SendTOTCSMS`:
    - `OTCLength`, `OTCFormat`, `OTCDuration` — optional control values.
    - `Template` — default `"TokenOTCSend"`; `.htm` for email, `.txt` for SMS.
    - `Subject`, `From`, `DisplayName`, `TemplateData` used by email.
- Behavior:
  - Validates token and user account status, generates OTC (or uses provided external code), stores `TokenInfo.OTC.AuthData` (SHA256 of token name + numeric code), sends message and persists token.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid name, user not found, send failed, account errors.

---

### POST `api/QMFA/Authorize/Token/OTC/Verify`
- Purpose: Verify an OTC previously sent.
- InputParameters:
  - `TokenName` — required.
  - `OTC` — required.
- Behavior:
  - Checks OTC expiry, computes SHA256 (token name + numeric code) and compares with stored `TokenInfo.OTC.AuthData`.
  - On success updates `EmailAddressVerified` or `SMSNumberVerified`, clears/updates `InvalidAuthAttempts`, expires OTC where applicable, persists user and token.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid OTC, expired OTC, verify failed, account errors.

---

### POST `api/QMFA/Admin/Token/TOTP/Reset`
- Purpose: Reset a token's TOTP secret and deliver setup (QR/manual code).
- InputParameters:
  - `TokenName` — required.
  - Used by `ResetTOTP`: `Template` (default `ResetTokenTOTP`), `Using` (default `"SMS"`), `IssuerName`, `Subject`, `From`, `DisplayName`, `TemplateData`.
- Behavior:
  - Generates a 10-char key, encrypts into `TokenInfo.TOTPSecret`, stores token, builds TOTP setup (QR URL + manual entry code) via `Google.Authenticator`, sends via email or SMS.
  - Resets the user's `InvalidAuthAttempts`.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid name, token not found, user not found.

---

### POST `api/QMFA/Authorize/Token/TOTP/Verify`
- Purpose: Verify a user-provided TOTP.
- InputParameters:
  - `TokenName` — required.
  - `TOTP` — required.
- Behavior:
  - Decrypts `TokenInfo.TOTPSecret`, strips non-digits from `TOTP`, validates using `Google.Authenticator` with tolerance configured by `TOTPTimeTolerance` (default 5 minutes), updates `InvalidAuthAttempts` and `LastLoginAttempt`.
- Responses:
  - 200: `AccessTokenDTO`
  - Errors: invalid name, verify failed, account errors.

---

### POST `api/QMFA/Admin/Token/VAS/Create`
- Purpose: Create Apple VAS / Wallet-optimized token, optionally generate QR and `.pkpass`, and deliver to user via email/SMS/claims.
- InputParameters highlights:
  - `TokenName` — optional (GUID default).
  - `Username` — required (owner).
  - `Data`, `TemplateData`, `Description`, `MaxUses`, `ExpDate`, `ActionType`, `AllowedTimes`, `AuthDevList` — optional.
  - `PKUseNFC` (read with `Utils.GetDictValue`) — optional; influences default `Type` (`"VAS"` vs `"Barcode"`).
  - Delivery options:
    - `Using` — `"SMS"` default, `"email"`, or `"claims"`.
    - `Template` — default `"GenerateVASToken"`.
    - `TokenURL` — used to build QR code (token URL + token name).
    - QR customization: `QRPixelsPerModule`, `QRDarkColor`, `QRLightColor`, `QRLogo`, `QRIconSizePercent`, `QRIconBorderWidth`, `QRDrawQuietZones`.
    - PKPass options: `PKPassName`, `PKPassAttach` (`"false"` default).
    - Email send options: `Subject`, `From`, `DisplayName`.
- Behavior:
  - Inserts token, generates QR if requested, optionally generates `.pkpass`, and either sends email/SMS with attachments or writes values into user's claims.
- Responses:
  - 200: `ExternalAuthResponse` (built from `UserInfo`)
  - Errors: invalid username, user not found, pass generation failure.

---

Example request (generic)
```json
{
  "InputParameters": {
    "TokenName": "TOTP~958a2153-606a-4539-bffa-796ffa3a24e9",
    "Using": "SMS",
    "Template": "TokenOTCSend",
    "OTCLength": "6"
  },
  "Claims": {
    "role": "admin"
  }
}
```

Header note
- Header: `QwantumProfile` — optional; when present it selects DB collections (`DBAuth`, `DBToken`, `DBTransaction`).

General usage notes
- Provide `Username` where user-specific operations require it.
- Many endpoints accept optional `Using` (`"SMS"` default) to choose delivery channel (SMS vs email).
- Templates and mail/sms fields are read by `DBToken.GetDictValue` KVPs (see per-endpoint lists).
- Error responses use `ExternalError.Response(...)` with codes from `ExternalError.ErrorCode`.
- Token/time formats: `ExpDate` parseable by `Convert.ToDateTime`; TOTP tolerance configured by `TOTPTimeTolerance` (default 5).

Endpoints

---

### POST `api/QMFA/Authorize/User/Message/Send`
- Purpose: Send an arbitrary message to a user (email or SMS).
- InputParameters (KVPs):
  - `Username` (string) — required.
  - `Using` (string) — optional, default `"SMS"`. Accepts `"email"` or `"sms"`.
  - `Template` (string) — optional, default `"MsgSend"`.
  - `Subject`, `From`, `DisplayName`, `TemplateData` — optional for email templates.
- Behavior:
  - Validates user and account status.
  - Calls `SendMessageEmail` or `SendMessageSMS` depending on `Using`.
  - `SendMessageEmail` reads `Emailcc`, `Emailbcc`.
- Success: 200 with `ExternalAuthResponse` (user info / claims).
- Errors: invalid username, user not found, account status, send failure.

---

### POST `api/QMFA/Authorize/User/OTC/Send`
- Purpose: Generate and send a one‑time code (OTC) to a user via SMS or email.
- InputParameters:
  - `Username` — required.
  - `Using` — optional, default `"SMS"`.
  - Template/send KVPs used by send helpers:
    - `Template` (default `"OTCSend"`), `Subject`, `From`, `DisplayName`, `TemplateData`.
    - OTC generation overrides use `OTCLength`, `OTCFormat`, `OTCDuration` when present (from user record in this controller).
- Behavior:
  - Validates user and account status.
  - Uses `SendOTCEmail` or `SendOTCSMS` which generate code, compute `AuthData` (SHA256 of username + code), set `userInfo.OTC` fields and persist via `DBAuth.Upsert`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found, account status, send failure.

---

### POST `api/QMFA/Authorize/User/OTC/Verify` 
- Purpose: Verify an OTC provided by the user.
- InputParameters:
  - `Username` — required.
  - `OTC` — required.
- Behavior:
  - Loads user, checks `userInfo.OTC.ExpDate`, computes SHA256 of username + numeric code and compares to `userInfo.OTC.AuthData`.
  - On success sets `EmailAddressVerified` or `SMSNumberVerified`, expires the OTC, resets invalid attempts and persists.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username/OTC, OTC expired, verify failed, account status.

---

### POST `api/QMFA/Authorize/HID/Verify`
- Purpose: Verify an HID tag using `HIDVerify`.
- InputParameters:
  - `tagID` (string) — required.
  - `tac` (string) — required (Tag Authentication Code).
- Behavior:
  - Creates `HIDVerify` and calls `VerifyHID(m_Profile, tagID, tac)`.
  - Returns the verification response object directly.
- Success: 200 with `verifyResponse`.
- Errors: propagation of verify errors (via `ExternalError.Response`).

---

### POST `api/QMFA/Authorize/User/Password/Verify`
- Purpose: Verify a user password.
- InputParameters:
  - `Username` — required.
  - `Password` — required (can be empty but Verify will fail).
- Behavior:
  - Loads user, checks account status, calls `VerifyPassword` which compares SHA256(user.Name + password) to stored `PasswordAuthData`.
  - Updates `InvalidAuthAttempts` and `LastLoginAttempt`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found, verify failed, account status.

---

### POST `api/QMFA/Authorize/User/Password/Update`
- Purpose: Allow a user to change their password.
- InputParameters:
  - `Username` — required.
  - `Password` — current password (string).
  - `NewPassword` — new password (string).
  - Template/send overrides via `RequestDictionary` used by `UpdatePassword`.
- Behavior:
  - Validates user, account status, calls `UpdatePassword` which:
    - Verifies current password (if `PasswordAuthData` present), then sets SHA256(user.Name + NewPassword) into `PasswordAuthData`.
    - Sends notification via `Template`/`Using` (`UpdatePassword`/`ACUpdatePassword`).
    - Updates `InvalidAuthAttempts` and `LastLoginAttempt`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found, verify/update failed.

---

### POST `api/QMFA/Authorize/User/TOTP/Verify`
- Purpose: Verify a user TOTP.
- InputParameters:
  - `Username` — required.
  - `TOTP` — required.
- Behavior:
  - Loads user, account status check, calls `VerifyTOTP` which decrypts `userInfo.TOTPSecret`, strips non-digits from `TOTP`, validates against `Google.Authenticator` with tolerance `TOTPTimeTolerance` (default 5).
  - On failure increments `InvalidAuthAttempts`; on success clears it and updates `LastLoginAttempt`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, verify failed, account status.

---

### POST `api/QMFA/Admin/User/TOTP/Reset`
- Purpose: Generate and send a new TOTP secret (QR + manual code) to a user.
- InputParameters:
  - `Username` — required.
  - `Template` (default `"ResetTOTP"`), `Using` (`"SMS"` default), `Subject`, `From`, `DisplayName`, `IssuerName`, `TemplateData` — optional.
- Behavior:
  - Generates a 10-char TOTP key, encrypts into `userInfo.TOTPSecret`, persists, generates setup QR/manual codes using `Google.Authenticator`, and sends via SMS or email.
  - Resets `InvalidAuthAttempts` and `LastLoginAttempt`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found, send failure.

---

### POST `api/QMFA/Admin/WebAuth/Reset`
- Purpose: Reset WebAuth API key for a user (creates a new `WebAPIKey` and stores SHA256).
- InputParameters:
  - `Username` — required.
  - `Template` (default `"ResetWebAuth"`), `Using` (`"SMS"` default), `Subject`, `From`, `DisplayName`, `TemplateData` — optional.
- Behavior:
  - Creates `WebAPIKey` (`user.Name + "-" + GUID`), stores SHA256 into `userInfo.WebAPIAuthData`, persists.
  - Inserts `WebAPIKey` and selected claims into `RequestDictionary` and sends via configured channel.
  - Resets `InvalidAuthAttempts` and `LastLoginAttempt`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found, send failure.

---

### POST `api/QMFA/Admin/User/Password/Reset`
- Purpose: Reset a user password (generate random password and notify).
- InputParameters:
  - `Username` — required.
  - `Format` (string) — optional for password generator, default `"WDDW"`.
  - `Using` (default `"SMS"`), `Template`, `Subject`, `From`, `DisplayName`, `TemplateData` — optional for notification.
- Behavior:
  - Generates new password using `Utils.GenerateRandomPassword(Format)`, sets `PasswordAuthData` to SHA256(user.Name + NewPassword), persists user.
  - Sends the new password to user via `SendOTCEmail`/SMS-like template (templates default to `"ResetPassword"` / `"ACResetPassword"` based on previous password presence).
  - Resets `InvalidAuthAttempts` and `LastLoginAttempt`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, send/update failure.

---

### POST `api/QMFA/Admin/User/Create`
- Purpose: Create a new user account.
- InputParameters:
  - `Username` — required.
  - `Firstname`, `Lastname`, `Password` (optional), `Email`, `SMSNumber`, `MaxInvalidAttempts` (default `"5"`), `Claims` via `apiRequest.Claims`.
  - If `Password` omitted, controller calls `ResetPassword` to generate and send one.
- Behavior:
  - Inserts user (`DBAuth.Insert`), validates account status; if `Password` provided sets via `UpdatePassword`, else calls `ResetPassword`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, create failed, update/reset failed.

---

### POST `api/QMFA/Admin/User/Read`
- Purpose: Read user details.
- InputParameters:
  - `Username` — required.
- Behavior: Returns `ExternalAuthResponse` derived from `WebAPIAuthType`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found.

---

### POST `api/QMFA/Admin/User/Update`
- Purpose: Update user properties.
- InputParameters (KVPs read via `DBToken.GetDictValue`):
  - `Username` — required.
  - Optional updates include: `Firstname`, `Lastname`, `Email`, `SMSNumber`, `EmailAddressVerified`, `SMSNumberVerified`, `AccountStatus`, `ExpDate`, `BlockSeconds`, `InvalidAuthAttempts`, `MaxInvalidAuthAttempts`, `OTCLength`, `OTCFormat`, `OTCDuration`, `IsLocked`.
  - `Claims` may be provided in `apiRequest.Claims` (replaces).
- Behavior: Loads user, applies provided fields, `DBAuth.Upsert`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found.

---

### POST `api/QMFA/Admin/User/Delete`
- Purpose: Delete a user.
- InputParameters:
  - `Username` — required.
- Behavior: Deletes via `DBAuth.Delete`, returns `ExternalAuthResponse`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found.

---

### POST `api/QMFA/Admin/User/List`
- Purpose: Return a list of user names matching a search.
- InputParameters:
  - `Search` — optional, default `"%"`.
  - `SearchType` — optional, default `"StartsWith"`.
- Behavior: Calls `DBAuth.List(Search, SearchType)` and returns `List<string>` of `user.Name`.
- Success: 200 with `List<string>`.

---

### POST `api/QMFA/Admin/User/NameList`
- Purpose: Return a list of lightweight user info objects.
- InputParameters:
  - `Search` — optional, default `"%"`.
  - `SearchType` — optional, default `"StartsWith"`.
- Behavior: Calls `DBAuth.List` and maps to `UserInfo` entries (`Name`, `FirstName`, `LastName`, `Email`).
- Success: 200 with `List<UserInfo>`.

---

### POST `api/QMFA/Admin/User/Lock`
- Purpose: Lock a user account.
- InputParameters:
  - `Username` — required.
- Behavior: Sets `IsLocked = true` and persists via `DBAuth.Upsert`.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found.

---

### POST `api/QMFA/Admin/User/Unlock`
- Purpose: Unlock a user account and reset invalid attempts.
- InputParameters:
  - `Username` — required.
- Behavior: Sets `IsLocked = false`, `InvalidAuthAttempts = 0`, persists.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found.

---

### POST `api/QMFA/Admin/QRCode/Create`
- Purpose: Generate a QR code from provided data and deliver (email/SMS/claims).
- InputParameters:
  - `Username` — required.
  - `QRCodeData` — optional; if present generates QR base64.
  - QR customization KVPs: `QRPixelsPerModule`, `QRDarkColor`, `QRLightColor`, `QRLogo` (default `"QRLogo"`), `QRIconSizePercent`, `QRIconBorderWidth`, `QRDrawQuietZones`.
  - `Template` (default `"GenerateQRCode"`), `Using` (default `"SMS"`), `TemplateData`, `Subject`, `From`, `DisplayName`.
- Behavior:
  - Generates base64 QR and sets `RequestDictionary["QRCodeBase64"]`. If `Using == "claims"` places `QRCodeBase64` and `QRCodeBase64UrlEncoded` into `UserInfo.Claims`.
  - Sends via email/SMS templates when applicable.
- Success: 200 with `ExternalAuthResponse`.
- Errors: invalid username, user not found, send failure.

---

### POST `api/QMFA/Authorize/Transaction/Create`
- Purpose: Create a transient transaction and send transaction ID to recipient(s).
- InputParameters:
  - `ExpirationSeconds` — optional, default `"600"` (10 minutes).
  - Delivery KVPs used by `SendTransactionID`: `Template` (default `"TransactionIDSend"`), `Subject`, `From`, `DisplayName`, `SMSNumber`, `EmailAddress`, `TemplateData`.
- Behavior:
  - Inserts `MongoTransaction` with `Claims` and GUID `Id`, sets expiration, persists.
  - Calls `SendTransactionID` which sends via SMS/Email using `Request.InputParameters`.
- Success: 200 with `MongoTransactionResponse` (Id set to `"Sent_To_Recipient"` to avoid leaking).
- Errors: send failure.

---

### POST `api/QMFA/Authorize/Transaction/Redeem`
- Purpose: Redeem/complete a transaction (mark as redeemed).
- InputParameters:
  - `TransactionToken` — required.
  - `RedemptionStatus` — required (string, converted to boolean).
  - `RedemptionReason` — required.
- Behavior:
  - Validates existence, expiration and previous redemption.
  - Sets `trans.Redemption` with `Date`, `Redeemed`, `Reason`, `Status` and upserts transaction.
- Success: 200 with `MongoTransactionResponse`.
- Errors: missing parameters, token not found, expired, already redeemed.

---

### POST `api/QMFA/Authorize/Transaction/Read`
- Purpose: Read transaction details by token.
- InputParameters:
  - `TransactionToken` — required.
- Behavior:
  - Loads transaction and returns `TransactionResponse`.
- Success: 200 with `MongoTransactionResponse`.
- Errors: missing token, token not found.

---
