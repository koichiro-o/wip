#### ForecastingUserPreference

Represents the forecasting selections that a user has made, such as display options, date range, forecasting type, and currency.

##### Supported Calls
```
create(), describeSObjects(), query(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

##### Fields

```
ExternalId
ForecastingDisplayedTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A unique system-generated numerical identifier for the user.

**Type**
reference


-----

```
ForecastingPeriodDuration
ForecastingPeriodType
ForecastingStartPeriod
ForecastingViewCurrency
IsForecastingHideZeroRows

```

**Properties**
Create, Group, Sort, Update

**Description**

An identifier for the forecasting type that’s displayed.

**Type**
int

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

How long the forecasting period lasts.

**Type**
picklist

**Properties**
Create, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The forecasting period’s type. Valid values include: Month, Quarter, Week, or Year

**Type**
int

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

The date when the forecasting period begins.

**Type**
string

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

The currency shown on the forecasts page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows zero-value rows.


-----

```
IsForecastingShowQuantity
IsHideForecastingGuidedTour
IsHideForecastingQuotaColumn
IsShowForecastingChangeSignals
IsShowForecastingQuotaAttainment
