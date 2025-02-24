#### ForecastingQuota

This object represents an individual user’s or territory’s quota for a specified time period. The Managed Quotas user permission is required
for creating, updating, or deleting quotas. (Users can only edit their subordinates’ or child territories’ quotas, not their own.) The View
All Forecasts permission is required to view any user's forecast, regardless of the forecast hierarchy. Available in API versions 25.0 and
later. Forecast managers can view the forecasts of subordinates and territories below them in the forecast hierarchy.

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
ForecastingGroupItemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The currency code of the quota. If omitted, the default is the importing user’s
personal currency.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the quota belongs to. This field is a relationship field. Available in API version 60.0
and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem


-----

```
ForecastingTypeId
IsAmount
IsQuantity
PeriodId
ProductFamily
QuotaAmount

```

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
Filter, Group, Nillable, Sort

**Description**

Period ID for the quota. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The product family for the quota. This field is available in API version 29.0 and
later.

**Type**
currency


-----

```
QuotaOwnerId
QuotaQuantity
StartDate
Territory2Id

##### Usage

```

**Properties**
Create, Filter, Sort, Update

**Description**

The revenue quota amount for an individual user or territory and for a specific
period.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

ID that identifies the quota owner.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The quantity quota amount for an individual user and for a specific period. This
field is available in API version 28.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The start of the quota, expressed as month and year. The date can include any
day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.


Use this object to get an individual user’s or territory’s quota for a specified time period.


-----

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
```
  ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

```
and ForecastingFact objects can all have records with different ForecastingTypeId values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota,` `ForecastingAdjustment,`
```
  ForecastingItem, or ForecastingFact records as necessary.

```
SEE ALSO:

ForecastingAdjustment

ForecastingFact

ForecastingItem
