#### PaymentGatewayProvider

Setup entity for payment gateways. Defines the connection to a payment gateway Apex adapter. This object is available in API version
48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
ApexAdapterId
Comments

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of an APEX adapter class. The adapter interacts with your payment gateway to complete
transactions. This field is unique within your organization.

This field is a relationship field.

**Relationship Name**
ApexAdapter

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
DeveloperName
IdempotencySupported
Language
LastViewedDate

```

**Description**
Additional details about a record. Maximum of 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
(Optional) An internal name you assign the adapter. For reference only.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If the same payment request is made in rapid succession, this field defines whether the
Payments platform charges the customer or merchant’s card multiple times for the same
transaction. This situation can occur when a user clicks a Pay button twice, or the gateway’s
server goes down after fulfilling a payment request and the client immediately tries making
another payment. If this field has a value of Yes, the Payments platform ignores identical
payment requests made immediately after an original request.

Different payment gateways have varying levels of idempotency support. When configuring
a new payment gateway integration, plan accordingly.

Possible values are:

**•** `No`

**•** `Yes`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Customer language used for the payment gateway.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
 MasterLabel
 NamespacePrefix
