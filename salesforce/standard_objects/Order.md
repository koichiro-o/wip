#### Order

Represents an order associated with a contract or an account.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the Account associated with this order. Can only be updated
when the order’s StatusCode value is Draft.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account


-----

```
ActivatedById
ActivatedDate
BillingAddress
BillingCity
BillingCountry

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the User who activated this order.

This is a relationship field.

**Relationship Name**
ActivatedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
Date and time when the order was activated.

**Type**
address

**Properties**
Filter, Nillable

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the billing address for this order. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the billing address for this order. Maximum size is 80 characters.


-----

```
BillingCountryCode
BillingEmailAddress
BillingGeocodeAccuracy
BillingLatitude
BillingLongitude

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the billing address for this order.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address for this order’s billing address.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode of the address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLongitude to specify the precise geolocation of a billing
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLatitude to specify the precise geolocation of a billing
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.


-----

```
BillingPhoneNumber
BillingPostalCode
BillingState
BillingStateCode
BillingStreet
BillToContactId

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for this order’s billing address.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the billing address for this order. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the billing address for this order. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the order’s billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address.

**Type**
reference


-----

```
CompanyAuthorizedById
CompanyAuthorizedDate
ContractId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that the order is billed to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user who authorized the account associated with the order.

This is a relationship field.

**Relationship Name**
CompanyAuthorizedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which your organization authorized the order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contract associated with this order. Can only be updated when the
order’s StatusCode value is Draft.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract


-----

```
CurrencyIsoCode
CustomerAuthorizedById
CustomerAuthorizedDate
Description
EffectiveDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact who authorized the order.

This is a relationship field.

**Relationship Name**
CustomerAuthorizedBy

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date on which the contact authorized the order.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the order.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date at which the order becomes effective. Label is Order Start Date.


-----

```
EndDate
GrandTotalAmount
IsReductionOrder
LastReferencedDate
LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date at which the order ends. Label is Order End Date.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` and TotalTaxAmount.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Determines whether an order is a reduction order. Label is Reduction
**Order.**

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.


-----

```
Name
OpportunityId
OrderedDate
OrderManagementReferenceIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name for this order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for the opportunity that’s associated with this order.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the order was placed.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is used by Order Management to store the external reference Identifier
for B2C Commerce orders. On creation, the B2C Integration sets this value to B2C
`realm ID` + "_" + `B2C instance ID` + "@" + `B2C Commerce`
`catalog/domain ID` + "@" + `B2C Commerce order number.`
Otherwise, it isn’t set.

When you create an OrderSummary, if you don’t specify an
ExternalReferenceIdentifier value, it’s set to this value. If this value is null, then
the system generates a value for ExternalReferenceIdentifier. This value isn’t
required to be unique in an organization, but the OrderSummary
ExternalReferenceIdentifier is.

This field is available in API version 56.0 and later.


-----

```
OrderNumber
OrderReferenceNumber
OriginalOrderId
OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Order number assigned to this order (not the unique, system-generated ID
assigned during creation). Maximum size is 30 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order reference number assigned to this order. Maximum size is 80 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Optional. ID of the original order that a reduction order is reducing, if the reduction
order is reducing a single order. Label is Original Order.

Editable only if isReductionOrder is true. If the reduction order is
reducing more than one order, leave blank.

This is a relationship field.

**Relationship Name**
OriginalOrder

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the User or queue that owns this order.

This is a polymorphic relationship field.

**Relationship Name**
Owner


-----

```
PaymentTermId
PoDate
PoNumber
Pricebook2Id

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The ID of the related payment term. This field is available in API version 55.0 and
later. This field is available if Subscription Management is enabled in your org.

This is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date of the purchase order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number identifying the purchase order. Maximum is 80.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the price book associated with this order.

This is a relationship field.


-----

```
QuoteId
RecordTypeId
RelatedOrderId

```

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the quote that’s associated with this order.

If you set `QuoteId` to null, `QuoteLineItemId` on all of the order’s child
order products is set to null.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type assigned to this order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The original order that a change order was created from.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

This field is a relationship field.

**Relationship Name**
RelatedOrder

**Relationship Type**
Lookup

**Refers To**
Order


-----

```
SalesChannelId
SalesStoreId
ShippingAddress
ShippingCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to a sales channel entity.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the RetailStore or WebStore associated with this Order.

This field is a polymorphic relationship field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v46.0 and later.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**Type**
address

**Properties**
Filter, Nillable

**Description**
Shipping address for the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City of the shipping address. Maximum size is 40 characters.


-----

```
ShippingCountry
ShippingCountryCode
ShippingGeocodeAccuracy
ShippingLatitude
ShippingLongitude
ShippingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country of the shipping address. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the order’s shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode of the shipping address.

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


-----

```
ShippingState
ShippingStateCode
ShippingStreet
ShipToContactId
Status

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code of the shipping address. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State of the shipping address. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the order’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address of the shipping address. Maximum of 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that the order is shipped to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Picklist of values that indicate order status. Each value is within one of two status
categories defined in StatusCode. For example, the status picklist might
contain Draft, Ready for Review, and Ready for Activation
values with a StatusCode of Draft.


-----

```
StatusCode
TaxLocaleType
TotalAdjDeliveryAmtWithTax

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status category for the order. An order can be either Draft or Activated.
Label is Status Category.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of tax calculation that Salesforce uses for the order’s order items. VAT
regions use gross tax, which includes tax in all sale amounts. US regions use net
tax, which calculates tax separately from the initial sale amount and then adds
the sale and tax amounts together in a total.

Use TaxLocaleType to determine which types of tax fields to show on your
order. If TaxLocaleType is null, the order shows all tax fields.

**Gross Tax Fields**
```
   TotalAdjDeliveryAmtWithTax
   TotalAdjProductAmtWithTax
   TotalProductAdjDistAmtWithTax
   TotalDeliveryAdjDistAmtWithTax

```
To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of delivery line amounts, delivery line adjustments, and tax. Order products
with null Type fields aren’t included.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v49.0 and later.


-----

```
TotalAdjProductAmtWithTax
TotalAdjustedDeliveryAmount
TotalAdjustedDeliveryTaxAmount
TotalAdjustedProductAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of product line amounts, line adjustments, and tax. Order products with
null Type fields aren’t included.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of delivery line amounts and delivery line adjustments. Order products with
null Type fields aren’t included.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of delivery line tax amounts and delivery line tax adjustments.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of product line amounts and line adjustments. Order products with null
Type fields aren’t included.


-----

```
TotalAdjustedProductTaxAmount
TotalAmount
TotalDeliveryAdjDistAmount
TotalDeliveryAdjDistAmtWithTax

```

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of line tax amounts and line tax adjustments. Order products with null Type
fields aren’t included.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The net total amount for the order products associated with this order.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s delivery adjustment distributed amounts. Used only when
the Order Adjustment Group has a Type value of Header.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s delivery adjustment distributed amounts and tax. Used
only when the Order Adjustment Group has a Type value of Header.


-----

```
TotalDeliveryAdjDistTaxAmount
TotalProductAdjDistAmount
TotalProductAdjDistAmtWithTax

```

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s delivery adjustment distributed tax amounts. Used only
when the Order Adjustment Group has a Type value of Header.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s product adjustment distributed amounts. Order products
with null Type fields aren’t included. Used only when the Order Adjustment
Group has a Type value of Header.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s product adjustment distributed amounts. Order products
with null Type fields aren’t included. Used only when the Order Adjustment
Group has a Type value of Header.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v49.0 and later.


-----

```
TotalProductAdjDistTaxAmount
TotalTaxAmount
Type

##### Usage

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s product adjustment distributed tax amounts. Order products
with null Type fields aren’t included. Used only when the Order Adjustment
Group has a Type value of Header.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll up of all tax on the order. Includes delivery taxes, price adjustment taxes, and
product taxes.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license or a B2B Commerce License.

This field is available in API v48.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If you want to show more information about your order, you can add custom
values to the Type picklist. By default, the Type field doesn't perform any
actions or show any values.


The `Status` field specifies the current state of an order. Status strings represent its current state (Draft or Activated).

When a client application creates an order, the Status Code must be Draft and the Status must be any value that corresponds
to a `Status Code` of Draft. The application can then activate an order by updating it and setting the value in its `Status` field
to an Activated state; however, the `Status field is the only field you can update when activating the order.`

After an order is activated, your client application can change the Status back to the `Draft state—but only if the order doesn’t`
have any child reduction order products. Your client application can delete orders when the Status is `Draft` but not when its
`Status` is `Activated.`


-----

Client applications can use the API to create, update, delete, and query any Attachment associated with an order.

##### Orders Without Price Books

If your organization manages products and Price books in an external platform, you can use Salesforce API to create orders and order
items without values for their Price book and Price book entry fields. This feature is available only for Salesforce orgs with the B2B
Commerce, B2B Commerce Starter, B2B Commerce Growth, or B2B Commerce Plus packages. Admins enable orders without Price books
by going to Salesforce Order Settings and selecting the Optional Price Book setting.

In a standard order, Salesforce prompts the sales rep to select a Price book when they add the first order product to the order. The sales
rep can then add order products that have price book entries in the selected price book. In an order without a Price book, Salesforce
hides the order’s Add Products button and Edit Products button so that sales reps must manage their products and price books using
their external system.

You can create orders without Price books only by creating an order with Salesforce API and leaving the `Pricebook2Id` field null.
Orders without Price books follow several different guidelines compared to standard orders.

**•** Orders without price books don’t support reduction orders or change orders.

**•** Order products without price book entries require list prices.

**•** Orders without price books support only order items without price book entries. Orders with price books support only order items
with price book entries.

**•** Important: Orders without Price books are supported with B2B licenses only. Salesforce Order Management requires price
books for orders and price book entries for order products.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OrderChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[OrderFeed (API version 29.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[OrderHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[OrderOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

SEE ALSO:

OrderHistory

OrderItem

OrderSummary

SalesChannel
