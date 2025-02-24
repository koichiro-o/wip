#### PaymentTerm

Defines your company's method and expectations for receiving payment. This object is available in API version 55.0 and later.

Timely payment helps your company maintain cash flow. Payment terms are used to determine the payment due date on invoices. Use
with the PaymentTermItem object.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
Description
IsDefault
LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined field that describes the payment term. For example, use `Net 30` to describe
a payment term where the payment is due within 30 days of the billing date.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this payment term is the default term for your org. A default payment
term must be defined in your org.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


-----

```
LastViewedDate
Name
Status

##### Usage

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the payment term. For example, Net 30 or Cash on delivery (COD).

This name appears on the invoice.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the payment term is available for use on invoices.

Possible values are:

**•** `Active—The payment term is available for use and can be applied to an order. Only`
active payment terms can be applied to transactions or orders.

**•** `Draft—The payment term exists but isn't activated yet.`

**•** `Inactive—The payment term exists but can't be applied to new transactions or`
orders.

The default value is `Draft.`


A payment term is applied to an order or transaction, and is passed on to the billing schedule that’s used to generate the invoice. The
due date on the invoice is derived from the payment.

For example, a Net 30 payment term means that the customer has 30 days to pay from the invoice date. Suppose that an invoice with
a Net 30 payment term is generated on January 1. The invoice date is January 1, and the due date is January 31 (1 + 30 days = 31).


-----
