#### AIInsightAction

Represents an Einstein prediction insight action. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

AIInsightAction is a one-to-many child of AIRecordInsight. AIInsightAction contains information about predicted actions for this particular
insight. AIInsightAction has one or more AIInsightValue children which contain predicted values for the action. For example, an
AIInsightAction could represent a quick action, and have a child AIInsightValue with the recommended value used by the quick action.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Prediction insight objects are only available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

##### Fields

```
ActionId
ActionName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated action, such as the ID of a Macro.

This is a polymorphic relationship field.

**Relationship Name**
Action

**Relationship Type**
Lookup

**Refers To**
ApexClass, AuraDefinitionBundle

**Type**
picklist


-----

```
AiRecordInsightId
Confidence
Name
Type

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The ID of the action. For example, a value of “Case.SendEmail” indicates a send email quick
action on Case.

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

**Refers To**
AIRecordInsight

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight. Higher values (near 1.0)
indicate stronger confidence.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightAction.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of action. Possible values are:


-----

**•** `InvocableAction—Invocable Action`

**•** `Macro—Macro`

**•** `QuickAction—Quick action.`

**•** `StandardAction—Standard Action. An example standard action would be to`
update a record.

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
