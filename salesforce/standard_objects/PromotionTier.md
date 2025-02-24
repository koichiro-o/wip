#### PromotionTier

Represents a tier of a promotion that includes multiple tiers. A promotion can have up to 10 tiers. This object is available in API version
57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
LastReferencedDate

```

**Type**
dateTime


-----

```
LastViewedDate
Name
PromotionId
Rank

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it can mean that the user accessed this record or list view (LastReferencedDate) but
didn’t view it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the promotion tier.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the promotion tier.

This field is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
Priority of the tier among the associated promotion’s tiers. Tiers are evaluated in order from
lowest to highest rank. Each tier in a promotion must have a unique rank.

##### Usage

Use promotion tiers with promotion qualifiers and promotion targets to create tiered promotions. Instead of associating one promotion
qualifier and one promotion target with each promotion, associate one promotion qualifier and one promotion target with each
promotion tier.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionTierFeed on page 54**
Feed tracking is available for the object.

**PromotionTierHistory on page 62**
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
