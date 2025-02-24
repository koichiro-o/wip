#### OrderAdjustmentGroup

Group containing a set of adjustments applied to an order. This object is available in API version 48.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

##### Fields

```
AdjustmentBasisReferenceId
AdjustmentCauseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

This field can only refer to Coupon when B2B Commerce is enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This field is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier, Promotion


-----

```
AdjustmentSource
AdjustmentType
AdjustmentValue

```

This field is available in API version 52.0 and later.

This field can only refer to Promotion when B2B Commerce is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the origin of the adjustment.

Possible values are:

**•** `Discretionary—The adjustment originates from a decision made by an individual,`
for example, a manager’s discount granted to a client.

**•** `Promotion—The adjustment originates from a promotion, for example, a holiday`
sale discount.

**•** `Rule—Reserved for future use.`

**•** `System—The adjustment originates from the system, for example, a volume discount`
after the amount of items reaches a specific number.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the type of mathematical adjustment to be applied to the order.

Possible values are:

**•** `AdjustmentAmount—The adjustment is a numerical amount, for example, a cash`
discount of 20.

**•** `AdjustmentPercentage—The adjustment is a percentage amount, for example,`
a 10% discount.

**•** `OverrideAmount—The adjustment is a manual price override.`

This field is available in API version 57.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The specified `AdjustmentType’s amount to be applied to the order.`


-----

```
CurrencyIsoCode
Description
GrandTotalAmount
Name
OrderId

```

For example, when the `AdjustmentType` value is `AdjustmentAmount, the`
`AdjustmentValue` is expected to equal the value of the `TotalAmount` field.

When the `AdjustmentType` value is `AdjustmentPercentage, the`
`AdjustmentValue represents the percentage number, and the TotalAmount` field’s
value will show the calculated adjustment amount.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency used for the checkout session. Default value is `USD.`

Possible values are:

**•** `USD—U.S. Dollar`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
User-entered information about the order adjustment group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all total amounts of all adjustments in this group, including tax.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the order adjustment group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Priority
RelatedAdjustmentGroupId
TotalAmount

```

**Description**
The unique identifier of the order related to the adjustments in this order adjustment group.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A numeric value that represents the order of precedence of the order adjustment group.

It can also represent the order of precedence when applying the `AdjustmentType`
values. For example, an order can have two adjustments: a $100 discount and a 10% discount.
This field will tell the pricing engine which adjustment needs to be applied first.

This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the original order’s adjustment group. This field is a useful reference
in change order scenarios.

This field is a relationship field.

**Relationship Name**
RelatedAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
OrderAdjustmentGroup

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalTaxAmount
Type

##### Associated Objects

```

**Description**
The total of all order adjustments in this order adjustment group, excluding tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total tax for all order adjustments in this order adjustment group.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the adjustment was applied to the order.

Possible values are:

**•** `Header: — The adjustment was applied to the order’s balance, and then distributed`
among the order products in the adjustment group.

**•** `SplitLine— The adjustment was applied to order product balances for the order`
products in the adjustment group.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderAdjustmentGroupChangeEvent on page 67**
Change events are available for the object.

**OrderAdjustmentGroupFeed on page 54**
Feed tracking is available for the object.

**OrderAdjustmentGroupHistory on page 62**
History is available for tracked fields of the object.

**OrderAdjustmentGroupOwnerSharingRule on page 64**
Sharing rules are available for the object.

**OrderAdjustmentGroupShare on page 66**
Sharing is available for the object.


-----
