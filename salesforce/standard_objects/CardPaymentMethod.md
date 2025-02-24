#### CardPaymentMethod

Represents a credit card or debit card payment method, which implements the PaymentMethod object. This object is available in API
version 48.0 and later.

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
AccountId
AuditEmail

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customer account for the payment method.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
AutoCardType
CardBin
CardCategory
CardHolderFirstName
CardHolderLastName

```

**Description**
Email address of the card owner where audit information about payments gets sent.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for orgs that
upgraded from v48.0. Users must add it to the CardPaymentMethod page layout on their
own.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Card network type, derived from the card number.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
First six digits of the card number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines whether the card is a credit card or debit card.

Possible values are:

**•** `CreditCard`

**•** `DebitCard`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the cardholder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
CardHolderName
CardLastFour
CardPaymentMethodNumber
CardType
CardTypeCategory

```

**Description**
Last name of the cardholder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Full name of the cardholder.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Last four digits of the credit card or debit card.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for the card payment method.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Identifies the credit card type.

Possible values are:

**•** `American Express`

**•** `Diners Club`

**•** `JCB`

**•** `Maestro`

**•** `Master Card`

**•** `Visa`

**Type**
picklist


-----

```
Comments
CompanyName
DisplayCardNumber
Email

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Further identifies the credit card. Used for internal reference.

Possible values are:

**•** `AmericanExpress`

**•** `DinersClub`

**•** `Discover`

**•** `Jcb`

**•** `Maestro`

**•** `MasterCard`

**•** `UnionPay`

**•** `Visa`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Payment admin can add comments to provide additional details about a record. Maximum
of 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company of the cardholder.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Masked digits for the full credit card number except the last four digits.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ExpiryMonth
ExpiryYear
GatewayDate
GatewayResultCode
GatewayResultCodeDescription
GatewayToken

```

**Description**
Email address of the payer.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The card’s expiration month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The card’s expiration year.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the payment gateway logs a card activity.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The result of the card payment method’s interaction with the payment gateway during a
transaction request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the gateway result code. Descriptions vary between payment
gateway providers.

**Type**
string


-----

```
GatewayTokenDetails
GatewayTokenEncrypted
InputCardNumber
IpAddress

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the card
payment method during transactions. GatewayToken is for use with APIs earlier than
version 52.0. For version 53.0 and latter, use the GatewayTokenEncrypted field. To secure
the token, use the GatewayTokenEncrypted field.

An error message appears if you try to record a `GatewayToken` for a card payment
method that already has a GatewayToken or GatewayTokenEncrypted value.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional information about the gateway token.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
Encrypted unique token ID generated by the payment gateway to represent the card payment
method during transactions. Encrypted using Salesforce Classic Encryption.

Available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Used by a payer to enter a credit card number when storing an external-type card payment
method. After entry, the credit card number isn’t saved, so the InputCardNumber value
always appears blank. The credit card number appears as a masked value in
```
  DisplayCardNumber, which shows only the last four digits.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
IP address of the card payment method holder.


-----

```
IsAutoPayEnabled
LastReferencedDate
LastViewedDate
MacAddress

```

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is `False.`

This field is available in API version 55.0 and later. For orgs that upgraded from version 54.0,
you must add this field to the Card Payment Method page layout in the UI. It isn't automatically
added.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record or list view related to this
record, but didn’t access it directly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user referenced this record but didn’t view it directly.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
MAC address of the card payment method holder.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.


-----

```
NickName
PaymentGatewayId
PaymentMethodAddress
PaymentMethodCity
PaymentMethodCountry

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payer-defined nickname for the card payment method.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The payment gateway used to create a gateway token. For transactions with a saved payment
method in Salesforce, this field stores the payment gateway ID used in the transaction.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
address

**Properties**
Filter, Nillable

**Description**
Full address associated with the card payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
PaymentMethodDetails
PaymentMethodGeocodeAccuracy
PaymentMethodLatitude

```

**Description**
Country of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Optional information about the payment method type. This field is available in API version
57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the payment method address. An accuracy level contains
information about the location of a latitude and longitude. For more information about
geolocation fields, see Geolocation Compound Field.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.


-----

```
PaymentMethodLongitude
PaymentMethodPostalCode
PaymentMethodState
PaymentMethodStreet
PaymentMethodSubType
PaymentMethodType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLatitude to specify
the precise geolocation of the address. For details on geolocation compound fields, see
Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State of the address for the payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of payment method types such as Apple
Pay and Google Pay. This field is available in API version 57.0 and later.

**Type**
picklist


-----

```
Phone
ProcessingMode

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction. This field is available in API version 57.0 and later.

Possible values are:

**•** `AfterpayClearpay`

**•** `AmericanExpress`

**•** `ApplePay`

**•** `BanContact`

**•** `DinersClub`

**•** `Discover`

**•** `EPS`

**•** `GooglePay`

**•** `Jcb`

**•** `Klarna`

**•** `Maestro`

**•** `MasterCard`

**•** `Other`

**•** `PayPal`

**•** `SepaDebit`

**•** `UnionPay`

**•** `Venmo`

**•** `Visa`

**•** `iDeal`

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the payer.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


-----

```
SavedPaymentMethodId
SfResultCode

```

**Description**
Defines whether the card payment method is used for transactions made by Salesforce
Payments or by an external third-party payment provider.

Possible values are:

**•** `External—Transactions happened outside of the Salesforce payments platform.`

**•** `Salesforce—Salesforce made and recorded an external call to the payment platform.`

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

You must enter a value for this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record. This field is available in API version 60.0 and
later.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The results of the card payment method’s interaction with the payment gateway.

Possible values are:

**•** `Decline`

**•** `Indeterminate`

**•** `PermanentFail`

**•** `RequiresReview`

**•** `Success`

**•** `SystemError`

**•** `ValidationError`


-----

```
StartMonth
StartYear
Status

##### Usage

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The month is activated.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The year the card is activated.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the payment method.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `InActive`


The following fields drop zeroes that appear at the beginning of the field value, and introduce commas for values with four or more
digits:

**•** `CardLastFour`

**•** `CardBin`

**•** `ExpiryYear`

For example, a CardLastFour entered value of 0004112233445566 would appear as 4,112,233,445,566 on the record.

As a workaround, create a String-type custom formula field with the same label as the field that you want to replace, then hide the
original field. Here are some examples for replacing `CardLastFour,` `CardBin, and ExpiryYear.`

**CardLastFour**
```
  IF(ISBLANK(CardLastFour), NULL,RIGHT("0000" & TEXT(CardLastFour), 4))

```
**CardBin**
```
  IF(ISBLANK(CardBin), NULL,RIGHT("000000" & TEXT(CardBin), 6))

```

-----

**ExpiryYear**
```
  IF(ISBLANK(ExpiryYear), NULL,TEXT(ExpiryYear)))
