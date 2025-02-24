#### PriceAdjustmentItemShape

Defines the business logic for an item-level price adjustment, for example, a discount on an order item. This object is available in API
version 57.0 and later.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

##### Fields

```
AdjustmentAmountScope

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
AdjustmentSource
AdjustmentType

```

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total—The adjustment applies to the line item's total and isn’t multiplied by the`
quantity.

For example, let's say a sales transaction item quantity is 10 and the
`TotalLineAmount` is 1000. If the price adjustment item has an
`AdjustmentValue` of -10, an AdjustmentType of AdjustmentAmount,
and an `AdjustmentAmountScope` of Total, the $10 discount is applied to the
total line amount. The TotalAmount of the price adjustment item is $1000 + (-$10)
= $990.

**•** `Unit—The adjustment is multiplied by the line item’s quantity.`

For example, let's say a sales transaction item quantity is 5 and the
`TotalLineAmount` is 1000. If the price adjustment item has an
`AdjustmentValue` of -10, an AdjustmentType of AdjustmentAmount,
and an `AdjustmentAmountScope` of Unit, the $10 discount is applied to each
line amount. The TotalAmount of the price adjustment item is $1000 + (-$10 x 5) = $950.

**•** `UnproratedTotal—No adjustment is applied to the line items.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the source of the adjustment.

Possible values are:

**•** `Discretionary— The adjustment is entered manually; for example, by a sales rep.`

**•** `Promotion— The adjustment is a promotion.`

**•** `Rule— Reserved for future use.`

**•** `System— The adjustment is determined by the pricing configuration for the product;`
for example, as part of a discount schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the adjustment is a percentage, an amount, or an override.

Possible values are:

**•** `AdjustmentAmount—The adjustment value is a numerical amount.`


-----

```
AdjustmentValue
Description
PriceAdjustmentCauseId
PriceAdjustmentGroupShapeId

```


**•** `AdjustmentPercentage— The adjustment value is a percentage.`

**•** `OverrideAmount— The override value is a numerical amount.`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The value of the adjustment. Used together with AdjustmentAmountScope to
determine the amount of the adjustment.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The user-entered description of the price adjustment item. Available in API version 57.0.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that caused the adjustment. For example, if the price adjustment is due
to a promotion, this field contains the ID of the Promotion record. If the price adjustment is
due to a price adjustment tier, this field contains the ID of the PriceAdjustmentTier
record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
PriceAdjustmentItemShapeName
Priority
SalesTransactionItemShapeId

```

**Description**
A reference to the object interface or object that summarizes the values from multiple price
adjustment items. If the related entity is an object, the object must implement the
```
  PriceAdjustmentGroupShape object.

```
This field is a relationship field.

**Relationship Name**
PriceAdjustmentGroupShape

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentGroupShape

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the price adjustment item shape.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A positive integer indicating the order in which this price adjustment item is applied, relative
to other price adjustment items. A `Priority of` `1` indicates this price adjustment item
is applied first.

Price adjustments with a null priority are applied after price adjustments with a specified
priority. If two or more price adjustments have a null priority, percentage adjustments are
applied before amount adjustments. Applying a percentage adjustment before an amount
adjustment results in a larger total adjustment.

Note: The value of Priority must be unique among price adjustment items
related to the same price adjustment group. For example, you can’t have two price
adjustment items with a priority of 1.

For example, let’s say that two price adjustment items apply to the same item to be priced.
The first price adjustment, Spring_Promotion, defines a 10% discount and has Priority
of 1. The second price adjustment, Early_Renewal_Discount, defines a $2,000 discount and
has a `Priority` of 2. In this case, the Spring_Promotion price adjustment is applied
before the Early_Renewal_Discount price adjustment.

**Type**
reference


-----

```
TotalAmount

```

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the sales transaction shape item that the price adjustment item applies to.

This field is a relationship field.

**Relationship Name**
SalesTransactionItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total amount of the adjustment that applies to the item to be priced, inclusive of quantity,
prorated for the duration of the subscription.

For example, let’s say the price adjustment item has an AdjustmentAmountScope of
`Unit, an AdjustmentType` of AdjustmentAmount, and an AdjustmentValue
of -10. This configuration indicates a $10 per-unit discount. If the subscription is priced for
12 months and the pricing term is `1, the PricingTermCount` on the sales transaction
item is 12. If the quantity is 5, the value of `TotalAmount` is 5 x 12 x -10 = -600

