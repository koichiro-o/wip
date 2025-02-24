#### SchedulingConstraint

Represents scheduling constraints on each service resource. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
The org requires the Workforce Engagement license. To view records, the user requires the Workforce Engagement Agent permission
set. To create, edit, or delete records, the user requires the Workforce Engagement Planner permission set.

##### Fields

```
LastReferencedDate
LastViewedDate
MaxNonstandardShiftsPerMonth
MaxShiftsPerDay

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the scheduling constraint was last modified. Its label in the user interface is
Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the scheduling constraint was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of non-standard shifts assigned to an agent in a month.

This field is available in API version 54.0 and later.

**Type**
int


-----

```
MaxShiftsPerMonth
MaxShiftsPerWeek
MaxWorkingHoursPerDay
MaxWorkingHoursPerMonth
MaxWorkingHoursPerWeek
Name

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a day.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of shifts an agent can have in a week.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a day.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a month.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of hours an agent can have in a week.

**Type**
string


-----

```
OwnerId
RestTimeMinutes

##### Associated Objects

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling constraint record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the scheduling constraint.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum rest time, in minutes, between an agent’s consecutive shifts.

This field is available in API versions 56.0 and later.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SchedulingConstraintOwnerSharingRule on page 64**
Sharing rules are available for the object.

**SchedulingConstraintShare on page 66**
Sharing is available for the object.
