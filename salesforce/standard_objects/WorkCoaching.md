#### WorkCoaching

Represents a single coaching relationship between two users. One of the users is defined as the coach and the other is defined as a
coachee. WorkCoaching is feed-enabled so there is a private feed available to the coach and coachee.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CoachId
CoachedId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

[Required] The coach in this 1:1 coaching relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
IsInactive
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Description**

[Required] The user being coached in this 1:1 coaching relationship.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the coaching relationship is `Inactive` (true) or not
(false).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this coaching relationship.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this coaching
relationship. If this value is null, this record might have been only referenced
(LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

[Required] The record’s name. Max length is 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the WorkCoaching record.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkCoachingFeed**

Feed tracking is available for the object.

**WorkCoachingHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkCoachingOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkCoachingShare**

Sharing is available for the object.
