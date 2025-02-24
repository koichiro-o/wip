#### CreditMemoInvApplication

Represents an amount applied from a credit memo to an invoice. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update()

 Special Access Rules

```
This object is available when Subscription Management is enabled.


-----

##### Fields

**Field**
```
Amount
AppliedDate
AssociatedLineId
CreditMemoBalance

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of the credit memo that was applied to or unapplied from the invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the credit memo was applied. If the credit memo invoice application's type
is Unapplied, this value is inherited from the Applied date of the credit memo referenced
in the AssociatedLineId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
For a credit memo invoice application that represents an unapplied credit memo, this field
shows the original credit memo invoice application.

This field is a relationship field.

**Relationship Name**
AssociatedLine

**Relationship Type**
Lookup

**Refers To**
CreditMemoInvApplication

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The balance of a credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.


-----

```
CreditMemoId
CreditMemoInvoiceNumber
Date
Description
EffectiveDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The credit memo that was applied or unapplied.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the invoice to which a credit memo is applied.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the credit memo amount was applied to the invoice.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit applied to an invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
HasBeenUnapplied
ImpactAmount
InvoiceBalance
InvoiceId

```

**Description**
The effective date of the application or unapplication of credit. Users can provide this value
when applying or unapplying the credit memo. This field is optional and provided only for
reporting purposes. It doesn't affect the credit memo invoice application's other fields.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows whether this credit memo application has been unapplied from the target invoice.

Possible values are:

**•** `NA`

**•** `No`

**•** `Yes`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The net adjustment to the invoice's balance after a credit memo is applied or unapplied. If
a credit memo was applied, this value is the negative version of the credit memo invoice
application's `Amount. If a credit memo was unapplied, this value is the positive version of`
the credit memo invoice application's `Amount.`

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The balance of the credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the invoice to which credit is applied.


-----

```
Type
UnappliedDate

##### Associated Objects

```

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the credit memo line application was generated because of an apply
action (application) or an unapply action (unapplication).

Possible values are:

**•** `Applied`

**•** `Unapplied`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when this application was unapplied from the target invoice.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoInvApplicationFeed on page 54**
Feed tracking is available for the object.

**CreditMemoInvApplicationHistory on page 62**
History is available for tracked fields of the object.
