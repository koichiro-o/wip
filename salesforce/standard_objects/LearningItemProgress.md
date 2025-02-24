#### LearningItemProgress

Represents the progress that a user has made towards completing an assigned learning item, such as a Learning Paths entry or Enablement
program. This object is available in API version 60.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=sf.prm_support_license_template.htm&language=en_US)


-----

##### Fields

**Field**
```
CompletedDate
CompletedOnDay
CompletedPercent
DaysInProgress
LearningItemId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the user completed the learning item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days that the user took to complete the learning item.

**Type**
percent

**Properties**
Filter, Sort

**Description**
Percentage of the learning item that’s complete.

**Type**
int

**Properties**
Nillable

**Description**
Number of days that have elapsed since the learning item was assigned.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the learning item. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup


-----

```
OwnerId
ProgressStatus

##### Associated Objects

```

**Refers To**
LearningItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the learning item. This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the learning item assignment. Possible values are:

**•** `Behind`

**•** `Completed`

**•** `CompletedLate`

**•** `CompletedOnTime`

**•** `InProgress`

**•** `NoLongerTracking`

**•** `NotStarted`

**•** `OnTrack`

**•** `Overdue`

[For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sf.enablement_analytics_completion_statuses.htm&language=en_US)


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemProgressChangeEvent on page 67**
Change events are available for the object.


-----

**LearningItemProgressOwnerSharingRule on page 64**
Sharing rules are available for the object.

**LearningItemProgressShare on page 66**
Sharing is available for the object.
