#### SalesforceInvoice

Read-only virtual object used in the Your Account App. Represents information about your organization’s invoices with Salesforce.

##### Supported Calls
```
describeLayout(), describeSObjects(), query()

 Fields

```
```
Balance
DueDate
ExternalId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for this invoice. Equal to the invoice’s total amount with tax, ignoring
payments and adjustments.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The customer must pay the invoice by the due date. Unpaid invoices past the due date can
be sent to collections.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.


-----

```
InvoiceCurrency
InvoiceDate
InvoiceNumber
SalesforceContractId
SalesforceInvoiceStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Currency associated with this invoice.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the invoice was posted. Used with payment terms to determine the invoice’s
`DueDate. For example, an invoice with an InvoiceDate` of April 1 and Net 30 payment
terms would have a `DueDate` of May 1.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
System-created ID for this invoice.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce Contract ID

This field is a relationship field.

**Relationship Name**
SalesforceContract

**Relationship Type**
Lookup

**Refers To**
SalesforceContract

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
TotalAmount

##### Usage

```

**Description**
The state of the invoice.

Possible values are:

**•** `DueSoon—`

**•** `Paid`

**•** `PastDue—`

**•** `Pending`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sum `TotalAmount` of the invoice items.


Used by Your Account to manage invoices for your organization’s Salesforce contract. Read-only.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceContract**

**SalesforcePayment**

**SalesforceQuote**
