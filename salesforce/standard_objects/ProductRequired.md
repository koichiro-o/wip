#### ProductRequired

Represents a product that is needed to complete a work order or work order line item in field service.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
LastReferencedDate
LastViewedDate
ParentRecordId
ParentRecordType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product required was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product required was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The work order or work order line item that the product is required for.

This is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Visit, WorkOrder, WorkOrderLineItem, WorkType

**Type**
string


-----

```
Product2Id
ProductName
ProductRequiredNumber
QuantityRequired

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the parent record is a work order or a work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The required product.

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
Filter, Group, Nillable, Sort

**Description**
The name of the product required.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number identifying the product required.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity required of the product.


-----

```
QuantityUnitOfMeasure

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the required product; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.


Required products can be added to work types, work orders, and work order line items to ensure that the assigned service resource
arrives with the right equipment.

Adding required products to work types saves you time and keeps your business processes consistent. Work orders and work order line
items inherit their work type’s required products. For example, if all light bulb replacement jobs require a ladder and a light bulb, add
the ladder and light bulb as required products to your Light Bulb Replacement work type. When it’s time to create a work order for a
customer’s light bulb replacement, applying that work type to the work order adds the required products.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProductRequiredChangeEvent**

Change events are available for the object.

**ProductRequiredFeed**

Feed tracking is available for the object.

**ProductRequiredHistory**

History is available for tracked fields of the object.
