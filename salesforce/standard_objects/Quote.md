#### Quote

Represents a quote, which is a record showing proposed prices for products and services. Available in API version 18.0 and later.

Quotes can be created from and synced with opportunities, and emailed as PDFs to customers

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AccountId
AdditionalAddress
AdditionalCity
AdditionalCountry
AdditionalCountryCode
AdditionalLatitude

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account that’s associated with the quote.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the additional address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's additional address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's additional address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s additional address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
AdditionalLongitude
AdditionalName
AdditionalPostalCode
AdditionalState
AdditionalStateCode

```

**Description**
Used with `AdditionalLongitude` to specify the precise geolocation of
an additional address. Acceptable values are numbers between –90 and 90
with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `AdditionalLatitude` to specify the precise geolocation of
an additional address. Acceptable values are numbers between –180 and 180
with up to 15 decimal places.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name associated with the quote's additional address. Limited: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code for the quote's additional address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's additional address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s additional address.


-----

```
AdditionalStreet
BillToContactId
BillingAddress
BillingCity
BillingCountry
BillingCountryCode

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Street name for the quote's additional address.

**Type**
reference

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
ID of the contact that the order is billed to. This field is available in API version
56.0 and later. This field is available with Subscription Management.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the billing address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's billing address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's billing address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
BillingLatitude
BillingLongitude
BillingName
BillingPostalCode
BillingState

```

**Description**
ISO country code for the quote’s billing address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a
billing address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLatitude to specify the precise geolocation of a billing
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Entity that the quote is billed to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code for the quote's billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's billing address. Up to 80 characters allowed.


-----

```
BillingStateCode
BillingStreet
CalculationStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the quote's billing address.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Price calculations are performed by Salesforce. Tax calculations are performed
by a third-party tax provider integration with Salesforce. Both of these
calculations are asynchronous, and you can use this field to see the status of
the asynchronous processes.

This field is available with Subscription Management or Revenue Cloud.

Possible values are:

**•** `CompletedWithPricing—Indicates that pricing is complete and`
tax will now be calculated.

**•** `CompletedWithTax—Indicates that pricing and tax calculation are`
complete.

**•** `CompletedWithoutPricing—Indicates that pricing and tax`
calculation were skipped.

**•** `ConfigurationFailed—Indicates that configuration failed. Available`
in API version 62.0

**•** `ConfigurationInProgress—Indicates that the configuration is`
in progress. Available in API version 62.0

**•** `NotStarted`

**•** `PriceCalculationFailed—Indicates that pricing failed. Available`
in API version 58.0 and later.

**•** `PriceCalculationInProgress—Available in API version 58.0`
and later.


-----

```
CanCreateQuoteLineItems
ContactId
ContractId

```


**•** `PriceCalculationQueued—The request is sent to the asynchronous`
price calculation process, but the process hasn’t started. Available in API
version 58.0 and later.

**•** `QuoteRequestFailed—Indicates that the requested quote changes`
weren’t saved. Available in API version 62.0

**•** `QuoteRequestPartiallySaved—Indicates that the requested`
quote changes were partially saved. Available in API version 62.0

**•** `ReconciliationFailed—Indicates that the arrangement of quote`
data failed. Available in API version 62.0

**•** `ReconciliationInProgress—Indicates that the arrangement of`
data is in progress. For a sales rep, this value appears as Saving on the
quote page. Available in API version 62.0

**•** `SaveFailedOrIncomplete—Some or all of the records couldn’t be`
saved. For example, some of the quote line item records weren’t saved.
Available in API version 58.0 and later.

**•** `Saving`

**•** `TaxCalculationFailed`

**•** `TaxCalculationInProcess`

**•** `TaxCalculationSuccess—Available in API versions 56.0 and 57.0`

**•** `TaxCalculationWaiting`

The default value is `NotStarted.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
This field isn’t used.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact that’s associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contract that’s associated with the quote.


-----

```
CurrencyIsoCode
Description
Discount
Email
ExpirationDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Restricted picklist

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2Id specified on the
quote, then the currency value of this field must match the currency of the
PricebookEntry objects that are associated with any quote line items it has.

This value is copied from the related Opportunity and can't be changed.

**Type**
textarea

**Properties**
Nillable

**Description**
Text description of the quote. Limit: 32,000 characters.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Difference between the sum of the QuoteLineItem record'sSubtotal and
the sum of the QuoteLineItem record's `Discount totals. Expressed as a`
percentage.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the contact who’s associated with the quote.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The date when this quote is no longer valid.


-----

```
Fax
GrandTotal
IsSyncing
LastReferencedDate
LastViewedDate
LineItemCount

```

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The fax number for the contact who’s associated with the quote.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The total price of the quote plus shipping and taxes.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the quote is syncing with an opportunity.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view but not
viewed it directly.

**Type**
int

**Properties**
Filter, Nillable


-----

```
Name
OpportunityId
Phone
Pricebook2Id
QuoteAccountId

```

**Description**
The number of line items on the quote.

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
Required. Name for the quote. Limit: 225 characters.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID for the opportunity associated with the quote.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The phone number of the contact who’s associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the price book associated with the quote.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with the quote. This field is available in API version
58.0 and later only when the Create Quotes Without a Related Opportunity
setting on the Quotes Settings page is enabled.

This field is a relationship field.


-----

```
QuoteNumber
QuoteToAddress
QuoteToCity
QuoteToCountry
QuoteToLatitude

```

**Relationship Name**
QuoteAccount

**Refers To**
Account

**Type**
string

**Properties**
Defaulted on create, Filter

**Description**
A system-generated number that identifies the quote.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the quote to address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the address to send the quote to for approval, such as a third
party-agency representing a buyer. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the address to send the quote to for approval. Up to 80 characters
allowed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
QuoteToLongitude
QuoteToName
QuoteToPostalCode
QuoteToState
QuoteToStreet

```

**Description**
Used with `QuoteToLongitude` to specify the precise geolocation of a
quote to address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with QuoteToLatitude to specify the precise geolocation of a quote
to address. Acceptable values are numbers between –180 and 180 with up to
15 decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The name of the entity (such as a person or business) that the quote is sent to
for approval. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address to send the quote to for approval.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the address to send the quote to for approval. Up to 80 characters
allowed.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
RecordTypeID
RelatedWorkId
ShippingAddress
ShippingCity
ShippingCountry

```

**Description**
Street name for the address to send the quote to for approval.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to the object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Relationship field that’s visible only if Field Service and Quotes are enabled in
the Salesforce org. This field refers to the work order that the quote is created
from. When a mobile worker creates a quote using the New Quote action in
the Field Service mobile app, this field is automatically populated. This field is
used in the related list that shows all of the quotes related to the work order.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Compound form of the shipping address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the quote's shipping address. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the quote's shipping address. Up to 80 characters allowed.


-----

```
ShippingCountryCode
ShippingHandling
ShippingLatitude
ShippingLongitude
ShippingName
ShippingPostalCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the quote’s shipping address.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update

**Description**
The total shipping and handling costs for the quote.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a
shipping address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The name of the entity (such as a person or business) that the quote is sent to
for approval.

**Type**
string


-----

```
ShippingState
ShippingStateCode
ShippingStreet
Status

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the quote's shipping address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the quote's shipping address. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the quote’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street name for the quote's shipping address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**

The status of the quote. The standard options are:

**•** —None—

**•** Draft

**•** Needs Review

**•** In Review

**•** Approved

**•** Rejected

**•** Presented

**•** Accepted


-----

```
Subtotal
Tax
TotalPrice
TotalPriceWithTax
TotalTaxAmount

```


**•** Denied

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The sum of sales price multiplied by quantity for line items, not including the
discount.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update

**Description**
The total taxes for the quote.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
The total of the quote line items after discounts and before taxes and shipping.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of TotalPrice and TotalTaxAmount. This field is available in
API version 55.0 and later. This field is available if Subscription Management is
enabled in your org.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of all taxes. This field is available in API version 55.0 and later.
This field is available if Subscription Management is enabled in your org.

This field is a calculated field.


-----

##### Usage

Use Quote to manage proposed product prices for customers. To update a Quote, your client application needs “Edit” permission.

**•** Client applications can create, update, delete, and query Attachment records associated with a quote via the API.

**•** You can sync a quote and its parent Opportunity.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteChangeEvent (API version 44.0)**
Change events are available for the object.

**QuoteFeed (API version 39.0)**
Feed tracking is available for the object.

**QuoteHistory (API version 57.0)**
History is available for tracked fields of the object.

**QuoteOwnerSharingRule (API version 41.0)**
Sharing rules are available for the object.

**QuoteShare (API version 41.0)**
Sharing is available for the object.

SEE ALSO:

QuoteLineItem

QuoteDocument

Opportunity
