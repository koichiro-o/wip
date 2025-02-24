#### Problem

Problems represent the root cause data of one or more incidents. This object contains all the details of a problem, documenting the
history of the problem from detection to closure. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Category
Description
Impact

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The type of problem. Administrators set field values.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem. This field can store up to 32 KB of data, but only the first 255
characters appear in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The problem's impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.


-----

```
LastReferencedDate
LastViewedDate
OwnerId
ParentProblemId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view.
(LastReferencedDate) but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This is a polymorphic relationship field that represents the user or group assigned to resolve
the problem.

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
The ID of a problem above one or more related problems in a problem hierarchy.

This is a relationship field.

**Relationship Name**
ParentProblem


-----

```
Priority
PriorityOverrideReason
ProblemNumber
ResolutionDateTime
ResolutionSummary

```

**Relationship Type**
Lookup

**Refers To**
Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of the problem.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the priority should be changed or edited.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated problem number.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the problem was resolved.

**Type**
textarea


-----

```
ResolvedById
RootCauseSummary
Status

```

**Properties**
Create, Nillable, Update

**Description**
A description of the steps needed to resolve the incident.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who resolved the problem.

This is a relationship field.

**Relationship Name**
ResolvedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem resolution or root cause. This field can store up to 32 KB of data,
but only the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any custom or granular stages customers wants to track. This will be a dependent picklist.

Possible values are:

**•** `Closed`

**•** `Fix in Progress`

**•** `Known Error`

**•** `New`

**•** `Open`

**•** `Pending Change`


-----

```
StatusCode
SubCategory
Subject
Urgency

```


**•** `Resolved`

**•** `Root Cause Analysis`

**•** `Work In Progress`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the problem.

Possible values are:

**•** `Closed`

**•** `FixInProgress`

**•** `KnownError`

**•** `New`

**•** `Open`

**•** `PendingChange`

**•** `Resolved`

**•** `RootCauseAnalysis`

**•** `WorkInProgress`

The default value is 'New'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of problem. One level deeper than Category. Administrators set field values.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the problem.

**Type**
picklist


-----

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A measure of how long a resolution can be delayed until an incident, problem, or change
has a significant business impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.
