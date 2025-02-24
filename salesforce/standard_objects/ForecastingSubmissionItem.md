#### ForecastingSubmissionItem

Represents the values for each forecast category in a submitted forecast. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Amount
CurrencyIsoCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
For forecasting types that use Amount as the measure, the amount for the forecast category.
Amounts must be provided in the corporate currency.

**Type**
picklist


-----

```
ForecastingItemCategory
ForecastingSubmissionId

```

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency code of the forecast submission. If omitted, the default is USD.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
The category the forecast belongs to.

**For individual forecast category rollups, the possible values are:**

**•** `PipelineOnly—Rollup from Pipeline opportunities only.`

**•** `BestCaseOnly—Rollup from Best Case opportunities only.`

**•** `MostLikelyOnly—Rollup from Most Likely opportunities only.`

**•** `CommitOnly —Rollup from Commit opportunities only.`

**For cumulative forecast rollups, the possible values are:**

**•** `OpenPipeline—Rollup from Pipeline, Best Case, Most Likely, and Commit`
opportunities.

**•** `BestCaseForecast —Rollup from Best Case, Most Likely, Commit, and Closed`
opportunities.

**•** `MostLikelyForecast—Rollup from Most Likely, Commit, and Closed`
opportunities.

**•** `CommitForecast —Rollup from Commit and Closed opportunities.`

**For either cumulative or individual forecast category rollups, the possible values**
**are:**

**•** `ClosedOnly—Rollup from Closed opportunities only.`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast submission.

This field is a relationship field.

**Relationship Name**
ForecastingSubmission

**Relationship Type**
Master-detail


-----

```
Name
Quantity
