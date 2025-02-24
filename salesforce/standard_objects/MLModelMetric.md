#### MLModelMetric

```


**•** `IsNotNull`

**•** `IsNull`

**•** `LessThan`

**•** `NotEquals`

**•** `StartsWith`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component is an equation, this field represents the name of the field on
the right side of the equation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor has multiple model factor components, this field indicates the order in
which this model factor component appears.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component specifies a value, this field represents the value. For example,
if the model factor component is `Title = CEO, this field is` `CEO.`


Represents a metric or statistic about the related model, such as accuracy, precision, or RSquared. Use a model’s metrics to learn about
its performance and to compare it with other models. This object is available in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

##### Fields

```
BasicMetricValue
ComplexMetricValue
DataSetType
EndTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value of a basic metric. A basic metric is a single number. For metrics that comprise a
set of graph points, see `ComplexMetricValue` .

**Type**
textarea

**Properties**
Nillable

**Description**
The X and Y values for a complex metric. A complex metric is a coordinate on a graph. For
example, in classification models, you can use a line on a graph to create classification
categories.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of dataset.

Possible values are:

**•** `Baseline`

**•** `HoldOut`

**•** `Live`

**•** `Model`

**•** `Training`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
GraphType
MetricType

```

**Description**
The date and time when the model training finished.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of graph.

Possible values are:

**•** `ConfidencePlot`

**•** `ConfusionMatrixPerThreshold`

**•** `DiscountedCumulativeGainsGraph`

**•** `HitRateGraph`

**•** `KBasedRankingGraph`

**•** `LiftPlot`

**•** `MeanReciprocalRankGraph`

**•** `MultiClassConfusionMatrixPerThreshold`

**•** `MultiClassMisclassifications`

**•** `NormalizedDiscountedCumulativeGainsGraph`

**•** `PrecisionGraph`

**•** `RecallGraph`

**•** `RegressionErrorBands`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of metric.

Possible values are:

**•** `Accuracy`

**•** `AveragePrecision`

**•** `BalancedAccuracy`

**•** `DiscountedCumulativeGainAtK`

**•** `ExpectedTopAbsoluteRank`

**•** `ExpectedTopPercentileRank`

**•** `F1Score`

**•** `FMeasure`


-----

```
ModelId
Name

```


**•** `HitRateAtK`

**•** `LiftBucket`

**•** `MeanAbsoluteError`

**•** `MeanAbsoluteRank`

**•** `MeanAveragePrecisionAtK`

**•** `MeanPercentileRank`

**•** `MeanReciprocalRank`

**•** `MeanReciprocalRankAtK`

**•** `MeanTopReciprocalRank`

**•** `NormalizedDiscountedCumulativeGainsAtK`

**•** `Precision`

**•** `PrecisionAtK`

**•** `RSquared`

**•** `Recall`

**•** `RecallAtK`

**•** `RootMeanSquaredError`

**•** `auPR`

**•** `auROC`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related MLModel.

This field is a polymorphic relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID that uniquely identifies the metric.


-----

```
RowCount
Span
StartTime

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time span for the metric. Possible values are:

**•** `Day`

**•** `Hour`

**•** `Month`

**•** `SinceLastAction`

**•** `Week`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the model training started.

