#### ShippingRateGroup

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Countries in the shipping rate area.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate area.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Reserved for future use.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping rate group

This field is a relationship field.

**Relationship Name**
ShippingRateGroup

**Relationship Type**
Lookup

**Refers To**
ShippingRateGroup


Available shipping rates based on shipping destination. This object is available in API version 59.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The ShippingRateGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
Name
ShippingProfileId
