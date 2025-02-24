#### FulfillmentOrderItemTax

Represents the tax on a FulfillmentOrderLineItem or FulfillmentOrderItemAdjustment. Corresponds to an OrderItemTaxLineItemSummary.
This object is available in API version 48.0 and later.

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
CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount of tax represented by the FulfillmentOrderItemTax.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
Description
FulfillmentOrderId
FulfillmentOrder
ItemAdjustId
FulfillmentOrderItem
TaxNumber

```

**Description**
ISO code for the currency of the FulfillmentOrderLineItem to which the tax applies. The
default value is USD.

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
Description of the FulfillmentOrderItemTax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated FulfillmentOrder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If this object represents tax on an adjustment, this value is the ID of the
FulfillmentOrderItemAdjustment to which the tax applies. If this value is null, the adjustment
applies to a FulfillmentOrderLineItem.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderItemTax.


-----

```
FulfillmentOrder
LineItemId
OrderItemTaxLineItem
SummaryId
Rate
TaxEffectiveDate
Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If this object represents tax on a FulfillmentOrderLineItem, this value is the ID of that
FulfillmentOrderLineItem. If this object represents tax on an adjustment, this value is the ID
of the FulfillmentOrderLineItem to which the adjustment applies.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemTaxLineItemSummary associated with the OrderItemSummary that
corresponds to the FulfillmentOrderLineItem to which the tax applies.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tax rate used to calculate the Amount.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the Amount is actual or estimated.

Possible values are:

**•** `Actual`

**•** `Estimated`


-----

**FulFillmentOrderItemTaxChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

FulfillmentOrder

FulfillmentOrderItemAdjustment

FulfillmentOrderLineItem

OrderItemTaxLineItemSummary
