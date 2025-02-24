#### PriceAdjustmentSchedule

Represents a series of discounts offered depending on your product's configuration, quantity, and when they’re purchased in combination
with other products. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when the B2B Commerce license is enabled or when Subscription Management is enabled.


-----

##### Fields

**Field**
```
AdjustmentMethod
Description
IsActive
LastReferencedDate
LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method for applying tiered pricing. Possible values are:

**•** `Range—All items receive the discount of the highest tier the quantity falls in.`

**•** `Slab—Items receive the discount defined for the tier they fall in.`

The default value is `Range. Term-based discounts can’t be of type` `Slab. This field is`
available in API version 51.0 and later.

The Slab method functions in the same way as the `Range method.`

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the price adjustment schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the price adjustment schedule is active (true) or not (false). You can
change this field’s value as often as necessary. Label is Active. The default value is False.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates whether the price adjustment schedule has been archived (true) or not (false).
This field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
ScheduleType

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the price adjustment schedule. This field is read-only. Label is Price
**Adjustment Schedule Name.**

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The Salesforce ID of the sales representative who owns the price adjustment schedule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the price adjustment is determined. This field is available when Subscription
Management is enabled. This field is available in API version 55.0 and later.

Possible values are:

**•** `Attribute—The characteristics or properties of a product determine the price`
adjustment.

**•** `Bundle—The price adjustment that is determined when you want to sell a group of`
products or services as a unit.

**•** `Custom—The price adjustment that can be customized for the user's needs.`

**•** `Term—The length of the subscription determines the price adjustment. Available in`
API version 58.0 and later.

**•** `Volume—The quantity purchased determines the price adjustment.`

The default value is `Volume.`


-----

##### Usage

When you create a PriceAdjustmentSchedule, you associate PriceAdjustmentTiers with it. A PriceAdjustmentSchedule is inactive until
at least one PriceAdjustmentTier is added to it. A PriceAdjustmentSchedule comprises all related PriceAdjustmentTiers, with a maximum
limit of 25 PriceAdjustmentTiers.

To use PriceAdjustmentSchedule, associate it with a PriceBookEntry.

**•** You can associate a PriceBookEntry with up to five PriceAdjustmentSchedules, but only one PriceAdjustmentSchedule can be
associated with a PriceBookEntry.

**•** When you activate or deactivate a PriceAdjustmentSchedule, its PriceBookEntry association is also activated or deactivated.

**•** An adjustment to a PriceBookEntry is applied only if the associated PriceAdjustmentSchedule is active.

**•** After a PriceAdjustmentSchedule is associated with a PriceBookEntry, if multicurrency is enabled, the currencyIsoCode field can’t be
modified.

**•** When you associate a PriceAdjustmentSchedule with a PricebookEntry, a junction object PricebookEntryAdjustment is created.

You can modify the PriceAdjustmentTier object, and the ScheduleType and `AdjustmentMethod fields, only when a`
PriceAdjustmentSchedule is inactive.

##### Code Sample


-----

SEE ALSO:

PriceAdjustmentTier

PricebookEntryAdjustment
