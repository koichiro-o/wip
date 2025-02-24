#### MLPredictionDefinition

Represents a prediction definition that specifies details about the prediction. This object is available in API version 50.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Fields

```
```
ApplicationId
DeveloperName
Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the parent AI Application.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

```
MasterLabel
NamespacePrefix
PredictionField

```

**Description**
The language of the prediction. Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the prediction throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the prediction, if installed with a managed package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
PushbackField
Status
Type

```

**Description**
Field that the prediction is based on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field that the prediction writes scores to.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the prediction. Possible values are:

**•** `Disabled`

**•** `Draft`

**•** `Enabled`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of model that returns the prediction values. Possible values are:

**•** `BinaryClassification`

**•** `DeepLearningIntentClassification`

**•** `DeepLearningNameEntityRecognition`

**•** `GlobalDeepLearningIntentClassification`

**•** `GlobalDeepLearningNameEntityRecognition`

**•** `LanguageDetection`

**•** `MulticlassClassification`

**•** `Regression`

**•** `ScoringSpecificOutcome`


-----
