#### OpportunitySplitType

OpportunitySplitType provides unique labels and behavior for each split type. This object is available in API version 28.0 and later.

There are two default split types: revenue splits, which must total 100%, and overlay splits, which can total any percentage.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update()

 Fields

```
```
Description
DeveloperName
IsActive
IsTotalValidated

```

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the purpose of the split type, providing context to future developers.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. In managed packages, this
field prevents naming conflicts on package installations. With this field, a
developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Enables or disables the split type.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
If true, the split must total 100%. If false, the split can total any percentage.


-----

```
Language
ManageableState
MasterLabel
NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates language of split labels in the user interface.

**Type**
ManageableState enumerated list

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the manageable state of the specified component that is contained in
a package:

**•** `beta`

**•** `deleted`

**•** `deprecated`

**•** `deprecatedEditable`

**•** `installed`

**•** `installedEditable`

**•** `released`

**•** `unmanaged`

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The user-interface label for the split type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.


-----

```
SplitEntity
SplitField
SplitDataStatus
