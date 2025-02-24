#### PaymentMethod

Represents the method that a buyer uses to compensate the seller of a good or service. Common payment methods include cash, checks,
credit or debit cards, money orders, bank transfers, and online payment services. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

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
Filter, Group, Nillable, Sort

**Description**
The account entity linked to this payment method.

This field is a relationship field.

**Relationship Name**
Account


-----

```
Comments
CompanyName
ImplementorType
IsAutoPayEnabled
Name

```

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
textarea

**Properties**
Nillable

**Description**
Users can add comments to provide additional details about a record. Maximum of 1000
characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Company name for this payment method. Part of the payment method’s address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Shows the type of payment method.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Payment Method page layout in the UI. It isn't automatically added.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
NickName
PaymentMethodAddress
PaymentMethodCity
PaymentMethodCountry
PaymentMethodDetails

```

**Description**
A unique number assigned to the payment method. Numbers start at 1000 and are read
only, but administrators can change the format.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User-defined nickname for this payment method.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Full address related to the alternative payment method. For more information about address
fields, see Address Compound Fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional information about the payment method type. This field is available in API version
57.0 and later.


-----

```
PaymentMethodGeocodeAccuracy
PaymentMethodLatitude
PaymentMethodLongitude
PaymentMethodPostalCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

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
Filter, Nillable, Sort

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Longitude of the payment method address. Used with the PaymentMethodLatitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
string


-----

```
PaymentMethodState
PaymentMethodStreet
PaymentMethodSubType
PaymentMethodType
SavedPaymentMethodId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Part of the address for this payment method.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Payment method address details.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be a digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The payment method used for the transaction, such as Visa, Mastercard, EPS, SepaDebit,
UnionPay, and Klarna. Method types can also be direct debit payments like ACH, Becs, and
BACS. This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record.


-----

```
Status

```

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
The state of the payment method.

Possible values are:

**•** `Active—The Payments platform can use the payment method to make payments.`

**•** `Canceled—The Payments platform can no longer use the payment method to make`
payments.

**•** `InActive—The Payments platform currently can’t use the payment method to make`
payments. Admins can change this value to Active when needed.

