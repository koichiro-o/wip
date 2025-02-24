#### MLModel

Represents an AI model that can be used in Einstein Prediction Builder, Einstein Recommendation Builder, and other Einstein features.
This object is available in API version 53.0 and later.

This object contains information that represents many types of AI models. Some fields contain information for only a specific type of
model.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available with Einstein Prediction Builder and Einstein Recommendation Builder.

##### Fields

```
ApprovalStatus
Dataset
ModelType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the model is approved, pending approval, or rejected.

Possible values are:

**•** `Approved`

**•** `Pending`

**•** `Rejected`

The default value is `Pending.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the dataset used to create the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
Name
PredictionDefinitionId

```

**Description**
Indicates the type of model.

Possible values are:

**•** `BinaryClassification`

**•** `DecisionTree`

**•** `DeepLearningIntent`

**•** `DeepLearningNER`

**•** `GeneralizedLinearModels`

**•** `GlobalDeepLearningIntent`

**•** `GlobalDeepLearningNER`

**•** `GlobalLanguageDetection`

**•** `GradientBoostedTrees`

**•** `LinearRegression`

**•** `LinearSupportVectorClassifiers`

**•** `LogisticRegression`

**•** `MulticlassClassification`

**•** `NaiveBayes`

**•** `NeuralNet`

**•** `PopularityCount`

**•** `RandomForest`

**•** `Regression`

**•** `XGBoost`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically generated ID that uniquely identifies the model.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related prediction definition.

This field is a relationship field.

**Relationship Name**
PredictionDefinition


-----

```
RecommendationDefinitionId
ScoringStatus
TrainingEndTime
TrainingStartTime

```

**Relationship Type**
Lookup

**Refers To**
MLPredictionDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related recommendation definition.

This field is a relationship field.

**Relationship Name**
RecommendationDefinition

**Relationship Type**
Lookup

**Refers To**
MLRecommendationDefinition

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether scoring is enabled or disabled.

Possible values are:

**•** `Disabled`

**•** `Enabled`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the date and time when the training ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

**Description**
Indicates the date and time when the training started.
