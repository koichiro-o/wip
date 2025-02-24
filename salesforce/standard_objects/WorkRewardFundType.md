#### WorkRewardFundType

Represents the type of WorkRewardFund object.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CreditSystem
CurrencyCode
IsActive
IsPredefined
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The credit system that is used by the WorkRewardFundType object (gift codes
or points). If points are selected, the reward message will not consider the
`CurrencyCode` field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency code of the WorkRewardFundType

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the WorkRewardFundType is active and available in the UI

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the WorkRewardFundType is predefined (true) or not (false)

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId
RedemptionDisclaimer
RedemptionInfo

```

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkRewardFundType.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkRewardFundType. If this value is null, this record might have been only
referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkRewardFundType

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the WorkRewardFundType owner

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The redemption disclaimer text for the WorkRewardFundType

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Redemption text for the WorkRewardFundType


-----

```
RedemptionUrl
UploadCodeColumn
UploadValueColumn

##### Associated Objects

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The URL that’s linked to the redemption

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The column where the reward code is contained in the CSV file. The upload uses
the second value by default.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The column where the reward value is contained in the CSV file. The upload uses
the third column by default.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkRewardFundTypeFeed**

Feed tracking is available for the object.

**WorkRewardFundTypeHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkRewardFundTypeShare**

Sharing is available for the object.


-----
