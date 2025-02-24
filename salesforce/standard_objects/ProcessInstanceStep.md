#### ProcessInstanceStep

Represents one work item in an approval process (ProcessInstance).


-----

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

ProcessInstanceStep fields are never populated for approval process instances that were completed before the Summer '14 rollout. For
approval process instances that were pending during the Summer '14 rollout, all ProcessInstanceStep fields are populated only after the
approval process instance is next acted upon after the Summer '14 rollout.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ActorId
Comments
ElapsedTimeInDays

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who’s assigned to this approval step.

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Limit: 4,000 bytes.

The contents of this field can be publicly viewed.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
ElapsedTimeInHours
ElapsedTimeInMinutes
OriginalActorId
ProcessInstanceId

```

**Description**
The total time in days since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this step was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this step was started.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who was originally assigned to this approval step.

This is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ProcessInstance that this approval step belongs to.

This is a relationship field.

**Relationship Name**
ProcessInstance


-----

```
StepNodeId
StepStatus

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the node currently assigned to this approval step.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this approval step.

**•** Approved

**•** Fault

**•** Held

**•** NoResponse

**•** Pending

**•** Reassigned

**•** Rejected

**•** Removed

**•** Started

If the approval step requires unanimous approval and one approver rejects the request, the
value of this field for the other approvers changes to NoResponse. Likewise, if approval is
based on the first response and an approver responds, the value of this field for the other
approvers changes to NoResponse.


Query or retrieve a new step in an approval process (ProcessInstance).

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.


-----

**ProcessInstanceStepChangeEvent (API Version 58.0)**
Change events are available for the object.

SEE ALSO:

ProcessInstance

ProcessInstanceHistory

ProcessInstanceWorkitem
