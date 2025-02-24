#### ForecastingOwnerAdjustment

This object represents an individual forecast user’s adjustment of their own forecast, including territory forecasts they own, via a
ForecastingItem. Available in API versions 33.0 and later. This object is different from the ForecastingAdjustment object, which represents
managers’ adjustments of subordinates’ and child territories’ forecasts.


-----

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
CurrencyIsoCode
ForecastCategoryName
ForecastOwnerId
ForecastingGroupItemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The currency code of the adjustment. If omitted, the default is the importing
user’s personal currency.

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

The ID of the forecast owner.

**Type**
reference


-----

```
ForecastingItemCategory

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the owner adjustment belongs to. This field is a relationship field. Available in
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
This field indicates which type of forecast rollup the owner adjustment belongs
to. Depending on whether your organization uses individual forecast category
rollups or cumulative forecast rollups, you have these possible values for the
`ForecastingItemCategory` field.

**_Individual forecast category rollups:_**

**•** PipelineOnly - Rollup from Pipeline opportunities only.

**•** BestCaseOnly - Rollup from Best Case opportunities only. Adjustable.

**•** MostLikelyOnly - Rollup from Most Likely opportunities only. Adjustable.

**•** CommitOnly - Rollup from Commit opportunities only. Adjustable.

**_Cumulative forecast rollups:_**

**•** OpenPipeline - Rollup from Pipeline + Best Case + Most Likely + Commit
opportunities.

**•** BestCaseForecast - Rollup from Best Case + Most Likely + Commit +
Closed opportunities. Adjustable.

**•** MostLikelyForecast - Rollup from Most Likely + Commit + Closed
opportunities. Adjustable.

**•** CommitForecast - Rollup from Commit + Closed opportunities.
Adjustable.

**_Either cumulative or individual forecast category rollups:_**

**•** ClosedOnly - Rollup from Closed opportunities only.

The `ForecastingItemCategory field differs from the`
```
  ForecastCategoryName field.

```

-----

```
ForecastingItemId
ForecastingTypeId
IsAmount

```


**•** The `ForecastCategoryName field represents the forecast category`
of the underlying opportunities rolling up to forecast amounts. In organizations
using cumulative forecast rollups, the ForecastCategoryName field
can be null because the cumulative forecast amounts include opportunities
from multiple forecast categories.

**•** The new ForecastingItemCategory field represents the type of
_rollup a forecast amount or adjustment is from. In organizations using_
individual forecast category columns, it contains the individual forecast rollup
categories. In organizations using cumulative forecast rollups, it contains the
cumulative rollup categories.

When inserting owner adjustments, the values you insert for
```
  ForecastCategoryName and ForecastingItemCategory must

```
be compatible with each other. In organizations using cumulative forecast rollups,
the ForecastCategoryName is nillable. These pairs are the valid pairs.

**Individual forecast category rollups:**

**•** `ForecastCategoryName: BestCase,`
```
     ForecastingItemCategory: BestCaseOnly

```
**•** `ForecastCategoryName: Commit,`
```
     ForecastingItemCategory: CommitOnly

```
**Cumulative forecast category rollups:**

**•** `ForecastCategoryName: null, ForecastingItemCategory:`
BestCaseForecast

**•** `ForecastCategoryName: null, ForecastingItemCategory:`
CommitForecast

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingItem.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean


-----

```
IsQuantity
OwnerAdjustedAmount
OwnerAdjustedQuantity
OwnerAdjustmentNote
PeriodId

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true, then the adjustment is made in a revenue amount. If false, then`
`IsQuantity` must be `true.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true, then the adjustment is made in a quantity amount. If false, then`
`IsAmount` must be `true.`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A text note providing information about the adjustment. The maximum length
is 255 characters. This field does not appear in reports.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ProductFamily
StartDate
Territory2Id

##### Usage

```

**Description**

Period ID for the adjustment. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The Product Family for the adjustment. Read only.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The start of the adjustment, expressed as month and year. The date can include
any day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.


Use this object to obtain a user’s adjustment details for a specified ForecastingItem in their own forecast.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
```
  ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

```
and ForecastingFact objects can all have records with different ForecastingTypeId values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota, ForecastingAdjustment,`
```
  ForecastingItem, or ForecastingFact records as necessary.

```
**ForecastingOwnerAdjustmentChangeEvent (API version 62.0)**
Change events are available for the object.


-----
