#### GtwyProvPaymentMethodType

The gateway provider payment method type allows integrators and payment providers to choose an active payment to receive an
order's payment data rather than allowing the Salesforce Order Management platform to select a default payment method. This object
is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), search(), update(), upsert()

```

-----

##### Fields

**Field**
```
Comments
DeveloperName
GtwyProviderPaymentMethodType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can provide additional details about the gateway provider payment method type
record. Supports a maximum of 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, Salesforce generates one for
each record, which slows performance.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links the Salesforce payment method to the payment method used in the Salesforce Order
Management storefront. Your payment gateway integration uses this field when finding a
payment method to link to a payment.

The value of GtwyProviderPaymentMethodType must match the payment method
value sent to the order's Payment Instrument in Salesforce Order Management.

Listed below are several examples of payment method values that Salesforce could receive
from Salesforce Order Management.

**•** `CREDIT_CARD`

**•** `BASIC_CREDIT`

**•** `CreditCard`

**•** `GooglePay`


-----

```
Language
LastViewedDate
MasterLabel
NamespacePrefix
PaymentGatewayProviderId

```


**•** `ApplePay`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the payment gateway integration.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view `(LastReferencedDate)`
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The gateway provider payment method type name that appears in the user
interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace of the payment gateway integration classes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the payment gateway provider that Salesforce Order Management should use
when processing payments. One payment gateway provider can be related to multiple
payment method types.

This is a relationship field.


-----

```
PaymentMethodType
RecordTypeId

##### Usage

```

**Relationship Name**
PaymentGatewayProvider

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayProvider

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of payment method used on an order in Salesforce Order Management.

Possible values are:

**•** `AlternativePaymentMethod`

**•** `CardPaymentMethod`

**•** `DigitalWallet`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type entity related to the gateway provider payment method type.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType


The Salesforce Order Management payment record must have a `ProcessorId` field with the same value as the payment gateway's
`ExternalReferenceId` field. The gateway provider payment method type record must have a `PaymentMethodType` field
that looks up to the payment method that you want to associate to your payment. Finally, the payment gateway and gateway provider
payment method type must have matching `PaymentGatewayProviderId` fields. When you've established these relationships,
the payment record can infer your payment method from the gateway provider payment method type record.


-----
