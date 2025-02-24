#### PaymentAuthAdjustment

Shows information about an adjustment made to an authorized transaction. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```
Note: You can only delete a payment in draft state, which you specify in the Status field.


-----

##### Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
AccountId
Amount
Comments
CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account for the payment authorization adjustment. Inherited from the payment
authorization.

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
Amount of adjustment applied to the parent payment authorization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
Date
EffectiveDate
Email
GatewayDate
GatewayRefDetails

```

**Description**
Three-letter ISO 4217 currency code associated with the payment authorization adjustment
record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the adjustment occurred.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the adjustment takes effect on the authorization.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the parent payment authorization owner.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the reversal transaction occurred in the payment gateway.

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
IpAddress
LastReferencedDate
LastViewedDate

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
Gateway-specific result code. Must be mapped to a Salesforce-specific result code

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
The IP address of the user who initiated the payment adjustment.

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


-----

```
MacAddress
PaymentAuthAdjustmentNumber
PaymentAuthorizationId
PaymentIntentId

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the person who initiated the payment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-provided unique ID for a payment authorization adjustment record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the payment authorization on which the adjustment occurred.

This is a relationship field.

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
ID of the payment intent record.

This field is a relationship field.

**Relationship Name**
PaymentIntent


-----

```
Phone
ProcessingMode
SfResultCode

```

**Relationship Type**
Lookup

**Refers To**
PaymentIntent

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the customer who initiated the authorization adjustment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

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

**•** `Decline—The gateway call failed, but it might work if the transaction is attempted`
again. For example, the customer had insufficient funds or briefly lost their connection.

**•** `Indeterminate—The gateway didn’t respond to the call. This response usually`
happens when Salesforce times out while waiting for a response from the gateway.

**•** `PermanentFail—The gateway call failed and won’t work even if tried again. Gateway`
calls fail permanently for one of two reasons:

**–** Hard Decline: The customer’s payment account has been closed or terminated.

**–** Fraud: The gateway recognized the payment or payment method as known fraud.


-----

```
Status
Type

```


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
Defines the state of the payment authorization reversal.

Possible values are:

**•** `Canceled—The payment authorization reversal has been canceled. The parent`
authorization has returned to its pre-reversal balance.

**•** `Draft: The payment authorization reversal can be edited before applying it against`
the parent authorization.

**•** `Pending: The payment authorization reversal is pending. This value is available in API`
version 61.0 and later.

**•** `Processed—The payment authorization reversal has been finalized.`

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how the customer used the reversal.

Possible value is:

**•** `Reversal`


-----
