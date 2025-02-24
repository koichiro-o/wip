#### AIInsightReason

Represents an Einstein prediction insight reason. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

AIInsightReason is a one-to-many child of AIInsightValue. AIInsightReason contains details about how Einstein predicted an insight value.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

##### Fields

```
AiInsightValueId
Contribution
FeatureType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIInsightValue.

This is a relationship field.

**Relationship Name**
AiInsightValue

**Relationship Type**
Lookup

**Refers To**
AIInsightValue

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The contribution weight for this insight reason.

**Type**
picklist


-----

```
FeatureValue
FieldName
FieldValue
Intensity
Name
Operator

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the feature, such as BOOL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the feature, such as TRUE or FALSE.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the field the insight uses for its evaluation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value for the field the insight uses for its evaluation.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The intensity weight for this insight reason.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightReason.

**Type**
picklist


-----

```
ReasonLabelKey (Beta)
RelatedInsightReasonId
(Beta)
SortOrder (Beta)
Variance

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The logical operator the insight uses to compare the field value with the expression value.
For example, if the prediction evaluates whether the fieldValue for the field `bonus__c` is
greater than $5,000, the logical operator is `greater than.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key used to map an Einstein Key Accounts Identification (Beta) insight phrase or phrases
to the correct messaging template.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID used to relate multiple insights to a single model reason in the Einstein Key Accounts
Identification (Beta) feature.

This is a relationship field.

**Relationship Name**
RelatedInsightReason

**Relationship Type**
Lookup

**Refers To**
AIInsightReason

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A number value used to organize the phrases in the model’s insights message in the Einstein
Key Accounts Identification (Beta) feature.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

**Description**
The variance weight for this insight reason.

##### Usage

When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.
