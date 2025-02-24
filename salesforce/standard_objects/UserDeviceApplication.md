#### UserDeviceApplication

```

**Description**
The activity status of the device. The picklist options are:

**•** Approved

**•** Pending Approval

**•** Revoked

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the user’s last access.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
An identifier for the user’s device such as the International Mobile Equipment
Identity (IMEI) number or the device serial number.

Note: This field isn’t automatically populated. The developer must provide
values.


Represents information on applications installed on a device that is accessing Salesforce. Available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

You must have View Devices enabled to see devices.

##### Fields

```
ApplicationType
Name
Status
UserDeviceId
UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application used to log in to Salesforce.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
This field is system-generated and cannot be changed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The activity status of the device application. The picklist options are:

**•** Approved

**•** Pending Approval

**•** Revoked

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events.
`UserDeviceId` is a generated value that’s created when the mobile app is
initially run after installation.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
The ID of the user.
