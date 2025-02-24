#### AsyncOperationTracker

Represents the status of an asynchronous request initiated from the Quote, Order, and CreditMemo entities. This object is available in
API version 61.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
AsyncOperationNumber
CorrelationIdentifier
ExpiresAt
FailedJobItems
FinishedAt

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A string that identifies the operation being tracked in AsyncOperationTracker.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A string that identifies an operation across services.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when this record will be deleted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items within the job that have failed.

**Type**
dateTime


-----

```
JobType

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process completed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of job.

Possible values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion—Automated Negative`
Invoice Line Conversion

**•** `AutomaticRefunds—Automatic Refunds`

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `InvoiceDocgenJob`

**•** `InvoiceDocgenPostProcessJob`

**•** `InvoiceDocgenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `PSTCommonSyncStep`

**•** `PSTConfigAndPersist`

**•** `PSTOrderTaxAsync`

**•** `PSTPriceAndPersist`

**•** `PSTQuoteTaxAsync`

**•** `PearAmendQtyAssets—Initiate Amend Quantity`

**•** `PearCancelAssets—Initiate Cancellation`

**•** `PearRenewAssets—Initiate Renewal`

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote—Place Quote`

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`


-----

```
LastReferencedDate
LastViewedDate
OwnerId
ParentOperationId

```


**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment—Price Rule Deployment`

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `TransactionLineBom—Create Material Lines`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user or group that owns the job.,

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ReferenceEntityId
StartedAt
Status

```

**Description**
This field is a relationship field.

**Relationship Name**
ParentOperation

**Refers To**
AsyncOperationTracker

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the ID of a record associated with the asynchronous request. For example, if the
asynchronous request is associated with a credit memo, this field contains the ID of the credit
memo.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Refers To**
CreditMemo, InvoiceBatchRun, Order, Product2, Quote

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when Salesforce started the asynchronous process.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the asynchronous request.

Possible values are:

**•** `Completed`

**•** `CompletedWithFailures—Completed With Failures`

**•** `Failure`

**•** `InProgress—In Progress`

**•** `Submitted`


-----

```
StepName

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion—Automated Negative`
Invoice Line Conversion

**•** `AutomaticRefunds—Automatic Refunds`

**•** `CommerceVariationsUpsert`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `InvoiceDocgenJob`

**•** `InvoiceDocgenPostProcessJob`

**•** `InvoiceDocgenRetryJob`

**•** `InvoiceDraftToPosted`

**•** `PSTCommonSyncStep`

**•** `PSTConfigAndPersist`

**•** `PSTOrderTaxAsync`

**•** `PSTPriceAndPersist`

**•** `PSTQuoteTaxAsync`

**•** `PearAmendQtyAssets—Initiate Amend Quantity`

**•** `PearCancelAssets—Initiate Cancellation`

**•** `PearRenewAssets—Initiate Renewal`

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceOrderPriceAsync`

**•** `PlaceOrderTaxAsync`

**•** `PlaceQuote—Place Quote`

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment—Price Rule Deployment`

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`


-----

```
SubmittedAt
SuccessfulJobItems
TotalJobItems

```


**•** `TransactionLineBom—Create Material Lines`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was submitted by the REST
request.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successful items in this job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of items in this job.

