#### MobSecurityCertPinEvent

The event of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available in
API version 53.0 and later.

##### Supported Calls
```
create(), describeSObjects()

 Special Access Rules

```
Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

##### Fields

```
AppPackageIdentifier
AppVersion
CertPinResults
DeviceIdentifier

```

**Type**
string

**Properties**
Create

**Description**
The unique identifier for the certificate.

**Type**
string

**Properties**
Create

**Description**
The version of the app.

**Type**
json

**Properties**
Create

**Description**
The results of certificate pinning.

**Type**
string

**Properties**
Create


-----

```
DeviceModel
EventDate
EventDescription
EventIdentifier
EventUuid
OsName

```

**Description**
The hardware IDs or IDs to uniquely identify a mobile device.

**Type**
string

**Properties**
Create

**Description**
The model of the mobile device.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date of the certificate pinning event.

**Type**
string

**Properties**
Create, Nillable

**Description**
The description of the certificate pinning event.

**Type**
string

**Properties**
Create, Nillable

**Description**
The ID of the certificate pinning event.

**Type**
string

**Properties**
Nillable

**Description**
The universally unique identifier of the event.

**Type**
string

**Properties**
Create


-----

```
OsVersion
ReplayId
UserId
WebkitVersion

```

**Description**
The name of the operating system.

**Type**
string

**Properties**
Create

**Description**
The version of the operating system.

**Type**
string

**Properties**
Nillable

**Description**
The position of the event in the event stream.

**Type**
reference

**Properties**
Create

**Description**
This is polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Nillable

**Description**
The version of the web browser engine developed by Apple.

