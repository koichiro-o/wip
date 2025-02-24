#### Invoice

Represents a financial document describing the total amount a buyer must pay for goods or services provided. This object is available
in API version 48.0 and later.

Users can edit non-posted invoices. Posted invoices can’t be deleted. After an invoice is posted, users can make payments against it to
reduce its balance.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update()

 Special Access Rules

```
To access this object, your org must have a Salesforce Order Management or D2C Commerce license. A few fields require Commerce
Subscriptions to be enabled. These fields are available only in Lightning Experience.

##### Fields

```
Balance
BillToContactId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for this invoice. Equal to the invoice’s total amount with tax, ignoring
payments and adjustments.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Inherited from the account’s Bill to Account.


-----

```
BillingAccountId
CurrencyIsoCode
DaysInvoiceOpen

```

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The customer account for this invoice.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The three-letter ISO 4217 currency code associated with the invoice.

The default value is `USD.`

This field is available in API version 55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days since the invoice was created before it was paid.

This field is a calculated field.

This field is available in API version 55.0 and later.


-----

```
DaysInvoiceOverdue
Description
DocumentNumber
DueDate
FullSettlementDate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days since the date when payment was due.

This field is a calculated field.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Users can add more information about this invoice. Maximum of 1,000 characters.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-generated number that is used to organize financial documents. The number
can be sequential or random.

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The customer must pay the invoice by the due date. Unpaid invoices past the due date can
be sent to collections.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the invoice is paid in full.

This field is available in API version 55.0 and later.


-----

```
InvoiceBatchRunId
InvoiceDate
InvoiceNumber
LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Id of the invoice batch run that generated this invoice.

This field is a relationship field.

This field is available in API version 55.0 and later.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The date that the invoice was posted. Used with payment terms to determine the invoice’s
`DueDate. For example, an invoice with an InvoiceDate` of 04/01 and Net 30 payment
terms has a `DueDate` of 05/01.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
System-created unique ID for this invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

This field is available in API version 55.0 and later.


-----

```
LastViewedDate
NetCreditsApplied
NetPaymentsApplied
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view. If this value is null, it's possible the user accessed this record or list view
(LastReferencedDate) but didn't view it.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Represents the net credits applied to an invoice. Calculated by subtracting the sum of all
unapplied lines from the sum of all applied lines.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Represents net payments applied to an invoice. Calculated by subtracting the sum of
unapplied payments from the sum of payments applied to the invoice.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user who owns an invoice record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
PaymentExclusionReason
PaymentTermId
PostedDate
ReferenceEntityId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason for skipping creation of payment schedules and payment schedule items for the
invoice. This field is only available if Commerce Subscriptions is enabled for your org. Available
in API version 63.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment term used on this invoice.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the invoice was posted.

This field is available in API version 60.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the order or order summary that created this invoice.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity


-----

```
SettlementStatus
ShouldExcludePayment
Status

```

**Relationship Type**
Lookup

**Refers To**
Order, OrderSummary

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the invoice's payment.

Possible values are:

**•** `Not Applicable`

**•** `Not Settled`

**•** `Partially Settled`

**•** `Settled`

This field is available when Subscription Management is enabled.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether to skip creating payment schedules and payment schedule
items for the invoice (true) or not (false). The default value is `false. This field is only`
available if Commerce Subscriptions is enabled for your org. Available in API Version 63.0
and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the invoice.

Possible values are:

**•** `Canceled— Indicates that the invoice was generated and later canceled.`

**•** `Draft— Indicates that the invoice is a draft. Available in API version 60.0 and later.`

**•** `Draft In Progress— Indicates that the draft invoice is in progress. Available in`
API version 60.0 and later.


-----

```
TaxLocaleType
TotalAdjustmentAmount
TotalAdjustmentAmountWithTax
TotalAdjustmentTaxAmount

```


**•** `Error— Indicates that an error occurred when processing the invoice.`

**•** `Pending— Indicates that the invoice is being processed.`

**•** `Posted— Indicates that the invoice has been generated and sent to the customer.`

**•** `Posting In Progress—Indicates that the invoice posting is in progress. Available`
in API version 60.0 and later.

**•** `Void In Progress— Indicates that the invoice is pending a status change.`

**•** `Voided— The invoice’s status after the API successfully voids the invoice.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The system used to handle tax on the original Order associated with the Invoice. Gross usually
applies to taxes like value-added tax (VAT), and Net usually applies to taxes like sales tax. This
field is available when Order Management or B2B Commerce is enabled.

Possible values are:

**•** Gross: Displays most prices and taxes as combined values

**•** Net: Displays most prices and taxes as separate values

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice’s adjustment line amounts.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the amount fields on the invoice's adjustment-type invoice lines, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalAmount
TotalAmountWithTax
TotalChargeAmount
TotalChargeAmountWithTax
TotalChargeTaxAmount

```

**Description**
The total amount of tax applied to the invoice line's adjustment lines.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum `TotalAmount` values on the invoice’s lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TotalAmountWithTax` values on the invoice’s lines.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice’s charges.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the amount fields on the invoice's charge-type invoice lines, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the invoice's charge lines.


-----

```
TotalConvertedNegAmount
 TotalTaxAmount

##### Associated Objects

```

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all negative invoice lines that were converted to a credit memo. For example, if
one negative invoice line was for -$10 and one was for -$15, the total amount that’s converted
to a credit memo is -$25.

This field is a calculated field.

This field is available when Subscription Management is enabled.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TaxAmount` values on the invoice lines.

This field is a calculated field.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceFeed on page 54**
Feed tracking is available for the object.

**InvoiceHistory on page 62**
History is available for tracked fields of the object.

**InvoiceOwnerSharingRule on page 64**
Sharing rules are available for the object.

**InvoiceShare on page 66**
Sharing is available for the object.
