#### StandardShippingRate

Standard shipping rate for a store. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The StandardShippingRate object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
ConditionFactor
ConditionRangeMax
ConditionRangeMin
CurrencyIsoCode
Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Conditions that affect the shipping rate.

Possible values are:

**•** `OrderPriceFactor—Condition based on the order price value.`

**•** `OrderWeightFactor—Condition based on delivery weight. This value is available`
in API version 62.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum value of the shipping rate condition.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Minimum value of the shipping rate condition. This value can't be negative.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string


-----

```
Price
ShippingCarrierMethodId
ShippingZoneId

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the standard shipping rate.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Price of standard shipping.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shipping service carrier method. This field is available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
ShippingCarrierMethod

**Relationship Type**
Lookup

**Refers To**
ShippingCarrierMethod

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping zone.

This field is a relationship field.

**Relationship Name**
ShippingZone

**Relationship Type**
Parent-detail

**Refers To**
ShippingRateArea (the master object)


-----

```
TransitTimeMax
TransitTimeMin
TransitTimeUnit
WeightUnit

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum value of the shipping transit time. This field is available in API version 61.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum value of the shipping transit time. This value can't be negative. This field is available
in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of value for shipping transit time. This field is available in API version 61.0 and later.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of measurement for the weight of the cart items. This field is available in API version
62.0 and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`


-----
