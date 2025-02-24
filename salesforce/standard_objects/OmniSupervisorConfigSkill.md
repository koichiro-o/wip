#### OmniSupervisorConfigSkill

Represents the skills that are visible to the supervisors of an Omni-Channel supervisor configuration. These skills, if visible, appear in the
Skills Backlog tab of Omni Supervisor. This object is available in API version 53.0 and later.

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


-----

```
SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the skill that’s made visible to the supervisors who are assigned to the
Omni-Channel supervisor configuration.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

