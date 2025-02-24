#### OrderItemSummary

Represents the current properties and state of a product or charge on an OrderSummary. Corresponds to one or more order item objects,
consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

##### Fields

```
AdjustedLineAmount
AdjustedLineAmtWithTax
AssetId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including line adjustments but not order-lever adjustments or tax, of the
OrderItemSummary. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the OrderItemSummary, inclusive of adjustments and tax. This amount is equal
to AdjustedLineAmount + TotalAdjustedLineTaxAmount.

This is a calculated field. This field is available in API version 49.0 and later.

**Type**
reference


-----

```
CurrencyIsoCode
DeliveryEstimationReference
DeliveryEstimationTimeZone

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated asset. This field is available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the OrderSummary associated with the OrderItemSummary.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique reference ID for the delivery estimation.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Timezone in which the estimated delivery times are based.


-----

```
Description
EarliestEstimatedDeliveryDate
EarliestEstimatedDeliveryTime
EndDate
GrossUnitPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the OrderItemSummary.

This field can be edited.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Earliest date when the item is estimated to be delivered.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Earliest time of the day when the item is estimated to be delivered.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Unit price, including tax, of the OrderItemSummary. This value is equal to UnitPrice + the
amount of tax on the UnitPrice.


-----

```
LastEstimatedDeliveryDate
LastEstimatedDeliveryTime
LineNumber
ListPrice

```

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is available in API version 49.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Latest date when the item is estimated to be delivered.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Latest time of the day when the item is estimated to be delivered.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order line number assigned to this OrderItemSummary. For example, if this object is the
third in the displayed list of OrderItemSummaries belonging to the OrderSummary, this value
is 3.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
List price of the product represented by this OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


-----

```
Name
OrderDeliveryGroup
SummaryId
OrderSummaryId
OriginalOrderItemId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderItemSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderDeliveryGroupSummary to which this object belongs.

This field is a relationship field.

**Relationship Name**
OrderDeliveryGroupSummary

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryGroupSummary

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary to which this object belongs.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
PricebookEntryId
Product2Id

```

**Description**
ID of the original order item associated with this summary object. Nillable=true only if the
associated order summary is unmanaged. For managed order summaries, nillable=false.

This field is a relationship field.

**Relationship Name**
OriginalOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the pricebook entry associated with this OrderItemSummary.

This field is available in API version 54.0 and later.

This field is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the product represented by this OrderItemSummary.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


-----

```
ProductCode
Quantity
QuantityAllocated
QuantityAvailable
ToCancel
QuantityAvailable
ToFulfill

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product code of the product represented by this OrderItemSummary.

**Type**
double

**Properties**
Filter, Sort

**Description**
Current total quantity of products represented by this order item summary. Equal to
QuantityOrdered minus (QuantityCanceled and QuantityReturned).

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
double

**Properties**
Filter, Sort

**Description**
Allocated quantity on this order item summary. This quantity is associated with one or more
FulfillmentOrderLineItems.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Quantity that can still be canceled on this OrderItemSummary. Equal to QuantityOrdered
minus (QuantityCanceled and QuantityAllocated). This value duplicates
QuantityAvailableToFulfill. This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
QuantityAvailable
ToReship
QuantityAvailable
ToReturn
QuantityCanceled
QuantityFulfilled

```

**Description**
Quantity available to be fulfilled on this OrderItemSummary. Equal to QuantityOrdered minus
(QuantityCanceled and QuantityAllocated). This value duplicates QuantityAvailableToCancel.
This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Quantity available to be reshipped on this OrderItemSummary. Equal to QuantityFulfilled
minus (QuantityReshipped and QuantityReturnInitiated).

This field is available in API version 53.0 and later. This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Quantity available to be returned on this OrderItemSummary. Equal to QuantityFulfilled
minus QuantityReturnInitiated. This is a calculated field.

**Type**
double

**Properties**
Filter, Sort

**Description**
Canceled quantity on this OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
double

**Properties**
Filter, Sort

**Description**
Fulfilled quantity on this OrderItemSummary. This quantity can no longer be canceled.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


-----

```
QuantityNetOrdered
QuantityOrdered
QuantityReshipped
QuantityReturned
QuantityReturnInitiated

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Quantity available to be allocated on this OrderItemSummary. Equal to QuantityOrdered
minus QuantityCanceled.

**Type**
double

**Properties**
Filter, Sort

**Description**
Ordered quantity on this OrderItemSummary. It includes the originally ordered quantity plus
any quantity added to the order later.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Reshipped quantity on this OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is available in API version 53.0 and later.

**Type**
double

**Properties**
Filter, Sort

**Description**
Returned quantity on this OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
double


-----

```
QuantityShipped
ReferencePrice
ReservedAtLocationId
ServiceDate

```

**Properties**
Filter, Sort

**Description**
Quantity returned or pending return on this OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Quantity shipped on this OrderItemSummary.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The original or reference price of the order product.

This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Service or start date of the OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


-----

```
Status
TaxTreatmentId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status of the OrderItemSummary. The default value is ORDERED. When a quantity value
changes, each status formula is evaluated in order. If a formula is true, no more evaluations
are performed for that change.

Possible values and their formulas, in the order of evaluation, are:

**•** `RETURNINITIATED—Return Initiated — (Quantity > 0) & (QuantityReturnInitiated`
= QuantityFulfilled) & (QuantityReturned < QuantityReturnInitiated)

**•** `RESHIPPED—Reshipped — (QuantityReshipped = QuantityFullfilled) &`
(QuantityFullfilled > 0) & (QuantityReturnInitiated = 0) & (QuantityFulfilled =
QuantityOrdered)

**•** `RETURNED—Returned — (Quantity = 0) & (QuantityReturned > 0)`

**•** `CANCELED—Canceled — (Quantity = 0) & (QuantityCancelled > 0) & (QuantityReturned`
= 0)

**•** `FULFILLED—Fulfilled — (Quantity > 0) & ((QuantityOrdered - QuantityCancelled)`
<= QuantityFulfilled)

**•** `PARTIALLYFULFILLED—Partially Fulfilled — (QuantityFulfilled > 0) &`
(QuantityFulfilled < (QuantityOrdered - QuantityCancelled))

**•** `ALLOCATED—Allocated — (Quantity > 0) & (Quantity <= QuantityAllocated)`

**•** `PARTIALLYALLOCATED—Partially Allocated — (QuantityAllocated > 0) &`
(QuantityAllocated < Quantity)

**•** `ORDERED—Ordered — None of the other formulas apply`

**•** `PAID—Paid — N/A`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax treatment.

This field is available in API version 63.0 and later. This field is available with Subscription
Management.

This field is a relationship field.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup


-----

```
StockKeepingUnit
TotalAdjusted
LineTaxAmount
TotalAdjustmentAmount
TotalAdjustment
AmtWithTax
TotalAdjustmentDistAmount

```

**Refers To**
TaxTreatment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit (SKU) of the Product2 associated with the OrderItemSummary.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the AdjustedLineAmount. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all price adjustments applied to this OrderItemSummary. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of all price adjustments applied to this OrderItemSummary, inclusive of tax.
This amount is equal to TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalAdjustmentDist
AmtWithTax
TotalAdjustmentDist
TaxAmount
TotalAdjustmentTaxAmount
TotalAmtWithTax
TotalLineAdjustmentAmount

```

**Description**
Total of all order-level price adjustments applied to this OrderItemSummary. This value
includes OrderItemAdjustmentLineSummaries that belong to
OrderAdjustmentGroupSummaries of type Header. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the order-level price adjustments applied to this OrderItemSummary,
inclusive of tax. This amount is equal to TotalAdjustmentDistAmount +
TotalAdjustmentDistTaxAmount.

This field is available in API version 49.0 and later. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentDistAmount. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the OrderItemSummary, inclusive of tax. This amount is equal to TotalPrice +
TotalTaxAmount.

This field is available in API version 49.0 and later. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalLineAdjustment
AmtWithTax
TotalLineAdjustment
TaxAmount
TotalLineAmount
TotalLineAmountWithTax

```

**Description**
Total of all non-order-level price adjustments applied to this OrderItemSummary. This value
includes OrderItemAdjustmentLineSummaries that don’t belong to an
OrderAdjustmentGroupSummary, or that belong to an OrderAdjustmentGroupSummary of
type SplitLine. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all non-order-level price adjustments applied to this OrderItemSummary, inclusive
of tax. This amount is equal to TotalLineAdjustmentAmount +
TotalLineAdjustmentTaxAmount.

This field is available in API version 49.0 and later. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAdjustmentAmount. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, not including adjustments or tax, of the OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total unadjusted amount of the OrderItemSummary, inclusive of tax. This amount is equal
to TotalLineAmount + TotalLineTaxAmount.

This field is available in API version 49.0 and later. This is a calculated field.


-----

```
TotalLineTaxAmount
TotalPrice
TotalTaxAmount
Type
TypeCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount. This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including line and order-level adjustments but not tax, of the OrderItemSummary. This
is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalPrice. This is a calculated field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the OrderItemSummary. Delivery Charge indicates that the OrderItemSummary
represents a delivery charge. Fee indicates that it represents another type of fee, such as a
return fee. Order Product indicates that it represents any other type of product, service, or
charge. Each type corresponds to one type code, shown here in parentheses.

Possible values are:

**•** `Delivery Charge (Charge)`

**•** `Fee (Charge)` This value is available in API v56.0 and later.

**•** `Order Product (Product)`

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
picklist


-----

```
 UnitPrice

##### Associated Objects

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type code of the OrderItemSummary. Charge indicates that the OrderItemSummary represents
a charge or fee. Product indicates that it represents any other type of product, service, or
charge. A type code can be associated with one or more types.

Possible values are:

**•** `Charge`

**•** `Product`

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Unit price of the product represented by the OrderItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

FulfillmentOrderLineItem

OrderItem

OrderItemAdjustmentLineSummary

OrderItemTaxLineItemSummary

OrderSummary


-----
