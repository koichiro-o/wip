#### ProductItemTransaction

Represents an action taken on a product item in field service. Product item transactions are auto-generated records that help you track
when a product item is replenished, consumed, or adjusted.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), undelete(), upsert()

 Special Access Rules

```
**•** Field Service must be enabled.

**•** Only users with Modify All Data or Modify All Records permissions can delete this object.

##### Fields

```
Description
LastReferencedDate
LastViewedDate
ProductItemId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the transaction. The description is blank when the transaction
record is created, but can be updated.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
ProductItemTransactionNumber
Quantity
RelatedRecordId

```

**Description**
The associated product item.

This is a relationship field.

**Relationship Name**
ProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) Auto-generated number identifying the product item transaction.

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
The quantity of the product item involved in the transaction. If inventory was
consumed, the quantity is negative.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The product consumed or product transfer related to the action. If
the action wasn’t related to consumption or transfer, the related record is blank.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
ProductTransfer, Visit


-----

```
TransactionType

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The action that the transaction tracks.

**•** Replenished: When a part is stocked at a location. A Replenished transaction
is created when a product item is created.

**•** Consumed: When parts are consumed to complete a work order. A Consumed
transaction is created when a record is added to the Products Consumed
related list on a work order or work order line item.

**•** Adjusted: When there’s a discrepancy or a change in consumption. An
Adjusted transaction is created when a product item’s Quantity on Hand is
edited, a product consumed is updated or delete, or a product transfer is
deleted.

**•** Transferred: When parts are transferred between locations.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**ProductItemTransactionChangeEvent**

Change events are available for the object.

**ProductItemTransactionFeed**

Feed tracking is available for the object.

**ProductItemTransactionHistory**

History is available for tracked fields of the object.
