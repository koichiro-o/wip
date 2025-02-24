#### PaymentScheduleItem

A payment schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each
of a schedule’s items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts.
When a payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for payment
processing if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Subscription Management.

##### Fields

```
Comments
CurrencyIsoCode

```

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


-----

```
LastPaymentGatewayLogId
LastReferencedDate
LastViewedDate
PaymentAccountId

```

**Description**
Three-letter ISO 4217 currency code associated with the payment schedule item record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most recent payment gateway log created following a payment gateway request to
make a payment based on the payment schedule item.

This is a relationship field.

**Relationship Name**
LastPaymentGatewayLog

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayLog

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account assigned to payments made from the payment schedule item. When a payment
schedule item is created, its `PaymentAccountId` inherits the payment schedule’s
```
  DefaultPaymentAccountId. However, you can provide a new

```

-----

```
PaymentBatchRunId
PaymentId
PaymentMethodId

```

`PaymentAccountId` at any time. If you change the `PaymentAccountId, only`
payments made after the change use the new account.

This is a relationship field.

**Relationship Name**
PaymentAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment batch run that evaluated the payment schedule item for payment processing.

This is a relationship field.

**Relationship Name**
PaymentBatchRun

**Relationship Type**
Lookup

**Refers To**
PaymentBatchRun

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment that a payment run created for the payment schedule item after picking up
the parent payment schedule. This field is unique within your organization

This is a relationship field.

**Relationship Name**
Payment

**Relationship Type**
Lookup

**Refers To**
Payment

**Type**
reference


-----

```
PaymentProcessingMessage
PaymentRunMatchingValue
PaymentScheduleId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment method assigned to payments created from the payment schedule item. When
a payment schedule item is created, its `PaymentMethodId` inherits the payment
schedule’s `DefaultPaymentMethodId. However, you can provide a new`
`PaymentMethodId` at any time. If you change the PaymentMethodId, only payments
made after the change use the new account.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
CardPaymentMethod, DigitalWallet

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Shows information about whether the payment creation process has completed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value used to match a payment schedule item to a payment run based on the payment
run’s matching criteria.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The parent payment schedule for the payment schedule item.

This is a relationship field.

**Relationship Name**
PaymentSchedule

**Relationship Type**
Lookup


-----

```
PaymentScheduleItemNumber
PaymentSource
ProcessedAmount
RequestedAmount
Status

```

**Refers To**
PaymentSchedule

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
User-defined reference number for the payment schedule item.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The feature that caused a payment to be created from the payment schedule item.

Possible values are:

**•** `PaymentRun`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the payment schedule item that has been processed for payment and
converted to a payment record.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The initial amount of the payment schedule item upon creation.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the payment schedule item.

Possible values are:


-----

```
TargetPaymentProcessingDate

```


**•** `Canceled: The payment schedule item can’t be picked up by payment runs for`
processing. When a user or process changes the item’s status to Canceled, the item’s
`CanceledAmount becomes` `RequestedAmount` – `ProcessedAmount.`

**•** `Apply Failed: The payment run encountered an error when attempting to process`
the payment schedule item for payment. For more information, review the payment
run’s revenue transaction error log.

**•** `Applied: The payment schedule item has been successfully applied.`

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date after picking up a payment schedule item that the payment run makes a payment
request to the payment gateway.

