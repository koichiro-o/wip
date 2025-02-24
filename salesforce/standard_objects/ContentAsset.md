#### ContentAsset

Represents a Salesforce file that has been converted to an asset file in a custom app in Lightning Experience. Use asset files for org setup
and configuration. Asset files can be packaged and referenced by other components. This object is available in API version 38.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** Only admin users can edit or delete ContentAssets.

**•** Users with file access can create and query ContentAssets.

**•** It isn’t necessary to create asset files for regular, collaborative use of Salesforce Files. “Assetize” files only when they’re used in setup
and configuration situations.

**•** Neither the file (ContentDocument) nor the asset settings record (ContentAssets) can be deleted if the asset file is referenced by
another component.

**•** ContentAsset doesn’t support search or most recently used (MRU) lists.

**•** ContentAsset doesn’t support Apex triggers.


-----

##### Fields

**Field**
```
ContentDocumentId
DeveloperName
IsVisibleByExternalUsers
Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the asset file in the API. ContentAsset.DeveloperName:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether unauthenticated users can see the asset file.

**Type**
picklist


-----

```
MasterLabel
NamespacePrefix
