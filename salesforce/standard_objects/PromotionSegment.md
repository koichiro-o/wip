#### PromotionSegment

Represents a promotion segment, which you can assign to different stores or buyer groups, allowing them to access the promotion.
This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The PromotionSegment object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
CurrencyIsoCode
LastReferencedDate

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


-----

```
LastViewedDate
Name
OwnerId

##### Associated Objects

```

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the promotion segment.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created this promotion segment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionSegmentFeed on page 54**
Feed tracking is available for the object.


-----

**PromotionSegmentHistory on page 62**
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
