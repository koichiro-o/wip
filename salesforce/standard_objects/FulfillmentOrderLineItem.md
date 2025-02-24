#### FulfillmentOrderLineItem

Represents a product or delivery charge belonging to a FulfillmentOrder. Corresponds to an OrderItemSummary. This object is available
in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs.

##### Fields

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the FulfillmentOrder associated with the FulfillmentOrderLineItem.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

This field is available in API version 49.0 and later.


-----

```
Description
EndDate
FulfillmentOrderId
FulfillmentOrder
LineItemNumber
GrossUnitPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the FulfillmentOrderLineItem.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
End date of the FulfillmentOrderLineItem.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrder associated with the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
FulfillmentOrder

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


-----

```
IsReship
MainFulfillmentOrderLineItemId
OrderItemId

```

**Description**
Unit price, including tax, of the FulfillmentOrderLineItem. This value is equal to TotalPrice +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the FulfillmentOrderLineItem belongs to a reshipment. The default value
is false.

This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original FulfillmentOrderLineItem.

This field is a relationship field.

This field is available in API version 63.0 and later.

**Relationship Name**
FulfillmentOrderLineItem

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrderLineItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original OrderItem for the OrderItemSummary associated with the
FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
OrderItem

**Relationship Type**
Lookup


-----

```
OrderItemSummaryId
OriginalQuantity
Product2Id
Quantity

```

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemSummary associated with the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
OrderItemSummary

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Original quantity of the FulfillmentOrderLineItem.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the product represented by the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double


-----

```
QuantityUnitOfMeasure
RejectedQuantity
RejectReason
ReshipReason

```

**Properties**
Create, Filter, Sort, Update

**Description**
Current quantity of the FulfillmentOrderLineItem. Equal to the original quantity minus any
canceled quantity.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unit of measure of the quantity, for example: unit, gallon, ton, or case.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used by the Distributed Order Management package and Store Fulfillment app to store the
quantity that has been rejected by a fulfillment location.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the FulfillmentOrderLineItem was rejected by a fulfillment location, the reason for the
rejection.

Default values are:

**•** `Damaged`

**•** `Just Sold`

**•** `Other`

**•** `Out of Packing Supplies`

**•** `Out of Stock`

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ServiceDate
TotalAdjustmentAmount
TotalAdjustment
AmountWithTax
TotalAdjustment
TaxAmount
TotalAmount

```

**Description**
If the FulfillmentOrderLineItem belongs to a reshipment, the reason for the reshipment.

Default values are:

**•** `Damaged`

**•** `Lost`

**•** `Unknown`

**•** `Wrong Item`

This field is available in API version 53.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Service or start date of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of any price adjustments applied to the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the FulfillmentOrderLineItem, inclusive of
tax. This amount is equal to TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

**Type**
currency


-----

```
TotalLineAmount
TotalLineAmountWithTax
TotalLineTaxAmount
TotalPrice
TotalTaxAmount

```

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
Total, not including adjustments or tax, of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the FulfillmentOrderLineItem, inclusive of tax. This amount is equal to
TotalLineAmount + TotalLineTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of the FulfillmentOrderLineItem. Equal to UnitPrice
times Quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
Type
TypeCode
UnitPrice

```

**Description**
Tax on the TotalPrice.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of the FulfillmentOrderLineItem. Matches the type of the associated OrderItemSummary.
Delivery Charge indicates that the FulfillmentOrderLineItem represents a delivery charge.
Fee indicates that it represents another type of fee, such as a return fee. Order Product
indicates that it represents any other type of product, service, or charge. Each type corresponds
to one type code, shown here in parentheses.

Possible values are:

**•** `Delivery Charge` (Charge)

**•** `Fee` (Charge) This value is available in API v56.0 and later.

**•** `Order Product` (Product)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type code of the FulfillmentOrderLineItem. Matches the type code of the associated
OrderItemSummary. Processing depends on this value. Charge indicates that the
FulfillmentOrderLineItem represents a charge or fee. Product indicates that it represents any
other type of product, service, or charge. A type code can be associated with one or more
types.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
Unit price of the FulfillmentOrderLineItem.


-----

**[FulFillmentOrderChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

SEE ALSO:

FulfillmentOrder

FulfillmentOrderItemAdjustment

FulfillmentOrderItemTax

OrderItemSummary
