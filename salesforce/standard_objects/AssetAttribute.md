#### AssetAttribute

Stores asset attributes to track and analyze asset conditions to improve their uptime. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
AssetId
AttributeDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the attribute definition for this asset attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup


-----

```
AttributeName
AttributePicklistValueId
AttributeValue
ExternalId

```

**Refers To**
AttributeDefinition

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name given to the asset attribute in the UI by the user.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the attribute picklist value if the attribute is a picklist type.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**
AttributePicklistValue

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores the value of an asset attribute, for example 5-TB storage .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An auto-generated ID of the attribute record saved in an external system (for example an
HBase database).


-----

##### Usage

Add asset descriptors to the AssetAttribute object instead of creating multiple custom attributes on an asset. This helps scale to a high
asset volume in the system.

SEE ALSO:

AttributeDefinition

AttributePicklist

AttributePicklistValue

RecordsetFltrCritMonitor
