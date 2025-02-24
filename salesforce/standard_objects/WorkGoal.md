#### WorkGoal

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of resources allocated or needed at specific time period. It represents the
updated count after the adjustment. This value is the same as `OriginalTotalCount`
if no adjustments were made.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The foreign key to WorkDemographic object.

This is a relationship field.

**Relationship Name**
WorkDemographic

**Relationship Type**
Lookup

**Refers To**
WorkDemographic

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The foreign key to WorkCapacity object.

This is a relationship field.

**Relationship Name**
WorkforceCapacity

**Relationship Type**
Lookup

**Refers To**
WorkforceCapacity


Represents the components of a goal, such as its description and associated metrics. This object has been deprecated as of API version
35.0. Use the Goal object to query information about WDC goals.


-----

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Related

```
WorkGoalCollaborator, WorkGoalLink, WorkGoalFeed

##### Fields

```
ActualValue
ActualValueExternalUrl
CompletionDate
Description

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual value of the WorkGoal metric. Applicable only to WorkGoal objects of
```
  Type: Metric.

```
**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains a URL that references WDC data synchronization for the actual value of
a metric. Applicable only to WorkGoal objects of Type: Metric.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the goal.

Note: Field-level security limits access to only administrators and owners
by default, and only they can complete a goal.

**Type**
textarea (max length 4000)


-----

```
DueDate
FlaggedAs
ImageUrl
InitialValue

```

**Properties**
Create, Nillable, Update

**Description**
The description of the goal.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the WorkGoal object is due (optional). Applicable only to WorkGoal
objects of Type: Metric.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The progress of the WorkGoal object. Applicable only to WorkGoal objects of
```
  Type: Metric.

```
Possible values:

**•** On Track: Progress on the metric is on track.

**•** Behind: Progress on the metric is behind schedule.

**•** Postponed: The metric is postponed.

**•** Critical: Progress on the metric is critical.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the goal image. The image must be stored in Documents and set as
externally available. Applicable only to WorkGoal objects of `Type: Goal.`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The initial value of the WorkGoal metric. Applicable only to WorkGoal objects of
```
  Type: Metric and MetricType: Progress or Percent.

```

-----

```
IsKeyCompanyGoal
LastReferencedDate
LastSyncDate
LastViewedDate
MetricType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Used to indicate if the goal is a key company goal. Used for the Company Goal
Showcase. Applicable only to WorkGoal objects of Type: Goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this goal.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time stamp that indicates when the actual value was last synced with the
associated metrics report.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this goal.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of metric that is represented. (See values in the following list). Applies
only to WorkGoal objects of `Type: Metric.`

Possible values:

**•** Progress: ActualValue / TargetValue as a percentage

**•** Percent: the metric as a percentage only


-----

```
MetricTypeDataSource
Name
OverallStatus
OwnerId
ParentId

```


**•** YesNo: the completed / not completed metric as a milestone

**•** Absolute: Deprecated

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies how the metric (ActualValue and CurrentValue) is updated. Applies only
to WorkGoal objects of `Type: Goal and Metric.`

Possible values:

**•** Manual: indicates that the actual and target value of the metric is updated
manually by the user

**•** Rollup: indicates that the actual and target value of a goal is rolled up
automatically by WDC Goals

**•** DataSyncActualOnly: indicates that the actual value of the metric is linked to
a Salesforce report

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkGoal object. (Maximum length is 255.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The overall calculated status of the WorkGoal based on `FlaggedAs and`
```
  CompletionDate.

```
**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the WorkGoal.

**Type**
reference


-----

```
Progress
RootId
State
TargetValue

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the structural parent of the WorkGoal. For example, a goal that has a
metric is represented by a WorkGoal of Type Metric, which has a parent of
WorkGoal of Type Goal.

Note: The root and the parent must be set to the parent goal for any
child metrics.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read Only. The overall progress of the WorkGoal.

**Type**
reference to a WorkGoal object

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the structural root of the WorkGoal. For example, a goal that has a metric
is represented by a WorkGoal of `Type` Metric, which has a root of WorkGoal of
`Type` Goal.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the WorkGoal object. Applies only to WorkGoal objects of Type:
Metric.

Possible values:

**•** Draft: the draft state for the WorkGoal

**•** Published: published state for the WorkGoal

**•** Archived: archived state for the WorkGoal (for example, goals that no longer
apply)

**Type**
double


-----

```
Type
Weight

##### Associated Objects

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The target value of the WorkGoal. Applies only to WorkGoal objects of Type:
Metric.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the WorkGoal object, used to differentiate between the components
of a goal. (This field is used to represent components of a goal such as its
description and associated metrics.)

Possible values:

**•** Goal: a goal

**•** Metric: a metric (typically associated with goals)

**•** Objective: an objective

**•** KeyResult: a key result (typically associated with objectives

**•** V2Mom: a V2MOM (pilot feature)

**•** Vision: a vision (pilot feature — typically associated with V2MOM)

**•** Value: a value (pilot feature - typically associated with V2MOM)

**•** Method: a method (pilot feature - typically associated with V2MOM)

**•** Obstacle: an obstacle (pilot feature - typically associated with V2MOM)

**•** Measure: a measure (pilot feature - typically associated with a method)

Note: Administrators can rename goals and metrics to objectives and
key results, respectively. If this preference is enabled, use the Type
Objective or KeyResult. Otherwise, use the default Type Goal or KeyResult.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The weight of the goal or metric. The sum of the weights should equal 100%.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**WorkGoalFeed (API verison 35.0)**
Feed tracking is available for the object.

**WorkGoalHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkGoalOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkGoalShare**

Sharing is available for the object.
