#### ShipmentItem

Represents an order item included in a shipment. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Health Cloud Visit Inventory

**•** Consumer Goods Cloud Retail Execution

##### Fields

```
Description

```

**Type**
string


-----

```
ExpectedDeliveryDate
FulfillmentOrderLineItemId
OrderItemSummaryId
Product2Id

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the shipment item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Expected delivery date of the shipment that contains the shipment item.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The FulfillmentOrderLineItem (fulfillment order product) corresponding to the shipment
item.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The OrderItemSummary (order product summary) corresponding to the shipment item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product represented by the shipment item.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


-----

```
Quantity
ReturnOrderLineItemId
ShipmentId
ShipmentItemNumber
TrackingNumber

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of products represented by the shipment item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For a return ShipmentItem, the associated ReturnOrderLineItem.

This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The shipment that contains the shipment item.

This is a relationship field.

**Relationship Name**
Shipment

**Relationship Type**
Lookup

**Refers To**
Shipment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the shipment item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
TrackingUrl

##### Associated Objects

```

**Description**
The tracking number of the shipment that contains the shipment item.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking URL of the shipment that contains the shipment item.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShipmentItemFeed**

Feed tracking is available for the object.

**ShipmentItemHistory**

History is available for tracked fields of the object.

SEE ALSO:

Shipment

FulfillmentOrderLineItem
