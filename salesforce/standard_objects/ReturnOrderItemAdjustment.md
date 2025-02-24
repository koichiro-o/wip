#### ReturnOrderItemAdjustment

Represents a price adjustment on a return order line item. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
Order Management must be enabled.

##### Fields

```
Amount
Description

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount, not including tax, of the adjustment.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
OrderItemAdjustLineSummaryId
ReturnOrderId
ReturnOrderItemAdjustmentNumber
ReturnOrderLineItemId

```

**Description**
Description of the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item adjustment line summary associated with the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the return order associated with the return order line item to which the adjustment
applies.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the return order item adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the return order line item to which this adjustment applies.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem


-----

```
TotalAmtWithTax
TotalTaxAmount

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
ReturnOrderLineItem

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the Amount.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderItemAdjustmentChangeEvent (API version 62.0)**
Change events are available for the object.
