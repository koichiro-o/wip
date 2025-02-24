#### Goal

The Goal object represents the components of a goal such as its name, description, and status.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CompletionDate
Description

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the goal.

**Type**
textarea


-----

```
DueDate
ImageUrl
IsKeyCompanyGoal
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Nillable, Update

**Description**
The description of the goal. The maximum length is 65,535 characters.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the goal is due.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the goal image. The image must be stored in Documents and set as
externally available. Applicable only to Goal objects of `Type: Goal.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the goal is a key company goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed a record that is related to
this goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
Progress
StartDate
Status

```

**Description**
The timestamp that indicates when a user last viewed this goal. If this value is
null, this record might have been only referenced (LastReferencedDate)
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the goal. The maximum length is 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the goal.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The progress of the goal measured as a percentage.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the goal.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the goal.

Possible values:

**•** Draft


-----

**•** Published

**•** Completed

**•** Canceled

**•** Not Completed

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**GoalFeed**

Feed tracking is available for the object.

**GoalHistory**

History is available for tracked fields of the object.

**GoalOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**GoalShare**

Sharing is available for the object.
