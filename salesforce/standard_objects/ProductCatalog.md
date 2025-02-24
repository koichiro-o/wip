#### ProductCatalog

```


**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The name of the product associated with the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product associated with the product attribute set.


The container that holds a Product Category hierarchy. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
You must have the Industries, Retail, or B2B Commerce license.


-----

##### Fields

**Field**
```
CatalogCode
CatalogType
CurrencyIsoCode
Description
EffectiveEndDate

```

**Type**
text

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique ID associated with the catalog. Maximum size is 80 alphanumeric characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The category of an entry in the catalog. These categories can be customized. Examples
include: sellable products, services, parts, technical services, or technical resources.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the category.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date after which the catalog is unavailable to end users.


-----

```
EffectiveStartDate
LastReferencedDate
LastViewedDate
Name
NumberOfCategories
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the catalog is available to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the ProductCatlog record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of ProductCategory records assigned to this ProductCatalog record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
Status
