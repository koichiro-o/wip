#### OmniSupervisorConfigTab

Represents the visible tabs specified in an Omni Supervisor configuration. This object is available in API version 60.0 and later.

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

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order in which tabs are displayed in Omni Supervisor.


-----

```
OmniSupervisorConfigId
OmniSupervisorTabType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Omni-Channel supervisor configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Tabs shown on the Omni Supervisor page. Possible values are:

**•** `Agents` — the Agents tab

**•** `AssignedWork` — the Assigned Work tab

**•** `FlexiPageType` — A custom tab created using Lightning App Builder, with the
`OmniSupervisorPageType` value of the `FlexiPage Type` field

**•** `QueuesBacklog` — the Queues Backlog tab

**•** `SkillsBacklog` — the Skills Backlog tab

**•** `Wallboard` — the Wallboard tab

