#### QuoteLineItem

Represents a quote line item, which is a member of the list of Product2 products associated with a Quote, along with other information
about those line items on that quote. Available in API version 18.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The user must have “Edit” permissions on Quote records in order to create or update quote line items on a quote. The user must have
“Edit” permissions on Quote records to delete a quote line item.

Some of the fields are available when Subscription Management is enabled.

##### Fields

```
BillingFrequency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period that indicates how often the quote line item is billed. This field is available
in API version 55.0 and later. This field is available when Subscription Management is enabled.


-----

```
BindingInstanceTargetId
CurrencyIsoCode
Description
Discount

```

Possible values are:

**•** `Annual`

**•** `Monthly`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the add on product target ID for a usage-based quote line item, order Item, or asset
allocation.

This field is a polymorphic relationship field.

**Relationship Name**
BindingInstanceTarget

**Refers To**
Asset, QuoteLineItem

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Available only for organizations enabled for multiple currencies. Contains the ISO code for
any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2 is specified on the quote (the
`Pricebook2Id` field isn’t blank), then the currency value of this field must match the
currency of the PricebookEntry objects for any associated quote line items.

This value is copied from the related Quote and can't be changed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the line item. Limit: 225 characters.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
DiscountAmount
Division
EffectiveGrantDate
EndDate
EndQuantity

```

**Description**
Editable number from 0 to 100.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The fixed amount discount to apply to the quote line item. Available in API version 59.0 and
later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which the resources associated with the quote line item are granted.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
If the quote line item is sold on subscription, this field indicates the date on which the
subscription ends. This field is available in API version 55.0 and later. This field is available if
Subscription Management is enabled in your org.

You can indicate a subscription’s length using either `StartDate` and `EndDate, or by`
using StartDate and SubscriptionTerm. If you provide a value for both EndDate
and `SubscriptionTerm,` `EndDate` is used to determine the subscription’s length.

**Type**
double


-----

```
IsPrimarySegment
HasQuantitySchedule
HasRevenueSchedule
HasSchedule

```

**Properties**
Filter, Nillable, Sort

**Description**
If the quote line item is sold on a subscription, this field indicates the end quantity when
the subscription ends. This field is available in API version 60.0 and later. This field is available
with Subscription Management.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the segment for the order item is a primary segment (true) or not (false).

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity line item that the quote line item is synced
with has a quantity schedule.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity line item that the quote line item is synced
with has a revenue schedule. If this object has a revenue schedule, the GrandTotal and
`TotalPrice` fields can't be updated. In addition, the Quantity field can't be updated
if this object has a quantity schedule. The system ignores any attempt to update this field.
The update isn't rejected but the updated value is ignored.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the line item uses schedules.


-----

```
LastReferencedDate
LastViewedDate
LineNumber
ListPrice
ListPriceTotal

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user only accessed this record or list view (LastReferencedDate) but not viewed
it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. An automatically generated number identifying the quote line item. In the form
of `QL-XXXXX.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. Corresponds to the UnitPrice on the PricebookEntry that is associated with
this line item, which can be in the standard price book or a custom price book. A client
application can use this information to show whether the unit price (or sales price) of the
line item differs from the price book entry list price.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The `ListPrice` times the `Quantity. This field is a calculated field.`


-----

```
NetTotalPrice
NetUnitPrice
OpportunityLineItemId
ParentQuoteLineItemId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The price after all adjustments, inclusive of quantity, prorated for the duration of the
subscription. This field is a calculated field equal to `TotalAdjustmentAmount` plus
```
  TotalLineAmount.

```
This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The unit price after all price adjustments are applied.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the related opportunity line item. This field is populated by the API during creation of
the quote line item. Not editable. Available in API version 40.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the related line item in the parent quote.

This field is populated by the API during creation of the quote line item.

This field is available in version 58.0 and later. This field is available when Subscription
Management is enabled.

This field is a relationship field.

**Relationship Name**
ParentQuoteLineItem

**Relationship Type**
Lookup


-----

```
PartnerDiscountPercent
PartnerUnitPrice
PeriodBoundary
PeriodBoundaryDay

```

**Refers To**
QuoteLineItem

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The partner’s discount percent applied to the quote lines. Available in API version 59.0 and
later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price after applying the discount given to the partner for the quote line item.
Available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The period boundary helps determine the start and end date of the billing periods.

This field is available in API version 55.0 and later. This field is available with Subscription
Management.

Possible values are:

**•** `AlignToCalendar—the period starts on the first day of the term unit; for example,`
the first day of the month.

**•** `Anniversary—The start date determines the boundary. For example, if a monthly`
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod—the period starts on the day indicated by PeriodBoundaryDay.`

**•** `LastDayOfPeriod—the period starts on the last day of the pricing term unit.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
PeriodBoundaryStartMonth
PricebookEntryId
PricingContractId

```

**Description**
Required when `PeriodBoundary` is `DayOfPeriod. Indicates day of the week or`
month that marks the period boundary. Must be an integer from 1 through 31.

This field is available in API version 55.0 and later. This field is available with Subscription
Management.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
The field is populated based on input in the StartDate, PeriodBoundary, and
PeriodBoundaryDay when BillingFrequency is Annual and PricingTermUnit is Annual or by
manual user entry. Possible values are:

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
Create, Filter, Group, Sort

**Description**
Required. ID of the associated PricebookEntry. Exists only for orgs with Products enabled. In
API 38.0 and earlier, if `Product2Id` is populated with `PricebookEntryId data,`
you receive an error message. In API 39.0 and later, `Product2Id` is made null, and
`PricebookEntryId is populated with the` `PricebookEntryId` data.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
PriceWaterfallIdentifier
PricingTerm
PricingTermCount
PricingTermUnit

```

**Description**
The contract used for pricing that's associated with the quote line item.

This field is a relationship field.

**Relationship Name**
PricingContract

**Refers To**
Contract

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The price waterfall identifier generated by Salesforce Pricing that's associated with the pricing
of the detail record. Available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of terms in the subscription. For example, if a monthly subscription is priced
yearly, this field is 12.

This field is available in API version 55.0 and later. This field is available with Subscription
Management.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
A calculated field indicating the number of pricing terms in the subscription. This field is
available in API version 55.0 and later. This field is available with Subscription Management.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of time for the pricing term. This field is available in API version 55.0 and later. This
field is available with Subscription Management.


-----

```
Product2Id
ProductInstanceIdentifier
ProductSellingModelId
ProrationPolicyId

```

Possible values are:

**•** `Annual—Available in API version 58.0 and later. UI label is` `Years.`

**•** `Months.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 associated with this QuoteLineItem. In API 38.0 and earlier, if
`Product2Id` is populated with `PricebookEntryId data, you receive an error`
message. In API 39.0 and later, `Product2Id` is made null, and `PricebookEntryId`
is populated with the `PricebookEntryId` data.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product instance that’s added to a quote. Each quote line item created for the
same product instance has the same product instance identifier value.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related product selling model. This field is available in API version 55.0 and
later. This field is available with Subscription Management.

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
Filter, Group, Nillable, Sort


-----

```
Quantity
QuantityUnitOfMeasureId
QuoteActionId

```

**Description**
The ID of the related proration policy. This field is available in API version 55.0 and later. This
field is available with Subscription Management.

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
Required. The number of units for the line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unit of measure for the quantity, start quantity, and end quantity.

This field is a relationship field.

**Relationship Name**
QuantityUnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related quote action. This field is available in API version 58.0 and later. This
field is available with Subscription Management and Revenue Lifecycle Management.

This field is a relationship field.

**Relationship Name**
QuoteAction


-----

```
QuoteId
RampIdentifier
SegmentIdentifier
SegmentName
SegmentType

```

**Relationship Type**
Lookup

**Refers To**
QuoteAction

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated Quote.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ramp ID used to group order item segments.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the segment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the order item segment.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time period for the segment.

Possible values are:

**•** `Custom`


-----

```
SellingModelType
ServiceDate
SortOrder
StandardTaxAmount

```


**•** `FreeTrial—Free Trial`

**•** `Yearly`

The default value is `Yearly.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the quote line item is sold as a one-time purchase, an evergreen
subscription, or as a termed subscription. This field is available in API version 55.0 and later.
This field is available with Subscription Management.

Possible values are:

**•** `Evergreen`

**•** `OneTime`

**•** `TermDefined`

The default value is `OneTime.`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the product revenue is recognized and the product quantity is shipped.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of where the line item is in the sorted order, such as 1, 2, 3. The SortOrder value
determines the order in which a quote line item displays in the Quote Line Items related list
and the Quote PDF. Client applications can use this value to match the sort order in Salesforce.
This field is only available in API versions 21.0 and greater.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The tax amount for the standard term.


-----

```
StartDate
StartQuantity
StartingPriceTotal
StartingUnitPriceSource
Status

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the quote line item is sold on subscription, this field indicates the date on which the
subscription starts. This field is available in API version 55.0 and later. This field is available
with Subscription Management.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
If the quote line item is sold on a subscription, this field indicates the item quantity when
the subscription starts. This field is available in API version 60.0 and later. This field is available
with Subscription Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The starting unit price times the quantity.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the starting unit price was entered manually or calculated. This field is
available in API version 55.0 and later. This field is available with Subscription Management.

Possible values are:

**•** `Manual`

**•** `System`

**•** `Inherited`

**Type**
dynamic picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
SubscriptionTerm
SubscriptionTermUnit
Subtotal
TaxTreatmentId

```

**Description**
Represents the status of the Quote Line Item. This field is available in API version 60.0 and
later. The `QuoteLineItemStatus` permission is required to access this field.

Possible values are:

**•** `In Progress`

**•** `Pending`

**•** `Approved`

**•** `Rejected`

Default value is `In Progress.`

**Type**
int

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The number of terms in the subscription.

You can indicate a subscription’s length using either `StartDate` and `EndDate, or by`
using StartDate and SubscriptionTerm. If you provide a value for both EndDate
and SubscriptionTerm, EndDate is used and SubscriptionTerm is ignored.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of time used to define the subscription. This field is available in API version 55.0 and
later. This field is available with Subscription Management.

Possible values are:

**•** `Annual—UI label is` `Years`

**•** `Months`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The line item's `Quantity` multiplied by the `UnitPrice.`

**Type**
reference


-----

```
TotalAdjustmentAmount
TotalLineAmount
TotalPrice

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax treatment associated with the quote line item. Available in API version 60.0
and later.

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
Filter, Nillable, Sort

**Description**
The sum of the adjustments applied to the quote line item, inclusive of quantity, prorated
for the duration of the subscription.

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total price of the quote line item, before price adjustments, inclusive of quantity, prorated
for the duration of the subscription. This price is a calculated field equal to TotalPrice times
Quantity times PricingTermCount.

This field is available in API version 56.0 and later. This field is available with Subscription
Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. Calculated by applying the Discount to the Subtotal. This field is nillable,
but you can't set both `TotalPrice` and `UnitPrice` to null in the same update. To
insert the `TotalPrice` for a quote line item via the API (given only a unit price and the


-----

```
TotalPriceWithTax
TotalTaxAmount
UnitPrice
ValidationResult

```

quantity), calculate this field as the unit price multiplied by the quantity. This field is read
only if the quote line item has a revenue schedule.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TotalPrice` and `TotalTaxAmount. This field is available in API version`
55.0 and later. This field is available with Subscription Management.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
the total amount of tax for the quote line item. his field is available in API version 55.0 and
later. This field is available with Subscription Management.

This field is a calculated field.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The price per unit for the quote line item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the quote line item was configured and priced by Revenue Lifecycle
Management.

A quote can be activated only after all its quote line items are configured and priced by
Revenue Lifecycle Management.

Valid values are:

**•** `Warning—Indicates that the quote line item wasn’t configured and priced by Revenue`
Lifecycle Management.

Available in API version 60.0 and later.


-----

##### Usage

A Quote record can have QuoteLineItem records only if the Quote has a Pricebook2. A QuoteLineItem must correspond to a Product2
that is listed in the quote's Pricebook2.

Note: If the multicurrency option has been enabled, the `CurrencyIsoCode` field is present. It can't be modified, it’s always
set to the value of the `CurrencyIsoCode` of the parent Quote.

Effects on Quotes

Quotes with related QuoteLineItem objects are affected in the following ways:

**•** Creating a QuoteLineItem increments the Quote value by the `TotalPrice` of the QuoteLineItem.

**•** When you create or update a QuoteLineItem, the API verifies that the line item corresponds to a PricebookEntry in the Pricebook2
that is associated with the quote.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteLineItemChangeEvent (API version 44.0)**
Change events are available for the object.

**QuoteLineItemHistory (API version 57.0)**
History is available for tracked fields of the object.

SEE ALSO:

Quote

QuoteDocument

Opportunity
