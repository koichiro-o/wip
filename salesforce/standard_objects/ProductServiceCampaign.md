#### ProductServiceCampaign

Represents a set of activities to be performed on a product service campaign asset, such as a product recall for safety issues or product
defects. This object is available in API version 51.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
Description
EndDate
LastReferencedDate
LastViewedDate
OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the product service campaign.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which the product service campaign ends.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. The UI label is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
reference


-----

```
Priority
Product2Id
ProductServiceCampaignName
StartDate

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The product service campaign’s owner. By default, the product service campaign owner is
the user who created the product service campaign record. The UI label is Product Service
Campaign Owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the product service campaign.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Medium`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Product2 associated with this campaign. The UI label is Product.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the product service campaign.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date on which the product service campaign starts.


-----

```
Status
StatusCategory
Type

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the product service campaign. The picklist includes the following values, which
can be customized:

**•** `New—Product service campaign created, but there hasn’t yet been any activity.`

**•** `In Progress—Product service campaign has begun.`

**•** `On Hold—Work is paused.`

**•** `Completed—Work is complete.`

**•** `Cannot Complete—Work couldn’t be completed.`

**•** `Closed—All work and associated activity is complete.`

**•** `Canceled—Work is canceled, typically before any work began.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `StatusCategory` field has eight
default values: seven values that are identical to the default `Status` values, and `None`
for statuses without a status category.

If you create custom `Status` values, you must indicate which category it belongs to. For
example, if you create a Waiting for Response value, add it the On Hold category.
To learn which processes reference `StatusCategory, see How are Status Categories`
[Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of the product service campaign. The picklist includes the following values, which
can be customized:

**•** `Modification—The asset requires an on-site alteration.`

**•** `Recall—The asset must be returned to the manufacturer for modification or upgrade.`

**•** `Service—The asset needs to be serviced.`

**•** `Upgrade—The asset needs updating.`


-----

```
WorkTypeId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the product service campaign. A customer uses this field as
a guide when setting work type for work orders for the product service campaign.
```
  Duration, Duration Type, and required skills.

```

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductServiceCampaignFeed**

Feed tracking is available for the object.

**ProductServiceCampaignHistory**

History is available for tracked fields of the object.

**ProductServiceCampaignOwnerSharingRule**

Sharing rules are available for the object.

**ProductServiceCampaignShare**

Sharing is available for the object.
