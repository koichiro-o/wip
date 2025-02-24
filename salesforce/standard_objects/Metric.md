#### Metric

The Metric object represents the components of a goal metric such as its name, metric type, and current value.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
CompletionDate
CurrentValue
Description
DueDate
GoalId
InitialValue

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the metric.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The current value of the metric.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the metric. The maximum length is 65,535 characters.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The due date of the metric.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the goal the metric is related to.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update


-----

```
IsCompletionMetric
LastComment
LastReferencedDate
LastViewedDate
Name

```

**Description**
The initial value of the metric.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. If `true, the metric measures whether or not the metric is finished.`
If `false, the metric measures how much is finished compared to a targeted`
value.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A comment that provides more context about the metric, such as its status or
progress. The maximum length is 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed a record that is related to
this metric.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed this metric. If this value is
null, this record might have been only referenced (LastReferencedDate)
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
OwnerId
Progress
RecordTypeId
StartDate
Status

```

**Description**
The name of the metric.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the metric.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The overall progress of the metric.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the related record type.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the metric.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the metric. Possible values include:

**•** Not Started

**•** On Track

**•** Behind

**•** Critical


-----

```
TargetValue
Weight

##### Associated Objects

```


**•** Completed

**•** Postponed

**•** Canceled

**•** Not Completed

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The target value of the metric.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The weight of the metric. The sum of the weights should equal 100%.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MetricFeed**

Feed tracking is available for the object.

**MetricHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**MetricOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**MetricShare**

Sharing is available for the object.
