#### PicklistValueInfo

Represents the active picklist values for a given picklist field. This object is available in API version 40.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
DurableId
EntityParticleId
IsActive
IsDefaultValue

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the picklist field to which this value is related.

**Relationship Name**
EntityParticle

**Relationship Type**
Lookup

**Refers To**
EntityParticle

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the picklist value is active or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this value is the default for the picklist field. Only one value can be the
default value.


-----

```
Label
ValidFor
Value
