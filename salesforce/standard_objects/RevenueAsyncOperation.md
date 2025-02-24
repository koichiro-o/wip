#### RevenueAsyncOperation

Represents the status of an asynchronous process initiated by a REST request in Subscription Management. This object is available in
API versions 57.0 to 59.0. Use AsyncOperationTracker instead of RevenueSyncOperation in API version 59.0 and later.

For example, `asset-management/assets/collection/actions/initiate-amend-quantity` creates a
RevenueAsyncOperation record when it initiates an asynchronous process. The ID of the record is returned in the REST response.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management.

##### Fields

```
AsyncOperationNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
CorrelationIdentifier
ExpiresAt
FailedJobItems
FinishedAt
JobType

```

**Description**
A unique identifier for this revenue async operation record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique identifier for the API request associated with this revenue async operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when this record will be deleted.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items that weren’t successfully processed by the sync operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was completed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The REST request that initiated the asynchronous process.

Valid values are:

**•** `AssetizationAsyncJob`

**•** `AutomatedNegativeInvoiceLineConversion`

**•** `AutomaticRefunds`


-----

```
LastReferencedDate
LastViewedDate
ParentOperationId

```


**•** `BatchInvoiceDraftToPosted`

**•** `ContextPersistence`

**•** `CreateCPQContractsJob`

**•** `InvoiceDraftToPosted`

**•** `PearAmendQtyAssets`

**•** `PearCancelAssets`

**•** `PearRenewAssets`

**•** `PlaceOrder`

**•** `PlaceOrderPersistSync`

**•** `PlaceQuote`

**•** `PlaceQuotePersistAndPriceSync`

**•** `PlaceQuotePersistSync`

**•** `PlaceQuotePriceAsync`

**•** `PlaceQuoteTaxAsync`

**•** `PriceRuleDeployment`

**•** `PriceSheetDeployJob`

**•** `QuoteToOrderJob`

**•** `RuleLibraryDeployment`

**•** `TransactionLineBom`

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


-----

```
ReferenceEntityId
StartedAt
Status

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

This field is a relationship field.

**Relationship Name**
ParentOperation

**Relationship Type**
Lookup

**Refers To**
RevenueAsyncOperation

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the ID of a record associated with the asynchronous request. For example, if the
asynchronous request is associated with a credit memo, this field contains the ID of the credit
memo.

This field is a relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
CreditMemo

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
The status of the asynchronous process.


-----

```
SubmittedAt
SuccessfulJobItems
TotalJobItems

```

Possible values are:

**•** `Completed`

**•** `CompletedWithFailures`

**•** `Failure`

**•** `InProgress`

**•** `Submitted`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the asynchronous process was submitted by the REST
request.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of items successfully processed by the sync operation.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of items processed by the sync operation, including both successfully
processed items and failed items.

