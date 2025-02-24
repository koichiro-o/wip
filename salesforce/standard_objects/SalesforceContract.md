#### SalesforceContract

Read-only virtual object used in the Your Account App. Represents contract information related to your organization’s Salesforce
subscription.

##### Supported Calls
```
describeLayout(), describeSObjects(), query()

 Fields

```
```
AutoRenewCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
BillingAddressCity
BillingAddressCountry
BillingAddressPostalCode
BillingAddressState
BillingAddressStreet

```

**Description**
Determines if contract renews automatically

Possible values are:

**•** `No`

**•** `Yes`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this contract. Maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address of this contract.


-----

```
BillingCompany
BillingEmail
BillingFrequency
BillingName
BillingPhone
ContractId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the billing company.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for billing this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Define billing periods.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contact name for this contract.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Phone number for billing this contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID for this contract.


-----

```
ContractNumber
CreditCardExpirationMonth
CreditCardExpirationYear
CreditCardNumber
CreditCardType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Number of the contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Month the credit card expires.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Year the credit card expires.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
16-digit credit card number.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Credit card provider.

Possible values are:

**•** `AmericanExpress—`

**•** `JCB`

**•** `MasterCard`

**•** `Visa`


-----

```
EndDate
ExternalId
FirstNameOnCreditCard
LastNameOnCreditCard
PaymentTerm

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the contract.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Cardholder’s first name on the credit card.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Cardholder’s last name on the credit card.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment terms definition.

Possible values are:

**•** `Net0—Due upon receipt`

**•** `Net10—DD-Germany: Net 10`

**•** `Net30—`

**•** `Net30EOM—JP-Net 30 EOM`

**•** `Net45—`


-----

```
PaymentType
SalesforceContractStatus
ShippingAddressCity
ShippingAddressCountry

```


**•** `Net60—`

**•** `Net60EOM—JP-Net 60 EOM`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Payment type definition.

Possible values are:

**•** `Check`

**•** `CreditCard—`

**•** `DirectDebit—`

**•** `WireTransfer—`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the contract

Possible values are:

**•** `Activated`

**•** `Draft`

**•** `Expired`

**•** `Terminated`

**•** `inApproval—`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. City maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ShippingAddressPostalCode
ShippingAddressState
ShippingAddressStreet
StartDate
SubscriptionDaysLeft

##### Usage

```

**Description**
Details of the shipping address. Country maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. State maximum size is 80 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address of the shipping address. Maximum of 255 characters.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Start date of the contract.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Days remaining for this subscription.


Used by Your Account to manage contracts related to your organization’s Salesforce subscription. Read-only.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceInvoice**

**SalesforcePayment**

**SalesforceQuote**
