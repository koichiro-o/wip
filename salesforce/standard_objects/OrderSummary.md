#### OrderSummary

Represents the current properties and state of an order. Corresponds to one or more order objects, consisting of an original object and
any change objects applicable to it. This object is available in API version 48.0 and later.

For performance and data integrity reasons, CRUD operations on OrderSummary records don't fire Apex triggers.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.


-----

##### Fields

**Field**
```
 AccountId
ActiveProcess
ExceptionCount
 BillingAddress
 BillingCity

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account or person account associated with the OrderSummary. It represents the
shopper in the storefront.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of active process exceptions on the OrderSummary.

This field is available in API version 50.0 and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Billing address associated with the OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string


-----

```
BillingCountry
BillingCountryCode
BillingEmailAddress
BillingGeocodeAccuracy

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address country.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO country code for the billing address. The default value is `US.`

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address on the billing address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the billing address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`


-----

```
BillingLatitude
BillingLongitude
BillingPhoneNumber
BillingPostalCode
BillingState

```


**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLongitude to specify the precise geolocation of the billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLatitude to specify the precise geolocation of the billing address. Acceptable
values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address state.


-----

```
BillingStateCode
BillingStreet
BillToContactId
BusinessModel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO state or province code for the billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing address street.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the OrderSummary. It represents the shopper in the
storefront when not using person accounts.

If the `OrderLifeCycleType` field is set to UNMANAGED, then users with the Edit
Unmanaged Order Summaries or B2B Commerce Integrator user permission can modify this
field.

This field is available in API version 49.0 and later.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The business model of the OrderSummary.

Possible values are:

**•** `B2B`

**•** `B2C`


-----

```
ChangeOrderId
CurrencyIsoCode
Description
ExternalReference
Identifier

```

This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only with the multicurrency feature enabled. Contains the ISO code for the currency
of the original Order associated with the OrderSummary.

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
Description of the OrderSummary.

This field can be edited.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Used internally to prevent duplicate records. This value is case-sensitive.

In API version 56.0 and later, for orders ingested from B2C Commerce, this value is set to
`B2C realm ID` + "_" + `B2C instance ID` + "@" + `B2C Commerce`
`catalog/domain ID` + "@" + `B2C Commerce order number.`


-----

```
GrandTotalAmount
IsSuspended
LastReferencedDate
LastViewedDate
OrderedDate

```

In API version 55.0, the standard B2C Commerce integration set this value to "SFDC" + "@"
+ nanotime + "@" + UUID and High Scale Orders set it to the value used in later versions.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount, including adjustments and tax, of the OrderSummary.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the OrderSummary is suspended. The default value is false.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date of the original order associated with this OrderSummary.


-----

```
OrderLifeCycleType
OrderNumber
OrderProductLineCount
OriginalOrderId

```

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether the OrderSummary is managed by Salesforce Order Management
(MANAGED) or by an external system (UNMANAGED). An unmanaged OrderSummary is
stored in Salesforce for reference purposes.

**•** Some Order Management APIs reject input records that are associated with unmanaged
OrderSummaries.

**•** Order Management does not update financial bucket fields on some records that are
associated with unmanaged OrderSummaries.

**•** A user with the EditUnmanagedOrderSummaries or B2BCommerceIntegrator permission
can edit certain fields on objects related to unmanaged OrderSummaries that are normally
only accessible via APIs.

Possible values are:

**•** `MANAGED—Managed`

**•** `UNMANAGED—Unmanaged`

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderSummary.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of unique products ordered on this Order Summary.

This field is available in API version 52.0 and later.

**Type**
reference


-----

```
OwnerId
PoDate
PoNumber

```

**Properties**
Filter, Group, Sort

**Description**
ID of the original order associated with this OrderSummary.

This field is a relationship field.

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
The ID of the user who currently owns this OrderSummary. Default value is the ID of the user
who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Purchase order date associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is available in API version 52.0 and later.

**Type**
string


-----

```
Pricebook2Id
RoutingAttempts
SalesChannelId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Purchase order number associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the pricebook associated with this OrderSummary.

This field is available in API version 54.0 and later.

This field is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The number of attempts that have been made to route the order summary to inventory
locations.

This field is available in API version 51.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the SalesChannel associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.


-----

```
SalesStoreId
SourceProcess
Status

```

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
ID of the RetailStore or WebStore associated with this OrderSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the order process that created the OrderSummary.

Possible values are:

**•** `Exchange` The OrderSummary was created by an Exchange process

**•** `OrderOnBehalf` The OrderSummary was created by an Order on Behalf Of process

**•** `Standard` The OrderSummary was not created by an Order on Behalf Of or Exchange
process

This field is available in API version 57.0 and later.

**Type**
picklist


-----

```
SourceOrderSummaryId
TaxLocaleType

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the order summary. Unlike the Status and Status Category fields on the order and
FulfillmentOrder objects, this field is optional.

We recommend that you use the same values in this picklist that you use in the Status picklist
for the order object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source order summary that’s associated with this OrderSummary.

This field is populated when the SourceProcess of this OrderSummary is an exchange process.

**Relationship Name**
SourceOrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original Order associated with the OrderSummary.
Gross usually applies to taxes like value-added tax (VAT), and Net usually applies to taxes like
sales tax. Automatic taxes use currency to determine if the tax is added on top of the price
(excluded) or included in the price.

Possible values are:

**•** `Gross` (displays most prices and taxes as combined values)

**•** `Net` (displays most prices and taxes as separate values)

**•** `Automatic` (displays most prices and taxes as combined or separate, based on
the currency)

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

This field is available in API version 49.0 and later.


-----

```
TotalAdjDelivery
AmtWithTax
TotalAdjDistAmount
TotalAdjDist
AmountWithTax
TotalAdjDistTaxAmount
TotalAdjFeeAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of all OrderItemSummaries of type Delivery Charge belonging to this
OrderSummary, inclusive of item-level adjustments and tax. This amount is equal to
TotalAdjustedDeliveryAmount + TotalAdjustedDeliveryTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of distributed adjustments applied to OrderItemSummaries belonging to this
OrderSummary. This amount is equal to TotalProductAdjDistAmount plus
TotalDeliveryAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of distributed adjustments applied to OrderItemSummaries belonging to this
OrderSummary, inclusive of tax. This amount is equal to TotalAdjDistAmount plus
TotalAdjDistTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalAdjProduct
AmtWithTax
TotalAdjusted
DeliveryAmount
TotalAdjusted
DeliveryTaxAmount
TotalAdjustedFeeAmount
TotalAdjusted
FeeTaxAmount

```

**Description**
Total amount of all OrderItemSummaries of type Fee belonging to this OrderSummary,
inclusive of item-level adjustments and tax. This amount is equal to TotalAdjustedFeeAmount
plus TotalAdjustedFeeTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of all OrderItemSummaries of type code Product belonging to this
OrderSummary, inclusive of item-level adjustments and tax. This amount is equal to
TotalAdjustedProductAmount plus TotalAdjustedProductTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including item-level adjustments but not order-level adjustments or tax, of all
OrderItemSummaries of type Delivery Charge belonging to this OrderSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustedDeliveryAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including item-level adjustments but not order-level adjustments or tax, of all
OrderItemSummaries of type Fee belonging to this OrderSummary.

This field is available in API version 56.0 and later.

**Type**
currency


-----

```
TotalAdjustedProduct
Amount
TotalAdjustedProduct
TaxAmount
TotalAmount
TotalDeliveryAdj
DistAmount
TotalDeliveryAdj
DistAmtWithTax

```

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustedFeeAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including item-level adjustments but not order-level adjustments or tax, of all
OrderItemSummaries of type code Product belonging to this OrderSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustedProductAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of all OrderItemSummaries belonging to this
OrderSummary. Equal to TotalAdjustedProductAmount plus TotalAdjustedFeeAmount plus
TotalAdjustedDeliveryAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Delivery
Charge belonging to this OrderSummary. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header.

**Type**
currency


-----

```
TotalDeliveryAdj
DistTaxAmount
TotalDeliveryAmount
TotalDeliveryAmount
WithTax
TotalDeliveryTaxAmount

```

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Delivery
Charge belonging to this OrderSummary, inclusive of tax. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header. It is equal to TotalDeliveryAdjDistAmount + TotalDeliveryAdjDistTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjDistAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the Total Line Amounts of all OrderItemSummaries of type Delivery Charge belonging
to this OrderSummary, not including adjustments or tax.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all OrderItemSummaries of type Delivery Charge belonging to this OrderSummary,
including tax but not including adjustments. It is equal to TotalDeliveryAmount +
TotalDeliveryTaxAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.


-----

```
TotalFeeAdjDistAmount
TotalFeeAdj
DistAmtWithTax
TotalFeeAdj
DistTaxAmount
TotalFeeAmount
TotalFeeAmountWithTax

```

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Fee
belonging to this OrderSummary. This value includes OrderItemAdjustmentLineSummaries
that belong to OrderAdjustmentGroupSummaries of type Header.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type Fee
belonging to this OrderSummary, inclusive of tax. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header. It is equal to TotalFeeAdjDistAmount + TotalFeeAdjDistTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjDistAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the Total Line Amounts of all OrderItemSummaries of type Fee belonging to this
OrderSummary, not including adjustments or tax.

This field is available in API version 56.0 and later.

**Type**
currency


-----

```
TotalFeeTaxAmount
TotalProductAdj
DistAmount
TotalProductAdj
DistAmtWithTax
TotalProductAdj
DistTaxAmount

```

**Properties**
Filter, Nillable, Sort

**Description**
Total of all OrderItemSummaries of type Fee belonging to this OrderSummary, including tax
but not including adjustments. It is equal to TotalFeeAmount + TotalFeeTaxAmount.

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
Total of all order-level price adjustments applied to OrderItemSummaries of type code
Product belonging to this OrderSummary. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all order-level price adjustments applied to OrderItemSummaries of type code
Product belonging to this OrderSummary, inclusive of tax. This value includes
OrderItemAdjustmentLineSummaries that belong to OrderAdjustmentGroupSummaries of
type Header. It is equal to TotalProductAdjDistAmount + TotalProductAdjDistTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAdjDistAmount.


-----

```
 TotalProductAmount
 TotalProductAmount
 WithTax
 TotalProductTaxAmount
 TotalTaxAmount

##### Associated Objects

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the Total Line Amounts of all OrderItemSummaries of type code Product belonging
to this OrderSummary, not including adjustments or tax.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all OrderItemSummaries of type code Product belonging to this OrderSummary,
including tax but not including adjustments. It is equal to TotalProductAmount +
TotalProductTaxAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

This field is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax on all OrderItemSummaries belonging to this OrderSummary. Equal to
TotalAdjustedDeliveryTaxAmount plus TotalAdjustedFeeTaxAmount plus
TotalAdjustedProductTaxAmount.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**OrderSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

**OrderSummaryFeed**

Feed tracking is available for the object.

**OrderSummaryOwnerSharingRule**

Sharing rules are available for the object.

**OrderSummaryShare**

Sharing is available for the object.

SEE ALSO:

FulfillmentOrder

Order

OrderItemSummary

OrderPaymentSummary

OrderSummaryRoutingSchedule

PendingOrderSummary

SalesChannel
