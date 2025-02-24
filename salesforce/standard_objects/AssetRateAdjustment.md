#### AssetRateAdjustment

Stores the tier rate adjustments for the asset rate card entries. This object is available in API version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available in orgs where Revenue Cloud is enabled.


-----

##### Fields

**Field**
```
AdjustmentType
AdjustmentValue
AssetRateCardEntryId
LowerBound

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of rate adjustment.

Valid values are:

**•** `Amount—Adjusts rate by using a specific amount.`

**•** `Override—Adjusts rate by using the override rate.`

**•** `Percentage—Adjusts rate by using a percentage.`

**Type**
double

**Properties**
Filter, Sort

**Description**
The value of the adjustment.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent asset rate card entry record associated with the asset rate adjustment.

This field is a relationship field.

**Relationship Name**
AssetRateCardEntry

**Relationship Type**
Master-detail

**Refers To**
AssetRateCardEntry (the master object)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The minimum quantity for the adjustment to be applicable.


-----

```
Name
UpperBound
