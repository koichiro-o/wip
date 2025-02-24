#### ReturnOrder

Represents the return or repair of inventory or products in Field Service, or the return of order products in Order Management. This object
is available in API version 42.0 and later.

Return orders are available in Lightning Experience, Salesforce Classic, the Salesforce mobile app, the Field Service mobile app for Android
and iOS, and communities built using Salesforce Tabs + Visualforce.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service or Order Management must be enabled. If return orders are enabled by a Salesforce Order Management license, they must
be created with a Status corresponding to the Status Category Activated. The default Statuses corresponding to Activated are Submitted
and Approved.


-----

##### Fields

**Field Name**
```
AccountId
CaseId
ContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the return order.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the return order.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the return order.

This is a relationship field.

**Relationship Name**
Contact


-----

```
CurrencyIsoCode
Description
DestinationLocationId

```

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the
currency of the OrderSummary associated with the ReturnOrder.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes or context about the return order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location where the items are being returned to. For example, if the return
order tracks the return of products from a technician’s van to a warehouse, the
warehouse is the destination location.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup


-----

```
ExpectedArrivalDate
ExpirationDate
GrandTotalAmount
LastReferencedDate
LastViewedDate

```

**Refers To**
Location

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the items are expected to arrive at the destination location.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Authorizations can’t be captured after their expiration dates.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the products, fees, and delivery charges
on the return order. This includes all return order line items associated with the
return order. This amount is equal to TotalAmount + TotalTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order was last modified. Its label in the user interface
is `Last Modified Date.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LifeCycleType
OrderId
OrderSummaryId

```

**Description**
The date when the return order was last viewed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the order summary is managed by Salesforce Order
Management (MANAGED) or by an external system (UNMANAGED). An
unmanaged order summary is stored in Salesforce for reference purposes.

**•** Some Order Management APIs reject input records that are associated with
unmanaged order summaries.

**•** Order Management does not update financial bucket fields on some records
that are associated with unmanaged order summaries.

**•** A user with the EditUnmanagedOrderSummaries or B2BCommerceIntegrator
permission can edit certain fields on objects related to unmanaged order
summaries that are normally only accessible via APIs.

Possible values are:

**•** `MANAGED—Managed`

**•** `UNMANAGED—Unmanaged`

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order associated with the return order. When you associated a return order
with an order, you can associate the return order’s line items with order products.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference


-----

```
OwnerId
ProductRequestId

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the order summary associated with the return order.

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the return order.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product request associated with the return order. When you associated a
return order with a product request, you can associate the return order’s line
items with the product request’s line items.

A return order might be related to a product request if the return order tracks
the return of unused products or products to be repaired or replaced. For example,
a technician creates a product request for three motors to prepare for a field visit.
If the technician finds that only two motors are needed, they can create a return
order to return the third to the original location, and list the product request in
this field.

This is a relationship field.

**Relationship Name**
ProductRequest

**Relationship Type**
Lookup

**Refers To**
ProductRequest


-----

```
ProductServiceCampaignId
ReturnOrderNumber
ReturnedById
ShipFromAddress

```

This field is available only if Field Service or Health Cloud is enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign associated with the return order

This field is available only if Field Service is enabled.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number identifying the return order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user returning the items.

This is a relationship field.

**Relationship Name**
ReturnedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
address

**Properties**
Filter, Nillable

**Description**
The return shipping address. This address tracks the location of the items at the
start of the return or repair. For example, if a customer is returning an item, the
Ship From address is the customer’s address.


-----

```
ShipFromCity
ShipFromCountry
ShipFromGeocodeAccuracy
ShipFromLatitude
ShipFromLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the return shipping address. This address tracks the location of
the items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the return shipping address. See Compound
Field Considerations and Limitations for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the return shipping
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places. See Compound Field Considerations and Limitations for details
on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double


-----

```
ShipFromPostalCode
ShipFromState
ShipFromStreet
ShipmentType

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the return shipping
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places. See Compound Field Considerations and Limitations for details
on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the return shipping address. This address tracks the location
of the items at the start of the return or repair. For example, if a customer is
returning an item, the Ship From address is the customer’s address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the return shipping address. This address tracks the location of the
items at the start of the return or repair. For example, if a customer is returning
an item, the Ship From address is the customer’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment associated with the return order. Available values are:


-----

```
SourceLocationId
Status
StatusCategory

```


**•** `Standard (default value)`

**•** `Rush`

**•** `Overnight`

**•** `Next Business Day`

**•** `Pick Up`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The items’ location at the start of the return or repair. For example, if the return
order tracks the return of products from a technician’s service vehicle to a
warehouse, the service vehicle is the source location.

This is a relationship field.

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the return order. Available values are:

**•** `Draft`

**•** `Submitted`

**•** `Approved`

**•** `Canceled`

**•** `Closed`

If return orders are enabled by a Salesforce Order Management license, they must
be created with a Status corresponding to the Status Category `Activated.`
The default Statuses corresponding to Activated are Submitted and Approved.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
TaxLocaleType
TotalAmount
TotalDeliveryAdjustAmount

```

**Description**
Status category of the return order. Processing of the return order depends on
this value. Each status category corresponds to one or more statuses.

Possible values are:

**•** `Activated`

**•** `Canceled`

**•** `Closed`

**•** `Draft`

**•** `Pending`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original order associated with the return
order. Gross usually applies to taxes like value-added tax (VAT), and Net usually
applies to taxes like sales tax.

Possible values are:

**•** `Automatic (displays most prices and taxes as combined values)`

**•** `Gross (displays most prices and taxes as combined values)`

**•** `Net (displays most prices and taxes as separate values)`

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Adjusted total, not including tax, of the return order line items, including products,
fees, and delivery charges, on the ReturnOrder.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalDeliveryAdjustAmtWithTax
TotalDeliveryAdjustTaxAmount
TotalDeliveryAmount
TotalDeliveryAmtWithTax

```

**Description**
Total amount of the price adjustments applied to the delivery charges on the
return order. This value only includes adjustments to return order line items of
type code Charge.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the
return order, inclusive of tax. This value only includes adjustments to return order
line items of type code Charge. This amount is equal to
TotalDeliveryAdjustAmount + TotalDeliveryAdjustTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjustAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges on the return order. This value only includes return
order line items of type code Charge.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency


-----

```
TotalDeliveryTaxAmount
TotalFeeAdjustAmount
TotalFeeAdjustAmtWithTax

```

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the delivery charges on the return order, inclusive of tax. This
value only includes return order line items of type code Charge. This amount is
equal to TotalDeliveryAmount + TotalDeliveryTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the return order.
This value only includes adjustments to return order line items of type Fee.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the return order,
inclusive of tax. This value only includes adjustments to return order line items
of type Fee. This amount is equal to TotalFeeAdjustAmount +
TotalFeeAdjustTaxAmount.

This is a calculated field.

This field is available in API version 56.0 and later.


-----

```
TotalFeeAdjustTaxAmount
TotalFeeAmount
TotalFeeAmtWithTax
TotalFeeTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjustAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the fees on the return order. This value only includes return order line
items of type Fee.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the fees on the return order, inclusive of tax. This value only
includes return order line items of type Fee. This amount is equal to
TotalFeeAmount + TotalFeeTaxAmount.

This is a calculated field.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAmount.

This is a calculated field.

This field is available in API version 56.0 and later.


-----

```
TotalProductAdjustAmount
TotalProductAdjustAmtWithTax
TotalProductAdjustTaxAmount
TotalProductAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the return
order. This value only includes adjustments to return order line items of type
code Product.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the return
order, inclusive of tax. This value only includes adjustments to return order line
items of type code Product. This amount is equal to TotalProductAdjustAmount
+ TotalProductAdjustTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAdjustmentAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the product charges on the return order. This value only includes return
order line items of type code Product.

This is a calculated field.

This field is available in API version 50.0 and later.


-----

```
TotalProductAmtWithTax
TotalProductTaxAmount
TotalTaxAmount

##### Usage

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the product charges on the return order, inclusive of tax. This
value only includes return order line items of type code Product. This amount is
equal to TotalProductAmount + TotalProductTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

This is a calculated field.

This field is available in API version 50.0 and later.


You can use return orders to track customer returns, customer repairs, or the return of inventory from a technician’s van stock to a
warehouse or supplier. Customers can initiate a return from a community, or agents can create return orders in response to a customer
call or technician request.

Return orders are composed of return order line items, which allow you to add details about the items being returned. To represent the
returned items, each line item must list one or more of the following: product, product item, asset, product request line item, and order
product. Return orders can be associated with a product request, case, account, contact, and order if needed. This versatility lets you use
return orders to track a wide range of return scenarios.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderChangeEvent (API version 48.0)**
Change events are available for the object.

**ReturnOrderFeed**

Feed tracking is available for the object.

**ReturnOrderHistory**

History is available for tracked fields of the object.

**ReturnOrderOwnerSharingRule**

Sharing rules are available for the object.

**ReturnOrderShare**

Sharing is available for the object.
