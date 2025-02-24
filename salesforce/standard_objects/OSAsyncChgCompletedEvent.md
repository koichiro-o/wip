#### OSAsyncChgCompletedEvent

An event that allows the processing of the credit memo, invoices, and other entities after a bulk action has successfully completed. The
event provides all of the values that would exist on the synchronous APIs. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), describeSObjects()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs.

##### Fields

```
ActionType

```

**Type**
string

**Properties**
Create, Nillable

**Description**
The type of the action that gets applied to Order Summary

Possible values are:

**•** CANCEL_ALL


-----

```
AsyncOperationLogId
CurrencyIsoCode
EventUuid
FeeChangeOrderId

```


**•** RETURN_ALL

**Type**
reference

**Properties**
Create, Nillable

**Description**
The ID of the AsyncOperationLog.

This field is a relationship field.

**Relationship Name**
AsyncOperationLog

**Refers To**
AsyncOperationLog

**Type**
string

**Properties**
Create, Nillable

**Description**
The ISO code for the currency of the OrderSummary that's associated with the
FulfillmentOrder. This field is available only for orgs with multicurrencies enabled.

Possible values are:

**•** `CNY—Chinese Yuan`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string

**Properties**
Nillable

**Description**
Uniquely identifies an event message. The ID used to match the events that are returned in
the callback result with the events in the publish call.

**Type**
reference

**Properties**
Create, Nillable

**Description**
The change order for the fee ID. This order usually used for invoices.


-----

```
GrandTotalAmount
InFulfillmentChangeOrderId
OrderSummaryId
PostFulfillmentChangeOrderId

```

This field is a relationship field.

**Relationship Name**
FeeChangeOrder

**Refers To**
Order

**Type**
double

**Properties**
Create, Nillable

**Description**
The new order summary's grand total.

This amount is equal to TotalAmount + TotalTaxAmount.

**Type**
reference

**Properties**
Create, Nillable

**Description**
The change order for any items during fulfillment.

This field is a relationship field.

**Relationship Name**
InFulfillmentChangeOrder

**Refers To**
Order

**Type**
reference

**Properties**
Create, Nillable

**Description**
The foreign key for the master Order Summary entity.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Refers To**
OrderSummary

**Type**
reference


-----

```
PreFulfillmentChangeOrderId
TotalAdjDistAmount
TotalAdjDistTaxAmount
TotalAdjustedDeliveryAmount

```

**Properties**
Create, Nillable

**Description**
The change order for any items post-fulfillment. This ID is used for credit memos refunds

This field is a relationship field.

**Relationship Name**
PostFulfillmentChangeOrder

**Refers To**
Order

**Type**
reference

**Properties**
Create, Nillable

**Description**
The change order for any items that haven't been fulfilled.

This field is a relationship field.

**Relationship Name**
PreFulfillmentChangeOrder

**Refers To**
Order

**Type**
double

**Properties**
Create, Nillable

**Description**
The total distributed adjustment amount without taxes.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total distributed adjustment taxes.

**Type**
double

**Properties**
Create, Nillable


-----

```
TotalAdjustedDeliveryTaxAmount
TotalAdjustedProductAmount
TotalAdjustedProductTaxAmount
TotalAmount
TotalExcessFundsAmount
TotalFeeAmount

```

**Description**
The total delivery adjusted amount without taxes.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total delivery adjusted tax amount .

**Type**
double

**Properties**
Create, Nillable

**Description**
The total adjusted product amount without tax.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total adjusted product tax amount.

This amount is equal to TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total amount, not including taxes.

**Type**
double

**Properties**
Create, Nillable

**Description**
The amount used to determine if a refund is needed pre-fulfillment.

**Type**
double


-----

```
TotalFeeTaxAmount
TotalRefundableAmount
TotalRequiredFundsAmount
TotalTaxAmount
