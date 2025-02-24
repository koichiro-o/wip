#### FlowOrchestrationStepInstance

Represents a run-time instance of a step in a run-time instance of a stage of a run-time instance of an orchestration. This read-only object
is available in API version 53.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

If sharing rules are defined for FlowOrchestrationStepInstance, they determine access to specific orchestration step run records. Or the
user must have the View All Data permission.

##### Fields

```
Description
Label
Name
OrchestrationInstanceId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the step.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the step.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the step.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationInstance associated with the orchestration step instance.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance


-----

```
OwnerId
StageInstanceId
Status

```

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
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationStageInstance associated with the orchestration step instance.

This field is a relationship field.

**Relationship Name**
StageInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationStageInstance

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the orchestration step instance. Valid values are:

**•** `Completed—The step instance completed.`

**•** `Discontinued—The step instance was in progress or completed when it’s associated`
stage instance completed, or the step was in progress or completed when the
orchestration instance encountered an error.

**•** `Error—The step instance encountered an error or the autolaunched flow associated`
with a step instance encountered an error.


-----

```
StepType

##### Associated Objects

```


**•** `InProgress—The step instance is running, the step instance was in progress when`
its associated stage encountered an error, or the screen flow associated with the step
instance encountered an error.

**•** `NotStarted—The step instance was created, but hasn’t met its entry condition.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of step. Valid values are:

**•** `InteractiveStep—Interactive Step`

**•** `BackgroundStep—Background Step`

**•** `AynchronousBackgroundStep—Asynchronous Background Step`

This value is available in API version 54.0 and later.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationStepInstanceFeed on page 54**
Feed tracking is available for the object.

**FlowOrchestrationStepInstanceHistory on page 62**
History is available for tracked fields of the object.

**FlowOrchestrationStepInstanceOwnerSharingRule on page 64**
Sharing rules are available for the object.

**FlowOrchestrationStepInstanceShare on page 66**
Sharing is available for the object.
