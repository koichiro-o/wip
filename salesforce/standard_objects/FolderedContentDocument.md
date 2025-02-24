#### FolderedContentDocument

Represents the relationship between a parent and child ContentFolderItem in a ContentWorkspace.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
ContentDocumentId
ContentSize
FileExtension

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the ContentDocument that can be in a folder.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

File size of the ContentDocument.

**Type**
string


-----

```
FileType
IsFolder
ParentContentFolderId
Title

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the ContentDocument.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File type of the ContentDocument.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates that the FolderedContentDocument is a folder, rather than a file.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the ContentFoldr the ContentDocument resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Name of the file or folder in a ContentFolder.


-----
