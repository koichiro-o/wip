#### ProductItem

Represents the stock of a particular product at a particular location in field service, such as all bolts stored in your main warehouse.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
LocationId
OwnerId

```

**Description**
The date when the product item was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product item was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Location associated with the product item. This usually indicates where the
product item is stored.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The product item’s owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
Product2Id
ProductItemNumber
ProductName
QuantityOnHand
QuantityUnitOfMeasure

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Product associated with the product item, which represents the type of product
in your inventory.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) Auto-generated number identifying the product item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A name for the product item. Try to select a name that indicates what is being
stored where; for example, Batteries in Warehouse A.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity at the location. If you want to add a serial number, this value must
be 1.

**Type**
picklist


-----

```
SerialNumber

##### Usage

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the product item; for example, kilograms or liters. Quantity Unit of Measure
picklist values are inherited from the Quantity Unit of Measure field on products.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique number for identification purposes. If you want to enter a serial number,
the Quantity on Hand must be 1.


Each product item is associated with a product and a location in Salesforce. If a product is stored at multiple locations, the product will
be tracked in a different product item for each location.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductItemFeed**

Feed tracking is available for the object.

**ProductItemHistory**

History is available for tracked fields of the object.

**ProductItemOwnerSharingRule**

Sharing rules are available for the object.

**ProductItemShare**

Sharing is available for the object.
