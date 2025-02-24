#### WorkforceCapacityUnit

Represents the number of resources allocated or needed for a specific set of work items at a timestamp within a specific duration. This
object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Special Access Rules

The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user must have the Workforce
Engagement Analyst permission set.

##### Fields

```
AssignedTotalCount
AvailableTotalCount
Capacity
DateTime
IsOmni

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The number of shifts assigned at specific time period.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total number of shifts scheduled at a specific time period.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Staffing prediction for a capacity plan. This field is available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The timestamp of the data point.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived from the isOmni field on WorkforceCapacity. Indicates that the workload is
Omni-based.


-----

```
IsShiftTemplateNonStandard
JobProfileName
MaxCount
MeasureUnit

```

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift template that’s used at a specific time period is a non-standard
shift. This field is available in API version 53.0 and later.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from the WorkDemographic SkillSet field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The max number of resources allocated or needed at a specific time period.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time interval (in minutes) used in capacity plans.

Possible values are:

**•** `43200—Monthly for long-term capacity plans. This value is available in API version`
54.0 and later.

**•** `10080—Weekly`

**•** `1440—Daily`

**•** `60—Hourly`

**•** `30—30 minutes. Reserved for future use.`

**•** `15—15 minutes. Reserved for future use.`

The default value is '1440'.


-----

```
OriginalTotalCount
ResourceGap
ServiceTerritoryName
ShiftTemplateDuration
ShiftTemplateDurationType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The original total number of resources allocated or needed at specific time period calculated
from the planning process.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the resource gap between the available and required resources.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from the WorkDemographic Region field.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The duration of the shift template that’s used at a specific time period. This field is available
in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the duration of the shift template that’s used at a specific time period is
in minutes or hours. This field is available in API version 53.0 and later.

Possible values are:

**•** `H—Hours`

**•** `M—Minutes`

The default value is `H.`


-----

```
ShiftTemplateId
ShiftTemplateJobProfile
ShiftTemplateName
ShiftTemplateStartTime
TotalCount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the shift template that’s used at a specific time period. This field is available in API
version 53.0 and later.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The job profile that relates to the shift template that’s used at a specific time period. This
field is available in API version 53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the shift template that’s used at a specific time period. This field is available in API
version 53.0 and later.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start time of the shift template that’s used at a specific time period. This field is available
in API version 53.0 and later.

**Type**
int


-----

```
WorkDemographicId
WorkforceCapacityId
