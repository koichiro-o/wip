#### ReturnOrderItemTax

Represents the tax on a return order line item or return order item adjustment. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
Order Management must be enabled.


-----

##### Fields

**Field**
```
Amount
Description
OrderItemTaxLineItemSummaryId
Rate
ReturnOrderId

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount of tax represented by the return order item tax.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the return order item tax.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order item tax line item summary associated with the order item summary that
corresponds to the return order line item to which the tax applies.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Tax rate used to calculate the Amount.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated return order.

This is a relationship field.

**Relationship Name**
ReturnOrder


-----

```
ReturnOrderItemAdjustmentId
ReturnOrderItemTaxNumber
ReturnOrderLineItemId

```

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If this object represents a tax on an adjustment, this value is the ID of the return order item
adjustment to which the tax applies. If this value is null, the adjustment applies to a return
order line item.

This is a relationship field.

**Relationship Name**
ReturnOrderItemAdjustment

**Relationship Type**
Lookup

**Refers To**
ReturnOrderItemAdjustment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the return order item tax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If this object represents a tax on a return order line item, this value is the ID of that return
order line item. If this object represents a tax on an adjustment, this value is the ID of the
return order line item to which the adjustment applies.

This is a relationship field.

**Relationship Name**
ReturnOrderLineItem

**Relationship Type**
Lookup


-----

```
TaxEffectiveDate
Type

##### Associated Objects

```

**Refers To**
ReturnOrderLineItem

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows whether the amount on the tax line is an estimate or the final calculated amount.
Doesn’t set a value by default. Users can define automation to set and change the value as
needed.

Possible values are:

**•** `Actual`

**•** `Estimated`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderItemTaxChangeEvent (API version 62.0)**
Change events are available for the object.
