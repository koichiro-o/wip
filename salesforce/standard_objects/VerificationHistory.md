#### VerificationHistory

Represents the past six months of your org users’ attempts to verify their identity. This object is available in API version 36.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

Only users with Manage Users permission can access this object.

##### Fields

```
Activity

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The action the user attempted that requires identity verification. The label is User
Activity. Available values are:

**•** `AccessReports—The user attempted to access reports or dashboards.`

**•** `Apex—The user attempted to access a Salesforce resource with a verification`
Apex method.

**•** `ChangeEmail—The user attempted to change an email address.`

**•** `ConnectSms—The user attempted to connect a phone number.`


-----

```
EventGroup
LoginGeoId

```


**•** `ConnectToopher—The user attempted to connect Salesforce`
Authenticator.

**•** `ConnectTotp—The user attempted to connect a one-time password`
generator.

**•** `ConnectU2F—The user attempted to register a U2F security key.`

**•** `ConnectWebAuth—The user attempted to register a built-in`
authenticator.

**•** `ConnectedApp—The user attempted to access a connected app.`

**•** `EnableLL—The user attempted to enroll in Lightning Login.`

**•** `ExportPrintReports—The user attempted to export or print reports`
or dashboards.

**•** `ExternalClientApp— The user attempted to access an external client`
app.

**•** `ExtraVerification—Reserved for future use.`

**•** `ListView—The user attempted to access a list view.`

**•** `Login—The user attempted to log in.`

**•** `Registration—Reserved for future use.`

**•** `TempCode—The user attempted to generate a temporary verification code.`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
ID of the verification attempt. Verification can involve several attempts and use
different verification methods. For example, in a user’s session, a user enters an
invalid verification code (first attempt). The user then enters the correct code and
successfully verifies identity (second attempt). Both attempts are part of a single
verification and, therefore, have the same ID. The label is Verification Attempt.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a
successful or unsuccessful identity verification attempt. Due to the nature of
geolocation technology, the accuracy of geolocation fields (for example, country,
city, postal code) can vary.

This is a relationship field.

**Relationship Name**
LoginGeo


-----

```
LoginHistoryId
Policy

```

**Relationship Type**
Lookup

**Refers To**
LoginGeo

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID for the record of the user’s successful or unsuccessful login attempt.

This is a relationship field.

**Relationship Name**
LoginHistory

**Relationship Type**
Lookup

**Refers To**
LoginHistory

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The identity verification security policy or setting. The label is Triggered By.
Available values are:

**•** `CustomApex—Identity verification made by a verification Apex method.`

**•** `DeviceActivation—Identity verification required for users logging in`
from an unrecognized device or new IP address. This verification is part of
Salesforce’s risk-based authentication.

**•** `EnableLightningLogin—Identity verification required for users`
enrolling in Lightning Login. This verification is triggered when the user
attempts to enroll. Users are eligible to enroll if they have the Lightning Login
User user permission and the org has enabled Allow Lightning Login in
Session Settings.

**•** `ExtraVerification—Reserved for future use.`

**•** `HighAssurance—High assurance session required for resource access.`
This verification is triggered when the user tries to access a resource, such as
a connected app, report, or dashboard, that requires a high-assurance session
level.

**•** `LightningLogin—Identity verification required for internal users logging`
in via Lightning Login. This verification is triggered when the enrolled user


-----

```
Remarks
ResourceId

```

attempts to log in. Users are eligible to log in if they have the Lightning Login
User user permission and have successfully enrolled in Lightning Login. Also,
from Session Settings in Setup, Allow Lightning Login must be enabled.

**•** `PageAccess—Identity verification required for users attempting to`
perform an action, such as changing an email address or adding a verification
method for multi-factor authentication (MFA).

**•** `PasswordlessLogin—Identity verification required for customers`
attempting to log in to an Experience Cloud site that is set up for passwordless
login. The admin controls which registered verification methods can be used,
for example, email, SMS, Salesforce Authenticator, or TOTP.

**•** `ProfilePolicy—Session security level required at login. This verification`
is triggered by the Session security level required at login setting on the user’s
profile.

**•** `TwoFactorAuthentication—Multi-factor authentication (formerly`
called two-factor authentication) required at login. This verification is triggered
by the Multi-Factor Authentication for User Interface Logins user permission
assigned to a custom profile. Or the user permission is included in a
permission set that is assigned to a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The text the user sees on the page or in Salesforce Authenticator when prompted
to verify identity. For example, if identity verification is required for a user’s login,
the user sees “You’re trying to Log In to Salesforce.” In this case, the Remarks
value is “Log In to Salesforce.” But if the Activity value is Apex, the Remarks value
is a custom description passed by an Apex method. If the user is verifying identity
using Salesforce Authenticator, the custom description also appears in the app.
If the custom description isn’t specified, the value is the name of the Apex method.
The label is Activity Message.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the Activity value is ConnectedApp, the `ResourceId value is the ID`
of the connected app. The label is Connected App ID.

This is a relationship field.

**Relationship Name**
Resource


-----

```
SourceIp
Status

```

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The IP address of the machine from which the user attempted the action that
requires identity verification. For example, the IP address of the machine from
where the user tried to log in or access reports. If it’s a non-login action that
required verification, the IP address can be different from the address from where
the user logged in. This address can be an IPv4 or IPv6 address.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the identity verification attempt. Available values are:

**•** `AutomatedSuccess—Salesforce Authenticator approved the request`
for access because the request came from a trusted location. After users
enable location services in Salesforce Authenticator, they can designate
trusted locations. When a user trusts a location for a particular activity, such
as logging in from a recognized device, that activity is approved from the
trusted location for as long as the location is trusted.

**•** `Denied—The user denied the approval request in the authenticator app,`
such as Salesforce Authenticator.

**•** `FailedGeneralError—An error caused by something other than an`
invalid verification code, too many verification attempts, or authenticator
app connectivity.

**•** `FailedInvalidCode—The user entered an invalid verification code.`

**•** `FailedInvalidPassword—The user entered an invalid password.`

**•** `FailedPasswordLockout—The user attempted to enter a password`
too many times.

**•** `FailedTooManyAttempts—The user attempted to verify identity too`
many times. For example, the user entered an invalid verification code
repeatedly.

**•** `Initiated—Salesforce initiated identity verification but hasn’t yet`
challenged the user.


-----

```
UserId
VerificationMethod

```


**•** `InProgress—Salesforce challenged the user to verify identity and is`
waiting for the user to respond or for Salesforce Authenticator to send an
automated response.

**•** `RecoverableError—Salesforce can’t reach the authenticator app to`
verify identity, but it continues to retry.

**•** `ReportedDenied—The user denied the approval request in the`
authenticator app, such as Salesforce Authenticator, and also flagged the
approval request to report to an administrator.

**•** Succeeded—The user’s identity was verified.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user verifying identity.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The method by which the user attempted to verify identity in the verification
event. The label is Method. Available values are:

**•** `BuiltInAuthenticator—A built-in authenticator set up on the user’s`
device, such as Touch ID or Windows Hello, generated the required
credentials. This value is available in API version 53.0 and later.

**•** `Email—Salesforce sent an email with a verification code to the address`
associated with the user’s account.

**•** `EnableLL—Salesforce Authenticator sent a notification to the user’s mobile`
device to enroll in Lightning Login. This value is available in API version 38.0
and later.

**•** `LL—Salesforce Authenticator sent a notification to the user’s mobile device`
to approve login via Lightning Login. This value is available in API version
38.0 and later.


-----

```
VerificationTime

##### Usage

```


**•** `SalesforceAuthenticator—Salesforce Authenticator sent a`
notification to the user’s mobile device to verify account activity.

**•** `Sms—Salesforce sent a text message with a verification code to the user’s`
mobile device. SMS messaging requires a Salesforce add-on license for Identity
Verification Credits.

**•** `TempCode—A Salesforce admin or a user with the Manage Multi-Factor`
Authentication in User Interface permission generated a temporary verification
code for the user. This value is available in API version 37.0 and later.

**•** `Totp—An authenticator app generated a time-based, one-time password`
(TOTP) on the user’s mobile device.

**•** `U2F—A U2F security key generated required credentials for the user. This`
value is available in API version 38.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the identity verification attempt, for example,
`7/19/2025, 3:19:13 PM PDT.` The time zone is based on GMT. The
label is Time.


Here are two examples queries that you can perform on VerificationHistory.

**Query** **String**

Show verification history for a user’s login record `SELECT Activity, EventGroup, Policy,`
```
                          Remarks, Status, UserId,VerificationMethod,
                          VerificationTime FROM VerificationHistory
                          WHERE LoginHistoryId = '0YaD000#########'

```

Get detailed geographic location information for a user’s verification
attempt
