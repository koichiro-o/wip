#### OrderItemRelationship

Describes a relationship between order products. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
AssociatedOrderItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the associated order product.

This field is a relationship field. In a bundle relationship, this order product is the bundle
component.

**Relationship Name**
AssociatedOrderItem


-----

```
AssociatedOrderItemPricing
AssociatedOrderItemRole
AssociatedQuantScaleMethod

```

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how the associated order product is priced relative to the main order product. The
value is informative; the system doesn’t check whether the associated order product is
included in the bundle price.

Possible values are:

**•** `IncludedInBundlePrice—The associated order product’s cost is $0 because`
it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice—The associated order product has a cost because`
it’s not included in the bundle’s price.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated order product in the relationship.

Possible values are:

**•** `BundleComponent—The associated order product is part of a bundle.`

**•** `SetComponent—The associated order product is part of a set.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the quantity of the associated order product scales, relative to the main order product.
The value is informative; the system doesn’t check whether the scaled quantities are correct.

Possible values are:

**•** `Constant— The associated order’s product quantity remains the same in relation to`
the main order product’s quantity. For example, the main order product has a quantity
of one and the associated order product has a quantity of one.


-----

```
MainOrderItemId
MainOrderItemRole
Name

```


**•** `Proportional— The associated order’s product quantity increases or decreases`
based on the main order product’s quantity. For example, the main order product has
a quantity of one and the associated order product has a quantity of two. In other words,
there are two associated order products for every one main order product.

The default value is `Proportional.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The main order product’s unique identifier.

This field is a relationship field. In a bundle relationship, this order product is the bundle
parent.

**Relationship Name**
MainOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the role of the main order product in the relationship.

Possible values are:

**•** `Bundle— The main order product is the bundle parent.`

**•** `Set— The main order product is the set parent.`

Note: Subscription Management doesn’t support the `Set` value.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the order product relationship.


-----

```
OrderId
ProductRelationshipTypeId

##### Associated Objects

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the related order.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the record that describes the relationship between the main and
associated order products.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemRelationshipChangeEvent**

Change events are available for the object.

**OrderItemRelationshipFeed**

Feed tracking is available for the object.

**OrderItemRelationshipHistory**

History is available for tracked fields of the object.


-----

**OrderItemRelationshipOwnerSharingRule**

Sharing rules are available for the object.

**OrderItemRelationshipShare**

Sharing is available for the object.
