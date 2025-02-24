#### ForecastingItem

This object is read-only used for individual forecast amounts. Users see amounts based on their perspectives and forecast roles. The
amounts users see include one of these values when forecasting in revenue: `AmountWithoutAdjustments,`
```
AmountWithoutManagerAdjustment, ForecastAmount, OwnerOnlyAmount. The amounts users see include one of

```
these values when forecasting in quantity: QuantityWithoutAdjustments, QuantityWithoutManagerAdjustment,
```
ForecastQuantity, OwnerOnlyQuantity. Available in API version 26.0 and later.

```
Other users can see the ForecastingItem object, but not its records. See these access guidelines.

**•** Users with the “View All Forecasts” permission have access to all ForecastingItem fields.

**•** Users without the “View All Forecasts” permission have access to all fields for their own subordinates and child territories.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

##### Fields

```
AmountWithoutAdjustments
AmountWithoutManagerAdjustment
AmountWithoutOwnerAdjustment
ForecastAmount

```

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s owned revenue opportunities and the person's
subordinates’ and child territories’ opportunities, without adjustments.
Subordinates include everyone reporting up to a person in the role-based forecast
hierarchy. This amount is visible only on reports.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The forecast number as seen by the forecast owner. This number is the sum of
the owner’s revenue opportunities and the owner’s subordinates’ and child
territories’ opportunities, including adjustments made by the forecast owner on
the owner's or subordinates’ and child territories’ forecasts. It doesn’t include
adjustments made by forecast managers above the owner in the forecast
hierarchy.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The forecast amount as seen by the forecast owner without the owner's
adjustment. This amount is the sum of the subordinate's and child territories’
opportunities, including adjustments made by their manager or by the
subordinate themselves, plus the rollup of the owner's own opportunities. It
_doesn’t include adjustments made by the forecast owner._

**Type**
double


-----

```
ForecastCategoryName
ForecastQuantity
ForecastingGroupItemId

```

**Properties**
Filter, Sort, Nillable

**Description**

The revenue forecast from the forecast manager’s perspective and the sum of
the owner’s and subordinates’ and child territories’ opportunities, including all
forecast adjustments.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

A forecast category is the category within the sales cycle to which an opportunity
is assigned based on its opportunity stage. The standard forecast categories are
Pipeline, Best Case, Commit, Omitted (not included in forecasts), and Closed.
Salesforce admins can add a Most Likely category and can customize the forecast
category names in single category rollups. Change the forecast category name
only. Changing a forecast category’s API name can have unintended results.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The quantity forecast from the forecast manager’s perspective and the sum of
the owner’s and subordinates’ opportunities, including all forecast adjustments.
This field is available in API version 28 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the forecast total belongs to. This field is a relationship field. Available in API
version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem


-----

```
ForecastingItemCategory
ForecastingTypeId

```

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
This field indicates which type of forecast rollup the forecasting item belongs to.
Depending on whether your organization uses individual forecast category rollups
or cumulative forecast rollups, you have these possible values for the
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

The `ForecastingItemCategory` field differs from the
`ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category
of the underlying opportunities rolling up to forecast amounts. In organizations
using cumulative forecast rollups, the `ForecastCategoryName` field
can be null because the cumulative forecast amounts include opportunities
from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the type of
_rollup a forecast amount or adjustment is from. In organizations using_
individual forecast category columns, it contains the individual forecast rollup
categories. In organizations using cumulative forecast rollups, it contains the
cumulative rollup categories.

**Type**
reference


-----

```
HasAdjustment
HasOwnerAdjustment
IsAmount
IsQuantity
IsUpToDate

```

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag that indicates the forecasting item includes a manager adjustment. This
flag is true only when the item includes an adjustment and the user performing
the query has read access to the adjustment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag that indicates the forecasting item includes an owner adjustment. This flag
is true only when the item includes an adjustment and the user performing the
query has read access to the adjustment. Available in API version 33.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

True indicates that the adjustment is made in a revenue amount. If false, then
`IsQuantity` must be true. This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

True indicates that the adjustment is made in a quantity amount. If false, then
`IsAmount` must be true. This field is available in API version 28.0 and later.

**Type**
boolean


-----

```
OwnerId
OwnerOnlyAmount
OwnerOnlyQuantity
ParentForecastingItemId
PeriodId

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag indicating whether a specific forecasting item reflects current information.
For example, if users are making adjustments that are in process, the item isn’t
up to date.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the forecast owner.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s revenue opportunities, without adjustments.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s quantity opportunities, without adjustments. This field is
available in API version 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the ForecastingItem that the current item rolls up to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ProductFamily
QuantityWithoutAdjustments
QuantityWithoutManagerAdjustment
QuantityWithoutOwnerAdjustment

```

**Description**

Period ID for the forecast.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product family of the forecast item. This field is available in API version 29.0
and later. Read only.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The sum of a person’s owned quantity opportunities and also his or her
subordinates’ opportunities, without adjustments. Subordinates include everyone
reporting up to a person in the forecast hierarchy. This field is available in API
version 28.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The forecast number as seen by the forecast owner. This number is the sum of
the owner’s quantity opportunities and subordinates’ opportunities, including
adjustments made on the subordinates’ forecasts. It doesn’t include adjustments
made by forecast managers above the owner in the forecast hierarchy. This field
is available in API version 28 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The forecast quantity as seen by the forecast owner without the owner's
adjustment. This number is the sum of the subordinate's opportunities, including
adjustments made by their manager or by the subordinate themselves, plus the
rollup of the owner's own opportunities. It doesn’t include adjustments made by
_the forecast owner. This field is available in API version 38.0 and later._


-----

```
SubordinateOverrides
Territory2Id

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of adjustments made to a forecast down the hierarchical chain.
For example, User A has a forecast without adjustments. If User A adjusts User
B’s forecast, User A’s `SubordinateOverrides` value is 1. Then if User B
adjusts User C’s forecast, User A’s `SubordinateOverrides` value is 2. If
User A removes his adjustment from User B’s forecast, User A’s
`SubordinateOverrides` value is 1.

This field is available in API version 38.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.


Use this object to obtain individual forecast amounts, either with or without adjustments, based on a user’s perspective and forecast
role. The ForecastingItem object is visible to all users, but only forecast managers and users above them in the forecast hierarchy can
read or write ForecastingAdjustment records.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
```
  ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

```
and ForecastingFact objects can all have records with different ForecastingTypeId values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota,` `ForecastingAdjustment,`
`ForecastingItem, or` `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingFact

ForecastingQuota
