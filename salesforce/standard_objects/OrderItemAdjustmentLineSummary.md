#### OrderItemAdjustmentLineSummary

Represents the current properties and state of price adjustments on an OrderItemSummary. Corresponds to one or more order item
adjustment line item objects, consisting of an original object and any change objects applicable to it. This object is available in API version
48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

##### Fields

```
AdjustmentBasisReferenceId
AdjustmentCauseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause


-----

```
Amount
CurrencyIsoCode
Description
Name

```

**Relationship Type**
Lookup

**Refers To**
Promotion

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount, not including tax, of the OrderItemAdjustmentLineSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderItemSummary to which the adjustment applies. The
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
Description of the OrderItemAdjustmentLineSummary.

This field can be edited.

**Type**
string


-----

```
OrderAdjustmentGroup
SummaryId
OrderItemSummaryId
OrderSummaryId
OriginalOrderItem
AdjustmentLineItemId
Priority

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderItemAdjustmentLineSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object belongs to an OrderAdjustmentGroupSummary, this value is the ID of that
OrderAdjustmentGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderItemSummary to which the OrderItemAdjustmentLineSummary applies.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderItemSummary to which this
OrderItemAdjustmentLineSummary applies.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original OrderItemAdjustmentLine associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
integer

**Properties**
Create, Nillable


-----

```
 TotalAmtWithTax
 TotalTaxAmount

```
SEE ALSO:

OrderItemAdjustmentLineItem

OrderItemSummary

OrderItemTaxLineItemSummary
