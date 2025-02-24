#### CartTax

Represents taxes for a line item in a WebCart that’s active in a store built with B2B Commerce or D2C Commerce. This object is available
in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

The CartTax object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustmentTargetType
Amount
CartId
CartItemId
CartItemPriceAdjustmentId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Target for the price adjustment (the cart itself or individual items). This field is available in
API version 52.0 and later.

Possible values are:

**•** `Cart`

**•** `Item`

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Calculated tax amount.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the `WebCart` being taxed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a cart item being taxed.

**Type**
reference


-----

```
CurrencyIsoCode
Description
Name
TaxCalculationDate
TaxRate

```

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a price adjustment for a cart item being taxed. (This field is available in API version
52.0 and later.)

**Refers To**
CartItemPriceAdjustment

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`
Valid values include:

**•** `USD—U.S. Dollar`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the tax. Enter up to 2000 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartTax` record. `Name` can be up to 255 characters.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date this tax was calculated.

**Type**
percent


-----

```
TaxType

##### Associated Objects

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The applied tax rate for this line of tax.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of tax for this line of tax. Possible values are:

**•** `Actual`

**•** `Estimated`


This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartTaxChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

WebCart
