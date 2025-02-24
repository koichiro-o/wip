#### PaymentGateway



**•** `Canceled—This payment has been unapplied from its target and can to longer be`
allocated.

**•** `Draft—The payment can be edited before posting it and allocating it to a target.`

**•** `Failed—Authorization for the payment failed.`

**•** `Pending—`

**•** `Processed—This payment has been finalized and can be allocated against a target.`

Users can manually change the Status field’s values as follows:

**•** Draft to Processed

**•** Processed to Canceled

**•** Draft to Canceled

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all processed authorization reversals against the payment authorization.

This is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all authorization captures related to this payment authorization.


Platform object that represents the connection to an external payment gateway. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
Comments
DefaultTapToPayLocation
ExternalReference
GatewayMode

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Admin-provided details about a record. Maximum of 1000 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Stores the locationId of the location record created at Stripe. The Field Service app uses the
location to process where tap-to-pay transactions are made.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Identifier of an external payment gateway. This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The operational mode of the payment gateway. This field determines the payment gateway’s
ability to accept payments. For production orgs, the gateway must be in Live mode.

Possible values are:

**•** `Connected– Payment gateway is active but it can’t accept payments. This option is`
only valid in production orgs.

**•** `Live– Payment gateway is active and can accept payments. This option is only valid`
in production orgs.


-----

```
LastReferencedDate
LastViewedDate
MerchantAccountId
MerchantCredentialId

```


**•** `Test` –Payment gateway is active but not able to accept payments. This option is only
valid in sandbox orgs, and the account can accept only test transactions.

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
The timestamp for when the current user last viewed this record. If this value is null, it's
possible this record is only referenced (LastReferencedDate) but not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the merchant account used by the payment gateway. This merchant account links to
a merchant account at a payment processor.

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
Create, Filter, Group, Sort, Update

**Description**
ID of the merchant credential setup entity to reference merchant information.

This field is a relationship field.


-----

```
PaymentGatewayName
PaymentProcessor
PaymentStatus
PayoutStatus

```

**Relationship Name**
MerchantCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Admin-defined name for the payment gateway.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of payment gateway provider.

Possible values are:

**•** `Paypal`

**•** `Stripe`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The payment gateway is active and can accept payments.

Possible values are:

**•** `Enabled`

**•** `Disabled`

The default value is Disabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
PaymentGatewayProviderId
ProviderAccount
Status

```

**Description**
Money can be moved from the payment provider account to the merchant bank account
linked to it.

Possible values are:

**•** `Enabled`

**•** `Disabled`

The default value is Disabled.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the payment gateway that handles transactions between the merchant account and
the payment processor.

This field is a relationship field.

**Relationship Name**
PaymentGatewayProvider

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Account ID assigned by the payment provider that identifies the linked Salesforce Payments
account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines whether Salesforce Payments can use this payment gateway for calls to the external
payment gateway. Inactive payment gateways can’t be used.

Possible values are:

**•** `Active`  - the merchant account can accept payments.


-----

**•** `Complete` – `PaymentStatus` and `DepositStatus` are enabled and the
account provided all the required information.

**•** `Enabled` – PaymentStatus and PayoutStatus are enabled, but the payment
provider can require more information later. If the merchant doesn't provide the
information then the account can become restricted. The time limit that the merchant
has to provide the information is longer than the RestrictedSoon state.

**•** `Pending–The merchant account exists but it can’t accept payments. This option`
maintains backward compatibility for accounts that were created with API version 55.0
and earlier. Pending is no longer in use for API version 57.0 and higher.

**•** `Rejected` – The payment provider has rejected the merchant account with an
explanation.

**•** `Restricted` – merchant account functionality is limited. This state is only applicable
if `PaymentStatus,` `PayoutStatus, or both are disabled.`

**•** `RestrictedSoon` – `PaymentStatus` and `PayoutStatus are enabled, but`
the payment provider requires more information. If the merchant doesn't provide the
information in a specific time period, then the merchant account becomes restricted.
