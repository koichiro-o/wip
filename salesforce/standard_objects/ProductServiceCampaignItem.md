#### ProductServiceCampaignItem

Represents a product service campaign's asset. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
AssetId

```

**Type**
reference


-----

```
LastReferencedDate
LastViewedDate
Product2Id
ProductServiceCampaignId
ProductServiceCampaignItemNumber

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the product service campaign. Must be present if Product2Id
is not present.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last modified. Its UI label is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the asset was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Product2 associated with this campaign. The UI label is Product. Must be present
if `AssetID` is not present.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The item’s parent product service campaign record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the product service campaign item.


-----

```
Status
StatusCategory

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the product service campaign item. The picklist includes the following values,
which can be customized:

**•** `New—Product service campaign item created, but there hasn’t yet been any activity.`

**•** `In Progress—Product service campaign item has begun.`

**•** `On Hold—Product service campaign item is paused.`

**•** `Completed—Product service campaign item is complete.`

**•** `Cannot Complete—Product service campaign item couldn’t be completed.`

**•** `Closed—All product service campaign item and associated activity is complete.`

**•** `Canceled—Product service campaign item is canceled, typically before any work`
began.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `StatusCategory` field has eight
default values: seven values that are identical to the default `Status` values, and `None`
for statuses without a status category.

If you create custom `Status` values, you must indicate which category it belongs to. For
example, if you create a `Waiting for Response` value, add it to the `On Hold`
category. To learn which processes reference `StatusCategory, see How are Status`
[Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductServiceCampaignItemFeed**

Feed tracking is available for the object.

**ProductServiceCampaignItemHistory**

History is available for tracked fields of the object.

**ProductServiceCampaignItemOwnerSharingRule**

Sharing rules are available for the object.

**ProductServiceCampaignItemShare**

Sharing is available for the object.


-----
