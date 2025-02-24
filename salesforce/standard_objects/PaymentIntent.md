#### PaymentIntent

```

**Description**
The web store record that initiated the payment. For example, a B2B, D2C, or Pay Now store.

This field is a relationship field.

**Relationship Name**
WebStore

**Refers To**
WebStore

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The work order record that submitted the payment. This field is available only for the Field
Service application.

This field is a relationship field.

**Relationship Name**
WorkOrder

**Refers To**
WorkOrder

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The work order line item record that made the payment. This field is only available with the
Field Service application.

This field is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Refers To**
WorkOrderLineItem


Represents data temporarily stored during a transaction’s lifecycle that can identify the buyer, the merchant, and the amount the buyer
is sending to the merchant. Data such as timestamp and amount returned can also be stored in PaymentIntent. This object is available
in API version 58.0 and later.


-----

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

##### Fields

```
AccountId
AmountCapturable
AmountRefundable
AuthorizationReversal
Amount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account record of the buyer.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Payment amount that a merchant can collect after the fulfillment of an order.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the payment that the merchant can refund.

**Type**
currency


-----

```
AuthorizedAmount
BillingAddress
BillingCity
BillingCountry
BillingCountryCode

```

**Properties**
Filter, Nillable, Sort

**Description**
Amount canceled before completing the transfer of funds from buyer to merchant.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount authorized by the payer’s bank.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The billing address of the account holder. This field is the compound form of the billing
address. Read-only. For details on compound address fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the billing address.


-----

```
BillingGeocodeAccuracy
BillingLatitude
BillingLongitude
BillingPostalCode
BillingState
BillingStreet

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the billing address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
Compound Field Considerations and Limitations for details on geolocation compound fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. Maximum size is 80 characters.

**Type**
textarea


-----

```
CapturedAmount
ContextData
CurrencyIsoCode
DisputeEvidenceDueDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount that a merchant secured from a buyer.

**Type**
string

**Properties**
Nillable

**Description**
Additional metadata or information about a payment, such as the source of the payment,
user data, or any other relevant information that can help in processing or tracking the
payment.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code for any currency allowed by the organization. Available only for orgs with the
multicurrency feature enabled.

Possible values are:

**•** `Euro`

**•** `USD`

The default is USD.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date by which the merchant must submit information related to the dispute.


-----

```
DisputeFee
DisputeStatus
DisputedAmount
EntryMode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that the credit card company charges the merchant for each disputed payment.
The fee is also known as a chargeback fee.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the disputed transaction.

Possible values are:

**•** `Closed—The dispute inquiry is closed.`

**•** `Created—The payment gateway opens a payment dispute.`

**•** `Lost—The bank ruled in the account owner’s favor and refunded the charge. The`
refund is permanent and the dispute fee isn’t returned.

**•** `Won—The bank ruled in the merchant's favor. The issuing bank returns the debited`
chargeback amount to the payment gateway, who passes this amount back to the
merchant.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount the customer is challenging.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how the payment information was provided.

Possible values are:

**•** `Flow—Salesforce flow that initiated the payment.`

**•** `Merchant—The credit card isn’t available so the merchant entered the payment`
information via the phone or an email.

**•** `Payer_Online—The payer entered their payment information online.`


-----

```
Guid
IncurrenceStatus
IntentAmount
IsCaptureComplete

```


**•** `TapToPay—The card was available and the payer tapped that card or device on the`
payment terminal.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique ID of the payment sent to Stripe or PayPal. This ID links the Payments Merchant
Account record with the payment at the payment provider.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of an orphaned payment. An orphaned payment occurs when a payment transaction
is complete, but the workflow is disrupted, and the payment isn't recorded in the consuming
flow. An unexpected error can cause an orphaned payment. For example, a payment is
accepted at checkout, but the order doesn't get placed because of a network issue.

Possible values are:

**•** `Canceled—The workflow was disrupted and the payment was canceled or refunded.`

**•** `Claimed—The payment was recorded and the workflow was completed.`

**•** `Pending—The consuming workflow hasn't recorded the payment yet.`

If there isn't a value for this field, it means that the consumer doesn't rely on it to track
orphaned payments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount that a merchant expects to receive from a buyer.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Verification whether the funds for a given payment are paid.

The default value is `false.`


-----

```
IsEvidenceSubmitted
LastReferencedDate
LastViewedDate
MerchantAccountId
PaymentGatewayId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Status of the requested information that the merchant provides to the bank about the dispute.

The default value is `false.`

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
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced but not viewed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required field. The merchant account record associated with a payment intent record.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
PaymentInitiationSourceId
PaymentIntentNumber
PaymentLinkGmvDate
PaymentLinkId

```

**Description**
The payment gateway record that processed the payment.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment initiation source record associated with the payment. The record identifies the
originating application and object of the payment.

**Relationship Name**
PaymentInitiationSource

**Relationship Type**
Lookup

**Refers To**
PaymentInitiaionSource

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated number assigned to the payment record, for example `PI-000000001.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Date the payment is captured from a payment link transaction. The total amount paid is
expressed as the Gross Merchandise Value (GMV).

**Type**
reference


-----

```
PaymentMethodDetails
PaymentMethodId
PaymentMethodSubType

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment link record.

This field is a relationship field.

**Relationship Name**
PaymentLink

**Relationship Type**
Lookup

**Refers To**
PaymentLink

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional information about the payment method type such as the four last digits of a card
number.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The payment method record, indicating a card payment method, digital wallet, or alternative
payment method.

This field is a polymorphic relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
PaymentMethod

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
PaymentMethodType
ProviderReference
RefundedAmount
ShippingAddress
ShippingCity

```

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of payment method types such as Apple
Pay and Google Pay.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment method used for the transaction.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A payment record at the payment gateway that identifies the payment provider.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total or partial amount refunded to the buyer due to product return, merchant’s lack of
inventory, or shipping and delivering problems.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Delivery address for the purchase. The compound form of the shipping address. Read-only.
See Address Compound Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. City maximum size is 40 characters.


-----

```
ShippingCountry
ShippingCountryCode
ShippingGeocodeAccuracy
ShippingLatitude
ShippingLongitude
ShippingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. Country maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the shipping address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with ShippingLongitude to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. For
details on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
string


-----

```
ShippingState
ShippingStreet
Status
SubmittedById

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The maximum size of the postal code is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. State maximum size is 80 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. Maximum of 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the payment record.

Possible values are:

**•** `Authorized`

**•** `Canceled`

**•** `Created`

**•** `Expired`

**•** `Failed`

**•** `PartiallyCaptured`

**•** `PartiallyRefunded`

**•** `Pending`

**•** `Refunded`

**•** `Succeeded`

**Type**
reference


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
The submitted by record, which identifies who processes the payment on the customer's
behalf. The customer provides the authorization to submit the payment over the phone or
through the mail.

This field is a relationship field.

**Relationship Name**
SubmittedBy

**Relationship Type**
Lookup

**Refers To**
User
