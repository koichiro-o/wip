#### PipelineInspMetricConfig

Represents the configuration of a forecast category metric that appears in the Pipeline Inspection view. This object is available in API
version 55.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
DeveloperName
IsCumulative

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Read only. The unique name of a Pipeline Inspection metric configuration in the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Language
MasterLabel
Metric

```

**Description**
Read only. Whether the metric is cumulative.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Read only. The language of the Pipeline Inspection metric.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Customized label of the Pipeline Inspection metric. Limit: 50 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The Pipeline Inspection metric.

Possible values are:

**•** `BestCase`

**•** `ClosedLost`

**•** `ClosedWon`

**•** `Commit`

**•** `MostLikely`

**•** `OpenPipeline`

**•** `TotalPipeline`

