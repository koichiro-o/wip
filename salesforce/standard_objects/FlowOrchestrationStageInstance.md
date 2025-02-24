#### FlowOrchestrationStageInstance

Represents a run-time instance of a stage in a run-time instance of an orchestration. This read-only object is available in API version 53.0
and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
If sharing rules are defined for FlowOrchestrationStageInstance, they determine access to specific orchestration stage run records. Or
the user must have the View All Data permission.

##### Fields

```
Label

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the flow orchestration stage instance. This label helps users and administrators
differentiate between step instances from the same orchestration.


-----

```
Name
OrchestrationInstanceId
OwnerId
Position

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name for the flow orchestration stage instance.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationInstance associated with the orchestration stage instance.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
For internal use only.


-----

```
Status

##### Associated Objects

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The run status of the orchestration stage instance. Valid values are:

**•** `Completed—The stage instance completed.`

**•** `Discontinued—The stage was in progress or completed when the orchestration`
instance encountered an error.

**•** `Error—The stage instance encountered an error, an instance of a background step`
within the stage encountered and error, or an autolaunched flow called by a background
step within the stage encountered an error.

**•** `InProgress—The stage instance is in progress.`

**•** `Suspended—The stage was in progress when the orchestration instance was manually`
suspended.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationStageInstanceFeed on page 54**
Feed tracking is available for the object.

**FlowOrchestrationStageInstanceHistory on page 62**
History is available for tracked fields of the object.

**FlowOrchestrationStageInstanceOwnerSharingRule on page 64**
Sharing rules are available for the object.

**FlowOrchestrationStageInstanceShare on page 66**
Sharing is available for the object.
