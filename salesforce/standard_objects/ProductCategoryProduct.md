#### ProductCategoryProduct

Holds the relation between product and product category to assign products to a category. This object is available in API version 55.0
and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
You must have the Industries, Retail, or B2B Commerce license.

##### Fields

```
Catalog
CurrencyIsoCode
EffectiveEndDate
EffectiveStartDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The foreign key to the ProductCatalog ID of the Category.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Possible values are:

**•** EUR—Euro

**•** USD—U.S. Dollar

The default value is `USD.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date after which the catalog is unavailable to end users.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the catalog is available to end users.


-----

```
IsPrimaryCategory
Name
ProductCategory
Product
ProductToCategory
Status

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the ProductCategory is the primaryProductCategory for a given product in a
ProductCatalog. The default value is `false.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the ProductCategoryProduct record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Foreign key to the ProductCategory ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the product.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenated Product ID and Category ID.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


-----

**Description**
The lifecycle state of the catalog. Possible values include: Draft, Active, Inactive

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductCategoryProductEvent (API version 55.0)**
Change events are available for the object.
