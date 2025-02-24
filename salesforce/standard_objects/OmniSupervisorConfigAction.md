#### OmniSupervisorConfigAction

Represents the actions available to the supervisors of an Omni-Channel supervisor configuration. This object is available in API version
56.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

##### Fields

```
DisplayOrder
OmniSupervisorActionType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order in which the action is displayed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
An action that a supervisor can perform.

Possible values are:

**•** `AgentDetails.CustomAction`

**•** `AllAgents.AWSDashboard—All Agents - View Amazon Real-Time Metrics`

**•** `AllAgents.AssignLearning`

**•** `AllAgents.ChangeQueues`


-----

```
OmniSupervisorConfigId

```


**•** `AllAgents.ChangeSkills`

**•** `AllAgents.CustomAction`

**•** `AssignedWork.AWSDashboard—Assigned Work - View Amazon Real-Time`
Metrics

**•** `AssignedWork.CustomAction`

**•** `AssignedWorkDetails.CustomAction`

**•** `QueueDetails.CustomAction`

**•** `QueuesBacklog.AWSDashboard—Queues Backlog - View Amazon Real-Time`
Metrics

**•** `QueuesBacklog.CustomAction`

**•** `QueuesBacklog.ManageQueues—Queues Backlog - Assign Agents to Queues`

**•** `SkillDetails.CustomAction`

**•** `SkillsBacklog.AWSDashboard—Skills Backlog - View Amazon Real-Time`
Metrics

**•** `SkillsBacklog.CustomAction`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Omni-Channel supervisor configuration.

This field is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

