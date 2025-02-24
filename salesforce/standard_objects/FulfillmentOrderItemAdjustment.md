#### FulfillmentOrderItemAdjustment

Represents a price adjustment on a FulfillmentOrderLineItem. Corresponds to an OrderItemAdjustmentLineSummary associated with
the corresponding OrderItemSummary. This object is available in API version 48.0 and later.

This object is used for calculations and doesn’t have a default record page.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs.

##### Fields

```
Amount
CampaignName

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount, not including tax, of the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
CouponName
CurrencyIsoCode
Description
FulfillmentOrderId
FulfillmentOrderItem
AdjustmentNumber

```

**Description**
Campaign associated with the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon associated with the adjustment.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the FulfillmentOrderLineItem to which the adjustment applies.
The default value is USD.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrder associated with the FulfillmentOrderLineItem to which the
adjustment applies.

**Type**
string


-----

```
FulfillmentOrder
LineItemId
OrderItemAdjust
LineSummaryId
PromotionName
TotalAmtWithTax
TotalTaxAmount

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderLineItemAdjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrderLineItem to which this adjustment applies.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemAdjustmentLineSummary associated with the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Promotion associated with the adjustment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

**Description**
Tax on the Amount.

SEE ALSO:

FulfillmentOrder

FulfillmentOrderItemTax

FulfillmentOrderLineItem

OrderItemAdjustmentLineSummary
