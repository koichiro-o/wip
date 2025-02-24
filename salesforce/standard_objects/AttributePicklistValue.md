#### AttributePicklistValue

Represents the values of an asset attribute picklist. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
Abbreviation
Code

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A short name of the picklist value that's displayed at run time. Use up to 255 alphanumeric
characters. Can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $
”.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
DisplayValue
IsDefault
LastReferencedDate
LastViewedDate
Name

```

**Description**
A picklist value code unique to the picklist. Maximum size is 80 alphanumeric characters.
Can include the following special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The displayed picklist value if it’s different from the Name field. For example, the Name ‘5’
could have a DisplayValue ‘Five’.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the picklist value is the default for the associated picklist. Only one value
can be the default for a picklist.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist value was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the attribute picklist value was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the attribute picklist value.


-----

```
PicklistId
Sequence
Status
Value

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the picklist that the value is associated with.

This field is a relationship field.

**Relationship Name**
Picklist

**Relationship Type**
Lookup

**Refers To**
AttributePicklist

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The order in which the picklist value appears in the picklist.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the attribute picklist value.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Draft.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

**Description**
The text value for a picklist item if the picklist data type is text. This value must be unique
within a picklist. Maximum size is 255 alphanumeric characters. Can include the following
special characters: @ ! - < > * ? + = % # ( ) / \ & ‘ £ € $ ”.

##### Usage

The AttributePicklistValue object is the child object and the AttributePicklist object contains the picklist. Let’s say you need an asset
attribute to track the T-shirt size, which can be small, medium, or large. Create an AttributePicklist parent record as a Text type for the
T-shirt size attribute. Then create AttributePicklistValue records, one for each picklist value small, medium, and large, and associate them
with the parent record..

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AttributePicklistValueHistory on page 62**
History is available for tracked fields of the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklist

RecordsetFltrCritMonitor
