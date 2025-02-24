#### CartItem

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple promotional adjustments, the order in which the shipping promotion
is applied.


Represents an item in a `WebCart` that’s active in a store built with B2B or D2C Commerce. Cart item can be of type `Product` or
```
Charge. This object is available in API version 49.0 and later.

##### Supported Calls
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The CartItem object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustmentAmount
AdjustmentTaxAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Non-itemized adjustments for this cart item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The tax that’s calculated on the AdjustmentAmount.


-----

```
CartDeliveryGroupId
CartId
ChildProductCount
CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the `CartDeliveryGroup that’s associated with a cart item.`

This field is a relationship field.

**Relationship Name**
CartDeliveryGroup

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the `WebCart` that’s associated with a cart item.

This field is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of child products associated with this cart item. If a child product is a
bundle, its own ChildProductCount is included in this total. For simple products that
don’t have any child products, the ChildProductCount value is zero.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
DistributedAdjustmentAmount
DistributedAdjustmentTaxAmount
GrossAdjustmentAmount
GrossUnitPrice

```

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`
Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the amount of a cart-wide promotional adjustment when
distributed across all items in the cart. This field is for display purposes only and is valid only
during checkout. This field is available in API version 52.0 and later.

You receive $10 off, and there are 5 items in the cart. The distributed adjustment is (-$2).

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the amount of a cart-wide tax adjustment due to
promotions when distributed across all items in the cart. This field is available in API version
52.0 and later.

EXAMPLE: Your discount causes a cart-wide tax reduction of (-$10), and there are 5 items in
the cart. The distributed tax adjustment is (-$2).

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The gross amount of the price adjustment on the cart item (tax inclusive). This is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gross amount of the unit price for a cart item (tax inclusive). This is available in API version
55.0 and later.


-----

```
ItemizedAdjustmentAmount
ItemizedAdjustmentTaxAmount
ListPrice
Name
NetAdjustmentAmount

```

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the total amount of promotional adjustments that are
specific to an item. This field is available in API version 52.0 and later.

EXAMPLE: One cart item has one discount code for $10 off. Your itemized adjustment amount
is (-$10) for that item.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the total amount of promotion-related tax adjustments
that are specific to an item. This field is available in API version 52.0 and later.

EXAMPLE: One cart item has one discount code for $10 off. This reduces the tax on that item
by (-$2). Your itemized adjustment tax amount is (-$2) for that item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The original price of the cart item. Typically shown with a line through it. List price is shown
only when it’s higher than the negotiated price. If the list price is the same or lower, it isn’t
shown to the buyer. This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartItem` record. Name can be up to 255 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
NetUnitPrice
ParentCartItemId
PerUnitWeight
Product2Id

```

**Description**
The net amount of the price adjustment made on the cart item (tax exclusive). This is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net amount of the unit price for the cart item (tax exclusive). This is available in API
version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the cart item's parent CartItem. The value is empty if the item is a top-level cart
item.

This field is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Lookup

**Refers To**
CartItem

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Weight per unit of this cart item, in the unit specified by WeightUnit. This field is available
in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a product type cart item. Cart items can be of type `PRODUCT` or CHARGE.


-----

```
ProductClass
ProductRelatedComponentId
ProductValidationKey

```

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The product class of the cart item. Default value is Simple. Possible values are:

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the cart item's `ProductRelatedComponent. The`
```
  ProductRelatedComponent represents a product that is included in a product

```
bundle, a set, or a product and an add-on. The ProductRelatedComponent is empty
if the item is a top-level cart item.

This field is a relationship field.

**Relationship Name**
ProductRelatedComponent

**Relationship Type**
Lookup

**Refers To**
ProductRelatedComponent

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Quantity
SalesPrice
Sku
StockCheckMethod
TaxTreatmentId

```

**Description**
The product validation key of the cart item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of a given cart item in a cart.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The discounted price of a cart item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Shelf-Keeping Unit ID of a cart item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines how inventory is assessed for a cart item that’s part of a bundle or set. Possible
values are:

**•** `ChildProducts—Inventory is assessed based on the child product or products.`

**•** `ParentProduct—Inventory is assessed based on the parent product.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax treatment for the cart item.


-----

```
TotalAdjustmentAmount
TotalAmount
TotalLineAmount
TotalLineGrossAmount
TotalLineNetAmount

```

This field is available in API version 63.0 and later. This field is available with Subscription
Management.

This field is a relationship field.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total amount of all promotional adjustments on the item, both distributed and itemized.
This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total cost of this cart item, including taxes and adjustments.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, based on sales price and quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount of the line item (tax inclusive). This is available in API version 55.0
and later.

**Type**
currency


-----

```
TotalLineTaxAmount
TotalListPrice
TotalPrice
TotalPriceAfterAllAdjustments

```

**Properties**
Filter, Nillable, Sort

**Description**
The total net amount of the line item (tax exclusive). This is available in API version 55.0 and
later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total tax amount for TotalLineAmount.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, based on ListPrice. We provide this value for comparison.
It's not the price that the buyer is paying.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, including adjustments but excluding taxes.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total price after all price adjustments are applied. This field is available in API version 52.0
and later.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)


-----

```
TotalPriceTaxAmount
TotalPromoAdjustmentAmount
TotalPromoAdjustmentTaxAmount
TotalTaxAmount
TotalWeight
Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax amount for a cart item before promotional adjustments, including quantity-based
adjustments. This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Total itemized and distributed adjustment amount in cart (only for promotions). This field is
available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total itemized and distributed adjustment tax amount in cart (only for promotions). This
field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax amount for this cart item. This value includes taxes for both TotalLineAmount
and AdjustmentAmount.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total weight of this cart item, in the unit specified by WeightUnit. This field is available
in API version 62.0 and later.

**Type**
picklist


-----

```
UnitAdjustedPrice
UnitAdjustedPriceWithItemAdj
UnitAdjustmentAmount
UnitItemAdjustmentAmount
WeightUnit

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The `CartItem` type. Possible values are:

**•** `Product`

**•** `Charge`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Price per quantity unit after a tier discount or surcharge is applied. This field is available in
API version 50.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price, including both tier and item level discounts, for the item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tier discount or surcharge to apply to a quantity unit. This amount is added to the
`SalesPrice` to get the UnitAdjustedPrice. This field is available in API version
50.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Item level adjustments made to the unit price for the item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
Unit of measurement for the weight of the cart item. This field is available in API version 62.0
and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`

##### Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

[Commerce Webstore Cart Promotions](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

[Commerce Webstore Promotions, Associate Action](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_associate.htm)

[Commerce Webstore Promotions, Execute Action](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_execute.htm)

CartDeliveryGroup

WebCart
