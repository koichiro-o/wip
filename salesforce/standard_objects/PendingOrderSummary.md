#### PendingOrderSummary

Object representing a B2C Commerce order ingested via High Scale Orders before an OrderSummary is created for it. Optimized for
online transaction processing (OLTP). This object is available in API version 55.0 and later.

##### Supported Calls
```
describeLayout(), query()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs where the High Scale Orders feature is enabled.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account or person account associated with the PendingOrderSummary. It represents
the shopper in the storefront.

This field is a relationship field.


-----

```
BillToContactId
BillingEmailAddress
BillingPhoneNumber
CurrencyIsoCode

```

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the PendingOrderSummary. It represents the shopper in
the storefront when not using person accounts.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
Email address on the billing address.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Phone number of the billing address.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
Description
ExternalId
ExternalReferenceIdentifier
GrandTotalAmount

```

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the original Order associated with the PendingOrderSummary.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the PendingOrderSummary.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is used internally.

This field isn’t synced with ZOS, so you can’t use it in a query or insert operation.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Used internally to prevent duplicate records. This value is case-sensitive. On creation, this
value is set to B2C realm ID + "_" + B2C instance ID + "@" + B2C Commerce
`catalog/domain ID` + "@" + `B2C Commerce order number.`

When the OrderSummary is created, this value is copied to its ExternalReferenceIdentifier
field. If you ingest orders from multiple sources, you can maintain uniqueness by including
a prefix based on the source.

**Type**
currency

**Properties**
Filter, Sort


-----

```
OrderNumber
OrderedDate
Payload
PayloadType

```
ProcessingInstructions


**Description**
Total amount, including adjustments and tax, of the PendingOrderSummary.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the PendingOrderSummary.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date of the original order associated with this PendingOrderSummary.

**Type**
textarea

**Properties**

**Description**
The order data payload.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The datatype of the Payload.

Possible values are:

**•** `JSON_GZIP`

**•** `JSON_RAW`

**Type**
textarea

**Properties**
Nillable

**Description**
Instructions about how the HSOI service should create the order summary. Options include
using the default without customizations or using a custom flow.


-----

```
SalesChannelId
SalesStoreId
ShopperName

```

Also includes instructions about how the HSOI service should dedupe account and contact
information using platform duplication and matching rules or by using simple email methods.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the SalesChannel associated with this PendingOrderSummary. The SalesChannel Name
matches the B2C Commerce catalog/domain ID.

This field is a relationship field.

**Relationship Name**
SalesChannel

**Relationship Type**
Lookup

**Refers To**
SalesChannel

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the RetailStore or WebStore associated with this PendingOrderSummary.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first name and last name of the shopper that placed the original order.


-----

##### Usage

If you need to view or service an ingested B2C Commerce order before the automated High Scale Orders process has created an
OrderSummary for it, you can manually trigger creation of the OrderSummary. In Salesforce, open the PendingOrderSummaries list, find
the record, and click Import.

PendingOrderSummary only supports certain methods and queries. It doesn’t support Apex triggers.

Supported Apex Methods:

**•** `Database.query(queryString)`

**•** `Database.query(queryString, accessLevel)`

Supported SOAP API Methods:

**•** `create()`

**•** `delete()`

**•** `describeLayout()`

**•** `query()`

**•** `queryMore()`

Supported REST API Methods:

**•** `/services/data/vXX.X/sobjects/sObject/ GET`

**•** `/services/data/vXX.X/sobjects/sObject/id/ GET`

**•** `/services/data/vXX.X/sobjects/sObject/id/ DELETE`

**•** `/services/data/vXX.X/sobjects/sObject/id/ POST`

**•** `/services/data/vXX.X/sobjects/sObject/describe/compactLayouts/ GET`

**•** `/services/data/vXX.X/sobjects/sObject/quickActions/ GET`

Supported Queries:

**convertCurrency() function**
Example: `SELECT Id, convertCurrency(AnnualRevenue) FROM Account`

**Child-to-Parent subquery**
Example: `SELECT ExternalReferenceIdentifier, Account.Name FROM PendingOrderSummary`
```
  WHERE ExternalReferenceIdentifier = 'a'

```
**Limit clause**
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`
```
  ExternalReferenceIdentifier = 'a' LIMIT 1

```
**Filter by index**
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`
```
  ExternalReferenceIdentifier = 'a'

```
**Filter by secondary index**
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE AccountId`
```
  = 'xxx'

```
**ORDER BY clause**
When using ORDER BY, you don’t need to specify a direction. However, if you sort ASC, you can’t use NULLS LAST. If you sort DESC,
you can only use NULLS LAST.


-----

Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary ORDER BY`
```
  ExternalReferenceIdentifier

```
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary ORDER BY`
```
  ExternalReferenceIdentifier ASC NULLS FIRST

```
Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary ORDER BY`
```
  ExternalReferenceIdentifier DESC NULLS LAST

```
**Equality filter**
Range filters aren’t supported.

Example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`
```
  ExternalReferenceIdentifier = 'realm_tenant@storesite@0000001'

```
Invalid example: `SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE`
```
  ExternalReferenceIdentifier < 'a'

```
SEE ALSO:

OrderSummary

Order
