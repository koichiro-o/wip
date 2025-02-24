#### FulfillmentOrder

```

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory

**Refers To**
ForecastingCustomCategory

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the
FrcstCustmCatgRampRateSrc.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this FrcstCustmCatgRampRateSrc value. This display value is the internal label that
doesn't get translated.


Represents a group of products, fees, and delivery charges on a single order that share the same fulfillment location, delivery method,
and recipient. The FulfillmentOrderLineItems belonging to a FulfillmentOrder are associated with OrderItemSummary objects belonging
to a single OrderSummary. This object is available in API version 48.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs.

##### Fields

```
AccountId
ActiveDate
BillToContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Account or Person Account associated with the FulfillmentOrder. It represents the
shopper in the storefront.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
datetime

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the fulfillment order becomes active.

This field is available in API version 61.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the FulfillmentOrder. It represents the shopper in the
storefront when not using person accounts.


-----

```
ClosedDate
CurrencyIsoCode
DeliveryMethodId

```

This field is available in API version 49.0 and later.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
datetime

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date the fulfillment order closed. Automatically entered.

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the OrderSummary associated with the FulfillmentOrder.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

This field is available in API version 49.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the DeliveryMethod used for this FulfillmentOrder.

This field is a relationship field.


-----

```
FulfilledFromLocationId
FulfilledToAddress
FulfilledToCity
FulfilledToCountry

```

**Relationship Name**
DeliveryMethod

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryMethod

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Location handling this FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
FulfilledFromLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
address

**Properties**
Filter, Nillable

**Description**
Address of the recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address country.


-----

```
FulfilledToEmailAddress
FulfilledTo
GeocodeAccuracy
FulfilledToLatitude
FulfilledToLongitude

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the recipient.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy of the geocode for the recipient address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLongitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
FulfilledToName
FulfilledToPhone
FulfilledToPostalCode
FulfilledToState
FulfilledToStreet
FulfillmentOrderNumber

```

**Description**
Used with FulfilledToLatitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name on the recipient address.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address street.

**Type**
string


-----

```
GrandTotalAmount
InvoiceId
IsReship
IsSuspended

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrder.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the products, fees, and delivery charges on the
FulfillmentOrder. This amount includes all FulfillmentOrderLineItems associated with the
FulfillmentOrder. This amount is equal to TotalAmount + TotalTaxAmount.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Invoice associated with the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the FulfillmentOrder is for a reshipment. The default value is false.

This field is available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
ItemCount
LastReferencedDate
LastViewedDate
OrderId
OrderSummaryId

```

**Description**
Indicates whether the FulfillmentOrder is suspended. The default value is false.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the quantities of the FulfillmentOrderLineItems included in the FulfillmentOrder.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. A null value can mean that this
record has only been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original Order that generated the FulfillmentOrder.

This field is a relationship field.

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
Status

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderSummary associated with the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this FulfillmentOrder. Default value is the User logged in
to the API to perform the create.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Status of the FulfillmentOrder. Each status corresponds to one status category, shown here
in parentheses. You can customize the status picklist to represent your business processes,
but the status category picklist is fixed because processing is based on those values. If you
customize the status picklist, include at least one status value for each status category.

Default values are:

**•** `Allocated (Activated)`

**•** `Assigned (Fulfilling)`

**•** `Cancelled (Cancelled)`


-----

```
StatusCategory
TaxLocaleType
TotalAdjustmentAmount

```


**•** `Draft (Draft)`

**•** `Fulfilled (Closed)`

**•** `Pick Complete` (Fulfilling) This value is available in API v56.0 and later.

**•** `Pickpack (Fulfilling)`

**•** `Printed (Fulfilling) This value is available in API v56.0 and later.`

**•** `Rejected (Rejected) This value is available in API v56.0 and later.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status category of the FulfillmentOrder. Processing of the FulfillmentOrder depends on this
value. Each status category corresponds to one or more statuses.

Possible values are:

**•** `ACTIVATED—Activated`

**•** `CANCELLED—Cancelled`

**•** `CLOSED—Closed`

**•** `DRAFT—Draft`

**•** `FULFILLING—Fulfilling`

**•** `REJECTED—Rejected This value is available in API v56.0 and later.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original Order associated with the FulfillmentOrder.
Gross usually applies to taxes like value-added tax (VAT), and Net usually applies to taxes like
sales tax.

Possible values are:

**•** `Gross (displays most prices and taxes as combined values)`

**•** `Net (displays most prices and taxes as separate values)`

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalAdjustment
AmtWithTax
TotalAdjustmentTaxAmount
TotalAmount
TotalDelivery
AdjustAmount
TotalDeliveryAdjust
AmtWithTax

```

**Description**
Total amount of the price adjustments applied to the products on the FulfillmentOrder. This
value only includes adjustments to FulfillmentOrderLineItems of type code Product, not
adjustments to delivery charges or fees.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the FulfillmentOrder,
inclusive of tax. This value only includes adjustments to FulfillmentOrderLineItems of type
code Product. This amount is equal to TotalAdjustmentAmount +
TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Adjusted total, not including tax, of the FulfillmentOrderLineItems, including products, fees,
and delivery charges, on the FulfillmentOrder.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the FulfillmentOrder.
This value only includes adjustments to FulfillmentOrderLineItems of type Delivery Charge.

**Type**
currency


-----

```
TotalDelivery
AdjustTaxAmount
TotalDeliveryAmount
TotalDeliveryAmtWithTax
TotalDeliveryTaxAmount

```

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the FulfillmentOrder,
inclusive of tax. This value only includes adjustments to FulfillmentOrderLineItems of type
Delivery Charge. This amount is equal to TotalDeliveryAdjustAmount +
TotalDeliveryAdjustTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjustAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges on the FulfillmentOrder. This value only includes
FulfillmentOrderLineItems of type Delivery Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the delivery charges on the FulfillmentOrder, inclusive of tax. This value only
includes FulfillmentOrderLineItems of type Delivery Charge. This amount is equal to
TotalDeliveryAmount + TotalDeliveryTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.


-----

```
TotalFeeAdjustAmount
TotalFeeAdjustAmtWithTax
TotalFeeAdjustTaxAmount
TotalFeeAmount
TotalFeeAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the FulfillmentOrder. This value
only includes adjustments to FulfillmentOrderLineItems of type Fee.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the FulfillmentOrder, inclusive
of tax. This value only includes adjustments to FulfillmentOrderLineItems of type Fee. This
amount is equal to TotalFeeAdjustAmount + TotalFeeAdjustTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjustAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the fees on the FulfillmentOrder, excluding adjustments and tax. This value
only includes FulfillmentOrderLineItems of type Fee.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalFeeTaxAmount
TotalProductAmount
TotalProductAmtWithTax
TotalProductTaxAmount
TotalTaxAmount

```

**Description**
Total price of the fees on the FulfillmentOrder, inclusive of tax. This value only includes
FulfillmentOrderLineItems of type Fee. This amount is equal to TotalFeeAmount +
TotalFeeTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the products on the FulfillmentOrder, excluding order adjustments, delivery
charges, and fees. This value only includes FulfillmentOrderLineItems of type code Product.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the products on the FulfillmentOrder, inclusive of tax. This value only includes
FulfillmentOrderLineItems of type code Product. This amount is equal to TotalProductAmount
+ TotalProductTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

**Type**
currency


-----

```
Type
TypeCategory

##### Associated Objects

```

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the FulfillmentOrder. Each type corresponds to one type category, shown here in
parentheses. You can customize the type picklist to represent your business processes, but
the type category picklist is fixed because processing is based on those values. If you customize
the type picklist, include at least one type value for each type category.

Default values are:

**•** `Download (Digital)`

**•** `Email (Digital)`

**•** `In Store Pickup` (Physical)

**•** `Retail Store` (Physical)

**•** `Supplier (Drop Ship)`

**•** `Warehouse (Physical)`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type category of the FulfillmentOrder. Processing of the FulfillmentOrder depends on this
value. Each type category corresponds to one or more types.

Possible values are:

**•** `DIGITAL—Digital`

**•** `DROPSHIP—Drop Ship`

**•** `PHYSICAL—Physical`


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[FulFillmentOrderChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.


-----

**[FulfillmentOrderFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[FulfillmentOrderOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[FulfillmentOrderShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

SEE ALSO:

FulfillmentOrderLineItem

Order

OrderSummary
