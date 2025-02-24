#### AssetAction

Represents a change made to a lifecycle-managed asset. The fields can’t be edited. This object is available in API version 50.0 and later.


-----

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.

##### Fields

```
ActionDate
ActualTaxChange
AdjustmentAmountChange
Amount

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date when an asset action change is recorded. This date can differ from the start date
of the related asset state period. For example, suppose that a customer cancels a subscription
in June, and the subscription expires in October. The date the customer cancels the
subscription (June) is the action date of the asset action. The cancellation's effective date
(October) is the start date of the asset state period.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of actual tax from all asset action sources. This field is populated by the system.
Label is Change in Actual Tax.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of adjustment amount from all asset action sources. This field is populated by the
system. Label is Change in Adjustment Amount.

This field is a calculated field.

**Type**
currency


-----

```
AssetActionNumber
AssetId
Category

```

**Properties**
Filter, Sort

**Description**
The delta in the total asset amount resulting from an asset action.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset action. Label is Name.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related lifecycle-managed asset. Label is Asset.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
A category to apply to the asset action. In your layouts and reports, replace this optional
picklist with the required Business Category picklist. Label is Category. Available in API
version 55.0 and earlier.

Possible values are:

**•** `Cancellations`

**•** `Cross-Sells`

**•** `Downsells`

**•** `Initial Sale`

**•** `Other`


-----

```
CategoryEnum
EstimatedTaxChange
MrrChange

```


**•** `Renewals`

**•** `Terms And Conditions Changes`

**•** `Transfers`

**•** `Upsells`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The business category of the asset action, for use in reporting. Asset action totals are broken
out by the picklist values on this required field, and those totals are in turn reflected on assets.
The following categories are available. They aren’t customizable. Label is Business Category.

Possible values are:

**•** `Cancellations`

**•** `Cross-Sells`

**•** `Downsells`

**•** `Initial Sale`

**•** `Other`

**•** `Renewals`

**•** `Terms And Conditions Changes`

**•** `Transfers`

**•** `Upsells`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of estimated tax from all asset action sources. This field is populated by the system.
Label is Change in Estimated Tax.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The delta in the asset’s monthly recurring revenue resulting from an asset action. For example,
suppose that the MRR during an asset state period is $200 and the next asset action adds
$100. Then this field’s value is $100. Label is Change in Monthly Recurring Revenue.


-----

```
ProductAmountChange
QuantityChange
SubtotalChange
TotalAmount
TotalCancellationsAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of product amount from all asset action sources. This field is populated by the
system. Label is Change in Product Amount.

This field is a calculated field.

**Type**
double

**Properties**
Filter, Sort

**Description**
The delta in the asset quantity resulting from an asset action. For example, suppose that the
asset quantity during an asset state period is 20 and the next asset action adds 10. Then this
field’s value is 10. Label is Change in Quantity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The rollup of subtotal from all asset action sources. This field is populated by the system.
Label is Change in Subtotal.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the current and previous asset action amount. This field is populated by the
system.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalCrossSellsAmount
TotalDownsellsAmount
TotalInitialSaleAmount
TotalMrr
TotalOtherAmount

```

**Description**
The sum of current and previous asset action amounts categorized as `Cancellations.`
This field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as Cross-Sells. This
field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Downsells. This`
field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Initial Sale.`
This field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the monthly recurring revenue for the current and previous asset action. This
field is populated by the system. Label is Total Monthly Recurring Revenue.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalQuantity
TotalRenewalsAmount
TotalTermsAndConditionsAmount
TotalTransfersAmount
TotalUpsellsAmount

```

**Description**
The sum of current and previous asset action amounts categorized as `Other. This field is`
populated by the system.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the changes in quantity for the current and previous asset action. This field is
populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as Renewals. This field
is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Terms and`
```
  Conditions Changes. This field is populated by the system. Label is Total Terms

```
**and Conditions Changes Amount.**

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of current and previous asset action amounts categorized as `Transfers. This`
field is populated by the system.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
Type
