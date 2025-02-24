#### OrderItemAdjustmentLineItem

An adjustment that has been made to an order item. This object is available in API version 48.0 and later.

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
AdjustmentAmountScope
AdjustmentBasisReferenceId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total—The adjustment scope is the total price.`

**•** `Unit—The adjustment scope is the unit price.`

**•** `UnproratedTotal—The adjustment scope is the unprorated total price.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.


-----

```
AdjustmentCauseId
AdjustmentSource

```

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

This field is available in API version 52.0 and later.

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


-----

```
AdjustmentType
AdjustmentValue
Amount
CurrencyIsoCode

```

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
The specified `AdjustmentType’s amount to be applied to the order item.`

For example, when the AdjustmentType value is `AdjustmentAmount, the`
`AdjustmentValue` is expected to equal the value of the `Amount field.`

When the `AdjustmentType` value is AdjustmentPercentage, the
`AdjustmentValue` represents the percentage number, and the `Amount field’s value`
will show the calculated adjustment amount.

This field is available in API version 57.0 and later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The net total value of the adjustment line. The value is rounded to the nearest possible
amount associated with the currency of the order item.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
Description
Name
OrderAdjustmentGroupId
OrderId
OrderItemId

```

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization. Default value is `USD.`

Possible values are:

**•** `USD—U.S. Dollar`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can add a custom description to the record to provide additional detail.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the adjustment line.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order adjustment group that contains the order item adjustment line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent order of the order item related to the adjustment line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order item that the adjustment line applies to.


-----

```
Priority
RelatedAdjustmentLineItemId
TotalAmtWithTax
TotalTaxAmount

```

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
The original order item adjustment line. Useful for reference in change order scenarios.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Equals the order item’s price plus TotalTaxAmount for the order item adjustment line
item.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order Management
license. Commerce Orders fields are available only in Lightning Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the adjustment line.


-----
