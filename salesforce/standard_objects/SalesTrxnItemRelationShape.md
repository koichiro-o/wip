#### SalesTrxnItemRelationShape

Describes the relationship between sales transaction shape items; for example, a bundle or set. This object is available in API version 57.0
and later.

##### Supported Calls
```
create() describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

##### Fields

```
AssocSalesTrxnItemShapeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the associated sales transaction shape item.

This field is a relationship field. In a bundle relationship, this sales transaction shape item is
the bundle component.


-----

```
AssocSalesTrxnItemShapeRole
AssociatedItemShapePricing
MainSalesTrxnItemShapeId

```

**Relationship Name**
AssocSalesTrxnItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated sales transaction shape item in the relationship.

Possible values are:

**•** `BundleComponent—The associated sales transaction shape item is part of a bundle.`

**•** `SetComponent—The associated sales transaction shape item is part of a set.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes how the associated sales transaction shape item is priced, relative to the main
sales transaction shape item.

Possible values are:

**•** `IncludedInBundlePrice— The associated sales transaction shape item’s cost`
is $0 because it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice— The associated sales transaction shape item`
has a cost because it’s not included in the bundle’s price.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the main sales transaction shape item.

This field is a relationship field. In a bundle relationship, this sales transaction shape item is
the bundle parent.

**Relationship Name**
MainSalesTrxnItemShape


-----

```
MainSalesTrxnItemShapeRole
ProductRelationshipTypeId
QuantityScaleMethod

```

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the position of the main sales transaction shape item in the relationship.

Possible values are:

**•** `AddOnComponent— The main sales transaction shape item is an add on component.`
Available in API version 58.0 and later.

**•** `Bundle— The main sales transaction shape item is the bundle parent.`

**•** `Set— The main sales transaction shape item is the set parent.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that describes the relationship between the main and associated sales
transaction shape items.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How to scale the quantity of the associated sales transaction shape item, relative to the main
sales transaction shape item. The value is informative; the system doesn’t check whether the
scaled quantities are correct. If this field has a non-null value, you can't edit the associated
sales transaction shape item’s quantity.


-----

```
SalesTransactionShapeId
SalesTrxnItemRelationShapeName

```

Possible values are:

**•** `Constant—The associated sales transaction’s item quantity remains the same in`
relation to the main sales transaction shape item’s quantity. For example, let’s say that
the main sales transaction shape item has a quantity of one and the associated sales
transaction shape item has a quantity of one. If you increase the quantity of the main
sales transaction shape item to two, the associated sales transaction shape item’s quantity
remains at one.

**•** `Proportional—The associated sales transaction’s item quantity increases or`
decreases based on the main sales transaction shape item’s quantity. For example, let’s
say that the main sales transaction shape item has a quantity of one and the associated
sales transaction shape item has a quantity of two. If you increase the quantity of the
main order item to two, the associated order item’s quantity increases to four.

The default value is `Proportional.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related sales transaction shape.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Name of the relationship of the sales transaction shape item.

