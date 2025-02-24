#### OmniSupervisorConfigQueue

Represents the queues that are visible to the supervisors of an Omni-Channel supervisor configuration. The queue, if visible, appears in
the Queues Backlog and Assigned Work tabs of Omni Supervisor. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

##### Fields

```
OmniSupervisorConfigId
QueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
om

A unique identifier for the Omni-Channel supervisor configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the queue that’s made visible to the supervisors who are assigned to
the Omni-Channel supervisor configuration.

This is a relationship field.


-----

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group
