#### PaymentGatewayLog

Stores information exchanged between the Salesforce payments platform and external payment gateways. Gateway logs can also record
payloads from external payment entities. This object is available in API version 48.0 and later.

Deleting or archiving a payment gateway log doesn’t impact financial data on other payment entities.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
GatewayAuthCode
GatewayAVSCode
GatewayDate
GatewayMessage
GatewayRefNumber
GatewayResultCode

```

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Authorization approval code from the gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Code sent by gateways that use an address verification system.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that of the gateway communication that leads to the creation of this
gateway log.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information or error messages sent from the gateway.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID created by the payment gateway.

**Type**
string


-----

```
GatewayResultCodeDescription
InteractionStatus
InteractionType

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Gateway-specific result code. Must be mapped to a Salesforce-specific result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the gateway’s result code. This field is useful for providing more information
around why the gateway returned a certain result code.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes the result of communication between the payments platform and a payment
gateway.

Possible values are:

**•** `Failed`

**•** `Initiated`

**•** `NoOp`

**•** `Success`

**•** `Timeout`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the type of interaction with the gateway. This field is required for logs created in
Salesforce.

Possible values are:

**•** `Authorization`

**•** `AuthorizationReversal`

**•** `Avs`

**•** `Capture`

**•** `CheckGiftCardBalance`


-----

```
IsNotification
LastReferencedDate
LastViewedDate
OrderPaymentSummaryId

```


**•** `PostAuth`

**•** `ReferencedRefund`

**•** `Sale`

**•** `Tokenize`

**•** `Void`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
For asynchronous transactions, shows whether the gateway log belongs to the notification
(yes) or the initial transaction (no).

Possible values are:

**•** `No`

**•** `Yes`

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
Order payment summaries show the balances of each authorization, capture, and refund
made against an order.


-----

```
PaymentGatewayId
PaymentGatewayLogNumber
ReferencedEntityId
Request

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Payments Platform payment gateway record used for communication with the external
payment gateway.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated unique ID for this payment gateway log record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Foreign key with DomainSet of PaymentAuth and Payment.

This field is a polymorphic relationship field.

**Relationship Name**
ReferencedEntity

**Relationship Type**
Lookup

**Refers To**
CardPaymentMethod, Payment, PaymentAuthAdjustment, PaymentAuthorization, Refund

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
Response
SfRefNumber
SfResultCode

```

**Description**
Raw payload. No sensitive attributes are stored.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Raw payload.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If an IdempotencyKey was passed in the API request, its value is stored here in text format.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline: The gateway call failed. If the transaction is attempted again, it can still work.`
For example, the customer has insufficient funds or briefly lost their connection.

**•** `Indeterminate: The gateway didn’t respond to the call. This response usually`
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail: The gateway call failed and can’t work. Gateway calls fail`
permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview: The customer bank requires more information before completing`
the payment.

**•** `Success: The gateway call succeeded.`

**•** `SystemError: Salesforce ended the payment request before receiving a response.`
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.


-----

**•** `ValidationError: Customer payment data was incorrect, such as a misspelling in`
the credit card address or an incorrect CVV.
