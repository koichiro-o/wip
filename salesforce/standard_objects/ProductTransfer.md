#### ProductTransfer

Represents the transfer of inventory between locations in field service.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
Description
DestinationLocationId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Details not recorded in the provided fields.

**Type**
reference


-----

```
ExpectedPickupDate
IsReceived
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The place the product is to be delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be picked up.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Checkbox identifying that the product was received.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.


-----

```
OwnerId
Product2Id
Product2TransferRecordMode

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner of the product transfer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product associated with the product transfer.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If serialized, indicates when the serial number is recorded. It is visible on the
product transfer as a read-only field depending on the field-level security. Possible
values are:

**•** `SendAndReceive` —The serial number is recorded when sending or
receiving.

**•** `ReceiveOnly —The serial number is recorded when receiving only.`

**Relationship Name**
Product2.TransferRecordMode


-----

```
ProductRequestId
ProductRequestLineItemId
ProductTransferNumber

```

**Relationship Type**
Lookup

**Refers To**
Product2.TransferRecordMode

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the product request associated with the product transfer.

This is a relationship field.

**Relationship Name**
ProductRequest

**Relationship Type**
Lookup

**Refers To**
ProductRequest

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product request line item associated with the product transfer.

This is a relationship field.

**Relationship Name**
ProductRequestLineItem

**Relationship Type**
Lookup

**Refers To**
ProductRequestLineItem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the product transfer.


-----

```
QuantityReceived
QuantitySent
QuantityUnitOfMeasure
ReceivedById
ReturnOrderId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of product received at the destination location.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Amount of product sent from the source location.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The units of the product, for example grams, liters, or units.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the contact who received the product at the destination location.

This is a polymorphic relationship field.

**Relationship Name**
ReceivedBy

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the product transfer.


-----

```
ReturnOrderLineItemId
ShipmentExpectedDeliveryDate
ShipmentId

```

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the product transfer.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the shipment related to the product transfer.

This is a relationship field.

**Relationship Name**
Shipment

**Relationship Type**
Lookup


-----

```
ShipmentStatus
ShipmentTrackingNumber
ShipmentTrackingUrl
SourceLocationId
SourceProductItemId

```

**Refers To**
Shipment

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field for the shipment related to the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the source location related to the product transfer.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference


-----

```
Status

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field for the product item related to the product transfer.

**Relationship Name**
SourceProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the product transfer.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductTransferChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductTransferFeed**

Feed tracking is available for the object.

**ProductTransferHistory**

History is available for tracked fields of the object.

**ProductTransferOwnerSharingRule**

Sharing rules are available for the object.

**ProductTransferShare**

Sharing is available for the object.
