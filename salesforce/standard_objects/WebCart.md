#### WebCart

Represents an online shopping cart for a store built with B2B Commerce or D2C Commerce, with total amounts for products, shipping
and handling, and taxes. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The WebCart object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AccountId
BillingAddress
BillingCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account that owns this `WebCart. In API version 51.0 and later, if the` `WebCart`
was created through Guest Browsing, this ID is the ID of the `GuestBuyerProfile.`

This field is a polymorphic relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
The mailing address to which this `WebCart` is billed.

**Type**
string


-----

```
BillingCountry
BillingGeocodeAccuracy
BillingLatitude
BillingLongitude

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the billing address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy rating of the geocode for the billing address. Possible values are:

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
The latitude of the geocode for the billing address.

**Type**
double


-----

```
BillingPostalCode
BillingState
BillingStreet
CurrencyIsoCode
GrandTotalAmount

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the geocode for the billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the billing address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the billing address. Enter up to 255 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`
Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions with multi-currency enabled, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

**Type**
currency


-----

```
GuestCompanyName
GuestEmailAddress
GuestFirstName
GuestLastName
GuestPhoneNumber

```

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items’ `TotalAmount, or` `WebCart TotalAmount` plus `WebCart`
```
  TotalTaxAmount. This value includes all taxes and adjustments.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with a delivery for a guest customer. This field is available in API
version 59.0 and later.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name (or surname) of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
phone


-----

```
GuestSecondName
InitialOrderReferenceNumber
InventoryReservationIdentifier
IsRepricingNeeded

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The second name of a guest buyer.

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier assigned to the WebCart at the beginning of the checkout process. Initially
populated when the checkout process is initiated, the
`InitialOrderReferenceNumber` is then associated with the order created when
the checkout is complete.

This field is available in API version 61.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

This field is available in API version 57.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the cart has changed since the last repricing. The default value is false.


-----

```
IsSecondary
LastRepricingDate
Name
OwnerId
PaymentGroupId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the cart is a secondary cart or a primary cart.

This field is available in API version 52.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when the last repricing was done.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `WebCart` record. `Name` can be up to 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this `WebCart.`

This field is a polymorphic relationship field.

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


-----

```
PaymentMethodId
PoNumber
Status

```

**Description**
The ID of the `WebCart` payment group.

This field is a relationship field.

**Relationship Name**
PaymentGroup

**Relationship Type**
Lookup

**Refers To**
PaymentGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The method of payment for this `WebCart.`

This field is a polymorphic relationship field.

**Relationship Name**
PaymentMethod

**Relationship Type**
Lookup

**Refers To**
AlternativePaymentMethod, CardPaymentMethod, DigitalWallet

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The purchase order number. Enter up to 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of this `WebCart. Possible values are:`

**•** `Active—Cart is created and available for modifications, like adding or removing products`
or promotions.

**•** `Checkout—Cart is in checkout. If the customer modifies the cart, the current checkout`
session is canceled.


-----

```
TaxLocaleType
TaxType
TotalAdjustmentAmount
TotalAmount

```


**•** `Closed—Checkout is complete and an order was created. The cart cannot be modified.`

**•** `PendingClosed—Cart is marked to be closed, but the request isn't completed yet.`
The cart can’t be modified. This value is available in API version 57.0 and later.

**•** `PendingDelete—Cart is marked for delete, but the request isn't completed yet. The`
cart can’t be modified.

**•** `Processing—Cart is processing. For example, taxes are being calculated. The cart`
can’t be modified.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of tax locale. Possible values are:

**•** `Net`

**•** `Gross`

This field is available in API versions 52.0 to 54.0.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of tax policy. Possible values are:

**•** `Automatic`

**•** `Net`

**•** `Gross`

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that reflects the total of all adjustments to the cart subtotal. Adjustments
include item, tier, and cart level discounts.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalAmountAfterAllAdjustments
TotalCartLevelAdjAmount
TotalChargeAmount
TotalChargeTaxAmount
TotalLineItemsWithErrors

```

**Description**
The sum of all cart items’ `TotalPrice, or` `TotalProductAmount` plus
```
  TotalChargeAmount. If the store tax type is Gross, the sum includes taxes.

```
[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required and must have a value greater than or equal to zero](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
(0).

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all cart items after all price adjustments are applied. Adjustments include various
types of discounts.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total cart level discount amount for the cart.

This field is available in API version 61.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all cart items’ `TotalPrice` for cart items of the type `Charge.`

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalTaxAmount for cart items of the type` `Charge.`

**Type**
int


-----

```
TotalListAmount
TotalProductAmount
TotalProductCount
TotalProductItemAdjAmount
TotalProductLineItemCount

```

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
A calculated field that shows the total number of cart line items of type `Product` with
errors.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Sum of all the cart items’ `TotalListPrice.`

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalPrice` for cart items of the type `Product.`

**Type**
double

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A count of all the products in the `WebCart.`

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total item level discount amount for the cart.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


-----

```
TotalProductListAmount
TotalProductTaxAmount
TotalPromoAdjustmentAmount
TotalPromoAdjustmentTaxAmount
TotalTaxAmount

```

**Description**
A calculated field that shows the total number of cart line items of type `Product.`

This field is available in API version 60.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ TotalListAmount for the CartItem type Product.

This field is available in API version 59.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The sum of all the cart items’ `TotalTaxAmount for the` `CartItem` type `Product.`

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The total of all item discounts related to product promotions.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The total tax adjustment for all item discounts related to product promotions.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
Type
UniqueProductCount
WebStoreId

##### Usage Notes

```

**Description**
The sum of all cart items’ `TotalTaxAmount, or` `TotalProductTaxAmount` plus
```
  TotalDeliveryTaxAmount.

```
**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The `WebCart` type. Default value is `Cart. Possible values are:`

**•** `Cart`

**•** `PayNowReadOnly`

**•** `ReadOnly`

**•** `Template`

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The count of unique product SKUs in the `WebCart.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The store ID related to this `WebCart.`

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore



**•** In a B2B Commerce for Lightning store, customers who created custom components for adding items to carts noticed that, after
adding items, the cart badge didn’t refresh. A hard refresh causes the value to properly update.


-----

##### Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**WebCartChangeEvent (API version 58.0)**
Change events are available for the object.

**WebCartHistory**

History is available for tracked fields of the object.

**WebCartOwnerSharingRule**

Sharing rules are available for the object.

**WebCartShare**

Sharing is available for the object.

SEE ALSO:

[Commerce Webstore Cart Promotions](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

[Commerce Webstore Promotions, Associate Action](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_associate.htm)

[Commerce Webstore Promotions, Execute Action](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_execute.htm)

_[Salesforce DX Developer Guide: Get Started with Scratch Org](https://developer.salesforce.com/docs/atlas.en-us.254.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_snapshots_get_started.htm)_
