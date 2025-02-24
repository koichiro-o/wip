#### QuoteLinePriceAdjustment

Indicates the calculated price adjustment that is applied to the quote line, for example, a calculated volume discount or the prorated
value of a manual discount. Use the quote line price adjustment to inform potential customers about the type, value, and total amount
of their discounts. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management.

##### Fields

```
AdjustmentAmountScope

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total—The adjustment applies to the line item's total and isn’t multiplied by the`
quantity. The adjustment amount is prorated for the duration of the subscription.

**•** `Unit—The adjustment is multiplied by the line item’s quantity, prorated for the duration`
of the subscription.

**•** `UnproratedTotal—The adjustment applies to the line item's total and isn’t`
multiplied by the quantity. The adjustment amount isn’t prorated for the duration of the
subscription.


-----

```
AdjustmentSource
AdjustmentType
AdjustmentValue
Description

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The source of the adjustment.

Possible values are:

**•** `Discretionary—The adjustment is entered manually; for example, by a sales rep.`

**•** `Promotion—Reserved for future use.`

**•** `Rule—The adjustment results from a system rule, such as a price rule or product rule.`

**•** `System—The adjustment is determined by the pricing configuration for the product;`
for example, as part of a discount schedule.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of adjustment to apply to a quote line.

Possible values are:

**•** `AdjustmentAmount—The adjustment is a numerical amount, for example, a cash`
discount of 20.

**•** `AdjustmentPercentage—The adjustment is a percentage amount, for example,`
a 10% discount.

**•** `OverrideAmount—The adjustment is a manual price override. Available in API`
version 59.0 and later.

**Type**
double

**Properties**
Filter, Sort

**Description**
The value of the adjustment. Used together with `AdjustmentAmountScope` to
determine the amount of the adjustment.

**Type**
textarea

**Properties**
Nillable

**Description**
The system-entered description of the quote line price adjustment.


-----

```
Name
PriceAdjustmentCauseId
Priority
QuoteAdjustmentGroupId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-entered name of the quote line price adjustment.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that caused the adjustment. `Null` if `AdjustmentSource` is
```
  Discretionary, indicating a manual adjustment.

```
For example, if the price adjustment is due to a price adjustment tier, this field contains the
ID of the `PriceAdjustmentTier` record.

This field is a polymorphic relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**reference**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the quote adjustment group, which totals all price adjustments for the quote.

This field is a relationship field.

**Relationship Name**
QuoteAdjustmentGroup


-----

```
QuoteLineItemId
TotalAmount

```

**Relationship Type**
Lookup

**Refers To**
QuoteAdjustmentGroup

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the quote line item that this price adjustment applies to.

This field is a relationship field.

**Relationship Name**
QuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
currency

**Properties**
Filter, Sort

**Description**
The total amount of the adjustment that applies to the quote line item, inclusive of quantity,
prorated for the duration of the subscription.

