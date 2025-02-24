#### OrderChangeLog

Represents a log record of all change requests made to an order post activation. A log record is always one-to-one to change an order
request. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Commerce Cloud standard objects in the inventory data model require at least one of the following licenses: B2B Commerce, D2C
Commerce.


-----

##### Fields

**Field**
```
ChangeLineId
ChangeLineType
ChangeOrderId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the main change line created as a result of the change request. For example, if you
change an order item, the `ChangeLineId` would be the change OrderItem ID, or if you
change a shipping address, the ChangeLineId would be the change OrderDeliveryGroup
ID.

This field is a polymorphic relationship field.

**Relationship Name**
ChangeLine

**Relationship Type**
Lookup

**Refers To**
OrderAdjustmentGroup, OrderDeliveryGroup, OrderItem, OrderItemAdjustmentLineItem,
OrderItemTaxLineItem

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The method used to implement the change.

Possible values are:

**•** `Delta`

**•** `New`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the change order.

This field is a relationship field.

**Relationship Name**
ChangeOrder

**Relationship Type**
Lookup


-----

```
ChangeRequest
ChangeSummary
ChangeType
CurrencyIsoCode

```

**Refers To**
Order

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique ID of the request of which this change is a part.

**Type**
textarea

**Properties**

**Description**
A human-readable summary of the change details.

Here’s an example of a change summary:
```
  Reduced quantity by -3.
  Change adjustment by $15.
  Added an adjustment of $20.
  Changed tax by $-0.11, effective 1/1/2020.
  Added a tax of $1.5, effective 1/1/2020.

```
**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the change request.

Possible values are:

**•** `NewAdjustmentGroups—Add a new header level adjustment.`

**•** `NewLineAdjustments—Add a new line level adjustment.`

**•** `NewOrderItems—Add a new order item.`

**•** `QuantityChange—Add or remove quantity from an original order item.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for any currency allowed by the organization.

Possible value is:


-----

```
Name
RelatedLineId
RelatedOrderId
Status

```


**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the order change log.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the main line that is changed as a result of this change.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
OrderAdjustmentGroup, OrderDeliveryGroup, OrderItem, OrderItemAdjustmentLineItem,
OrderItemTaxLineItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the order that is changed.

This field is a relationship field.

**Relationship Name**
RelatedOrder

**Relationship Type**
Master-detail

**Refers To**
Order (the master object)

**Type**
picklist


-----

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The order status of the change order.

Possible values are:

**•** `Activated`

**•** `Draft`

##### Usage

Order change log entries are automatically created each time an order is modified.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderChangeLogFeed on page 54**
Feed tracking is available for the object.

**OrderChangeLogHistory on page 62**
History is available for tracked fields of the object.
