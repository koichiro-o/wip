#### MerchAccPaymentMethodSet

Defines an ordered list of payment methods that are available to a merchant's cudstomer during checkout. You can configure multiple
payment method sets, each designated for a specific locale, payment region, or sale channel. This object is available in API version 58.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.


-----

##### Fields

**Field**
```
CurrencyIsoCode
DeveloperName
MerchantAccountId
PaymentMethodSetNumber
PaymentMethodSummary

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. The ISO code for
any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique name for the object given by the Payments admin.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Foreign key to the MerchantAccount.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-assigned ID for the `MerchAccPaymentMethodSet.`

**Type**
string


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
Summary field that is automatically populated with comma-separated values from
MerchAccPaymentMethodType.

This field is a calculated field.
