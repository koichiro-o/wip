#### MobileSecurityPolicy

Enables mobile security policies on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version 50.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

##### Fields

```
DeveloperName
EffectiveDate
IsEnabled
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date a mobile security policy is enforced.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A value indicating whether a mobile security policy is enabled.

The default value is 'false'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The two-to five-character code that represents the language and locale ISO.


-----

```
MasterLabel
MobilePlatform
MobileSecurityAssignmentId
NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the mobile security policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The mobile operating system.

Possible values are:

**•** `Android`

**•** `iOS`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the ID of the mobile security assignment.

This is a relationship field.

**Relationship Name**
MobileSecurityAssignment

**Relationship Type**
Lookup

**Refers To**
MobileSecurityAssignment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.


-----

```
RuleValue
RuleValueType
SeverityLevel
Type

```


**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the mobile security policy rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of mobile security policy rule.

Possible values are:

**•** `Boolean`

**•** `Text`

**•** `TextList`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The severity level of a mobile security policy.

Possible values are:

**•** `Critical`

**•** `Error`

**•** `Info`

**•** `Warn`

**Type**
picklist


-----

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of mobile security policy.

Possible values are:

**•** `AllowedDeviceList—Allowed Device List`

**•** `Block3dTouch—Block 3D Touch`

**•** `BlockCalendar—Block Calendar`

**•** `BlockCamera—Block Camera`

**•** `BlockContacts—Block Contacts`

**•** `BlockCustomKeyboard—Block Custom Keyboard`

**•** `BlockFileBackup—Block File Backup`

**•** `BlockMicrophone—Block Microphone`

**•** `BlockOsSharing—Block OS Share Actions`

**•** `BlockedDeviceList—Blocked Device List`

**•** `BrowserUriScheme—Mobile Browser URI Scheme`

**•** `CheckBiometric—Check Biometric Login Data`

**•** `DevicePasscode—Require Device Passcode`

**•** `DisableUrlCaching—Disable URL Caching`

**•** `JailbrokenDevice—Block Jailbroken Device`

**•** `LogCertPin—Log Certificate Pinning`

**•** `LogEmail—Log Email`

**•** `LogPhonecall—Log Phone Call`

**•** `LogPolicyResult—Log Security Policy Evaluation Result`

**•** `LogScreenshot—Log Screenshot`

**•** `LogTextmessage—Log SMS`

**•** `LogoutAfterRestart—Log Out User After Device Restart`

**•** `LogoutOnBiometricChange—Log Out User After Changing Biometric Login`
Data

**•** `MalwareDetection—Malware Detection`

**•** `ManInMiddle—Block Man In The Middle Attack`

**•** `MaxOffline—Maximum Days Offline Without Policy Refresh`

**•** `MaximumAppVersion—Maximum Application Version`

**•** `MaximumOsVersion—Maximum OS Version`

**•** `MinimumAppVersion—Minimum Application Version`

**•** `MinimumOsVersion—Minimum OS Version`

**•** `MinimumSecurityPatchVersion—Minimum Security Patch Version`

**•** `PhonecallUriScheme—Phone Call Application Handler`


-----

**•** `Screenshot—Block Screenshot`
