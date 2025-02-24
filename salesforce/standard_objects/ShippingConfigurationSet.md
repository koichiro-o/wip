#### ShippingConfigurationSet

Shipping configuration for a set of products in a store. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Special Access Rules

The ShippingConfigurationSet object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
IsDefault
Name
OwnerId
ProcessTime

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shipping configuration is the default `(True)` or not `(False).`

The default value is `False.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping configuration set.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the shipping configuration owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time to process an order before it is ready to ship.


-----

```
ProcessTimeUnit
TargetRecordId
