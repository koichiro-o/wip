#### WebStorePricebook

Represents a store price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the B2B Commerce license is enabled.

##### Fields

```
IsActive
LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the WebStorePricebook is active (true) or not (false). Default value
is `false.`

**Type**
dateTime


-----

```
LastViewedDate
Name
Pricebook2Id
WebStoreId

##### Usage

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the store price book record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book assigned to the store.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store assigned to the price book.


Use the WebStorePricebook object to assign price books to a store. When you assign a price book to a web store, any buyer who has
access to the store can price products from the assigned price books. When a store or buyer has multiple price book assignments,
including prices to the same product, the price is determined by the pricing strategy of the store.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WebStorePricebookFeed**

Feed tracking is available for this object.
