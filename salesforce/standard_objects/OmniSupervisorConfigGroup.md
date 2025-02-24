#### OmniSupervisorConfigGroup

Represents the group of agents who are visible to the supervisors of an Omni-Channel supervisor configuration. The group, if visible,
appears in the Agents tab of Omni Supervisor. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), query(), update(), retrieve()

```

-----

##### Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
GroupId
OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the group of agents that’s made visible to the supervisors who are
assigned to the Omni-Channel supervisor configuration.

This is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

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

