#### AttributeDefinition

Represents a product, asset, or object attribute, for example, a hardward specification or software detail. This object is available in API
version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
DataType
DefaultValue
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The data type of the attribute definition.

Possible values are:

**•** `Checkbox`

**•** `Date`

**•** `Datetime`

**•** `Number`

**•** `Picklist`

**•** `Text`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default value for this attribute.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
DeveloperName
IsActive
IsRequired
Label
LastReferencedDate

```

**Description**
Description of this attribute.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the attribute definition record.

This name must begin with a letter and use only alphanumeric characters and underscores.
It can't include spaces, end with an underscore, or have two consecutive underscores.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the attribute definition is active. Active attributes definitions can be selected
for assets.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the attribute definition is required for an asset.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the attribute.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId
PicklistId

```

**Description**
The date the attribute definition was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute definition was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the attribute.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the attribute definition.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the attribute picklist with the valid values for this attribute.

This field is a relationship field.

**Relationship Name**
Picklist


-----

```
SourceSystemIdentifier
UnitOfMeasureId

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
AttributePicklist

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the attribute definition in an external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the measurement unit for this attribute.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure


Add asset descriptors to the AssetDefinition object instead of creating multiple custom attributes on an asset. This helps scale to a high
volume of various assets in the system. When you create the AttributeDefinition, you must provide a unique API name. If the API name
is not unique, the system appends a number to the end of the API name. The value of this number depends on how many times the
same name has been used.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AttributeDefinitionHistory on page 62**
History is available for tracked fields of the object.

**AttributeDefinitionOwnerSharingRule on page 64**
Sharing rules are available for the object.


-----

**AttributeDefinitionShare on page 66**
Sharing is available for the object.

SEE ALSO:

AssetAttribute

AttributePicklist

AttributePicklistValue

RecordsetFltrCritMonitor
