#### RevenueTransactionErrorLog

Contains information about errors that occurred while processing a request. The error record persists until another error with the same
category, primary record, and (optionally) related record occurs. This object is available in API version 55.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

This object is available with Subscription Management and Revenue Cloud.

##### Fields

```
AsyncOperationTrackerId
Category

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the async operation tracker record created by the request. Async operation tracker
records contain information about the status of the asynchronous process initiated by the
request. This field is available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
AsyncOperationTracker

**Relationship Type**
Lookup

**Refers To**
AsyncOperationTracker

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides context about the source of error. For example, if an error occurs while processing
an /assets/collection/actions/initiate-cancellation request, the
category is `InitiateCancel.`

Possible values are:

**•** `ApplyAPI`

**•** AutomatedNegativeInvoiceLineConversion

**•** AutomaticRefunds

**•** `ConvertNegativeInvoiceLineToCredit—available in API version 56.0 and`
later

**•** `Core Invoice Generation Failure`

**•** `CreditInvoiceAPI`

**•** `CreditTaxIntegrationAPI`

**•** `InitiateAmendment—available in API version 56.0 and later`

**•** `InitiateCancel`


-----

```
ErrorCode

```


**•** `InitiateRenewal`

**•** `InsufficientAccess—Insufficient Access to start Invoice run`

**•** `InvoiceBatchRun`

**•** `InvoiceBatchRunInvoiceGeneration`

**•** `InvoiceBatchRunPostProcessor`

**•** `InvoiceBatchRunPreProcessor`

**•** `InvoiceBatchRunRecovery`

**•** `InvoiceBatchRunSelectionStep`

**•** `InvoiceBatchRunSummarizer`

**•** `InvoiceBatchRunTaxProcessor`

**•** `MaterialLineGeneration—available in API version 58.0 and later`

**•** `Invalid Tax API Input`

**•** `Invalid Tax Integration Input`

**•** `OrderTaxCalculationFailure—available in API version 61.0 and later of`
Revenue Cloud.

**•** `OrderToAsset`

**•** `OrderItemToAsset—available in API version 59.0 and later`

**•** `OrderToBillingSchedule`

**•** `PaymentSale`

**•** `PaymentScheduleGeneration—available in API version 56.0 and later`

**•** `QuotePriceCalculationFailure—available in API version 61.0 and later of`
Revenue Cloud.

**•** `QuoteTaxCalculationFailure—available in API version 61.0 and later of`
Revenue Cloud.

**•** `QuoteToOrder—available in API version 56.0 and later`

**•** `Post Tax API Failure`

**•** `Post-Credit Tax Failure`

**•** `Pre-Credit Tax Failure`

**•** `StandaloneCreditAPI`

**•** `Tax API Failure`

**•** `TransactionToContract—available in API version 59.0 and later`

**•** `Unknown Failure—available in API version 56.0 and later`

**•** `VoidPostedInvoiceAPI`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ErrorLogNumber
ErrorMessage
OwnerId
PrimaryRecordId

```

**Description**
The error code; for example, INVALID_INPUT.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated unique ID that identifies the error.

**Type**
textarea

**Description**
Contains information about the error and how to resolve it.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who made the request that resulted in the creation of the error log.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the record that’s associated with this error. For example, if the error occurred while
creating an invoice from an order, the primary ID is the ID of the order.

This field is a polymorphic relationship field.

**Relationship Name**
PrimaryRecord

**Relationship Type**
Lookup


-----

```
RelatedRecordId
RequestIdentifier
RevenueAsyncOperationId

```

**Refers To**
Asset, BillingBatchScheduler, BillingSchedule, CardPaymentMethod, CreditMemo, Invoice,
InvoiceBatchRun, InvoiceBatchRunRecovery, Order, Payment, PaymentBatchRun,
PaymentGateway, Quote, Refund

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. The ID of a record that can provide additional context about the error. For example,
if `PrimaryRecordId` is the ID of an order, this field could be the ID of an order item.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
BillingBatchScheduler, BillingSchedule, BillingScheduleGroup, CreditMemo, CreditMemoLine,
Invoice, InvoiceLine, OrderItem, Payment, PaymentSchedule, PaymentScheduleItem,
QuoteLineItem, Refund

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID returned by the request. Use this ID to identify the revenue transaction error
log records for a specific request. This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the revenue async operation record created by the request. Revenue async operation
records contain information about the status of the asynchronous process initiated by the
request. This field is available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
RevenueAsyncOperation


-----

**Relationship Type**
Lookup

**Refers To**
RevenueAsyncOperation
