#### ServiceResourceSkill

Represents a skill that a service resource possesses in Field Service and Lightning Scheduler. This object is available in API version 38.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
EffectiveEndDate
EffectiveStartDate
LastReferencedDate

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the skill expires. For example, if a service resource needs to be
re-certified after six months, the end date would be the date their certification
expires.

**Type**
datetime

**Properties**
Create, Filter, Sort, Update

**Description**
The date when the service resource gains the skill. For example, if the skill
represents a certification, the start date would be the date of certification.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource skill was last modified. Its label in the user interface
is `Last Modified Date.`


-----

```
LastViewedDate
ServiceResourceId
SkillId
SkillLevel

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource skill was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service resource who possesses the skill.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill the service resource possesses.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The service resource’s skill level. Skill level can range from zero to 99.99.


-----

```
SkillNumber

##### Usage

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the resource skill assignment.


You can assign skills to all service resources in your org to indicate their certifications and areas of expertise, and specify each resource’s
skill level from 0 to 99.99. For example, you can assign Maria the “Welding” skill, level 50.

If you intend to use the skills feature, determine which skills you want to track and how skill level should be determined. For example,
you may want the skill level to reflect years of experience, certification levels, or license classes.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceResourceSkillChangeEvent (API version 54.0)**
Change events are available for the object.

**ServiceResourceSkillFeed**

Feed tracking is available for the object.

**ServiceResourceSkillHistory**

History is available for tracked fields of the object.
