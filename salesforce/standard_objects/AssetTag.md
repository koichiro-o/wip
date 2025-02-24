#### AssetTag

```

**Description**
The value specified in the picklist type field that corresponds to the attribute in the
AttributePicklistValue object.

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
Filter, Group, Nillable, Sort

**Description**
The value of the asset state period attribute. For example, a shirt can have the value of blue,
which indicates the shirt's color, or it can have the value of `small, which indicates the`
shirt's size.


Associates a word or short phrase with an Asset.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

 Fields

```
```
ItemId

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.


-----

```
Name
TagDefinitionId
Type

##### Usage

```

**Type**
string

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

**Type**
reference

**Properties**
Filter

**Description**
ID of the parent TagDefinition object that owns the tag.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public—The tag can be viewed and manipulated by all users in an organization.`

**•** `Personal—The tag can be viewed or manipulated only by a user with a matching`
```
   OwnerId.

```

AssetTag stores the relationship between its parent TagDefinition and the Asset being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.
