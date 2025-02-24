#### OrderDeliveryGroupSummary

Represents the current properties and state of a group of OrderItemSummaries, belonging to one OrderSummary, to be fulfilled using
the same delivery method and delivered to the same address. A single shipment can include them all, but that isn’t guaranteed.
Corresponds to one or more order delivery group objects, consisting of an original object and any change objects applicable to it. This
object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

##### Fields

```
CurrencyIsoCode
DeliverToAddress
DeliverToCity
DeliverToCompanyName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderDeliveryGroupSummary. The default value is USD.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

This field is available in API version 49.0 and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
Address of the recipient. Users with the Edit Delivery Information user permission can modify
this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address city.

**Type**
string


-----

```
DeliverToCountry
DeliverToFullFirstName
DeliverToFullLastName
DeliverToFullName
DeliverToFullSalutation

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address country.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Possible values are:

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Prof.`


-----

```
DeliverTo
GeocodeAccuracy
DeliverToLatitude
DeliverToLongitude
DeliverToName

```

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

**Description**
Used with FulfilledToLatitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
DeliverToPostalCode
DeliverToState
DeliverToStreet
DeliveryInstructions
Description

```

**Description**
Name on the recipient address. Users with the Edit Delivery Information user permission can
modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

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
textarea

**Properties**
Create, Nillable, Update

**Description**
Special instructions for the delivery. Users with the Edit Delivery Information user permission
can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
textarea


-----

```
DesiredDeliveryDate
EmailAddress
GiftMessage
GrandTotalAmount

```

**Properties**
Create, Nillable, Update

**Description**
Description of the OrderDeliveryGroupSummary.

This field can be edited.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Desired date for delivery. This field is informational, available for customizations. Users with
the Edit Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the recipient. Users with the Edit Delivery Information user permission can
modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Gift message to include. Users with the Edit Delivery Information user permission can modify
this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency


-----

```
IsGift
OrderDeliveryGroup
SummaryNumber
OrderDeliveryMethodId
OrderSummaryId

```

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the delivery charges associated with the
OrderDeliveryGroupSummary. This value only includes OrderItemSummaries of type code
Charge.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the OrderDeliveryGroupSummary represents a gift. Users with the Edit
Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the OrderDeliveryGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the order delivery method specified for the OrderDeliveryGroupSummary. Users with
the Edit Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderDeliveryGroupSummary.


-----

```
OriginalOrderDelivery
GroupId
PhoneNumber
PromisedDeliveryDate
TotalAdjustmentAmount
TotalAdjustment
AmtWithTax

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original order delivery group associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the recipient. Users with the Edit Delivery Information user permission can
modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Promised date for delivery. This field is informational, available for customizations. Users with
the Edit Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price adjustments applied to delivery charges associated with the
OrderDeliveryGroupSummary. This value only includes adjustments to OrderItemSummaries
of type code Charge.

**Type**
currency


-----

```
TotalAdjustment
TaxAmount
TotalAmount
TotalLineAmount
TotalLineAmtWithTax

```

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges associated with the
OrderDeliveryGroupSummary, inclusive of tax. This amount is equal to
TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

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
Total, including adjustments but not tax, of the delivery charges associated with the
OrderDeliveryGroupSummary. This value only includes adjustments to OrderItemSummaries
of type code Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, not including adjustments or tax, of the delivery charges associated with the
OrderDeliveryGroupSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges associated with the OrderDeliveryGroupSummary, inclusive of
tax. This amount is equal to TotalLineAmount + TotalLineTaxAmount.

This field is available in API version 49.0 and later.


-----

```
 TotalLineTaxAmount
 TotalTaxAmount

##### Associated Objects

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderDeliveryGroupSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

OrderDeliveryGroup

OrderItemSummary
