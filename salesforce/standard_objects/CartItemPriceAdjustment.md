#### CartItemPriceAdjustment

Price adjustment for a cart item. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The CartItemPriceAdjustment object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
AdjustmentAmountScope
AdjustmentBasisReferenceId
AdjustmentSource
AdjustmentTargetType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Scope of the adjustment amount for a promotion.

Possible values are:

**•** `Total—The amount off the total price.`

This field is available in API version 54.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon code of the coupon associated with a promotion. This field is available in API version
54.0 and later.

This is a relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Price adjustment type.

Possible values are:

**•** `Discretionary`

**•** `Promotion`

**•** `System`

**Type**
picklist


-----

```
AdjustmentType
AdjustmentValue
CartId

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target for the price adjustment (the cart itself or individual items).

Possible values are:

**•** `Cart`

**•** `Item`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates if the price adjustment is applied as percentage or an absolute amount.

Possible values are:

**•** `AdjustmentAmount`

**•** `AdjustmentPercentage`

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Numeric value of the adjustment (for example, 10 if the price adjustment is either 10% off
or $10 off).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the WebCart that’s associated with a cart item. This field is available in API version
55.0 and later.

This is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart


-----

```
CartItemId
CurrencyIsoCode
Description
Name
PriceAdjustmentCauseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent cart item to which this adjustment belongs.

This is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Lookup

**Refers To**
CartItem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`

Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the price adjustment.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the price adjustment.

**Type**
reference


-----

```
Priority
TotalAmount
TotalGrossAmount
TotalNetAmount

```

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
ID of entity that caused this adjustment (for example, a promotion ID). If unspecified, then
`Description` populates the display name.

This is a relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple price adjustments, sequence in which the price adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total price after applying price adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount (tax inclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalTax
WebCartAdjustmentGroupId

##### Associated Objects

```

**Description**
The total net amount (tax exclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the total adjusted price.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the cart’s adjustment group.

This is a relationship field.

**Relationship Name**
WebCartAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
WebCartAdjustmentGroup


This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemPriceAdjustmentChangeEvent (API version 58.0)**
Change events are available for the object.
