#### PaymentAuthorization

Represents a single payment authorization event where users can capture or reverse a payment against a reserve of funds. This object
is available in API version 48.0 and later.

A common type of payment authorization occurs when a user sees a pending transaction against their credit card account.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```
Note: You can only delete a payment in draft state, which you specify in the Status field.

##### Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
AccountId
Amount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customer account.

This is a relationship field.

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
The amount authorized for the payment event.


-----

```
Balance
Comments
CurrencyIsoCode
Date
EffectiveDate
Email

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Authorized amount – total processed captured amount – total processed authorization
reversal amount. Balance can be positive or negative.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can enter comments to provide additional details about the authorization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the payment authorization record.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
By default, the day the authorization record was created. Users can also enter a different
date. Editable only when the payment authorization’s status is Draft.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the authorization takes effect. Editable only when the payment
authorization’s status is Draft.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ExpirationDate
GatewayAuthCode
GatewayDate
GatewayRefDetails
GatewayRefNumber

```

**Description**
Email address of the person who initiated the payment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Authorizations can’t be captured after their expiration dates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Authorization approval code from the payment gateway.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that of the gateway communication that leads to the successful payment
authorization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional data that can’t be stored in other fields on the payment record. You can use this
field for transactions following the initial transaction that creates the payment record. You
can use any data that isn’t normalized in financial entities. This field has a maximum length
of 1000 characters and can store data as JSON or XML.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique transaction ID from the payment gateway.


-----

```
GatewayResultCode
GatewayResultCodeDescription
IpAddress
LastReferencedDate
LastViewedDate
MacAddress

```

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
Description of the gateway’s result code. This field is useful for providing more information
around why the gateway returned a certain result code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the user who initiated the payment authorization.

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
record might only have been referenced `(LastReferencedDate)` and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
OrderPaymentSummaryId
PaymentAuthorizationNumber
PaymentGatewayId
PaymentGroupId

```

**Description**
The MAC address of the person who initiated the payment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order payment summaries show the balances of each authorization, capture, and refund
made against an order.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-provided unique ID for a payment authorization record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce payment gateway record that created this authorization. This gateway will
be used for subsequent captures.

This is a relationship field.

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
such as an account or contract. Populated from the authorization record if there is delayed
payment.


-----

```
PaymentIntentGuid
PaymentMethodId
Phone
ProcessingMode

```

This is a relationship field.

**Relationship Name**
PaymentGroup

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
The customer payment method provided during this authorization.

This is a relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the person who initiated the payment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


-----

```
SfResultCode
Status

```

**Description**
Defines whether the payment has been made outside of the payment platform.

Possible values are:

**•** `External—Transactions happened outside of the Salesforce payments platform.`

**•** `Salesforce—Salesforce made and recorded an external call to the payment gateway.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce-specific result code that can map to one or more gateway result codes. We
recommend configuring the payment gateway adapter layer to map gateway result codes
to the appropriate Salesforce result code.

Possible values are:

**•** `Decline—The gateway call failed, but it may still work if the transaction is attempted`
again. For example, the customer had insufficient funds or briefly lost their connection.

**•** `Indeterminate—The gateway didn’t respond to the call. This response usually`
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail—The gateway call failed and won’t work even if tried again. Gateway`
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.

**•** `RequiresReview—The customer bank requires more information before completing`
the payment.

**•** `Success—The gateway call succeeded.`

**•** `SystemError—Salesforce ended the payment request before receiving a response.`
For example, Salesforce lost credentials or access to its server. Salesforce ends payment
calls if it doesn’t receive a response from the gateway within two minutes.

**•** `ValidationError—Customer payment data was incorrect, such as a misspelling`
in the credit card address or an incorrect CVV.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of this payment.

Possible values are:


-----

```
TotalAuthReversalAmount
TotalPaymentCaptureAmount

```
SEE ALSO:

OrderPaymentSummary
