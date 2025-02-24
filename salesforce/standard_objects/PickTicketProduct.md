#### PickTicketProduct

Represents a quantity of a product to be picked as part of a PickTicket. It can include quantities for multiple FulfillmentOrders. This object
is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with an Order Management Growth license.

##### Fields

```
PickTicketId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the PickTicket associated with the PickTicketProduct.

This field is a relationship field.

**Relationship Name**
PickTicket

**Relationship Type**
Lookup

**Refers To**
PickTicket


-----

```
PickTicketProductNumber
PickedQuantity
Product2Id
ProductCode
Quantity

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicketProduct.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity of the PickTicketProduct that has been picked.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product associated with the PickTicketProduct.

This field is a relationship field.

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
Product code of the product associated with the PickTicketProduct.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Total quantity that’s requested to be picked of the associated product.


-----

```
RejectReason
RejectedQuantity
StockKeepingUnit

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reason why some or all of the requested quantity isn’t being picked.

Possible values are:

**•** `Defected`

**•** `Other`

**•** `Out of stock`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The requested quantity that hasn’t been picked. When the status category of the associated
PickTicket is set to `Completed, this value is automatically calculated as` `Quantity`   ```
  PickedQuantity.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit (SKU) of the associated product.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PickTicketProductFeed on page 54**
Feed tracking is available for the object.

SEE ALSO:

PickTicket

PickTicketAssignment

Product2


-----
