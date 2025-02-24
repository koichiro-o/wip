#### ProductCategory

```

**Description**
The ID of the owner.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The lifecycle state of the catalog. Possible values include: Draft, Active, Inactive


Represents the category that products are organized in.This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access product media.

##### Fields

```
CatalogId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the catalog.


-----

```
CurrencyIsoCode
Description
IsNavigational
LastReferencedDate
LastViewedDate
Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD.`

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the category.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is `false.`

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


-----

```
NumberOfProducts
ParentCategoryId
SortOrder

##### Associated Objects

```

**Description**
Name of the category.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of products in a category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product’s parent category.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
ProductCategory

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order that the category is displayed in.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductCategoryChangeEvent (API version 55.0)**
Change events are available for the object.
