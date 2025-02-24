#### ServiceCrewMember

Represents a technician service resource that belongs to a service crew.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
EndDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
IsLeader
LastReferencedDate
LastViewedDate
ServiceCrewId
ServiceCrewMemberNumber
ServiceResourceId

```

**Description**
The last day that the service resource belongs to the crew. You can use this field
to track employment dates for contractors.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the member is the crew leader.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew member was last modified. Its label in the user
interface is `Last Modified Date.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service crew member was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The crew that the service resource belongs to.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the service crew member.

**Type**
reference


-----

```
StartDate

##### Associated Objects

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource that belongs to the crew. Only service resources whose
resource type is Technician can be added to service crews.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The day the service resource joins the crew. Service resources can
belong to multiple crews as long as their start and end dates don’t overlap.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceCrewMemberChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceCrewMemberFeed**

Feed tracking is available for the object.

**ServiceCrewMemberHistory**

History is available for tracked fields of the object.
