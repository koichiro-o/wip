#### SkillLevelDefinition

Represents a skill which can be acquired by completing enablement site (myTrailhead) modules. This object is available in API version
51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

##### Fields

```
Description
IsAutoApproved

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Describes the mapping.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this mapping auto-approves.

The default value is 'false'.


-----

```
LearningContent
OwnerId
SkillId
SkillLevel

```

**Type**
string

**Properties**
Filter, Nillable

**Description**
The titles of the Trailhead modules associated to this mapping.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the Skill Level Definition.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill that this mapping is for.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The level to assign for the skill.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelDefinitionOwnerSharingRule on page 64**
Sharing rules are available for the object.

**SkillLevelDefinitionShare on page 66**
Sharing is available for the object.
