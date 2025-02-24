#### JobProfileQueueGroup

JobProfileQueueGroup defines the mapping between Queue and JobProfile and configurations for capacity plans in Workforce Engagement.
This object is available in API version 53.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
Org must have the Workforce Engagement, Workforce Engagement Configuration, and Omni org preferences enabled. User must have
the Workforce Engagement Analyst or Planner user permission set.

##### Fields

```
AnswerTime
CapacityPerJobProfile
GroupCapacity
GroupId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The answer time (in seconds) for a specific group.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The max number of work units that an agent can handle for a specific job profile.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distributed number of work units among groups to which a specific job profile is
associated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Identifies the group or queue record.

This is a relationship field.


-----

```
JobProfileId
JobProfileShrinkage
Priority
ServiceLevelAgreementPerc

```

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Identifies the job profile record.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The shrinkage for a specific job profile.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority of a group per job profile.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The expected SLA percentage for a specific group.


-----

```
WorkType
