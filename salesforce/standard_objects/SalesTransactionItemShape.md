#### SalesTransactionItemShape

Defines the business logic for a sales transaction shape item, for example, an item in an order. This object is available in API version 57.0
and later.

This object is visible in Object Manager for customization; for example, you can create custom fields for this object.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), query(), retrieve()

 Special Access Rules

```
This object is available with Subscription Management, B2B Commerce, or B2C Commerce.

##### Fields

```
BasisTransactionItemShapeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the sales transaction shape item to use as a reference when pricing this transaction.
For example, when pricing an order, this field refers to the order being canceled. This field
is available if Subscription Management is enabled.

This field is a relationship field.


-----

```
BillingFrequency
EndDate
ListPrice
ListPriceTotal

```

**Relationship Name**
BasisTransactionItemShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period that indicates how often the sales transaction shape item is billed. This field
is available if Subscription Management is enabled.

Possible values are:

**•** `Annual`

**•** `Monthly`

**•** `Quarterly`

**•** `Semi-Annual`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The last day the sales transaction shape item is available. For example, the last day of the
subscription. This field is available if Subscription Management is enabled.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The list price for the sales transaction shape item. This value is inherited from the related
price book entry.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


-----

```
NetUnitPrice
ObligatedAmount
ParentTransactionItemShapeId

```

**Description**
The list price, inclusive of quantity. This calculated field is equal to `ListPrice` times
```
  Quantity.

```
**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The final unit price of the product, after all adjustments are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**

**Description**
In a subscription, the amount a subscriber is billed for products used during the subscription
period that the subscriber returns before the subscription end date. This field's value is the
price for use of the product.

This field is available in version 57.0 and later. This field is available when Subscription
Management is enabled.

Note:

**•** A subscriber must submit a quantity amendment in order to change the
subscription's product quantity. A quantity amendment request is only valid until
the subscription end date.

**•** A subscriber is eligible for a refund only for the periods when the products weren’t
used.

**•** The subscription's proration policy indicates whether the obligated amount and
the refund are prorated for partial periods.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the parent TransactionItemShape.

This field is a relationship field.

**Relationship Name**
ParentTransactionItemShape


-----

```
PeriodBoundary
PeriodBoundaryDay
PeriodBoundaryStartMonth

```

**Refers To**
SalesTransactionItemShape

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The period boundary helps determine the start and end date of the billing periods. This field
is available if Subscription Management is enabled.

Possible values are:

**•** `AlignToCalendar—The period starts on the first day of the term unit, for example,`
the first day of the month.

**•** `Anniversary— The start date determines the boundary. For example, if a monthly`
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod— The period starts on the day indicated by PeriodBoundaryDay.`

**•** `LastDayOfPeriod— The period starts on the last day of the pricing term unit; for`
example, the last day of the month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required when `PeriodBoundary` is DayOfPeriod. Indicates day of the week or
month that marks the period boundary. Must be an integer from 1 through 31. This field is
available if Subscription Management is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay
when BillingFrequency is Annual or by manual user entry. Possible values are:

**•** `1-January`

**•** `2-February`

**•** `3-March`

**•** `4-April`

**•** `5-May`


-----

```
PricebookEntryId
PricingTermCount
PricingTransactionType

```


**•** `6-June`

**•** `7-July`

**•** `8-August`

**•** `9-September`

**•** `10-October`

**•** `11-November`

**•** `12-December`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related price book entry. The related price book entry contains all the pricing
information about the product being sold.

This field is a polymorphic relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntryInterface

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
A calculated field indicating the number of pricing terms in the subscription. This field is
available if Subscription Management is enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of pricing transaction, for example, a new sale, an amendment, or a renewal.
This field is available if Subscription Management is enabled.

Possible values are:

**•** `AmendmentAtLastNegotiatedPrice— Calculate the price of the amended`
sales transaction shape item using the same price book and price adjustments as the


-----

```
ProductId
ProductSellingModelId

```

new sale item. For example, an order item that is amended using a pricing transaction
type of `AmendmentAtLastNegotiatedPrice` is priced using the same price
book information and price adjustments as the new sale item. The amended order item
has the same price as the new sale order item.

**•** `AmendmentStartingFromListPrice— Calculate the price of the amended`
sales transaction shape item using current price book information, disregarding any
pricing information or adjustments that were applied to the new sale item. Typically, an
amended transaction item has a different price than the new sale transaction item.

**•** `Cancellation— Calculate the price of the canceled transaction. For example, let’s`
say that a 1-year subscription was purchased on January 1, then canceled on July 31.
The price of the canceled products and services from August 1 through Dec 31 is
calculated.

**•** `NewSale— The price of a new transaction is calculated.`

**•** `RenewalAtLastNegotiatedPrice— Calculate the price of the renewal sales`
transaction shape item using the same price book and price adjustments as the new
sale item. For example, an order item that is renewed using a pricing transaction type
ofRenewalAtLastNegotiatedPrice is priced using the same price book
information and price adjustments as the new sale item. The renewal order item has the
same price as the new sale order item.

**•** `RenewalAtListPrice— Calculate the price of the renewal sales transaction shape`
item using current price book information, disregarding any pricing information or
adjustments that were applied to the new sale item. Typically, a renewal transaction
item has a different price than the new sale transaction item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related product.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
ProrationPolicyId
Quantity
SalesItemType

```

**Description**
The ID of the related product selling model. The product selling model defines one method
by which a product can be sold; for example, as a one-time sale, an evergreen subscription,
or a termed subscription. This field is available if Subscription Management is enabled.

This field is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related proration policy. The proration policy defines how the price is calculated
for each subscription period; for example, whether partial periods are allowed, and how
remainder amounts are handled. This field is available if Subscription Management is enabled.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Number of units in the sales transaction shape item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of sale.


-----

```
SalesTransactionItemShapeName
SalesTransactionShapeId
StartDate
StartingPriceTotal

```

Possible values are:

**•** `Charge— An item that acts as a fee and can’t be fulfilled. For example, a delivery`
charge, a shipping fee, or a membership fee.

**•** `Product— An item that is a good or service that can be fulfilled. For example, a widget`
or a widget warranty.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Required. The name of the sales transaction shape item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the sales transaction shape. A sales transaction shape is the way in which
the sales transactions occur. For example, a cart, an order, or a quote.

This field is a relationship field.

**Relationship Name**
SalesTransactionShape

**Relationship Type**
Lookup

**Refers To**
SalesTransactionShape

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The start date of the subscription. This field is available if Subscription Management is enabled.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


-----

```
StartingUnitPrice
StartingUnitPriceSource
StockKeepingUnit
SubscriptionTerm

```

**Description**
The starting unit price, inclusive of quantity, prorated for the duration of the subscription.
This field has two ways to obtain its value. The value can be manually entered or automatically
calculated. The calculation is equal to `StartingUnitPrice` times Quantity.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The unit price before any adjustments.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the starting unit price was inherited, entered manually, or calculated.

Possible values are:

**•** `Inherited— The starting unit price is copied from a previous transaction; for example,`
from the order item being renewed.

**•** `Manual— The starting unit price is entered manually, for example, by a sales rep.`

**•** `System — The starting unit price is calculated using pricing information that was`
configured by an administrator; for example, a pricing tier.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The SKU assigned to the related product.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of terms in the subscription. You can indicate a subscription’s length using
either the start and end dates, or by using the start date and the subscription term. This field
is available if Subscription Management is enabled.


-----

```
TotalAdjustmentAmount
TotalAdjustmentDistAmount
TotalLineAmount
TotalPrice

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of all adjustments applied to the related sales transaction shape items, inclusive of
quantity, prorated for the duration of the subscription. Includes distributed price adjustment
items and price adjustment items applied directly. This calculated field is equal to the sum
of `TotalAdjustmentAmount on the related sales transaction shape items.`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The sum of the distributed price adjustment items applied to the sales transaction shape
item, prorated for the duration of the subscription. Doesn’t include price adjustment items
that are applied directly. A distributed price adjustment is automatically created to apply a
transaction-level adjustment to the transaction items. For example, let’s say that you have
an order with two order items: one for a file storage service and another for a video streaming
service. A 10% volume discount and a 15% manual discount are applied to the entire order.
An additional 20% discount is applied to the file storage service. To distribute the order-level
discounts, the system creates a 10% price adjustment item and a 15% price adjustment item
for each order item. In this example, the file storage service’s sales transaction shape item
has the following field values:

**•** `TotalAdjustmentAmount — The sum of all item-level adjustments, including`
the 10% price adjustment item, the 15% price adjustment item, and the 20% price
adjustment item.

**•** `TotalAdjustmentDistAmount— The sum of the distributed item-level`
adjustments, including the 10% price adjustment item and the 15% price adjustment
item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The total price before price adjustments, inclusive of quantity, prorated for the duration of
the subscription. This calculated field is equal to StartingPriceTotal times
```
  PricingTermCount.

```
**Type**
currency


-----

**Properties**
Create, Filter, Nillable, Sort

**Description**
The price after all adjustments, inclusive of quantity, prorated for the duration of the
subscription. This calculated field is equal to TotalAdjustmentAmount plus
```
                StartingPriceTotal.
