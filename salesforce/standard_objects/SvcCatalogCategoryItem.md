#### SvcCatalogCategoryItem

Represents an association between a Service Catalog item and category. Service catalog items can be grouped into categories. This
object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

##### Fields

```
IsPrimaryCategory

```

**Type**
boolean


-----

```
SortOrder
SvcCatalogCategoryId
SvcCatalogItemDefId

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the category is the primary category for a catalog item.

The default value is `false.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the order in which catalog items appear by default when you're viewing all items
in a single category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the category for which the service category item belongs.

This field is a relationship field.

**Relationship Name**
SvcCatalogCategory

**Relationship Type**
Lookup

**Refers To**
SvcCatalogCategory

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service category item definition.

This field is a relationship field.

**Relationship Name**
SvcCatalogItemDef

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef


-----
