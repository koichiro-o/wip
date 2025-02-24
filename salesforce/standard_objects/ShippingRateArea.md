#### ShippingRateArea

```

The default value is `1 Day.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time to process an order.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the target record.

This field is a relationship field.

**Relationship Name**
TargetRecord

**Relationship Type**
Lookup

**Refers To**
WebStore


A designated geographical area that’s available for shipping. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The ShippingRateArea object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
Countries
Name
Regions
ShippingRateGroupId
