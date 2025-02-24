#### CreditMemo

Represents a document that is used to reduce the amount that a buyer owes a seller under the terms of an earlier invoice. This object
is available in API version 48.0 and later.

A credit memo always decreases the balance of an invoice. Users can apply positive credit memos to positive invoices, for example, a
$10 credit memo reduces the balance of a $100 invoice line to $90.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update()

 Special Access Rules

```
This object is available when Order Management or Subscription Management is enabled.

##### Fields

```
AppType
Balance

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field that indicates which Salesforce application generated the credit memo.

Possible values are:

**•** `Commerce Cloud`

**•** `Revenue Cloud`

This field is available in API versions 54.0 to 55.0

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
BillToContactId
BillingAccountId
CreationMode

```

**Description**
Amount of the credit memo that's available for allocation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Inherited from the account’s Bill to Account field.

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
The customer account associated with this credit memo.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the credit memo originated in Salesforce or an external system.

Possible values are:

**•** `External`

**•** `Salesforce`


-----

```
CreditDate
CreditMemoNumber
CurrencyIsoCode
Description
DocumentNumber
EffectiveDate

```

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The date when the credit memo was posted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
A credit memo numbering alternative to DocumentNumber, containing a number in a format
of your choice. Credit memo numbering is optional.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.

The default value is USD.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated number for organizing financial documents, for example DOC-0000123.

**Type**
date


-----

```
ExternalReference
ExternalReferenceDataSource
LastReferencedDate
LastViewedDate
NetCreditsApplied

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the effective date of the credit memo. If this field is empty, the credit date is used.
For reporting purposes only; this field drives no other logic.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Contains an external system’s ID for the credit memo.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Contains the name of the external system that also contains the credit memo.

This field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible that this record was only referenced (LastReferencedDate) and not viewed.

**Type**
currency


-----

```
OwnerId
ReferenceEntityId
SourceAction

```

**Properties**
Filter, Nillable, Sort

**Description**
Represents the total difference between the credit applied to and credit unapplied from the
invoice.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user who owns a credit memo record.

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
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record that this credit memo was generated from. For example, the order, order
summary, or invoice.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Invoice, Order

This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
Status
TotalAdjustmentAmount
TotalAdjustmentAmountWithTax

```

**Description**
Indicates which Salesforce API created the credit memo.

Possible values are:

**•** `Invoice—Indicates that Credit Invoice API created the credit memo and applied it`
to the invoice.

**•** `NegativeInvoiceLineConversion—Indicates that Subscription Management`
created the credit memo when a negative invoice line was converted.

**•** `Standalone—Indicates that the Credit Memo API created the credit memo.`

**•** `VoidPostedInvoice—Indicates that the Void a Posted Invoice API created the`
credit memo to offset the amount that was voided on the invoice.

This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the credit memo.

Possible values are:

**•** `Canceled—Indicates that the credit memo isn't being used and doesn't have a`
financial impact.

**•** `Error—Indicates that the credit memo has an error and doesn’t have a financial impact.`

**•** `Pending—Indicates that the credit memo is being processed but hasn't yet been`
posted as a financial transaction.

**•** `Posted—The credit memo has been recorded as a financial transaction. Most fields`
can’t be edited.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s adjustment lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalAdjustmentTaxAmount
TotalAmount
TotalAmountWithTax
TotalChargeAmount
TotalChargeAmountWithTax

```

**Description**
The sum of the credit memo’s adjustment line amounts, including tax.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s adjustment line tax. Adjustment line balances are excluded.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the credit memo’s `TotalLineAmount` and `TotalAdjustmentAmount.`

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total credit memo amount, with tax included.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s charge lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalChargeTaxAmount
TotalCreditAmountApplied
TotalCreditAmountUnapplied
 TotalTaxAmount

##### Associated Objects

```

**Description**
The sum of the credit memo’s charge line amounts, including tax.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Credit memo amount that's been applied to invoices.

This field is available in API version 53.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Credit memo amount that's been unapplied from invoices.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s tax lines.

This field is a calculated field.


This object has the following associated objects. If the API version isn’t specified, the associated objects are available in the same API
versions as this object. Otherwise, they’re available in the specified API version and later.


-----

**CreditMemoFeed on page 54**
Feed tracking is available for the object.

**CreditMemoHistory on page 62**
History is available for tracked fields of the object.

**CreditMemoOwnerSharingRule on page 64**
Sharing rules are available for the object.

**CreditMemoShare on page 66**
Sharing is available for the object.
