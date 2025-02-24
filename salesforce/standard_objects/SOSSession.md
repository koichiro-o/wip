#### SOSSession

This object is automatically created for each SOS session and stores information about the session. This object is available in API versions
34.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AppVersion
CaseId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of the customer’s mobile application in which SOS is implemented.

**Type**
reference


-----

```
ContactId
DeploymentId
EndTime
IpAddress
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the SOS deployment that the SOS session originated from.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session ended.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
To protect the customer’s privacy, this field is now blank.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last referenced by a user.

**Type**
dateTime


-----

```
Name
OpentokSession
OwnerId
SessionDuration
SessionRecordingUrl
SosVersion

```

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the session.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
The ID of the OpenTok session that’s associated with the SOS video call.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the session record’s owner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time that the SOS session lasted.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL where the SOS session recording is stored.

**Type**
string


-----

```
StartTime
SystemInfo
WaitDuration

##### Usage

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of SOS that was used in your organization’s mobile application when
this session occurred.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session began.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information about the customer’s mobile device from which the SOS call
originated, such as the device’s operating system.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time the customer waited before an agent accepted the SOS
session and the call began.


Use this object to query and manage SOS session records.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SOSSessionFeed**

Feed tracking is available for the object.

**SOSSessionHistory**

History is available for tracked fields of the object.


-----

**SOSSessionOwnerSharingRule**

Sharing rules are available for the object.

**SOSSessionShare**

Sharing is available for the object.
