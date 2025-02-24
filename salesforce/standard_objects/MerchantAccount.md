#### MerchantAccount

A type of bank account that lets a merchant accept payments from a variety of payment methods, including credit or debit cards, or
digital wallets. A Salesforce Payments merchant account is linked to an underlying payment gateway to process payments This object
is available in API version 56.0 and later.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), undelete(), update(), upsert()

 Special Access Rules

```
To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.


-----

##### Fields

**Field**
```
AccountDescription
CountryIsoCode
CurrencyIsoCode
LastReferencedDate
LastViewedDate
Mode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Information about the merchant account.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Country where the legal entity representing the account is.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the organization. Available only for
organizations with multi-currency enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user can have accessed this record or list view but not viewed it.

**Type**
picklist


-----

```
Name
OwnerId
PaymentStatus

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The operational mode of the merchant account. This field determines the account’s ability
to accept payments. For production, the account must be in Live mode.

Possible values are:

**•** `Connected– Merchant account is active but it can’t accept payments. This option is`
only valid in production orgs.

**•** `Live– Merchant account is active and can accept payments. This option is only valid`
in production orgs.

**•** `Test` –Merchant account is active but not able to accept payments. This option is only
valid in sandbox orgs, and the account can accept only test transactions.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the merchant account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Name of the individual or group assigned to the merchant account.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Merchant account is active and can accept payments.

Possible values are:


-----

```
PayoutStatus
Status

```


**•** `Disabled`

**•** `Enabled`

The default value is `Disabled.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Money can be moved from the payment provider account to the designated merchant
account.

Possible values are:

**•** `Disabled`

**•** `Enabled`

The default value is `Disabled.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the state of the merchant account.

Possible values are:

**•** `Active`  - The merchant account can accept payments.

**•** `Complete`  - `PaymentStatus` and `DepositStatus` are enabled and all the
required information is provided.

**•** `Enabled`  - PaymentStatus and PayoutStatus are enabled, but the payment
provider requires more information later. If the merchant doesn't provide the information,
then the account becomes restricted. The time limit that the merchant has to provide
the information is longer than the `RestrictedSoon` state.

**•** `Pending`  - The merchant account exists but it can’t accept payments. This option
maintains backward compatibility for accounts that were created with API version 55.0
and earlier.

**•** `Rejected`  - The account is rejected and an explanation is provided.

**•** `Restricted`  - PaymentStatus, PayoutStatus, or both are disabled, so the
merchant account’s operation is limited.

**•** `Restricted Soon`  - PaymentStatus and PayoutStatus are enabled, but
the payment provider requires more information. If the merchant doesn't provide the
information in a specific time period, then the account becomes restricted.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MerchantAccountChangeEvent (API version 62.0)**
Change events are available for the object.

**MerchantAccountFeed**

Feed tracking is available for the object.

**MerchantAccountHistory**

History is available for tracked fields of the object.

**MerchantAccountOwnerSharingRule**

Sharing rules are available for the object.

**MerchantAccountShare**

Sharing is available for the object.
