#### CaseTag

Associates a word or short phrase with a Case


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

 Fields

```
```
ItemId
Name
TagDefinitionId
Type

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

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

-----

##### Usage

CaseTag stores the relationship between its parent TagDefinition and the Case being tagged. Tag objects act as metadata, allowing users
to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.
