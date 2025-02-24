#### MerchAccPaymentMethodType

Refers to a payment method that is in a payment method set, which is defined by the `MerchAccPaymentMethodSet` object.
This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

##### Fields

```
CurrencyIsoCode
PaymentInstrumentType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only when the multicurrency feature is enabled. Contains the ISO code for any
currency used by the org.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of instrument the payer can pay with.

Possible values are:


-----

```
PaymentMethodSetId
PaymentMethodSetTypeNumber

```


**•** `us_bank_account - ACH_Debit`

**•** `affirm - Affirm`

**•** `afterpay - Afterpay`

**•** `afterpay_clearpay - Afterpay/Clearpay`

**•** `amazon_pay - Amazon Pay`

**•** `applepay - Apple Pay`

**•** `au_becs_debit - BECS_Debit`

**•** `bacs_debit - BACS_Debit`

**•** `bancontact - Bancontact`

**•** `card - Credit Cards`

**•** `cashapp - Cash App`

**•** `clearpay - Clearpay`

**•** `eps - EPS`

**•** `googlepay - Google Pay`

**•** `ideal - iDEAL`

**•** `klarna - Klarna`

**•** `link - Link`

**•** `paypal - PayPal`

**•** `sepa_debit - SEPA Debit`

**•** `venmo - Venmo`

**•** `wechat_pay - WeChat Pay`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the MerchAccPaymentMethodSet.

This field is a relationship field.

**Relationship Name**
PaymentMethodSet

**Relationship Type**
Lookup

**Refers To**
MerchAccPaymentMethodSet

**Type**
string


-----

```
SortOrder

##### Associated Objects

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-assigned ID for the MerchAccPaymentMethodSet.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sort order for the MechAccPaymentMethodType within the
MerchAccPaymentMethodSetExperience.


This object has these associated object. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**MerchAccPaymentMethodTypeHistory on page 62**
History is available for tracked fields of the object.
