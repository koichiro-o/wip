#### UserServicePresence

Represents a presence user’s real-time presence status. This object is available in API version 32.0 and later.

##### Supported Calls
```
delete(), query(), getDeleted(), getUpdated(), retrieve(), undelete()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

##### Fields

```
AtCapacityDuration

```

**Type**
int


-----

```
AverageCapacity
ConfiguredCapacity
ConfiguredInterruptCapacity
IdleDuration
IsAway

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration that the user is at full capacity. This field is updated when the agent’s capacity
changes, such as when the agent is assigned, declines, or closes a work item. Available in
API versions 34.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The user’s average capacity. This field is updated when the agent’s capacity changes, such
as when the agent is assigned, declines, or closes a work item. Available in API versions 34.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s total configured primary capacity.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s total configured interruptible capacity. Available in version 57.0 and later when
the Interruptible Capacity feature is enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration that the user is idle. This field is updated when the agent’s capacity changes,
such as when the agent is assigned, declines, or closes a work item. Available in API versions
34.0 and later.

**Type**
boolean


-----

```
IsCurrentState
Name
OwnerId
ServicePresenceStatusId
StatusDuration

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user’s status is `Away.`

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a presence status is the user’s current state. If `true, the agent is in that`
presence status. Available in API versions 34.0 and later.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the UserServicePresence entity. For external routing, allows
the entity to be used in the Streaming API to listen to events whenever a
`UserServicePresence` record is created, modified, or deleted.

**Type**
reference

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The ID of the presence status that’s associated with the presence user that’s specified by the
```
  UserId.

```
**Type**
int


-----

```
StatusEndDate
StatusStartDate
UserId

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration of the user service presence status. This field is set only when the current user
service presence status ends, such as when the agent changes to another presence status
or logs out. Available in API versions 34.0 and later.

This field is a calculated field: StatusEndDate - StatusStartDate.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date of the user service presence status. This field is set only when the current user
service presence status ends, such as when the agent changes to another presence status
or logs out. Available in API versions 34.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date of the user service presence status. Available in API versions 34.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Omni-Channel user.


Apex triggers aren’t supported with `UserServicePresence.`

In API version 41.0 or later, UserServicePresence records can be deleted programmatically. The Customize Application permission
is required.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**UserServicePresenceChangeEvent (API version 62.0)**
Change events are available for the object.

**UserServicePresenceOwnerSharingRule**

Sharing rules are available for the object.

**UserServicePresenceShare**

Sharing is available for the object.
