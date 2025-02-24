#### UserDevice

Represents information unique to a device. Available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

You must have View Devices enabled to see devices.

##### Fields

```
BrowserType
DeviceNativeUid
DeviceType
IsVerified

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser used for login.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A unique string used to identify a mobile device.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The device used to log in to Salesforce. The picklist options are:

**•** `Desktop`

**•** `Tablet`

**•** `iPad`

**•** `iPhone`

**•** `Phone`

**•** `Unknown`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


-----

```
LastLoginHistoryId
Name
PlatformType
PlatformVersion
Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most recent LoginHistory associated with the device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
This field is system-generated and can’t be changed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The operating system of the device. The picklist options are:

**•** iOS

**•** Android

**•** OSX

**•** Linux

**•** Phone

**•** Windows

**•** AppleApp

**•** Blackberry

**•** Other

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the operating system running on the device.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
UserId
UserLastSeen
UserProvidedDeviceIdentifier
