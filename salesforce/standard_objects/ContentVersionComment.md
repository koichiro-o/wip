#### ContentVersionComment

Represents a comment on a version of a file. This object is available in API version 42.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

Only users with Modify All Data permission have access to this object.

##### Fields

```
ContentDocumentId
ContentVersionId
UserComment

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version of the file.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
ID of the user who commented on the file.


-----
