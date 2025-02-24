#### PromotionTarget

Represents the product, product category, or order that you want to target with your promotion in a B2B Store or D2C store. This object
is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The PromotionTarget object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustmentAmount
AdjustmentPercent
AdjustmentType

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The promotion discount is expressed as an amount, not as a percentage.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage discount of the promotion. Valid values include numbers from 1 through
100.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of adjustment discount applied to the product or group of products.

Possible values are:

**•** `FixedAmountOffLineItemTotal—Fixed amount off the total of all line`
items.


-----

```
CurrencyIsoCode
ExternalTarget
IsMinItemCountRequired
LastReferencedDate

```


**•** `FixedAmountOffTransaction—Fixed amount off the entire transaction.`
This value is available in API version 56.0 and later.

**•** `FixedAmountOffUnitPrice—Fixed amount off the unit price.`

**•** `FixedPrice—Fixed price for a product. This value is available in API version`
56.0 and later.

**•** `TotalFixedPrice—Fixed price for a set number of products. Requires a`
quantity limit. This value is available in API version 56.0 and later.

**•** `FixedAmountOffUnitPrice—Fixed amount off the unit price.`

**•** `PercentageDiscount—Percentage discount.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code
for any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A target product or product category stored outside of Salesforce. This field is available
in API version 56.0 and later.

Note: This field is available through the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, the max value in the` `RestrictionQuantity field must be met before`
the promotion is applied. The default value is false. This field is available in API version
56.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
PromotionId
PromotionTierId

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the promotion target.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to reference.

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
The ID of the promotion tier associated with the target. Only used with tiered promotions.

This is a relationship field.

This field is available in API version 57.0 and later.


-----

```
RestrictionQuantity
TargetId
TargetOperator

```

**Relationship Name**
PromotionTier

**Relationship Type**
Lookup

**Refers To**
PromotionTier

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum number of times the discount can be applied to the target. This field is
available in API version 56.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product or product category that you want to target.

This is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

**Type**
enum

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
For product and category targets, specify if the qualifying product or item in the
qualifying category must be in the cart to determine if the cart satisfies the promotions
criteria. For example, a quantity or amount across one or more items. This field is available
in API version 59.0 and later.

Possible values are:

**•** `EQUAL_TO—Specifies that the qualifying product or item in the qualifying category`
must be in the cart.


-----

```
TargetProductCategoryName
TargetProductName
TargetProductSku
TargetRuleCriteriaType
TargetType

```


**•** `NOT_EQUAL_TO—Specifies that the qualifying product or item in the qualifying`
category isn’t required to be in the cart.

**•** `NONE—Specifies that none of the other possible values apply. If the target type is`
for an order, you must use none.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product category referenced in the target. This field is available in API
version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product referenced in the target. This field is available in API version
55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit of the product referenced in the target. This field is available in
API version 55.0 and later.

**Type**
enum

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls what promotion rules must be met for the promotion to be valid. This field is
available in API version 59.0 and later.

Possible values are:

**•** `ALL—Specifies that all of the promotion rules must be met.`

**•** `ANY—Specifies that any of the promotion rules can be met.`

**Type**
picklist


-----

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The target of the promotion.

Possible values are:

**•** `Product—Applies the promotion to a single product.`

**•** `ProductCategory—Applies the promotion to a group of products.`

**•** `Shipping—Applies the promotion to all shipping methods on the order.`

**•** `StandardShippingRate—Applies the promotion to a single shipping method`
on the order.

**•** `Transaction—Applies the promotion to the entire order.`

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier
