#### OrderItemTaxLineItemSummary

Represents the current tax on an OrderItemSummary or OrderItemAdjustmentLineSummary. Corresponds to one or more order item
tax line items, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and
later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

##### Fields

```
Amount

```

**Type**
currency


-----

```
CalculationReferenceNumber
CurrencyIsoCode
Description
Name

```

**Properties**
Filter, Sort

**Description**
Amount of tax represented by the OrderItemTaxLineItemSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference number provided by the tax provider, such as Stripe, in the tax calculation API
response.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderItemTaxLineItemSummary. The default value is USD.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
Description of the OrderItemTaxLineItemSummary.

This field can be edited.

**Type**
string


-----

```
OrderItemAdjustmentLine
SummaryId
OrderItemSummaryId
OrderSummaryId
OriginalOrderItemTax
LineItemId
Rate

```

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderItemTaxLineItemSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object represents tax on an adjustment, this value is the ID of the
OrderItemAdjustmentLineSummary to which the tax applies. If this value is null, the
adjustment applies to an OrderItemSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
If this object represents tax on an OrderItemSummary, this value is the ID of that
OrderItemSummary. If this object represents tax on an adjustment, this value is the ID of the
OrderItemSummary to which the adjustment applies.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary that the associated OrderItemSummary or
OrderItemAdjustmentLineSummary belongs to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original order item tax line item associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
percent


-----

```
ReferenceNumber
TaxEffectiveDate
TransactionReferenceNumber
Type

```

**Properties**
Filter, Nillable, Sort

**Description**
Tax rate used to calculate the Amount.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Reference number provided by the tax provider (like Stripe) for each line item in the**
**tax calculation API call. Use this unique ID to revert taxes during cancellation or return**
**of an order.**

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**

**Reference number provided by the tax provider, such as Stripe, in the tax transaction**
**commit API request.**

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the Amount is actual or estimated.

Possible values are:


-----

**•** `Actual`

**•** `Estimated`

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemTaxLineItemSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

FulfillmentOrderItemTax

OrderItemAdjustmentLineSummary

OrderItemSummary

OrderItemTaxLineItem
