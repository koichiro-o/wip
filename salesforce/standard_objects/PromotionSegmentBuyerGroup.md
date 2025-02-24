#### PromotionSegmentBuyerGroup

Represents a promotion segment, associated with a buyer group, and used for B2B Commerce. This object is available in API version
52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The PromotionSegmentBuyerGroup object is available only if the B2B Commerce license is enabled.

##### Fields

```
BuyerGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Buyer Group that you want to include in your market segment.

This is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup


-----

```
CurrencyIsoCode
LastReferencedDate
LastViewedDate
Name
PromotionSegmentId

```

**Refers To**
BuyerGroup

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

This field is available in API version 53.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

This field is available in API version 53.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion segment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion segment you want to associate with your buyer group.


-----

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup

**Refers To**
PromotionSegment

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentBuyerGroupFeed on page 54**
Feed tracking is available for the object.

**PromotionSegmentBuyerGroupHistory on page 62**
History is available for tracked fields of the object.

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier
