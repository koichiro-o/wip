#### AssetStatePeriod

Represents a time span when an asset has the same quantity, amount, and monthly recurring revenue (MRR). An asset has as many asset
state periods as there are changes to it (asset actions) during its lifecycle. The dashboard and related pages show the current asset state
period. The fields can’t be edited. This object is available in API version 50.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
To use Customer Asset Lifecycle Management APIs, you must have the Access Customer Asset Lifecycle Management APIs permission
and Read access to the Asset, Asset Action, Asset Action Source, and Asset State Period objects.


-----

##### Fields

**Field**
```
Amount
AssetId
AssetStatePeriodNumber
EndDate
Mrr

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
An asset’s total amount during an asset state period.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The asset related to an asset state period. Label is Asset.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the asset state period. Label is Name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date and time of an asset state period. On an asset that is an evergreen subscription,
the last asset state period has no end date.

**Type**
currency


-----

```
Quantity
RampIdentifier
SegmentIdentifier
SegmentName

```

**Properties**
Filter, Sort

**Description**
An asset’s monthly recurring revenue during an asset state period.

**Type**
double

**Properties**
Filter, Sort

**Description**
The total quantity of an asset during an asset state period.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ramp record used to group order item segments for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order item segment for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the order item segment for this asset state period.

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.


-----

```
SegmentType
StartDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The period for the order item segment for this asset state period. Valid values are:

**•** `Custom`

**•** `Free Trial`

**•** `Yearly`

The default value is `Yearly.`

This field is available in orgs that have Revenue Cloud when the Ramp Deals setting is enabled.

This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The start date and time of an asset state period.

