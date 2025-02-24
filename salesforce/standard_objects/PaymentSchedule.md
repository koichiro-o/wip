#### PaymentSchedule

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the unit of time for the payment period. Used with the `Period` field.

For example, to define a payment term of Net 30, enter `30` as the `Period` and select
`Days` as the `PeriodUnit.`

Possible values are:

**•** `Days`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies how the payment term and invoice due date are derived.

Possible values are:

**•** `Period-Based—Tells the system to use the` `Period` and `PeriodUnit` fields
to calculate the invoice due date.

The default value is `Period-Based.`


The payment schedule represents a collection of payments that a customer wants to collect at different times for a certain record. A
schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each of a schedule’s
items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts. When a
payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for payment processing
if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Subscription Management.


-----

##### Fields

**Field**
```
AvailableRequestedAmount
Comments
CurrencyIsoCode
DefaultPaymentAccountId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The payment schedule’s remaining amount available for the creation of payment schedule
items. Equals `TotalRequestedAmount–TotalLineRequestedAmount.`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined comments.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment group record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When a payment run creates payments from a payment schedule item, it sets the payment’s
account to the item’s PaymentAccountId. Upon payment schedule item creation, the
item’s PaymentAccountId inherits the schedule’s DefaultPaymentAccountId.
However, you can override the PaymentAccountId with a different account as needed.
If you do, future payments made from the item use the new account.

This is a relationship field.

**Relationship Name**
DefaultPaymentAccount

**Relationship Type**
Lookup

**Refers To**
Account


-----

```
DefaultPaymentMethodId
LastReferencedDate
LastViewedDate
OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When a payment run creates payments from a payment schedule ID, it sets the payment’s
account to the item’s `PaymentMethodId. Upon payment schedule item creation, the`
item’s `PaymentMethoId` inherits the schedule’s `DefaultPaymentMethodId.`
However, you can override the `PaymentMethodId with a different account as needed.`
If you do, future payments made from the item will use the new account.

**Relationship Name**
DefaultPaymentMethod

**Relationship Type**
Lookup

**Refers To**
CardPaymentMethod, DigitalWallet

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
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who created the payment schedule.

This is a polymorphic relationship field.

**Relationship Name**
Owner


-----

```
PaymentScheduleNumber
ReferenceEntityId
RemainingAmountToBeProcessed
Status

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the payment schedule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The object that receives payments as a result of payment schedule items processed from
the payment schedule.

This is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Contract, Invoice, Order

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total pending amount of payment schedule items that haven’t yet been processed for
payment. Equals `TotalLineRequestedAmount` – `TotalProcessedAmount.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the payment schedule.


-----

```
TotalAppliedAmount
TotalCanceledAmount
TotalPaymentScheduleItemAmount
TotalProcessedAmount

```

Possible values are:

**•** `Canceled: Payment runs can’t evaluate payment schedules or use them to create`
payments.

**•** `Completed: All of the payment schedule’s payment schedule items have been`
processed for payments.

**•** `Draft: The payment schedule can be edited and configured. Payment runs don’t`
evaluate draft payment schedules.

**•** `Open: The payment schedule is available for payment run evaluation.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of all payment schedule items that have been applied to payments.

This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all `RequestedAmount` values on payment schedule items with a status of
Canceled.

**Type**
currency

**Properties**
Filter, Nillable, Sort\

**Description**
The total amount allocated from the payment schedule to its payment schedule items. Equals
the sum of each payment schedule item’s RequestedAmount – the sum of each payment
schedule item’s `Canceled Amount.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `ProcessedAmount` values on payment schedule items with a status of
Processed.


-----

```
TotalRequestedAmount

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The total amount available for a payment schedule to distribute to its payment schedule
items. The sum of payment schedule items can’t be greater than the
```
  TotalLineRequestedAmount of the parent payment schedule.

```
