#### SchedulingAdherenceSummary

Represents daily shift adherence data for a service resource in a service territory and job profile on a specific date. This object is available
in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The org requires a Workforce Engagement license, and both Workforce Engagement and Omni-Channel must be enabled. The user
requires the Workforce Engagement Planner or Workforce Engagement Admin permission set.

##### Fields

```
AdherencePercentage

```

**Type**
double


-----

```
ConformancePercentage
Date
JobProfileId

```

**Properties**
Filter, Sort

**Description**
Percentage of time that the agent was present during the scheduled shift time.

This is a calculated field.

**Formula**
```
  AdherencePercentage =
  TotalAdherenceMinutes / TotalScheduledMinutes

```
**Type**
double

**Properties**
Filter, Sort

**Description**
Percentage of time when the agent was present versus the duration of scheduled shifts. The
time that the agent is present can extend beyond the scheduled shift.

This is a calculated field.

**Formula**
```
  ConformancePercentage =
  TotalPresenceMinutes / TotalScheduledMinutes

```
**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date for which the adherence data is calculated.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the job profile.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup


-----

```
JobProfileName
Name
OwnerId
ServiceResourceId

```

**Refers To**
JobProfile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the job profile.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A number that identifies this summary record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the schedule adherence summary.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service resource.

This is a relationship field.

**Relationship Name**
ServiceResource


-----

```
ServiceResourceName
ServiceTerritoryId
ServiceTerritoryName
TotalAdherenceMinutes

```

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the service resource.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the service territory.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present during a shift.


-----

```
TotalInteractionMinutes
TotalPresenceMinutes
TotalScheduledMinutes
TotalShrinkageMinutes

##### Associated Objects

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was actively receiving work.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total minutes of agent presence time.

This is a calculated field.

**Formula**
```
  TotalPresenceMinutes =
  TotalInteractionMinutes + TotalShrinkageMinutes

```
**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Total minutes of scheduled shift time for the agent.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Total minutes that the agent was present but not receiving work, such as break times.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SchedulingAdherenceSummaryOwnerSharingRule on page 64**
Sharing rules are available for the object.

**SchedulingAdherenceSummaryShare on page 66**
Sharing is available for the object.


-----
