#### RefundLinePayment

A refund line that has been applied to a payment. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated.

##### Fields

```
Amount

```

**Type**
currency

**Properties**
Create, Filter, Sort


-----

```
AppliedDate
AssociatedAccountId
AssociatedRefundLinePaymentId
Comments

```

**Description**
The total amount applied to or unapplied from a payment by the refund line.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that the refund was applied to the linked payment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The account for the payment that received the refund.

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
The refundLine that was unapplied. Populated only when RefundLinePayment’s Type has a
value of Unapplied.

This is a relationship field.

**Relationship Name**
AssociatedRefundLinePayment

**Relationship Type**
Lookup

**Refers To**
RefundLinePayment

**Type**
textarea


-----

```
Date
EffectiveDate
EffectiveImpactAmount
HasBeenUnapplied

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can add comments to provide additional information on the refund line payment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
By default, the day the refund line payment record was created. Users can also enter a different
date.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Defines the date and time when the refund line application or unapplication becomes
effective.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment refund line impacts a customer’s accounts receivable. This value
is positive when RefundLinePayment’s Type field is Applied, and negative when
RefundLinePayment’s Type is Unapplied. If there’s an unapplied line related to this record,
EffectiveImpactAmount has a value of 0.

Note: EffectiveImpactAmount evaluates only the applied and unapplied line pair.
Therefore, the effective impact amount could be different for different lines within
the same refund.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Shows whether this refund line has been unapplied.

Possible values are:


-----

```
ImpactAmount
PaymentBalance
PaymentId
RefundBalance

```


**•** `No`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows how this payment refund line impacts a customer’s accounts receivable. This value
is positive when RefundLinePayment’s Type field is Applied, and negative when
RefundLinePayment’s Type is Unapplied.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The payment record’s balance following the application or unapplication of this refund line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The payment record that this refund line targets. Refund applications and unapplications
are made against this payment.

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The refund record’s balance following the application or unapplication of this payment
refund line.


-----

```
RefundId
RefundLinePaymentNumber
Type
UnappliedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent refund of this refund line.

This is a relationship field.

**Relationship Name**
Refund

**Relationship Type**
Lookup

**Refers To**
Refund

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this refund line.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether this line represents a refund that’s been applied or unapplied from a payment.

Possible values are:

**•** `Applied`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date that this refund line was unapplied from a payment.


-----

##### Usage

When you’re ready to apply a refund’s balance to a payment, create a refund line (RefundLinePayment). The refund line represents
the balance taken from the payment and applied toward the invoice. You can apply a refund’s balance when you create the refund
record or afterward. The refund line must have the same currency as the parent refund.

A refund has an amount, which represents the total amount taken from the refund, and a balance, which represents the remaining
amount after the refund line has been applied to a payment. A refund’s amount can’t be less than the sum of all of its refund line amounts.
You can apply any portion of a refund’s balance to a payment.

You can apply a refund to transactions on the same account or to different transacations across different

accounts.
