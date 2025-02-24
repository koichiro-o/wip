#### ProductConsumed

Represents an item from your inventory that was used to complete a work order or work order line item in field service.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

Note: To create products consumed, you need Read permission on product items.

Note: To delete or undelete product consumed for non-serialized products, you need Edit, Create, and Read permission on
product consumed. For product consumed records that lookup to serialized products, you need Modify All Data or Modify All
Records permission on product consumed.

##### Fields

```
Description
IsConsumed

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes and context about the product consumed.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that a product consumed has been processed if the Product2 it refers
to has IsSerialized=true selected. The default is false.


-----

```
IsLocked
IsProduct2Serialized
LastReferencedDate
LastViewedDate
MayEdit
PricebookEntryId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the product consumed record is locked or not.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates if a product is a serialized product. The default is false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product consumed was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product consumed was last viewed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the product consumed record can be edited or not.

The default value is `false.`

**Type**
reference


-----

```
Product2Id
ProductConsumedNumber
ProductItemId
ProductName
QuantityConsumed

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Price book associated with the product consumed. If the work order and the
product item’s associated product are related to the same price book, the Price
Book Entry auto-populates based on the product item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product associated with the product consumed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read Only) Auto-generated number identifying the product consumed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Product item associated with the product consumed. Creating a product
consumed record subtracts the quantity consumed from the linked product
item’s quantity.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name for the product consumed.

**Type**
double

**Properties**
Create, Filter, Sort, Update


-----

```
QuantityUnitOfMeasure
TotalPrice
UnitPrice
WorkOrderId
WorkOrderLineItemId

```

**Description**
The quantity of products consumed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Units of the consumed item; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price paid for the product items.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The price per unit of the product consumed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Work order that the product was consumed for.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Work order line item that the product was consumed for.


-----

##### Usage

When a product is consumed during the completion of a work order, create a product consumed record to track its consumption. You
can add products consumed to work orders or work order line items. Track product consumption at the line item level if you want to
know which products were used for each line item’s tasks.

The way you use products consumed depends on how closely you want to track the state of your inventory in Salesforce. If you want
to track the entire lifecycle of items in your inventory, including their storage, transfer, and consumption, link your products consumed
records to product items. This approach ensures that your inventory numbers auto-update to reflect the consumption of products from
your inventory. If you want to track product consumption only, however, specify a Price Book Entry on each product consumed record
and leave the Product Item field blank.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductConsumedChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductConsumedFeed**

Feed tracking is available for the object.

**ProductConsumedHistory**

History is available for tracked fields of the object.
