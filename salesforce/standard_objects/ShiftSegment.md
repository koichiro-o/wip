#### ShiftSegment

Represents a scheduled activity within a shift. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license and Workforce Engagement must be enabled. The user requires the Workforce
Engagement Planner or Workforce Engagement Admin permission set.


-----

##### Fields

**Field**
```
EndTime
IsInAdherence
Name
SegmentTypeId
ShiftId

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the agent is in adherence (true) or not (false) for the scheduled
segment activity.

The default value is `true.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the shift segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the associated shift segment type.

This is a relationship field.

**Relationship Name**
SegmentType

**Relationship Type**
Lookup

**Refers To**
ShiftSegmentType

**Type**
reference


-----

```
StartTime
