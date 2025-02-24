#### ContentFolderMember

```

**Description**
Indicates the status of enabling folders for the library. Valid values are:

**•** `C` — Completed folder enablement

**•** `S` — Started folder enablement

**•** `F` — Failed folder enablement

This field is available in API version 39.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Name of the entity the folder hierarchy is linked to.


Defines the association between a file and a folder. This object is available in API version 34.0 and later.

##### Supported Calls
```
describeSObjects(), delete(), query(), retrieve(), update()

 Special Access Rules

```
**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolderMember.

**•** All users with a content feature license can modify folders in their personal library.

**•** To modify ContentFolderMember, the user must be a member of the library and have permission to modify folders.

##### Fields

```
ChildRecordId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.


-----

```
ParentContentFolderId
