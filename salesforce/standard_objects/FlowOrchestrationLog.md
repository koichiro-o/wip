#### FlowOrchestrationLog

Represents logging data for a FlowOrchestrationInstance. This object is available in API version 54.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()update()

 Special Access Rules

```
If sharing rules are defined for FlowOrchestrationInstance and the Inherit orchestration run sharing rules to control orchestration run log
record access setting is enabled, then orchestration run log record access is inherited from related orchestration run records. If the Inherit
orchestration run sharing rules to control orchestration run log record access setting isn’t enabled, a user must have the Manage Flow
permission. Or the user must have the View All Data permission.

##### Fields

```
Actor
Assignee

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
For an interactive step, the user that completed the work item.

For a background or MuleSoft step, the username of the user that the step ran as.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
AssigneeType
Comments
Context
Duration

```

**Description**
For an interactive step, the user, group, or queue assigned to a work item when the
FlowOrchestrationLog relates to an interactive FlowOrchestrationStep.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For an interactive step, the assignee type associated with an interactive step's work item.
Valid values are:

**•** `Group`

**•** `Invalid`

**•** `Queue`

**•** `User`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string stored in an output variable with the API name of Comments from a flow called
by a completed orchestration step.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record where the assigned user completed the flow associated with an
interactive step in the Work Guide component.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
A long number that indicates the duration, in seconds, of the associated
FlowOrchestrationInstance, FlowOrchestrationStage, FlowOrchestrationStep, or
FlowOrchestrationWorkItem.


-----

```
Kind
Name
OrchestationInstanceId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The milestone associated with the FlowOrchestrationLog. Valid values are:

**•** `CancelInstance—The associated FlowOrchestrationInstance was canceled.`

**•** `DiscontinueStage—The associated FlowOrchestrationStage was discontinued.`

**•** `DiscontinueStep—The associated FlowOrchestrationStep was discontinued.`

**•** `EndInstance—The associated FlowOrchestrationInstance was completed`
successfully.

**•** `EndStage—The associated FlowOrchestrationStage was exited successfully.`

**•** `EndStep—The associated FlowOrchestrationStep was exited successfully.`

**•** `EndWorkItem—The associated FlowOrchestrationWorkItem was completed`
successfully.

**•** `FailInstance—The associated FlowOrchestrationInstance encountered an error.`

**•** `FailStage—The associated FlowOrchestrationStage encountered an error.`

**•** `FailStep—The associated FlowOrchestrationStep encountered an error.`

**•** `ResumeInstance—A failed or paused orchestration instance was resumed.`

**•** `ReassignWorkItem—The associated FlowOrchestrationWorkItem was reassigned.`

**•** `StartInstance—The associated FlowOrchestrationInstance started.`

**•** `StartStage—The associated FlowOrchestrationStage started.`

**•** `StartStep—The associated FlowOrchestrationStep started.`

**•** `StartWorkItem—The associated FlowOrchestrationWorkItem started.`

**•** `SuspendInstance—The associated FlowOrchestrationInstance was suspended.`

**•** `SuspendStage—The associated FlowOrchestrationStage was suspended.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name for the FlowOrchestrationLog record.

**Type**
reference

**Properties**
Filter, Sort, Group

**Description**
The FlowOrchestrationInstance associated with the FlowOrchestrationLog.


-----

```
OrchestrationName
OrchestrationVersion
StageName
StepName
Timestamp

```

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the orchestration.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
An integer for the FlowDefinitionVersion of the orchestration associated with the
FlowOrchestrationLog.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the stage in the associated orchestration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the step in the associated orchestration.

**Type**
dateTime

**Properties**
Filter, Sort


-----

**Description**
The date and time when the FlowOrchestrationLog milestone occured.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationLogFeed on page 54**
Feed tracking is available for the object.

**FlowOrchestrationLogHistory on page 62**
History is available for tracked fields of the object.

**FlowOrchestrationLogOwnerSharingRule on page 64**
Sharing rules are available for the object.

**FlowOrchestrationLogShare on page 66**
Sharing is available for the object.
