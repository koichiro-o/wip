#### PromotionSegmentSalesStore

Represents a promotion segment, associated with a store, and used for B2B Commerce. This object is available in API version 52.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The PromotionSegmentSalesStore object is available only if the B2B Commerce license is enabled.


-----

##### Fields

**Field**
```
CurrencyIsoCode
LastReferencedDate
LastViewedDate
Name
PromotionSegmentId

```

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

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

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
The ID of the promotion segment you want to associate with your store.

This is a relationship field.

**Relationship Name**
PromotionSegment


-----

```
SalesStoreId

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
PromotionSegment

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store you want to include in your promotion segment.

This is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentSalesStoreFeed on page 54**
Feed tracking is available for the object.

**PromotionSegmentSalesStoreHistory on page 62**
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


-----
