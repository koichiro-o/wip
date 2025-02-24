#### SalesTrxnItemRelationship

Describes the relationship between sales transaction items; for example, a bundle or set. This object interface is available in API version
58.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object interface is available if Subscription Management is enabled.

##### Fields

```
AssociatedItemPricing
AssociatedSalesTrxnItemId
AssociatedSalesTrxnItemRole

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes how the associated sales transaction item is priced, relative to the main sales
transaction item.

Possible values are:

**•** `IncludedInBundlePrice` — The associated sales transaction item’s cost is $0
because it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice` —The associated sales transaction item has a
cost because it’s not included in the bundle’s price.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the associated sales transaction item.

This field is a polymorphic relationship field. In a bundle relationship, this sales transaction
item is the bundle component.

**Relationship Name**
AssociatedSalesTrxnItem

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItem

**Type**
picklist


-----

```
ImplementorType
MainSalesTrxnItemId
MainSalesTrxnItemRole

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated sales transaction item in the relationship.

Possible values are:

**•** `AddOnComponent—The associated sales transaction item is an add-on component.`

**•** `BundleComponent—The associated sales transaction item is part of a bundle.`

**•** `ClassificationComponent—The associated sales transaction item is a`
classification component.

**•** `SetComponent—The associated sales transaction item is part of a set.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object that is implementing this object interface; for example, an OrderProduct object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the main sales transaction item.

This field is a polymorphic relationship field. In a bundle relationship, this sales transaction
item is the bundle parent.

**Relationship Name**
MainSalesTrxnItem

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItem

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the position of the main sales transaction item in the relationship.

Possible values are:


-----

```
ProductRelationshipTypeId
QuantityScaleMethod
SalesTransactionId

```


**•** `Bundle—The main sales transaction item is the bundle parent.`

**•** `Set—The main sales transaction item is the set parent.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the record that describes the relationship between the main and
associated sales transaction items.

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
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How to scale the quantity of the associated sales transaction item, relative to the main sales
transaction item. The value is informative; the system doesn’t check whether the scaled
quantities are correct. If this field has a non-null value, you can't edit the associated sales
transaction item’s quantity.

Possible values are:

**•** `Constant — The associated sales transaction’s item quantity remains the same in`
relation to the main sales transaction item’s quantity. For example, let’s say that the main
sales transaction item has a quantity of one and the associated sales transaction item
has a quantity of one. If you increase the quantity of the main sales transaction item to
two, the associated sales transaction item’s quantity remains at one.

**•** `Proportional` — The associated sales transaction’s item quantity increases or
decreases based on the main sales transaction item’s quantity. For example, let’s say that
the main sales transaction item has a quantity of one and the associated sales transaction
item has a quantity of two. If you increase the quantity of the main order item to two,
the associated order item’s quantity increases to four.

The default value is `Proportional.`

**Type**
reference


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the sales transaction to which the main and associated sales
transaction items belong to.

This field is a polymorphic relationship field.

**Relationship Name**
SalesTransaction

**Relationship Type**
Lookup

**Refers To**
SalesTransaction
