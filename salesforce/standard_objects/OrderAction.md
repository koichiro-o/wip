#### OrderAction

Indicates the type of order, such as a new sale or a cancellation. This object is available in API version 55.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
This object is available if Subscription Management is enabled in your org.

##### Fields

```
Name
OffsetOrderItemId
OrderId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name given to the order action.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the previous order item that is being modified by the business action. For example,
the order that is being canceled.

This is a relationship field.

**Relationship Name**
OffsetOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order containing the order item that implements the business action.

This is a relationship field.


-----

```
SourceAssetId
Type

```

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset that is changed as a result of the business action. For example, the asset that is
being canceled.

This is a relationship field.

**Relationship Name**
SourceAsset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The business action that created the order product.

Possible values are:

**•** `Cancellation`

**•** `New Sale`

**•** `No Change—A child product was added to the bundle, but the top-level product in`
the bundle was otherwise unchanged.

**•** `Quantity Amendment`

**•** `Renewal`

