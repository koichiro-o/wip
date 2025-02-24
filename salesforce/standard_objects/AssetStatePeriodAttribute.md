#### AssetStatePeriodAttribute

Represents a virtual object that holds the key-value pair of the asset attribute in a specified asset state period. This object is a child object
of AssetStatePeriod. This object is available in API version 60.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is available in Enterprise, Unlimited, and Developer Editions of Revenue Cloud.


-----

##### Fields

**Field**
```
AssetStatePeriodId
AttributeDefinitionId
AttributeName
AttributePicklistValueId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The asset state period that's associated with the asset attribute.

This field is a relationship field.

**Relationship Name**
AssetStatePeriod

**Relationship Type**
Master-detail

**Refers To**
AssetStatePeriod (the master object)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The attribute definition that's associated with the asset state period attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup

**Refers To**
AttributeDefinition

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the asset attribute.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
AttributeValue
