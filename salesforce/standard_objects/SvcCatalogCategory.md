#### SvcCatalogCategory

Represents a group of Service Catalog items by functional area. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

##### Fields

```
DeveloperName
ImageId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique developer name for the catalog item category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Allows a builder to pick an image displayed in the catalog.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup


-----

```
IsActive
Language
ParentCategoryId

```

**Refers To**
ContentAsset

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows service catalog builders to deprecate categories or create in-draft categories.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
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

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
reference


-----

```
SortOrder

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Parent category of this category. Allows categories to be grouped up to a max depth of 3.

This field is a relationship field.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
SvcCatalogCategory

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the order that the category is displayed to the end user.

