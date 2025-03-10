#### AlternativePaymentMethod

Represents a payment method that isn’t cash, a debit card, or a credit card. This object defines methods that aren’t defined by the
CardPaymentMethod or DigitalWallet objects. Examples of alternative payment methods include CashOnDeliver, Klarna, and Direct
Debit. `AlternativePaymentMethod` functions the same as any other type of payment method for processing transactions
through a payment gateway. This object is available in API version 51.0 and later.

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

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account for the alternative payment method.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup


-----

```
AlternativePaymentMethod
Number
AuditEmail
BankAccountHolderType
BankAccountType
BillingFirstName

```

**Refers To**
Account

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Salesforce ID number for the alternative payment method.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the payment owner where audit information about payments is sent.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines if the bank account is held by a business or an individual.

Possible values are:

**•** `Business`

**•** `Individual`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of bank account such as a checking or savings account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.


-----

```
BillingLastName
BillingName
Comments
CompanyName
Email
GatewayToken

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first and last name of the payment method owner, based on their billing address details.

This field is available in API version 58.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name for this payment method. Part of the payment method’s address.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the payment method holder.

**Type**
encryptedstring


-----

```
GatewayTokenDetails
IpAddress
IsAutoPayEnabled
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Nillable, Update

**Description**
Tokenized form of the alternative payment method, returned by the gateway. Stored as
encrypted text.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique tokenized ID generated by the payment gateway when this payment method first
interacts with the gateway. Used to identify the payment method during future transactions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
IP address for the payment method owner.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Alternative Payment Method page layout in the UI. It isn't automatically
added.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime


-----

```
MacAddress
NickName
OwnerId
PaymentGatewayId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mac Address of the payment method holder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined nickname for this payment method.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the alternative payment method.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the payment gateway entity used to handle transactions from this payment method.


-----

```
PaymentMethodAddress
PaymentMethodCity
PaymentMethodCountry
PaymentMethodDetails
PaymentMethodGeocode
Accuracy

```

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
Full address associated with the alternative payment method. For more information about
address fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment method address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payment method address details.

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


-----

```
PaymentMethodLatitude
PaymentMethodLongitude
PaymentMethodPostalCode

```

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
specify the precise geolocation of the address. For details about geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Longitude of the payment method address. Used with the PaymentMethodLatitude to
specify the precise geolocation of the address. For details about geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.


-----

```
PaymentMethodState
PaymentMethodStreet
PaymentMethodSubType
PaymentMethodType
Phone
ProcessingMode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the address for this payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be a digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction, such as Visa, Mastercard, EPS, SepaDebit, and
Klarna. This field is available in API version 57.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the payment method's owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


-----

```
SavedPaymentMethodId
StandardEntryClassCode
Status

```

**Description**
Indicates whether the payment method was created in Salesforce or externally. Required.

Possible values are:

**•** `External: Select this value if you create the alternative payment method record`
through any method other than the Salesforce Payments Connect API.

**•** `Salesforce: Select this value if you use Salesforce Payments Connect API to create`
the alternative payment method record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A three-letter code that indicates how a customer or a business initiated and authorized an
ACH payment.

Possible values are:

**•** `CCD—Corporate credit or debit entry`

**•** `PPD—Pre-arranged payment and deposit entry`

**•** `TEL—Telephone-initiated entry`

**•** `WEB—Internet or mobile-initiated entry`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the payment method. Required.


-----

Possible values are:

**•** `Active—The Payments platform can use the alternative payment method to make`
payments. Active alternative payment methods can't be deleted.

**•** `Canceled—The Payments platform can no longer use the payment method to make`
payments. A value of `Canceled` can't be changed back to Active or Inactive

**•** `InActive—The Payment platform currently can't use the payment method to make`
payments. Admins can change this value to `Active` or `Canceled` when needed.
