#### ContentFolder

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user following or commenting on the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Represents a folder in a content library for adding files. This object is available in API version 34.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolder.

**•** All users with a content feature license can modify folders in their personal library.

**•** To modify a folder, the user must be a member of the library and have permission to modify folders.

##### Fields

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the folder.


-----

```
ParentContentFolderId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the ParentFolder.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContentFolderChangeEvent (API version 62.0)**
Change events are available for the object.
