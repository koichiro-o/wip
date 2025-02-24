#### PaymentLink

A link that a merchant can share with customers to collect payments for products and services. The payment link, which you can embed
into a Salesforce app or send directly to a customer, directs the customer to a Pay Now payment page. The page can show a total amount
owed or an itemized list or products, shipping and tax charges, and a total amount owed. The customer enters their contact and payment
details, and submits their payment. The amounts are shown in the store's currency. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

##### Fields

```
AccountId
Amount
CartId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payer account.

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
Create, Filter, Sort, Update

**Description**
Amount the payer owes.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the cart record.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
Webcart


-----

```
CurrencyIsoCode
Description
Expiry Time
LastReferencedDate
LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
3-digit ISO code for the payment currency that is shown on the Pay Now page. Possible
values are:

**•** EUR – Euro

**•** GBP – British Pound

**•** USD – US Dollar

The default value is `USD.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text on the Pay Now payment page that’s visible to your customers. This text can
communicate any information you want.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the payment link expires. The time is based on the user’s time zone,
not the org’s time zone.

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
OwnerId
PaymentInitiationSource
PaymentLinkNumber
PaymentMethodSetId

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record can be referenced and not viewed directly.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this record.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The origin of the payment, based on the information in the Payment Link record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number that identifies the payment link.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the PaymentMethodSet object, which determines what payment methods are
shown to the payer.

This field is a relationship field.

**Relationship Name**
PaymentMethodSet


-----

```
PaymentUrl
QrCodeImageId
Status
TaxAmount

```

**Relationship Type**
Lookup

**Refers To**
MerchAccPaymentMethodSet

**Type**
url

**Properties**
Filter, Group, Sort

**Description**
Unique URL of the Pay Now page. This URL IS auto-generated, and not editable.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference to the QR code image included in the payment link record.

This field is a relationship field.

**Relationship Name**
QrCodeImage

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the payment link is active and can be used.

Possible values are:

**•** `Active`

**•** `Disabled`

The default value is `Active.`

**Type**
currency


-----

```
Title
Type
UsageType

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of the tax for the purchase. This amount is shown on the Pay Now page.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the Pay Now page, indicating what is being paid.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of payment link created, which the merchant can share with the customer
to receive payment. The payment link also determines which Pay Now page is generated
and what’s included on that page.

Possible values are:

**•** `CheckoutWithOrder` (only for orgs with Payments and Commerce)—includes the
amount owed based on the products you select, lists the products purchased, and
calculates tax using the billing address and selected shipping options. After a customer
makes a payment, this link type creates an order record.

**•** `PredefinedAmount—shows only an amount due for products purchased. The`
merchant enters the amount due when creating the payment link.

**•** `WithProducts—Deprecated. New payment links can't be created with this link type.`

The default value is `PredefinedAmount.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Determines whether the payment link is used one time or multiple times before the
configured expiration date and time.

Possible values are:

**•** `MultiUse`

**•** `SingleUse`

The default value is `MultiUse.`


-----

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**PaymentLinkOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PaymentLinkShare on page 66**
Sharing is available for the object.
