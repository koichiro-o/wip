#### ProductRelatedComponent

Represents a product that is included in a product bundle, a set, or a product and an add-on. This object is available in API version 57.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

In version 58.0 and later, this object is available when B2B Commerce, B2C Commerce, Industries Automotive, Industries EPC, or Subscription
Management is enabled.

In version 57.0, this object is available when B2B Commerce, B2C Commerce, or Industries Automotive is enabled.

##### Fields

```
ChildProductId
ChildProductRole
ChildSellingModelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the associated product.

This field is a relationship field. In a bundle relationship, this item is the child product.

**Relationship Name**
ChildProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The position of the associated product in the relationship.

Possible values are:

**•** `AddOnComponent—The child product is an add-on to another product. Available`
in API version 58.0 and later.

**•** `BundleComponent—The child product is a component in a bundle.`

**•** `SetComponent—The child product is a component in a set.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the associated product’s sales model.


-----

```
DoesBundlePriceIncludeChild
IsComponentRequired
IsDefaultComponent
IsQuantityEditable

```

This field is a relationship field.

**Relationship Name**
ChildSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the bundle price includes the associated product’s price.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated product is required for configuring a bundle or set.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated product is part of the product bundle or set automatically,
or can be added after the bundle’s or set’s creation.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether you can edit the component’s quantity in the bundle or set after the
bundle’s or set’s creation.

The default value is `false.`


-----

```
LastReferencedDate
LastViewedDate
MaxQuantity
MinQuantity
Name
ParentProductId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user accessed this record or list view (LastReferencedDate)
without viewing it.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The associated product’s allowed maximum quantity.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The associated product’s allowed minimum quantity.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the associated product.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
ParentProductRole
ParentSellingModelId
ProductComponentGroupId

```

**Description**
The unique identifier of the main product around which the bundle or set is built.

This field is a relationship field.

**Relationship Name**
ParentProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the position of the main product in the relationship.

Possible values are:

**•** `AddOn—The main product is the add-on parent. Available in API version 58.0 and later.`

**•** `Bundle—The main product is the bundle parent.`

**•** `Set— The main product is the set parent.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the main product’s sales model.

This field is a relationship field.

**Relationship Name**
ParentSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ProductRelationshipTypeId
Quantity
QuantityScaleMethod

```

**Description**
The unique identifier of the group of a product bundle or set. This group contains the
associated products that can be included in the main product’s bundle or set.

This field is a relationship field.

**Relationship Name**
ProductComponentGroup

**Relationship Type**
Lookup

**Refers To**
ProductComponentGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier of the record that describes the relationship between the main and
associated products.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The unit count of the associated product.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The scaling method is used to calculate the associated product’s quantity based on changes
made to the main product’s quantity in a transaction.

Possible values are:


-----

```
Sequence

```


**•** `Constant` — The associated product’s quantity remains the same in relation to the
main product’s quantity. For example, the main product has a quantity of one and the
associated component has a quantity of one. If you increase the quantity of the main
product to two, the associated component’s quantity remains at one.

**•** `Proportional` — The associated product’s quantity increases or decreases based
on the main product’s quantity. For example, the main component has a quantity of one
and the associated product has a quantity of two. If you increase the quantity of the main
product to two, the associated product’s quantity increases to four.

The default value is `Proportional.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the arrangement of the order products when configuring a bundle or set.

