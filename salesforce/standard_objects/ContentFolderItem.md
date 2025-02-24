#### ContentFolderItem

Represents a file (ContentDocument) or folder (ContentFolder) that resides in a ContentFolder in a ContentWorkspace. This object is
available in API version 35.0 and later.

##### Supported Calls
```
describeSObjects(), describeLayout(), query(), retrieve()

 Special Access Rules

 Fields

```
```
ContentSize

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
FileExtension
FileType
IsFolder
ParentContentFolderId
Title

```

**Description**

The file or folder size of the ContentFolderItem.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the file extension if the ContentFolderItem is a file.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the type of file if ContentFolderItem is a file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates that the ContentFolderItem is a folder, and not a file.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the ContentFolder that the ContentFolderItem resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

**Type**
string


-----

**Properties**
Filter, Group, Sort

**Description**

The name of the file or folder.
