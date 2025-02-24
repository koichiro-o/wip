#### QuoteAdjustmentGroup

Group containing a set of adjustments applied to a quote. This object is available in API version 58.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management.


-----

##### Fields

**Field**
```
AdjustmentSource
AdjustmentType
AdjustmentValue

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the origin of the price adjustment.

Possible values are:

**•** `Discretionary—The adjustment is entered manually; for example, by a sales rep.`

**•** `Promotion—The adjustment is part of a promotion; for example, a holiday sale`
discount.

**•** `Rule—The adjustment is due to a price rule.`

**•** `System—The adjustment originates from the system, for example, a volume discount.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of mathematical adjustment to be applied to the quote.

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
The specified AdjustmentType amount that is applied to the quote. For example, when
`AdjustmentType` is `AdjustmentAmount,` `AdjustmentValue` is the cash
amount of the price adjustment. When `AdjustmentType` value is
`AdjustmentPercentage,` `AdjustmentValue` is the percent value of the price
adjustment. When AdjustmentType is OverrideAmount, AdjustmentValue
overrides the total amount of the quote.


-----

```
Description
Name
Priority
QuoteId
TotalAmount

```

**Type**
textarea

**Properties**
Nillable

**Description**
User-entered information about the quote adjustment group.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The user-defined name of the quote adjustment group.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A numeric value that represents the order of precedence of the quote adjustment group. It
can also represent the order of precedence when applying the AdjustmentType values.

For example, a quote can have two adjustments: a $100 discount and a 10% discount. This
field indicates which adjustment to apply first.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the quote related to the adjustments in this group.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
currency


-----

**Properties**
Filter, Sort

**Description**
The total of all quote adjustments in this quote adjustment group, excluding tax.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteAdjustmentGroupChangeEvent on page 67**
Change events are available for the object.

**QuoteAdjustmentGroupFeed on page 54**
Feed tracking is available for the object.

**QuoteAdjustmentGroupHistory on page 62**
History is available for tracked fields of the object.

**QuoteAdjustmentGroupOwnerSharingRule on page 64**
Sharing rules are available for the object.

**QuoteAdjustmentGroupShare on page 66**
Sharing is available for the object.
