#### SalesTransactionShape

```
Defines the business logic for a sales transaction; for example, an order, a quote, or a cart. This object is available in API version 57.0 and
later.

This object is visible in Object Manager for customization; for example, you can create custom fields for this object.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier for the account associated with this sales transaction shape. This field
is available when OrgPermissions or Platform is enabled.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account


-----

```
SalesTransactionShapeName
TotalAdjustmentAmount
TotalAdjustmentDistAmount
TotalAmount
TotalListAmount

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the sales transaction shape. For example, Quote.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of all adjustments applied to the sales transaction shape, inclusive of quantity,
prorated for the duration of the subscription. Includes distributed price adjustment items
and price adjustment items applied directly. This calculated field is equal to the sum of
`TotalAdjustmentAmount` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the distributed price adjustment items applied to the related sales transaction
shape items, inclusive of quantity, prorated for the duration of the subscription. Does not
include price adjustment items that are applied directly. This calculated field is equal to the
sum of TotalAdjustmentDistAmount on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The final price of the sales transaction shape, after all adjustments, inclusive of quantity,
prorated for the duration of the subscription. This calculated field equal to the sum of
`TotalPrice` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


-----

```
TotalProductAmount

```

**Description**
The sum of the list price of the related sales transaction shape items, inclusive of quantity,
prorated for the duration of the subscription. This calculated field is equal to the sum of
`ListPriceTotal` on the related sales transaction shape items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total price of all related sales transaction shape items of type Product, before price
adjustments, inclusive of quantity, prorated for the duration of the subscription. This calculated
field is equal to the sum of TotalLineAmount on the related sales transaction shape
items of type Product.

