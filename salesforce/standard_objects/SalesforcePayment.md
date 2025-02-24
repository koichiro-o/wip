#### SalesforcePayment

Read-only virtual object used in the Your Account App. Represents information about payments related to your organization’s Salesforce
invoice.

##### Supported Calls
```
describeLayout(), describeSObjects(), query()

```

-----

##### Fields

**Field**
```
AppliedAmount
AppliedDate
Memo
PaymentCurrency
SalesforcePaymentName
SalesforcePaymentType

```

**Type**
double

**Properties**
Nillable, Sort

**Description**
Payment amount applied to your Salesforce invoice.

**Type**
date

**Properties**
Nillable, Sort

**Description**
Date the payment is applied to your Salesforce invoice.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Credit memo ID. Credit memos are issued for overpayment, rebates, and so forth.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Type of currency used for the payment.

**Type**
string

**Properties**
Nillable, Sort

**Description**
Payment name.

**Type**
picklist

**Properties**
Nillable, Sort


-----

**Description**
Payment method. Possible values are:

**•** `Boleto`

**•** `Check`

**•** `Credit Card`

**•** `Credit Memo`

**•** `Direct Debit`

**•** `Unknown`

**•** `Wire Transfer`

##### Usage

Used by Your Account to manage payments for your organization’s Salesforce contract. Read-only.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as
SalesforcePayment.

**SalesforceContract**

**SalesforceInvoice**

**SalesforceQuote**
