#### AssetActionSource

```

**Description**
The sum of current and previous asset action amounts categorized as `Upsells. This field`
is populated by the system.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The REST API used to generate the asset action. This field is populated by the system.

Possible values are:

**•** `Cancel`

**•** `Change`

**•** `Generate`


Represents an optional way to record what transactions caused changes to lifecycle-managed assets. Use it to trace financial and other
information about asset actions. This object supports Salesforce order products and work order line items, and transaction IDs from other
systems. The fields can’t be edited. This object is available in API version 50.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

##### Fields

```
ActualTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The region-specific tax amount determined at time of the order.


-----

```
AdjustmentAmount
AssetActionId
AssetActionSourceNumber
BillingReference
Discount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
An adjustment to the product amount, such as a discount.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The related asset action, that is, the change caused by an asset action source transaction.

This field is a relationship field.

**Relationship Name**
AssetAction

**Relationship Type**
Lookup

**Refers To**
AssetAction

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset action source. Label is Name.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the OrderItem or OrderItemDetail record that this AssetActionSource record is
created for.

**Type**
percent

**Properties**
Filter, Group, Nillable, Sort


-----

```
DiscountAmount
EffectiveGrantDate
EndDate
EstimatedTax
ExternalReference

```

**Description**
The discount, expressed as a percentage, that's applied to the asset.

This field is available in API version 62.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The discount, expressed as currency, that's applied to the asset.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resources associated with the asset were granted.

This field is available in orgs that have Revenue Cloud when Rate Management is enabled.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date of the service or change.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The estimate of the region-specific tax amount made at time of the transaction.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an asset action source transaction originating in a system outside of Salesforce.


-----

```
ExternalReferenceDataSource
LegalEntityId
ListPrice
NetUnitPrice
ObligatedAmount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A system outside of Salesforce that contains asset action source transactions.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the legal entity record associated with the asset action source transaction.

This field is a relationship field.

This field is available in API version 62.0 and later.

**Relationship Name**
LegalEntity

**Relationship Type**
Lookup

**Refers To**
LegalEntity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
List price for the order product. Value is inherited from the associated PriceBookEntry upon
order product creation.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The final adjusted unit price, inclusive of all adjustments, but exclusive of tax. The unit price
after all price adjustments are applied.

**Type**
currency


-----

```
PeriodBoundary
PeriodBoundaryDay
PeriodBoundaryStartMonth

```

**Properties**
Filter, Nillable, Sort

**Description**
When a line amount is prorated, this amount shows the service amount that’s been consumed.

**Type**
picklist

**Properties**
Filter, Nillable, Sort

**Description**
Boundary delimiters for periods. It determines when a period starts and/or ends. Enum:
anniversary, align to calendar, end of period, day of period.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number specifying the day number when Period Boundary is a specific day in a
week/month/year. It only applies when PeriodBoundary is set to "day of period.”

**Type**
picklist

**Properties**
Filter, Nillable, Sort

**Description**
Field is populated based on input in the StartDate, PeriodBoundary, and PeriodBoundaryDay
when BillingFrequency2 is Annual or by manual user entry. Possible values are:

1-January

2-February

3-March

4-April

5-May

6-June

7-July

8-August

9-September

10-October

11-November

12-December


-----

```
PricebookEntryId
PricingTermCount
ProductAmount
ProductSellingModelId
ProrationPolicyId
Quantity

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
PricebookEntry is used as a lookup for price information in order to pre-populate OrderItem's
ListPrice and UnitPrice.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of pricing terms is this subscription product.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The product amount after the asset action source transaction.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the product selling model type. Foreignkey to ProductSellingModel entity.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Id of the ProrationPolicy.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
ReferenceEntityItemId
SegmentIdentifier
StartDate
Subtotal

```

**Description**
The product quantity or the change in product quantity after the asset action source
transaction.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an asset action source transaction originating in Salesforce. The transaction can be
an order product or a work order line item.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, WorkOrderLineItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ramp segment associated with the asset action source transaction.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date of the service or change.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the product amount and the adjustment amount.

This field is a calculated field.


-----

```
TaxTreatmentId
TotalPrice
TotalLineAmount
TransactionDate
UnitPrice

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup to Tax Treatment entity. It's used to calculate tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated by the pricing engine for ARC. Summation of TotalAdjustmentAmount plus
TotalLineAmount for this item.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The price of the line before any price adjustments were applied. SalesTransactionItem:
ProratedStartingTotal / StartingPriceTotal. Note: TotalPrice is computed using the UnitPrice,
which includes discounts (price adjustments), while TotalLineAmount doesn’t include price
adjustments.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of a source transaction, such as an order date.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The unit price of the item before any discounts or tax calculation.


-----
