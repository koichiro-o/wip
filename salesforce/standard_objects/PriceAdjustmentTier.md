#### PriceAdjustmentTier

Represents a discount tier in a price adjustment schedule. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the B2B Commerce license is enabled.

##### Fields

```
LowerBound
Name

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The minimum quantity the discount can be applied to. It must be a positive integer and less
than or equal to the upper bound of the tier.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.


-----

```
PriceAdjustmentScheduleId
TierType
TierValue
UpperBound

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the price adjustment schedule that the discount is applied to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of the discount. Possible values are:

**•** `AdjustmentAmount—An amount discounted from an item’s list price. Label is`
Amount.

**•** `AdjustmentPercentage—A percentage discounted from an item’s list price.`
Label is Percentage.

**•** `AdjustmentOverride—An override of an item’s list price. Label is Override.`

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The value of the discount.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum quantity the discount can be applied to. The quantity must be a positive
integer. Not inclusive. Set this value one digit higher than the quantity you want the tier to
include. For example, if a tier’s upper bound is 99, set the value of `UpperBound` to 100.
For the last tier, the value is optional.


To use PriceAdjustmentTiers, associate them with a PriceAdjustmentSchedule.


-----

Tiers can’t overlap, and no gaps are allowed between tiers.

SEE ALSO:

PriceAdjustmentSchedule
