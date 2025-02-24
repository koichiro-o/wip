#### OrderItem

Represents an order product that your organization sells.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
The user must have Edit permission on Order records to create or update order products on an order. The user must have Edit permission
on Order records to delete an order product.

##### Fields

```
AdjustedLineAmount
AdjustedLineAmtWithTax
AvailableQuantity

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Line amount following line adjustments, excluding tax.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Line amount following line adjustments, including tax.

This field is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v49.0 and later.

**Type**
double


-----

```
BillingFrequency2
CurrencyIsoCode
DeliveryEstimationReference

```

**Properties**
Filter, Nillable, Sort

**Description**
Amount of an order product that is available to be reduced. Value must be greater
than or equal to 0. An order product is reducible only if AvailableQuantity
is greater than 0.

Value is always 0 if the order product’s parent order is a reduction order.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period that indicates how often the order item is billed.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

Possible values are:

**•** `Annual`

**•** `Monthly`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for the currency of the original Order associated with the OrderItem.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
DeliveryEstimationTimeZone
Description
EarliestEstimatedDeliveryDate
EarliestEstimatedDeliveryTime
EndDate
GrossUnitPrice

```

**Description**
Unique reference ID for the delivery estimation.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Timezone in which the estimated delivery times are based.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of this object. For Commerce stores, during checkout, this field
is populated with the value of a product name. The product name is copied from
the CartItem.Name field of a cart item that corresponds to the OrderItem.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Earliest date when the item is estimated to be delivered.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Earliest time of the day when the item is estimated to be delivered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. Last day the order product is available.

**Type**
currency


-----

```
LastEstimatedDeliveryDate

```
LastEstimatedDeliveryTime
```
LineNumber
ListPrice

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price including tax.

This field is a VAT field that includes tax. Salesforce populates it on order creation
only when Order.TaxLocaleType has a value of Gross.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Latest date when the item is estimated to be delivered.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Latest time of the day when the item is estimated to be delivered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Used to organize lines on the order.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
List price for the order product. Value is inherited from the associated
```
  PriceBookEntry upon order product creation.

```

-----

```
ListPriceTotal
NetUnitPrice
OrderActionId
OrderDeliveryGroupId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The `ListPrice` times the Quantity. This field is a calculated field.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price after all price adjustments are applied.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related order action. The order action indicates the type of order;
for example, a new sale or a cancellation.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

This field is a relationship field.

**Relationship Name**
OrderAction

**Relationship Type**
Lookup

**Refers To**
OrderAction

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The delivery group for the order product.


-----

```
OrderId
OrderItemNumber
OriginalOrderItemId

```

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

This field is a relationship field.

**Relationship Name**
OrderDeliveryGroup

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the order that this order product is a child of.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Automatically generated number that identifies the order product.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required if `isReductionOrder` on the parent order is `true.`

ID of the original order product being reduced.

This field is a relationship field.


-----

```
PeriodBoundary
PeriodBoundaryDay
PeriodBoundaryStartMonth

```

**Relationship Name**
OriginalOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The period boundary helps determine the start and end date of the billing periods.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

Possible values are:

**•** `AlignToCalendar—the period starts on the first day of the term unit;`
for example, the first day of the month.

**•** `Anniversary—The start date determines the boundary. For example, if`
a monthly subscription starts on September 13, the subscription starts on
the 13th day of each month.

**•** `DayOfPeriod—the period starts on the day indicated by`
```
   PeriodBoundaryDay.

```
**•** `LastDayOfPeriod—the period starts on the last day of the pricing term`
unit; for example, the last day of the month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when `PeriodBoundary` is DayOfPeriod. Indicates day of the
week or month that marks the period boundary. Must be an integer from 1
through 31.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update


-----

```
PricebookEntryId
PricingTermCount

```

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and
PeriodBoundaryDay when BillingFrequency2 is Annual or by manual user entry.
Possible values are:

**•** `1-January`

**•** `2-February`

**•** `3-March`

**•** `4-April`

**•** `5-May`

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
Required. ID of the associated PricebookEntry. This field must be specified when
creating OrderItem records. It can’t be changed in an update.

If they have a B2B Commerce, B2B Commerce Starter, B2B Commerce Growth,
or B2B Commerce Plus license, Salesforce users can create orders without price
books and order items without price book entries.

This field is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
PricingTransactionType

```

**Description**
A calculated field indicating the number of pricing terms in the subscription.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of pricing transaction. For example, a new sale, a cancellation,
an amendment, or a renewal.

Possible values:

**•** `AmendmentAtLastNegotiatedPrice—Calculate the price of the`
amended order item using the same price book and price adjustments as
the new sale item. For example, an order item that is amended using a pricing
transaction type of AmendmentAtLastNegotiatedPrice is priced using the
same price book information and price adjustments as the new sale item.
The amended order item has the same price as the new sale order item.

**•** `AmendmentStartingFromListPrice—Calculate the price of the`
amended order item using current price book information, disregarding any
pricing information or adjustments that were applied to the new sale item.
Typically, an amended order item has a different price than the new sale
transaction item.

**•** `Cancellation—Calculate the price of the canceled transaction. For`
example, let’s say that a 1-year subscription was purchased on January 1,
then canceled on July 31. The price of the canceled products and services
from August 1 through Dec 31 is calculated.

**•** `NewSale—The price of a new transaction is calculated.`

**•** `RenewalAtLastNegotiatedPrice—Calculate the price of the order`
item using the same price book and price adjustments as the new sale item.
For example, an order item that is renewed using a pricing transaction type
of RenewalAtLastNegotiatedPrice is priced using the same price
book information and price adjustments as the new sale item. The renewal
order item has the same price as the new sale order item.

**•** `RenewalAtListPrice—Calculate the price of the order item using`
current price book information, disregarding any pricing information or
adjustments that were applied to the new sale item. Typically, a renewal
order item has a different price than the new sale order item.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.


-----

```
ProFormaBillingPeriodAmount
Product2Id
ProductSellingModelId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The initial amount for the billing period. The final amount for the billing period
can include subsequent amendments, discounts, or charges.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Product2 associated with this OrderItem.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related product selling model. The product selling model defines
one method by which a product can be sold; for example, as a one-time sale, an
evergreen subscription, or a termed subscription.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

This field is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel


-----

```
ProrationPolicyId
Quantity
QuoteLineItemId
ReferencePrice

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related proration policy. The proration policy defines how the price
is calculated for each subscription period; for example, whether partial periods
are allowed, and how remainder amounts are handled.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

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
Create, Filter, Sort, Update

**Description**
Required. Number of units of this order product.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the associated quote line item.

If this field is specified, the quote line item’s QuoteId must match the QuoteId
for the order product’s parent order.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The original or reference price of the order product.

This field is available in API version 63.0 and later.


-----

```
RelatedOrderItemID
RoundedLineAmount
RoundedLineAmtWithTax
ServiceDate

```

**Type**
reference

**Properties**
Filter, Sort, Group

**Description**
Required for change orders, shows the original order product.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The rounded line amount, before tax and adjustments. Currency with decimal
values of 0.5 and higher are rounded to the next-highest whole unit of currency.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rounded line amount, including tax. Currency with decimal values of 0.5 and
higher are rounded to the next-highest whole unit of currency.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v49.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Start date for the order product.


-----

```
StartingPriceTotal
StartingUnitPriceSource
TaxTreatmentId
TotalAdjustedLineTaxAmount

```

Label is Start Date.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The starting unit price times the quantity.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the starting unit price was entered manually or calculated.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

Possible values are:

**•** `Manual`

**•** `System`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax treatment.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

This field is a relationship field.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
currency


-----

```
TotalAdjustmentAmount
TotalAdjustmentAmtWithTax
TotalAdjustmentDistAmount

```

**Properties**
Filter, Sort

**Description**
Sum of line tax amount and line adjustment tax amounts.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll-up of all the order product’s price adjustments.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll-up of all the order product’s price adjustments, including tax.

This field is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll-up of all adjustments on the order. Used only if the OrderAdjustmentGroup
has a Type value of Header.


-----

```
TotalAdjustmentDistTaxAmount
TotalAdjustmentDistAmtWithTax
TotalAdjustmentTaxAmount

```

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll-up of all adjustment tax amounts on the order. Used only if the
OrderAdjustmentGroup has a Type value of Header.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll-up of all adjustment tax amounts on the order, including tax. Used only if
the OrderAdjustmentGroup has a Type value of Header.

This field is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Sum of all the order product’s tax adjustments.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.


-----

```
TotalAmtWithTax
TotalLineAdjustmentAmount
TotalLineAdjustmentAmtWithTax
TotalLineAdjustmentTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Equals `TotalPrice` + TotalTaxAmount for the order item.

This field is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The sum of line-level adjustments for the order product.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The sum of line-level adjustments for the order product, including tax.

This field is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Total tax amount for adjustments made to the order product.


-----

```
TotalLineAmount
TotalLineTaxAmount
TotalPrice

```

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net total price of the order product, before price adjustments, inclusive of
quantity.

The decimal places for this value must match the decimal places for the currency
being used. For example, if the currency is US dollar, the decimal place for
TotalLineAmount must be 2. If the currency is the Japanese yen, the decimal
place for TotalLineAmount must be 0.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Total tax amount for this order product, excluding tax on adjustments.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price for this order product. The calculations for this field’s value are different
if Commerce Orders are enabled.

**Default Value**
`TotalPrice` = (UnitPrice  - Quantity)


-----

```
TotalTaxAmount
Type
TypeCode

```

**Commerce Orders**
If `TotalLineAmount` is null, (UnitPrice    - Quantity) is sent to
`RoundedLineAmount` and rounded. It’s then sent to `Total Price.`
Otherwise, TotalLineAmount is sent to RoundedLineAmount, rounded,
and then sent to `TotalPrice.`

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Sum of the order product’s tax and any adjustments.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes what the order item represents. Each value is associated with one type
code, shown here in parentheses.

Possible values are:

**•** `Delivery Charge (Charge)` — A charge, such as a delivery fee.

**•** `Fee (Charge)` — A charge, such as a return fee. This value is available
in API v56.0 and later.

**•** `Order Product (Product)` — An item that can be ordered.

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
picklist


-----

```
UnitPrice

##### Usage

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category associated with the type. A type code can be associated with one
or more types.

Possible values are:

**•** `Charge`

**•** `Product`

To access Commerce Orders fields, your org must have a Salesforce Order
Management license. Commerce Orders fields are available only in Lightning
Experience.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price for the order product.


An order can have associated order product records only if the order has a price book associated with it. An order product must correspond
to a product that is listed in the order’s price book.

Orders with associated OrderItem records are affected. When OrderItem records are directly deleted, they aren’t sent to the recycle bin
and can’t be undeleted. The getDeleted() call shows deleted OrderItem records until they’re purged, which is usually within the
same day or the next day.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemChangeEvent (API version 44.0)**
Change events are available for the object.

**OrderItemFeed (API version 29.0)**
Feed tracking is available for the object.


-----

**OrderItemHistory**

History is available for tracked fields of the object.

SEE ALSO:

Order

OrderItemSummary
