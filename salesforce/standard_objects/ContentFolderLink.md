#### ContentFolderLink

Defines the association between a library and its root folder. This object is available in API version 34.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
**•** Salesforce CRM Content must be enabled to access ContentFolderLink.

**•** ContentFolderLink is read-only in the context of a library.

##### Fields

```
ContentFolderId
EnableFolderStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the folder.

This is a relationship field.

**Relationship Name**
ContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
ParentEntityId
