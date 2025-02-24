#### SOSSessionActivity

Captures information about specific events that occur during an SOS video call, such as when an SOS call begins or ends. This object is
available in API version 34.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ActivityTime
Name
SessionId
Type

```

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the activity occurred.

**Type**
string

**Properties**
Autonumber, Defaulted on create, idLookup, Filter, Sort

**Description**
The name of the activity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the SOS session that’s associated with the event.

**Type**
picklist


-----

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of activity that occurred.

##### Usage

Use this object to query and manage SOS session activities.
