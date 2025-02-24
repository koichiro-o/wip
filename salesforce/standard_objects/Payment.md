#### Payment

Represents a single event when a shopper makes a payment. For credit cards, this event is a payment capture or payment sale, but it
doesn't appear on the shopper's credit card statement. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```
Note: You can edit or delete a payment only in draft state, which you specify with the Status field.

##### Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account of the customer who made the payment.

This field is a relationship field.


-----

```
Amount
Balance
CancellationDate
CancellationEffectiveDate
CancellationGatewayDate

```

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The amount to be debited or captured.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount – the net applied amount.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the payment was voided.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the cancellation of this payment takes effect.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gateway provides this date following a successful cancellation request.


-----

```
CancellationGatewayRefNumber
CancellationGatewayResultCode
CancellationSfResultCode
ClientContext
Comments
CurrencyIsoCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
System-provided unique transaction ID from the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A Salesforce result code that can be mapped to one or more gateway result codes. We
recommend that the payment gateway adapter layer maps gateway-specific codes to the
Salesforce result code.

**Type**
textarea

**Properties**
Nillable

**Description**
Contains caller context for payment APIs. Useful for re-establishing context during an
asynchronous payment transaction.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can provide additional details about the payment record. Supports a maximum of
1000 characters.

**Type**
picklist


-----

```
Date
EffectiveDate
Email
GatewayDate
GatewayRefDetails

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment group record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when this payment record was created.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that this payment takes effect.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the user who initiated the payment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gateway provides this date for reference following a successful gateway communication.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional data that can’t be stored in other fields on the payment record. You can use this
field for transactions following the initial transaction that creates the payment record. You
can use any data that isn’t normalized in financial entities. This field has a maximum length
of 1000 characters and can store data as JSON or XML.


-----

```
GatewayRefNumber
GatewayResultCode
GatewayResultCodeDescription
ImpactAmount
IpAddress
LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID created by the payment gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code that must map to a Salesforce-specific result code. One Salesforce
result code can map to multiple gateway result codes.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the gateway’s result code.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shows the payment’s financial impact against the customer’s accounts receivable. If the
payment is valid, this value is the negative of the payment amount. If the payment is voided,
this value is 0.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the user who initiated the payment.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
MacAddress
NetApplied
NetRefundApplied
OrderPaymentSummaryId
PaymentAuthorizationId

```

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record is possibly referenced (LastReferencedDate) but not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the person who initiated the payment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total payment amount of that has been applied, including adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total refund amount that has been applied to the payment, including adjustments.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summaries show the balances of each authorization, capture, and refund
made against an order.

**Type**
reference


-----

```
PaymentGatewayId
PaymentGroupId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The authorization record for this payment. If there's a delayed capture (when the capture
occurs after the authorization), all captures must be made against a previously successful
authorization transaction.

This field is a relationship field.

**Relationship Name**
PaymentAuthorization

**Relationship Type**
Lookup

**Refers To**
PaymentAuthorization

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment gateway that processed the payment. If there’s a delayed payment, the
field is populated from the authorization record.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment groups organize all the payment transactions that have been made against a record
such as an account or contract. If there’s a delayed payment, the field is populated from the
authorization record.

This field is a relationship field.

**Relationship Name**
PaymentGroup


-----

```
PaymentIntentGuid
PaymentIntentID
PaymentMethodId

```

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
Unique ID of the payment sent to Stripe or PayPal. Links the Payments Merchant Account
record with the payment at the payment provider.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment intent record.

This field is a relationship field.

**Relationship Name**
PaymentIntent

**Relationship Type**
Lookup

**Refers To**
PaymentIntent

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The payment method that the customer used to provide this payment information.

This field is a relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod


-----

```
PaymentNumber
Phone
ProcessingMode
SfResultCode

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-created unique ID for this payment record.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the customer who initiated the payment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the payment has been made outside of the payment platform.

Possible values are:

**•** `External: Transactions happened outside of the Salesforce payments platform.`

**•** `Salesforce: Salesforce made and recorded an external call to the payment gateway.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline: The gateway call failed, but if the problem is fixed and the transaction is`
retried, it can work. For example, the customer had insufficient funds or briefly lost their
connection.

**•** `Indeterminate: The gateway didn’t respond to the call. This response usually`
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail: The gateway call failed. If tried again, it still doesn't work. Gateway`
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.


-----

```
Status
TotalApplied
TotalRefundApplied

```

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview: The customer bank requires more information before completing`
the payment.

**•** `Success: The gateway call succeeded.`

**•** `SystemError: Salesforce ended the payment request before receiving a response.`
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError: Customer payment data was incorrect, such as a misspelling in`
the credit card address or an incorrect CVV.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of this payment.

Possible values are:

**•** `Canceled: This payment has been unapplied from its target and can no longer be`
allocated.

**•** `Draft: The payment can be edited before posting it and allocating it to a target. The`
payment can also be deleted.

**•** `Processed: This payment has been finalized and can be allocated against a target.`

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of this payment’s balance that has been applied against an invoice.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of a refund that has been applied against this payment.


-----

```
TotalRefundUnapplied
TotalUnapplied
Type

```
SEE ALSO:

OrderPaymentSummary


**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of a previously applied refund that has since been unapplied from this
payment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of this payment that was previously applied and then unapplied.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how the customer used this payment.

Possible values are:

**•** `Capture`

**•** `Sale`

