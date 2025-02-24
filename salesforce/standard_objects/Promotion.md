#### Promotion

Represents a promotion for B2B or D2C stores. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Some of the fields on the Promotion object are available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AreQualItemsExclFromDiscounts

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Exclude qualifying items from discount. You can use this field to create buy-one-get-one
promotions. The default value is false. This field is available in API version 56.0 and later.


-----

```
CurrencyIsoCode
Description
DiscountOrder
DiscountRestriction

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the promotion.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether to apply discounts first to the least expensive products or to the most
expensive products.

Possible values are:

**•** `LeastExpensive`

**•** `MostExpensive`

The default value is `MostExpensive.`

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether to restrict the products that can be discounted based on the least expensive
qualifying product.

Possible values are:

**•** `LeastExpensive`

**•** `None`

The default value is `None.`

This field is available in API version 56.0 and later.


-----

```
DisplayName
EndDateTime
ExclusivityType
IsActive
IsAutomatic

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Display name of the promotion.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when the promotion ends.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether a promotion can be combined with other promotions.

Possible values are:

**•** `No`  - Can be combined with other promotions.

**•** `Class`  - Can’t be combined with a promotion of the same class (product, order, or
shipment), but allows for promotions of separate classes to be combined. For example,
an order discount on top of a product discount.

**•** `Global`  - Only promotion that can be applied to the order, regardless of class.

The default value is `Class.`

This field is available in API version 58.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the promotion is active (true) or inactive (false).

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
IsCommercePromotion
IsTiered
LastReferencedDate
LastViewedDate

```

**Description**
Determines whether the promotion is automatic or manual. If the promotion is automatic,
it automatically applies to eligible carts with no buyer action required. if the promotion is
manual, the buyer applies a coupon to redeem the promotion.

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the promotion is a B2B Commerce promotion (true) or not (false).

The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the promotion uses promotion tiers (true) or not (false). This value can’t
be changed.

The default value is false.

A tiered promotion can have up to 10 associated tiers.

This field is available in API version 57.0 and later.

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
possible that this record was referenced and not directly accessed.


-----

```
MaximumUsageCount
Name
Objective
OwnerId
PriorityNumber

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum number of times the promotion can be applied to a cart. If left blank, the default
value is 1. This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the promotion.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
More information, if any, about the purpose of the promotion.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the promotion.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
QualifierCriteria
StartDateTime
TargetCriteria
TermsAndConditions

```

**Description**
Priority for the promotion. The priority determines which promotions apply first. The lower
the number, the higher the priority.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If a promotion has multiple qualifiers, this field determines whether all qualifiers must be
met or whether any must be met for the promotion to apply.

Possible values are:

**•** `All`

**•** `Any`

The default value is 'All'.

This field is available in API version 53.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when the promotion begins.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If a promotion has multiple targets, indicates whether a cart must meet the criteria for any
target or the criteria for all targets.

Possible values are:

**•** `All`

**•** `Any`

This field is available in API version 56.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

**Description**
Terms and conditions the buyer accepts before applying the promotion.

This field is available in API version 53.0 and later.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionFeed on page 54**
Feed tracking is available for the object.

**PromotionHistory on page 62**
History is available for tracked fields of the object.

**PromotionShare on page 66**
Sharing is available for the object.

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier
