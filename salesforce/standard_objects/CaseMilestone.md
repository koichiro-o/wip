#### CaseMilestone

Represents a milestone (required step in a customer support process) on a Case. This object is available in API version 18.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve(), update()

```

-----

##### Fields

**Field**
```
BusinessHoursId
CaseId
CompletionDate
ElapsedTimeInDays
ElapsedTimeInHrs
ElapsedTimeInMins

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the BusinessHours associated with the CaseMilestone.

**Type**
reference

**Properties**
Filter

**Description**
ID of the case.

**Type**
dateTime

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone was completed.

**Type**
double

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in days.

**Type**
double

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in hours.

**Type**
int

**Properties**
Filter, Nillable


-----

```
IsCompleted
IsViolated
MilestoneTypeId
StartDate
TargetDate
TargetResponseInDays

```

**Description**
The time required to complete a milestone in minutes.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the milestone is completed (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the milestone is violated (true) or not (false).

**Type**
reference

**Properties**
Filter, Nillable

**Description**
The ID of the milestone on the case.

**Type**
dateTime

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone started on the case.

**Type**
dateTime

**Properties**
Filter

**Description**
The date and time the milestone must be completed.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
TargetResponseInHrs
TargetResponseInMins
TimeRemainingInDays
TimeRemainingInHrs
TimeRemainingInMins
TimeSinceTargetInDays

```

**Description**
The time to complete the milestone in days.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time to complete the milestone in hours.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time to complete the milestone in minutes.

**Type**
double

**Properties**
Group, Nillable, Sort

**Description**
Time remaining to reach the milestone target, measured in days.

**Type**
text

**Properties**
Nillable

**Description**
Time remaining to reach the milestone target, measured in hours.

**Type**
text

**Properties**
Group, Nillable, Sort

**Description**
Time remaining to reach the milestone target. The format is minutes and seconds.

**Type**
double

**Properties**
Nillable, Sort


-----

```
TimeSinceTargetInHrs
TimeSinceTargetInMins

##### Usage

```

**Description**
The time elapsed since the milestone target, measured in days.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The time elapsed since the milestone target, measured in hours.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The time elapsed since the milestone target. The format is minutes and seconds.


This object lets you view a milestone on a case. It also lets you view if the milestone was completed and when it must be completed.

SEE ALSO:

Case

MilestoneType

SlaProcess
