#### AgentWorkSkill

Represents a skill used to route a work assignment to an agent. AgentWorkSkill is used for reporting and represents the result of a routing
decision. This object is available in API version 42.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

##### Fields

```
AgentWorkId
IsAdditionalSkill

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The AgentWork object associated with this skill.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Name
SkillId
SkillLevel
SkillPriority
WasDropped

```

**Description**
After a designated timeout period, a skill marked as additional is dropped from Omni-Channel
routing. The case is then routed to the best-matched agent, even if the agent doesn’t have
all the skills. The default value is false. Available in API version 48.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The skill that is required or additional.

**Type**
double

**Properties**
Filter, Sort

**Description**
The level of the required or additional skill. Skill levels can range from 1 to 10. Depending on
your business needs, you might want the skill level to reflect years of experience, certification
levels, or license classes.

**Type**
int

**Properties**
Aggregatable, Filter, Group, Nillable, Sort

**Description**
For additional skills, specifies the order in which skills are dropped if after the specified timeout
no agent with that skill is available. Higher priority-value skills are dropped first. Lower
priority-value skills, for example 0, are dropped last. Skills with the same priority value are
dropped as a group. You can set skill priority using attribute setup for skills-based routing or
Apex code.

**Type**
boolean

**Properties**
Filter, Group, Sort


-----

**Description**
For skills marked as additional, indicates if the skill was dropped from Omni-Channel routing
because an agent with this skill was not available. The default value is false. Available in API
version 48.0 and later.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AgentWorkSkillChangeEvent (API version 62.0)**
Change events are available for the object.
