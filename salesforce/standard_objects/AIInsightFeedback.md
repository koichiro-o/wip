#### AIInsightFeedback

Represents an Einstein prediction insight feedback. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

AIInsightFeedback is a one-to-many child of AIRecordInsight. AIInsightFeedback contains information about explicit and implicit feedback
collected from users for a particular insight.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.


-----

##### Fields

**Field**
```
 ActualValue
 AiFeedback
 AiInsightFeedbackType
 AiRecordInsightId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The raw feedback value. This field is null when no recommendation is selected.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The feedback user sentiment. Possible values are:

**•** `Negative—Negative feedback`

**•** `Neutral—Neutral feedback`

**•** `Positive—Positive feedback`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The nature of the feedback. Possible values are:

**•** `Explicit—Explicit feedback. For example, a user applies and saves an Einstein`
recommendation on a case.

**•** `Implicit—Implicit feedback. For example, a user edits or updates a case field without`
viewing or applying field recommendations from Einstein.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup


-----

```
 Name
 Rank
 ValueId

##### Usage

```

**Refers To**
AIRecordInsight

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightFeedback.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feedback score.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated AIInsightValue.

This is a polymorphic relationship field.

**Relationship Name**
Value

**Relationship Type**
Lookup

**Refers To**
AIInsightAction, AIInsightValue


Salesforce creates AIInsightFeedback records based on user responses to predictions after the prediction has been created. User feedback,
such as a thumbs up/down response or accepting a recommended value, results in the creation of a feedback record in which the
feedback type is explicit. An implicit feedback record is created when Einstein makes a recommendation but the field is updated in
another way, for example, by a process. Once the AIInsightFeedback record has been created, it’s immutable.

Custom fields can’t be added to Einstein insight objects.


-----
