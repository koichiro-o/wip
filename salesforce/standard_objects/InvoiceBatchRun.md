#### InvoiceBatchRun

Represents a batch processing job in Subscription Management or Revenue Lifecycle Management Billing. During an invoice batch run,
all billing schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API
version 55.0 and later.

An invoice batch run, controlled by a scheduler, tells the system to start the run at a scheduled date and time. The scheduler also includes
matching criteria, which are used to evaluate the billing schedules. Billing schedules that meet the specified criteria are included for
processing in the invoice batch run.

When an invoice batch run is started, Subscription Management or Revenue Lifecycle Management Billing:

**•** Evaluates the billing schedule to see if it meets the criteria for inclusion in the batch invoice run.

**•** Generates an invoice record with a pending state.

**•** Makes calls to an external tax provider.

**•** Adds the tax to the invoice.

**•** Summarizes information about the billing schedules that were included in the invoice batch run and displays this information in
the Invoice Batch Run record.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

```

-----

##### Special Access Rules

This object is available when Subscription Management or Revenue Lifecycle Management Billing is enabled.

##### Fields

```
BillingBatchSchedulerId
Comments
CompletionTime
InvoiceBatchRunNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related billing batch scheduler.

This field is a relationship field.

**Relationship Name**
BillingBatchScheduler

**Relationship Type**
Lookup

**Refers To**
BillingBatchScheduler

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Optional user-defined information about the scheduler.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the invoice batch run finished processing.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated sequential number.


-----

```
LastReferencedDate
LastViewedDate
OwnerId
RecoveryStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run was last modified. Its UI label is Last Modified
Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run was last viewed.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
System-generated field. The ID of the user who created the BillingBatchScheduler record. Its
UI label is Owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the state of the invoice batch run recovery process. This field is available in API
version 56.0 and later.

Possible values are:

**•** `CompletelyRecovered—All billing schedules included in the recovery run were`
reset to `Ready for Invoicing. These billing schedules are included in the next`
scheduled invoice batch run.


-----

```
StartTime
Status
TotalBillSchedRecovered

```


**•** `PartiallyRecovered—Some, but not all, billing schedules that were part of the`
recovery run were reset to `Ready for Invoicing. The billing schedules that`
were recovered are included in the next scheduled invoice batch run. The billing schedules
that weren’t successfully recovered must be manually reset to `Ready for`
`Invoicing` so they can be processed.

**•** `RecoveryFailed—The recovery job was unsuccessful. This value is available in API`
version 57.0 and later.

**•** `RecoveryStarted—The recovery job is in process.`

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Timestamp when the invoice batch run started processing.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The state of the invoice batch run.

Possible values are:

**•** `Canceled—This value is available in API version 57.0 and later.`

**•** `Completed`

**•** `Failed`

**•** `Started`

**•** `Stopped—This value is available in API version 57.0 and later.`

The default value is `Started.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of billing schedules that were part of the recovery run that were reset to Ready
```
  for Invoicing. These billing schedules are included in the next scheduled invoice

```
batch run.

This field is available in API version 57.0 and later.


-----

```
TotalBillSchedUnrecovered
TotalBillingSchedulesFailed
TotalBsSuccessfullyProcessed
TotalDraftInvoiceAmount
TotalDraftInvoices

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of billing schedules that were part of the recovery run that weren't reset to
```
  Ready for Invoicing. These billing schedules that weren’t successfully recovered

```
must be manually reset to Ready for Invoicing so they can be processed.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules that weren’t successfully processed. When a billing
schedule isn’t successfully processed, then the system doesn’t generate an invoice for it. For
details about errors, check the Revenue Transaction Error Log. This field is available in API
version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules for which the system was able to generate and process
invoices. This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice amounts for invoices in `Draft` status.

This field is available when Revenue Lifecycle Management Billing is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
TotalFilteredBillingSchedules
TotalInvSuccessfullyProcessed
TotalInvoicedAmount
TotalInvoicesCanceled

```

**Description**
The total number of invoices in `Draft` status generated in the batch run.

This field is available when Revenue Lifecycle Management Billing is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules that met the invoice run scheduler’s matching criteria.
The matching criteria specify which billing schedules are included in the invoice batch run.
Its field label is Total Matching Billing Schedules. This field is available in API version 56.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that were successfully processed.

When Revenue Lifecycle Management Billing is enabled, the field's value is either the same
as TotalPostedInvoices or TotalDraftInvoices based on the Invoice Status
selected when the Invoice Scheduler is set up.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of income including taxes represented by the successfully processed
invoices. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that weren't processed. To find out what went wrong, check
the Revenue Transaction Error Log. Fix the errors, then run the invoice batch run recovery
process.


-----

```
TotalInvoicesFailed
TotalInvoicesGenerated
TotalPostedInvoices
TotBillSchdUpdtDurDrftToPost

##### Associated Objects

```

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that weren’t processed successfully. To find out what went
wrong, check the Revenue Transaction Error Log. Then fix the errors and run the invoice
batch run recovery process. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that were generated from the billing schedules processed by
the invoice batch run. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices in `Posted` status generated during the batch run.

This field is available when Revenue Lifecycle Management Billing is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total billing schedules updated during the draft to posted run.

This field is available when Revenue Lifecycle Management Billing is enabled.

This field is available in API version 62.0 and later.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**InvoiceBatchRunChangeEvent on page 67**
Change events are available for the object.

**InvoiceBatchRunFeed on page 54**
Feed tracking is available for the object.

**InvoiceBatchRunHistory on page 62**
History is available for tracked fields of the object.

**InvoiceBatchRunOwnerSharingRule on page 64**
Sharing rules are available for the object.

**InvoiceBatchRunShare on page 66**
Sharing is available for the object.
