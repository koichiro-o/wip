#### SchedulingAdherenceDetail

Represents the breakdown of daily shift adherence data by agent status. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The org requires a Workforce Engagement license, and both Workforce Engagement and Omni-Channel must be enabled. The user
requires the Workforce Engagement Planner or Workforce Engagement Admin permission set.


-----

##### Fields

**Field**
```
IsShrinkage
Name
SchedulingAdherenceSummaryId
StatusId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the linked status is considered as shrinkage time (true) or not (false).
Shrinkage time is time, such as breaks, when an agent doesn’t receive work.

The default value is `false.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A number that identifies this detail record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Scheduling Adherence Summary.

This is a relationship field.

**Relationship Name**
SchedulingAdherenceSummary

**Relationship Type**
Lookup

**Refers To**
SchedulingAdherenceSummary

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the agent status represented by this detail record.

This is a relationship field.

**Relationship Name**
Status


-----

```
StatusName
TotalStatusMinutes

```

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the agent status represented by this detail record.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present with this status.

