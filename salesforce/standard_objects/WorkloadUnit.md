#### WorkloadUnit

Represents the number of work items and average handle time in a specific time interval. This object is available in API version 49.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The org must have a Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
Engagement Analyst permission set.

##### Fields

```
AverageHandleTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average handle time at a specific period of time.


-----

```
Channel
CustomWorkType
DateTime
IsOmni
MeasureUnit

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The channel value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field of WorkDemographic.CustomWorkType for the custom dimension value.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The timestamp of the single data point in the time series of the workload.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived from isOmni field in workload. Indicates that the workload is Omni-based

The default value is 'false'.

**Type**
string

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time interval (in minutes) used in the workload.

Possible values are:

**•** `43200—Monthly. Reserved for future use.`

**•** `10080—Weekly`

**•** `1440—Daily`

**•** `60—Hourly`


-----

```
Region
SkillSet
TotalCount
WorkDemographicId
WorkloadId

```


**•** `30—30 minutes. Reserved for future use.`

**•** `15—15 minutes. Reserved for future use.`

The default value is '1440'.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from WorkDemographic.Region for the region value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The derived field from WorkDemographic.SkillSet for the skill value.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The total number work items at a specific period of time.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The foreign key to the WorkDemographic object.

This is a relationship field.

**Relationship Name**
WorkDemographic

**Relationship Type**
Lookup

**Refers To**
WorkDemographic

**Type**
reference


-----

```
WorkloadType
