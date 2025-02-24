#### ProductAttributeSet

Represents a group of attributes that can be associated with a product. This object is available in API version 50.0 and later.


-----

##### Supported Calls
```
create, delete, describeSObjects(), query(), retrieve(), update, upsert

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access products.

##### Fields

```
Description
DeveloperName
Language

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Text description of the product attribute set.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `esSpanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`


-----

```
MasterLabel

```


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
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the product attribute set.

