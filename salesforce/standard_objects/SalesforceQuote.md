#### SalesforceQuote

Read-only virtual object used in the Your Account App. Represents information about your organization’s quotes with Salesforce.

##### Supported Calls
```
describeLayout(), describeSObjects(), query()

 Fields

```
```
ExternalId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
External reference ID set by Salesforce.


-----

```
QuoteNumber
SalesforceContractId
SalesforceQuoteStatus

##### Usage

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A system-generated number that identifies the quote.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contract that’s associated with the quote.

This field is a relationship field.

**Relationship Name**
SalesforceContract

**Relationship Type**
Lookup

**Refers To**
SalesforceContract

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the quote.

Possible values are:

**•** `Complete`

**•** `Expired`

**•** `NeedsApproval—`

**•** `NeedsSignature—`

**•** `Processing`


Used by Your Account to manage quotes related to your organization’s Salesforce contract. Read-only.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesforceContract**

**SalesforceInvoice**

**SalesforcePayment**
