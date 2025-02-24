#### WorkRewardFund

Represents a Reward Fund and describes the Reward Fund attributes.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
To use the Rewards feature, including WorkRewardFund and WorkReward, you must have the Reward permission enabled. To create
Rewards, the user must have Create on WorkRewardFund, which is not a standard permission.

##### Additional Considerations and Related Objects

WorkReward is a lookup to WorkRewardFund. WorkRewardFund must have at least one WorkReward record available. Each
WorkBadgeDefinition with a RewardFundId is a “Reward Badge.”

##### Fields

```
IsActive
LastReferencedDate
LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the WorkRewardFund is active (true) or not (false).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkRewardFund.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
RewardFundTypeId
TotalCodeCount
Type

```

**Description**
The time stamp that indicates when the current user last viewed this
WorkRewardFund. If this value is null, this record might have been only referenced
(LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the Reward Fund.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of User who is the Owner of the WorkRewardFund record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of the WorkRewardFundType that is associated with the
WorkRewardFund.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total reward codes that are available in the WorkRewardFund. Derived from
WorkReward records that are associated with the WorkRewardFund.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
RewardType of the WorkRewardFund. Default is Amazon.com.


-----

```
UsedCodeCount
Value

##### Associated Objects

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total reward codes that are used in the WorkRewardFund. Derived from the total
assigned WorkReward records that are associated with the WorkRewardFund.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Value of each of the reward codes in the WorkRewardFund.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardFundFeed**

Feed tracking is available for the object.

**WorkRewardFundHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundShare**

Sharing is available for the object.
