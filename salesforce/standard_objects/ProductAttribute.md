#### ProductAttribute

Represents the attributes that can be associated with a product. This object is available in API version 50.0 and later.

##### Supported Calls
```
create, delete, describeLayout(), describeSObjects(), getDeleted, getUpdated, query(), retrieve(),
undelete, update, upsert

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access products.

##### Fields

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD. Possible values are:`

**•** `USD—U.S. Dollar`


-----

```
Name
ProductId
Sequence
VariantParentId

##### Associated Objects

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the product attribute set.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the product that the attribute is associated with. This field is unique within your
organization.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product attributes appear in.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the variation parent record associated with the product attribute.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductAttributeEvent (API version 55.0)**
Change events are available for the object.
