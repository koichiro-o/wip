#### CartDeliveryGroup

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique reference number the shopper can use to refer to the order. In API version 63.0 and
later, LWR stores don't populate this field upon checkout. Instead, the
```
  InitialOrderReferenceNumber field on the WebCart object is populated.

```
**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The current state of the checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the cart that is used to create the checkout session.


Represents shipping information for the delivery of items in an order against a store built with B2B Commerce or D2C Commerce. This
object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The CartDeliveryGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
CartId
CompanyName
CurrencyIsoCode
DeliverToAddress
DeliverToCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID the `WebCart on page 5422` that’s associated with this delivery group.

This field is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with a delivery. This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`
Possible values are:

**•** `USD—U.S. Dollar`

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address to which a buyer order is delivered.

**Type**
string


-----

```
DeliverToCountry
DeliverToFirstName
DeliverToGeocodeAccuracy
DeliverToLastName

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city to which a buyer order is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country to which a buyer order is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of the person set to receive an order. This field is available in API version 57.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The geocode location to which a buyer order is delivered. Possible values are:

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
string


-----

```
DeliverToLatitude
DeliverToLongitude
DeliverToName
DeliverToPostalCode
DeliverToState

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name of the person to whom a buyer order is delivered. This field is available in API
version 57.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of a buyer delivery location.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of a buyer delivery location.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the person to which to deliver a buyer order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code to which to deliver a buyer order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state to which to deliver a buyer order.


-----

```
DeliverToStreet
DeliveryMethodId
DesiredDeliveryDate
GrandTotalAmount
IsDefault

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street to which to deliver a buyer order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID for the delivery method to use to deliver a buyer order. Populated if the selected
`CartDeliveryGroupMethod only has the` `ShippingFee` populated, but it has
reference to an existing `DeliveryMethodId` which contains the fields Carrier,
```
  ClassOfService, and ReferenceNumber. If not, the
  SelectedDeliveryMethod field is used.

```
This field is a relationship field.

**Relationship Name**
DeliveryMethod

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryMethod

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that a buyer requests to have an order delivered.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items’ TotalAmount, or CartDeliveryGroupTotalAmount plus
```
  CartDeliveryGroup TotalTaxAmount.

```
**Type**
boolean


-----

```
Name
SelectedDeliveryMethodId
ShipToPhoneNumber

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the delivery group is the default. This field is available in API version 59.0 and
later.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartDeliveryGroup record.` `Name` can be up to 255 characters. In
API version 62.0 and later, if IsDefault is true, the Name is Shipment1, a localized
string. In prior API versions, the Name for a default delivery group was `Cart Delivery`
```
  Group. Due to this change, any queries intended to identify default delivery groups should

```
use the `IsDefault` rather than Name field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the selected cart delivery group method. Populated if the selected
`CartDeliveryGroupMethod` has the fields Carrier, ClassOfService,
`ReferenceNumber, and` `ShippingFee, but the DeliveryMethodId` is null. If
not, the DeliveryMethodId field is used. This field is available in API version 59.0 or
later.

This field is a relationship field.

**Relationship Name**
SelectedDeliveryMethod

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroupMethod

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number associated with a delivery. This field is available in API version 59.0 and later.


-----

```
ShippingInstructions
TotalAdjustmentAmount
TotalAdjustmentTaxAmount
TotalAmount
TotalCartItemCount
TotalChargeAmount

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Instructions for delivering an order.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of all promotional adjustments on the cart delivery group. This field is
available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total tax amount for all promotional adjustments on the cart delivery group. This field
is available in API version 54.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items `TotalPrice, or` `TotalProductAmount` plus
```
  TotalChargeAmount.

```
**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of cart items, including their quantities, of the type PRODUCT in the delivery group.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalChargeTaxAmount
TotalProductAmount
TotalProductTaxAmount
TotalTaxAmount

##### Associated Objects

```

**Description**
Cart items can be of type Product or Charge. This field contains the sum of all the cart items
`TotalPrice` for all cart items of the `CHARGE type.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Cart items can be of type Product or Charge. This field contains the Sum of all the cart items
`TotalTaxAmount` for all cart items of the `CHARGE type.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Cart items can be of type Product or Charge. This field contains the sum of all the cart items
`TotalPrice` for all cart items of the `PRODUCT type.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Cart items can be of type Product or Charge. Sum of all the cart items TotalTaxAmount
for all cart items of the `PRODUCT` type.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items TotalTaxAmount, or TotalProductTaxAmount plus
```
  TotalChargeTaxAmount.

```

**CartDeliveryGroupChangeEvent (API version 58.0)**
Change events are available for the object.


-----
