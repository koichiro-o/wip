#### UnifiedActivityInsight

Represents an insight related to a unified activity. This object is available for reports and dashboards in the Winter ’24 release and later.


-----

##### Supported Calls
```
describeSObjects(), query()

```
Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

##### Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

##### Fields

```
ActivityId
AggregatedKeywordOccurrences
InsightType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the unified activity that this insight is associated with.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedEmail, UnifiedMeeting, UnifiedTask, UnifiedVideoCall, UnifiedVoiceCall

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of keyword occurrences that triggered this insight. This field is the sum of
occurrences for all the attached UnifiedActivityInsightKeyword objects.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Type of the insight.


-----

```
OwnerId
Scope

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. ID of the owner of the insight. Only user-scoped insights have owners
(Scope=USER).

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist, Sort

**Description**
The scope of the insight.

Possible values are:

**•** `ORG`

**•** `USER`

