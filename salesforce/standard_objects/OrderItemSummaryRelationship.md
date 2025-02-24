#### OrderItemSummaryRelationship

Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order
summary objects in a chain of exchange orders. This object is available in API version 60.0 and later. An exchange order is an OrderSummary
object whose SourceProcess property is set to Exchange. An original order summary can have an exchange order, which in turn can
have yet another exchange order, and so on. The OrderSummaryRelationship object maintains this relationship between OrderSummary
objects.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AssociatedOrderItemInventory
AssociatedOrderItemSumPricing
AssociatedOrderItemSummaryId
AssociatedOrderItemSummaryRole

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls whether the inventory of the associated order item is included in the inventory of
the main order item.

Possible values are:

**•** `IncludedInMainInventory—Included in Main Inventory`

**•** `NotIncludedInMainInventory—Not Included in Main Inventory`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
An enum that describes how the related order item summary is priced relative to the primary
order item summary.

Possible values are:

**•** `IncludedInBundlePrice—Included in Bundle Price`

**•** `NotIncludedInBundlePrice—Not Included in Bundle Price`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related order item summary of this order item summary relationship. For bundle
relationships, this denotes the ID of the child order item summary.

This field is a relationship field.

**Relationship Name**
AssociatedOrderItemSummary

**Refers To**
OrderItemSummary

**Type**
picklist


-----

```
AssociatedQuanScaleMethod
CurrencyIsoCode
MainOrderItemSummaryId

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The role of the associated order item summary of this relationship.

Possible values are:

**•** `AddOnComponent—Addon Component`

**•** `BundleComponent—Bundle Component`

**•** `ClassificationComponent—Product Classification Component`

**•** `SetComponent—Set Component`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
An enum that describes how to scale the quantity of the associated order item summary
relative to the main order item summary.

Possible values are:

**•** `Constant`

**•** `Proportional`

The default value is `Proportional.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency of the OrderSummary.

Possible values are:

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The primary order item summary ID of this order item summary relationship.

This field is a relationship field.


-----

```
MainOrderItemSummaryRole
MainOrderSummaryId
Name
OrderItemRelationshipId

```

**Relationship Name**
MainOrderItemSummary

**Relationship Type**
Master-detail

**Refers To**
OrderItemSummary (the master object)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The role of the primary order item summary of this relationship.

Possible values are:

**•** `AddOn—Addon Parent`

**•** `Bundle—Bundle Parent`

**•** `Set—Set Parent`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the main order item summary.

This field is a relationship field.

**Relationship Name**
MainOrderSummary

**Refers To**
OrderSummary

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
ProductRelatedComponentId
ProductRelationshipTypeId

```

**Description**
The order summary ID of the order item summary.

This field is a relationship field.

**Relationship Name**
OrderItemRelationship

**Refers To**
OrderItemRelationship

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The lookup ID from the product related component.

This field is a relationship field.

**Relationship Name**
ProductRelatedComponent

**Refers To**
ProductRelatedComponent

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lookup from the product relationship type.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Refers To**
ProductRelationshipType

