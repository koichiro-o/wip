#### CartDeliveryGroupMethodAdj

Represents the shipping promotion discount for a shipping method. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The CartDeliveryGroupMethodAdj object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustmentAmount

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update


-----

```
AdjustmentBasisReferenceId
AdjustmentType
AdjustmentValue
CartDeliveryGroupMethodId

```

**Description**
Amount subtracted from the price by the shipping promotion discount.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the adjustment basis reference. This is the coupon that causes the adjustment. This
field is a relationship field.

This field is available in API version 62.0 and later.

**Relationship Name**
AdjustmentBasisReference

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of shipping promotion discount.

Possible values are:

**•** `AdjustmentAmount`

**•** `AdjustmentPercentage`

**•** `OverrideAmount`

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Number representing the value of the price adjustment. For example, if the
`AdjustmentType` is `AdjustmentPercentage, a -10` `AdjustmentValue`
means 10 percent off. If the `AdjustmentType` is `AdjustmentAmount, a -10`
`AdjustmentValue` means 10 dollars off.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
CurrencyIsoCode
Name
PriceAdjustmentCauseId

```

**Description**
ID of the cart delivery group method.

This field is a relationship field.

**Relationship Name**
CartDeliveryGroupMethod

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroupMethod

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the cart delivery group method adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the price adjustment cause.

This field is a relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion


-----

```
Priority
