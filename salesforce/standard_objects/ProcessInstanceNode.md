#### ProcessInstanceNode

Represents a step in an instance of an approval process. Compare to ProcessNode, which describes the step in a process definition. Use
this object to retrieve approval history.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

ProcessInstanceNode fields are never populated for approval process instances that were completed before the Summer '14 rollout. For
approval process instances that were pending during the Summer '14 rollout, all ProcessInstanceNode fields are populated only after
the approval process instance is next acted upon after the Summer '14 rollout.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
CompletedDate
ElapsedTimeInDays

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The completion date and time of this step in the approval process. The ElapsedTimeDay,
`ElapsedTimeHours, and ElapsedTimeMinutes` field values are calculated using
```
  CompletedDate.

```
**Type**
double


-----

```
ElapsedTimeInHours
ElapsedTimeInMinutes
LastActorId
NodeStatus

```

**Properties**
Filter, Nillable, Sort

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
Filter, Group, Nillable, Sort

**Description**
The last actor that approved or rejected this step.

This is a relationship field.

**Relationship Name**
LastActor

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this approval instance, for example Started, Pending, or Approved.


-----

```
ProcessInstanceId
ProcessNodeId
ProcessNodeName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The approval process this step is part of.

This is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The identifier for this step.

This is a relationship field.

**Relationship Name**
ProcessNode

**Relationship Type**
Lookup

**Refers To**
ProcessNode

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of this step.

The contents of this field can be publicly viewed.

