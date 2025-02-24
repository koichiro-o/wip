#### WorkReward

Used to store reward codes tied to a Reward Fund. Reward Funds must have at least one WorkReward record.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
You must have the Reward permission enabled in order to use the Rewards feature, including WorkRewardFund and WorkReward.

##### Additional Considerations and Related Objects

WorkReward is a lookup to WorkRewardFund. WorkRewardFund must have at least one WorkReward record to be available for use. Each
WorkBadge record with a `RewardId` indicates a reward badge given to a Recipient.


-----

##### Fields

**Field Name**
```
Code
OwnerId
RecipientId
RedemptionDisclaimer
RedemptionInfo
RedemptionUrl

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents a singe reward code tied to a RewardFundId.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents the User ID of Owner of WorkReward record

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce User ID for User associated with this WorkReward record.

**Type**
textarea

**Properties**
Nillable

**Description**
The disclaimer information about the WorkReward.

**Type**
textarea

**Properties**
Nillable

**Description**
The instructions for redeeming the WorkReward.

**Type**
textarea

**Properties**
Nillable


-----

```
RewardFundId
RewardFundTypeId
Value

##### Associated Objects

```

**Description**
The URL for redeeming the WorkReward.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID for WorkRewardFund record that is associated with
WorkReward record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID of the WorkRewardFundType associated with the
WorkReward.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value of the WorkReward.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardShare**

Sharing is available for the object.


-----
