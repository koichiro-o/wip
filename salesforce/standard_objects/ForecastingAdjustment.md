#### ForecastingAdjustment

This object represents an individual forecast manager’s adjustment for a subordinate’s or child territory’s forecast via a ForecastingItem.
Available in API versions 26.0 and later. This object is different from the ForecastingOwnerAdjustment object, which represents forecast
users’ adjustments of their own forecasts, including territory forecasts they own.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

##### Fields

```
AdjustedAmount
AdjustedQuantity
AdjustmentNote

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The quantity amount of an individual forecast item, after an adjustment. This
field is available in API version 28.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A text note providing information about the adjustment. The maximum length
is 255 characters. This field doesn’t appear in reports.


-----

```
CurrencyIsoCode
ForecastCategoryName
ForecastingGroupItemId
ForecastingItemCategory

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The currency code of the adjustment. If omitted, the default is the user’s personal
currency.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category within the sales cycle that an opportunity is assigned to based on
its opportunity stage. The standard forecast categories are Pipeline, Best Case,
Commit, Omitted, and Closed. You can add a Most Likely category and can
customize forecast category names in single category rollups. The forecast
categories display information for that specific category; for example, Best Case
only reflects amounts in the Best Case category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the manager adjustment belongs to. This field is a relationship field. Available in
API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
The category the forecast belongs to.


-----

```
ForecastingItemId
ForecastingTypeId
IsAmount

```

**For individual forecast category rollups, the possible values are:**

**•** `PipelineOnly—Rollup from Pipeline opportunities only.`

**•** `BestCaseOnly—Rollup from Best Case opportunities only. The value`
in this category is adjustable.

**•** `MostLikelyOnly—Rollup from Most Likely opportunities only. The`
value in this category is adjustable.

**•** `CommitOnly—Rollup from Commit opportunities only. The value in`
this category is adjustable.

**For cumulative forecast rollups, the possible values are:**

**•** `OpenPipeline—Rollup from Pipeline, Best Case, Most Likely, and`
Commit opportunities.

**•** `BestCaseForecast—Rollup from Best Case, Most Likely, Commit,`
and Closed opportunities. The value in this category is adjustable.

**•** `MostLikelyForecast—Rollup from Most Likely, Commit, and`
Closed opportunities. The value in this category is adjustable.

**•** `CommitForecast—Rollup from Commit and Closed opportunities.`
The value in this category is adjustable.

**For either cumulative or individual forecast category rollups, the possible**
**values are:**

**•** `ClosedOnly —Rollup from Closed opportunities only.`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingItem.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsQuantity
OwnerId
PeriodId
ProductFamily
StartDate

```

**Description**

If `true, then the adjustment is made in a revenue amount. If` `false, then`
`IsQuantity` must be `true. This field is available in API version 28.0 and`
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true, then the adjustment is made in a quantity amount. If` `false, then`
`IsAmount` must be `true. This field is available in API version 28.0 and later.`

**Type**
reference

**Properties**
Create,Defaulted on create, Filter, Group, Sort

**Description**

The ID of the forecast owner.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the adjustment. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The Product Family for the adjustment. Read only. This field is available in API
version 29.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Sort


-----

```
Territory2Id

##### Usage

```

**Description**

The start of the adjustment, expressed as month and year. The date can include
any day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.


Use this object to obtain a manager’s adjustment detail for a specified ForecastingItem. The ForecastingAdjustment object is visible to
all users, but only forecast managers and users above them in the forecast hierarchy can read or write ForecastingAdjustment records.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
```
  ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

```
and ForecastingFact objects can all have records with different ForecastingTypeId values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota,` `ForecastingAdjustment,`
`ForecastingItem, or` `ForecastingFact` records as necessary.

The `ForecastingItemCategory` field differs from the `ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category of the underlying opportunities rolling up to forecast
amounts. In organizations using cumulative forecast rollups, the `ForecastCategoryName` field can be null because the
cumulative forecast amounts include opportunities from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the type of rollup a forecast amount or adjustment is from. In
organizations using individual forecast category columns, it contains the individual forecast rollup categories. In organizations using
cumulative forecast rollups, it contains the cumulative rollup categories.

When inserting manager adjustments, the values you insert for ForecastCategoryName and ForecastingItemCategory
must be compatible with each other. In organizations using cumulative forecast rollups, the `ForecastCategoryName` is nillable.
The following pairs are valid.

**For individual forecast category rollups:**

**•** `ForecastCategoryName:` `BestCase,` `ForecastingItemCategory:` `BestCaseOnly`

**•** `ForecastCategoryName:` `MostLikely,` `ForecastingItemCategory:` `MostLikelyOnly`

**•** `ForecastCategoryName:` `Commit,` `ForecastingItemCategory:` `CommitOnly`

**For cumulative forecast category rollups:**

**•** `ForecastCategoryName:` `null,` `ForecastingItemCategory:` `BestCaseForecast`

**•** `ForecastCategoryName:` `null,` `ForecastingItemCategory:` `MostLikelyForecast`


-----

**•** `ForecastCategoryName:` `null,` `ForecastingItemCategory:` `CommitForecast`

SEE ALSO:

ForecastingFact

ForecastingItem

ForecastingQuota
