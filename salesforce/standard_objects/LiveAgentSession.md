#### LiveAgentSession

```
This object is automatically created for each Chat session and stores information about the session. This object is available in API versions
28.0 and later.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update()

 Fields

```
```
AgentId
ChatReqAssigned
ChatReqDeclined

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the agent associated with the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that were assigned to an agent during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ChatReqEngaged
ChatReqTimedOut
LastReferencedDate
LastViewedDate
LoginTime
LogoutTime

```

**Description**
The number of chat requests that were declined by an agent during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chats in which an agent was engaged during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of chat requests that timed out in an agent’s queue during a session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time an agent logged in during the session.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


-----

```
Name
NumFlagLoweredAgent
NumFlagLoweredSupervisor
NumFlagRaised
OwnerId
TimeAtCapacity

```

**Description**
The date and time an agent logged out during a session.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookupSort

**Description**
The name of the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags lowered by the agent.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags lowered by the supervisor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of assistance flags raised by the agent.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the session record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
TimeIdle
TimeInAwayStatus
TimeInChats
TimeInOnlineStatus

##### Usage

```

**Description**
The amount of time an agent spent with the maximum number of chats in his
or her queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent idle during the session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with a status of “Away” during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent engaged in chats during a session.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time an agent spent with a status of “Online” during a session.


Use this object to query and manage chat session records.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LiveAgentSessionHistory**

History is available for tracked fields of the object.


-----

**LiveAgentSessionOwnerSharingRule**

Sharing rules are available for the object.

**LiveAgentSessionShare**

Sharing is available for the object.
