#### PaymentLineInvoice

```

**Refers To**
PaymentIntent

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the payment link record for which the event occurs. This field is available in API
version 63.0 and later.

This field is a relationship field.

**Relationship Name**
PaymentLink

**Refers To**
PaymentLink


Represents a payment allocated to or unallocated from an invoice. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated. Commerce Payments entities are available only in Lightning Experience.

##### Fields

```
Amount

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Total amount applied or unapplied by this payment line.


-----

```
AppliedDate
AssociatedAccountId
AssociatedPaymentLineId
Comments

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this line was applied to an invoice or payment. If this field is null, it inherits the
value of the payment line invoice’s Date field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The account for this payment line’s target invoice.

This is a relationship field.

**Relationship Name**
AssociatedAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The paymentLine that was unapplied. Populated only when PaymentLineInvoice’s Type field
has a value of Unapplied.

This is a relationship field.

**Relationship Name**
AssociatedPaymentLine

**Relationship Type**
Lookup

**Refers To**
PaymentLineInvoice

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
Date
EffectiveDate
EffectiveImpactAmount
HasBeenUnapplied

```

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time that this payment line was created.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Defines the date and time when the payment line application or unapplication becomes
effective.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment invoice line impacts a customer’s accounts receivable. This value
is positive when PaymentLineInvoice’s Type field is Applied, and negative when
PaymentLineInvoice’s Type is Unapplied. If there’s an unapplied line related to this record,
EffectiveImpactAmount has a value of 0.

Note: EffectiveImpactAmount evaluates only the applied and unapplied line pair.
Therefore, the effective impact amount could be different for different lines within
the same payment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether this payment line has been unapplied from the target invoice. Has a value
of NA when PaymentInvoiceLine’s Type field has a value of Unapplied. Can be No or Yes if
Type has a value of Applied.

Possible values are:

**•** `NA`


-----

```
ImpactAmount
InvoiceId
LastReferencedDate
LastViewedDate

```


**•** `No`

**•** `Yes`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows the payment’s financial impact against the customer’s accounts receivable. If
PaymentLineInvoice has a Type of Applied, the ImpactAmount is the negative equivalent of
the line’s Amount field. Otherwise, ImpactAmount equals Amount.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Target invoice for this payment line.

This is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

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
and LastReferenceDate is not null, the user accessed this record or list view indirectly.


-----

```
PaymentBalance
PaymentId
PaymentLineInvoiceNumber
Type
UnappliedDate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total balance of this line’s parent payment record following the application or unapplication
of this payment line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Parent payment for this payment line.

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for this payment line.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether this payment line has been applied or unapplied to the target invoice.

Possible values are:

**•** `Applied`

**•** `Unapplied`

**Type**
dateTime


-----

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this payment line was unapplied from the target invoice. Populated only when
the Type field equals Unapplied. Inherits the value of the Date field.

##### Usage

Use a payment line to apply all or part of a payment’s balance to an invoice. The PaymentLineInvoice object represents the balance
taken from the payment and applied toward the invoice. You can apply a payment’s balance when you create the payment record or
afterward. The payment line must have the same currency as the parent payment.

A payment line has an amount, which represents the total amount taken from the payment, and balance, which represents the remaining
amount after the payment line has been applied to an invoice. A payment’s amount can’t be less than the sum of all of its payment line
amounts.

One payment can have multiple payment lines. A payment line must be related to only payment.

You can create multiple payment lines on a payment apply each line to different invoices on the same account, or to invoices on different
accounts.

Here’s one way you could use Salesforce API to apply a payment to an invoice using a payment line.
