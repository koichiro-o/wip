#### SvcCatalogFilterCriteria

Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item. This object is available in API version
60.0 and later.

##### Supported SOAP API Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Supported REST API Methods
DELETE, GET, HEAD, PATCH, POST, Query

 Special Access Rules

```
To access this object, get the Service Catalog Access permission set license.

##### Fields

```
CriteriaRelation
Description
DeveloperName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Possible values are:

**•** `AllConditionsAreMet`

**•** `AnyConditionIsMet`

**Type**
textarea

**Properties**
Nillable

**Description**
A description that states the restriction placed on a user’s access to a catalog items eligibility.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:


-----

```
FullName
IsActive
Language

```


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
string

**Properties**
Create, Group, Nillable

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies if the eligibility rule is active.

The default value is `false.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Supported languages for eligibility rules

Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`


-----

```
ManageableState
MasterLabel
Metadata

```


**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the manageable state of a catalog item that is contained in a package.

Possible values are:

**•** `beta—Managed-Beta`

**•** `deleted—Managed-Proposed-Deleted`

**•** `deprecated—Managed-Proposed-Deprecated`

**•** `deprecatedEditable—SecondGen-Installed-Deprecated`

**•** `installed—Managed-Installed`

**•** `installedEditable—SecondGen-Installed-Editable`

**•** `released—Managed-Released`

**•** `unmanaged—Unmanaged`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the eligibility rule record.

**Type**
complexvalue

**Properties**
Create, Nillable, Update

**Description**
The metadata type associated with the SvcCatalogFilterCriteria object.


-----

```
NamespacePrefix
NumOfRelatedItems
