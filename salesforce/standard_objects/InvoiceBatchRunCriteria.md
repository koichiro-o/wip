#### InvoiceBatchRunCriteria

Represents a batch processing job and its required criteria in Subscription Management. During an invoice batch run, all billing schedules
that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version 55.0 and later.

A scheduled invoice batch run tells the system to start the run at a scheduled date and time by using certain criteria. The scheduler
includes the matching criteria, which are used to evaluate the billing schedules. Billing schedules that meet the specified criteria are
included for processing in the invoice batch run.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
Comments
CriteriaExpression

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional user-defined information about the batch run criteria.

**Type**
textarea

**Properties**
Filter, Nillable, Sort


-----

```
CriteriaMatchType
ExpectedInvoiceStatus
InvoiceBatchRunCriteriaNumber
OwnerId

```

**Description**
The formula that specifies criteria for filtering the billing schedules. For example, we can filter
billing schedules by currency code.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of matching criteria required for the batch.

Valid value is `MatchAll.`

The default value is `MatchAll.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of invoice a batch run generates.

Valid values are:

**•** `Draft`

**•** `Posted`

This field is available in API version 60.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated sequential number.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
System-generated field. The ID of the user who created the BillingBatchScheduler record. Its
UI label is `Owner.`

This field is a polymorphic relationship field.


-----

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User
