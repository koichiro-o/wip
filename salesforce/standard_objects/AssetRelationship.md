#### AssetRelationship

Represents a non-hierarchical relationship between assets due to an asset modification; for example, a replacement, upgrade, or other
circumstance. In Subscription Management and Revenue Lifecycle Management, this object represents an asset or assets grouped in a
bundle or set. This object is available in API version 41.0 and later.

Asset relationships appear in the Primary Assets and Related Assets related lists on asset records in the UI.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Some fields are available only in Subscription Management and Revenue Cloud. Field availability is noted in the field detail column.

##### Fields

```
AssetId
AssetRelationshipNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the new asset, which is the asset that is taking the place
of the existing asset.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
string


-----

```
AssetRole
CurrencyIsoCode
FromDate
GroupingKey

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the asset relationship.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the main asset relative to the other assets in the
relationship.

This field is available in API version 58.0 and later. This field is available in orgs
with Subscription Management or Revenue Cloud.

Possible values are:

**•** `Add-on—The main asset is an add-on.`

**•** `Bundle—The main asset is the bundle parent.`

**•** `Set—The asset is the main asset in the set.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the asset. The default value
is USD.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the new asset was installed.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
ProductRelationshipTypeId
ProductRelatedComponent
RelatedAssetId

```

**Description**
Read-only field used to indicate the bundle that an asset belongs to. For example,
if two assets have the same GroupingKey value, then it means that the assets are
bundled together.

This field is available in API v.60.0 and later. This field is available in orgs with
Subscription Management or Revenue Cloud.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the record that describes the relationship between the
main and associated assets.

This field is available in API version 58.0 and later. This field is available in orgs
with Subscription Management.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product related component that’s associated with the asset relationship.

This field is a relationship field.

This field is available in API 60.0 and later in Revenue Cloud.

**Relationship Name**
ProductRelatedComponent

**Relationship Type**
Lookup

**Refers To**
ProductRelatedComponent

**Type**
reference


-----

```
RelatedAssetPricing
RelatedAssetQtyScaleMethod
RelatedAssetRole

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The existing asset that is being modified.

This field is a relationship field.

**Relationship Name**
RelatedAsset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the price of the related asset is included in the bundle price.
Valid values are:

**•** `IncludedInBundlePrice`

**•** `NotIncludedInBundlePrice`

This field is available in API version 59.0 and later in Revenue Cloud.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies how the quantity of the related asset changes relative to the quantity
of the parent asset. Valid values are:

**•** `Constant`

**•** `Proportional`

This field is available in API version 59.0 and later in Revenue Cloud.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
RelationshipType
ToDate

```

**Description**
Describes the position of the associated asset relative to other assets in the
relationship.

This field is available in API version 58.0 and later. This field is available in orgs
with Subscription Management or Revenue Cloud.

Valid values are:

**•** `Add-on—The main asset is an add-on.`

**•** `Bundle—The main asset is the bundle parent.`

**•** `Set—The asset is the main asset in the set.`

**•** `Simple—The asset is purchased individually and isn’t associated with`
variations.

**•** `Variation Parent——The main asset is the variation parent.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of relationship between the existing asset and the new asset. This field
comes with three values—Replacement, Upgrade, and Crossgrade—, but you
can create more values in Setup.

Possible values are:

**•** `Crossgrade—The new asset is a crossgrade of an existing asset. For`
example, changing a subscription to a plan with the same service, but that
runs for a longer amount of time.

**•** `Replacement—The new asset is replacing an existing asset. For example,`
a customer’s faulty widget that was under warranty is being replaced with
a new one.

**•** `Upgrade—The new asset is an upgrade of an existing asset. For example,`
upgrading a customer’s existing subscription plan to a new plan with more
services.

The default value is `Replacement.`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the modified asset is uninstalled.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetRelationshipChangeEvent (Available in API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AssetRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AssetRelationshipOwnerSharingRule (Available in API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**
Sharing rules are available for the object.

**[AssetRelationshipShare (Available in API version 58.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**
Sharing is available for the object.
