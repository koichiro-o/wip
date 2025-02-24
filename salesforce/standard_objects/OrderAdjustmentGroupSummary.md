#### OrderAdjustmentGroupSummary

Represents the current properties and state of a group of related price adjustments. Associated with a set of
OrderItemAdjustmentLineSummaries that apply to OrderItemSummaries belonging to one OrderSummary. Corresponds to one or more
order adjustment group objects, consisting of an original object and any change objects applicable to it. This object is available in API
version 48.0 and later.

An OrderAdjustmentGroupSummary can represent an adjustment to an entire order as a group of adjustments to each of its products.
For example, representing “10% off the order” as a set of 10% off adjustments to each product on the order. It can also represent an
adjustment that applies to a subset of the products on an order. For example, representing “buy one, get one 50% off” as a 25% off
adjustment to each of two products.

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


-----

```
CurrencyIsoCode
Description
GrandTotalAmount

```

**Description**
References the specific promotions applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

This field is available in API version 52.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderSummary associated with the adjustments in the
group. The default value is USD.

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
Description of the OrderAdjustmentGroupSummary.

This field can be edited.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including tax, of the associated OrderItemAdjustmentLineSummaries.


-----

```
Name
OrderSummaryId
OriginalOrderAdjGroupId
TotalAmount
TotalTaxAmount
Type

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderAdjustmentGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderAdjustmentGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original OrderAdjustmentGroup associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, not including tax, of the associated OrderItemAdjustmentIineSummaries.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

**Description**
Type of the OrderAdjustmentGroupSummary. Header represents an order-level adjustment
with an OrderItemAdjustmentLineSummary for each OrderItemSummary on the
OrderSummary. SplitLine represents any other related set of
OrderItemAdjustmentLineSummaries.

Possible values are:

**•** `Header`

**•** `SplitLine`

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderAdjustmentGroupSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

OrderAdjustmentGroup

OrderItemAdjustmentLineSummary
