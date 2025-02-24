#### AttributePicklist

Represents a custom picklist for an asset attribute. This object is available in API version 57.0 and later.

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

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of this picklist.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Datetime`

**•** `Number`

**•** `Percent`

**•** `Text`

The default value is `Boolean.`


-----

```
Description
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the picklist. Maximum size is 32000 alphanumeric characters. Can include
the following special characters: @! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the picklist. Names must be unique.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the attribute picklist record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


-----

```
Status
UnitOfMeasureId

##### Usage

```

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the attribute picklist.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Draft.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the unit of measure associated with the product.

This field is a relationship field.

This field is available when Revenue Cloud is enabled.

This field is available in API version 63.0 and later.

**Relationship Name**
UnitOfMeasure

**Refers To**
UnitOfMeasure


The AttributePicklist object is the parent object and the AttributePicklistValue object contains the picklist values. Let’s say you need an
asset attribute to track the T-shirt size, which can be small, medium, or large. Create an AttributePicklist parent record as a Text type for
the T-shirt size attribute. Then create AttributePicklistValue records, one for each picklist value small, medium, and large, and associate
them with the parent record.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**AttributePicklistHistory on page 62**
History is available for tracked fields of the object.

**AttributePicklistOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AttributePicklistShare on page 66**
Sharing is available for the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklistValue

RecordsetFltrCritMonitor
