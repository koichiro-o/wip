#### PromotionMarketSegment

Represents a market segment within B2B Commerce that promotions can be assigned to. This object is available in API version 52.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The PromotionMarketSegment object is available only if the B2B Commerce license is enabled.

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

**Description**
The timestamp for when the current user last viewed a record related to this record.


-----

```
LastViewedDate
Name
PromotionId
PromotionSegmentId

```

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
The ID of the promotion that you want to associate with your promotion segment.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion segment that you want to associate with.

This is a relationship field.

**Relationship Name**
PromotionSegment

**Relationship Type**
Lookup


-----

**Refers To**
PromotionSegment

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier
