#### WebCartAdjustmentGroup

Group of price adjustments for a cart. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The WebCartAdjustmentGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustmentSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Price adjustment type.

Possible values are:

**•** `Discretionary`

**•** `Promotion`


-----

```
AdjustmentTargetType
AdjustmentType
AdjustmentValue
CartId

```


**•** `System`

**Type**
picklist

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
Create, Filter, Group, Sort

**Description**
ID of the cart to which the price adjustment belongs.

This is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup


-----

```
CurrencyIsoCode
Description
Name
PriceAdjustmentCauseId

```

**Refers To**
WebCart

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
Description of the adjustment group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the adjustment group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

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


-----

```
Priority
TaxAmount
TotalAmount
TotalAmountWithTax

##### Associated Objects

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple price adjustments, sequence in which the price adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tax on the total adjusted price.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total price after adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total adjusted price plus tax.


This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**WebCartAdjustmentGroupChangeEvent (API version 58.0)**
Change events are available for the object.
