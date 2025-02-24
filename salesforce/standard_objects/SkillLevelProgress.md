#### SkillLevelProgress

Represents training progress for a given user. This object is available in API version 51.0 and later.

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
CompletedCount
CompletedDate
OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Number of modules that have been completed towards this Skill Mapping.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when this progress was completed.

**Type**
reference


-----

```
ServiceResourceId
SkillLevelDefinitionId

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of skill level progress.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Service Resource that will be granted a service resource skill when the progress is
complete.

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
The corresponding skill mapping for this progress.

This is a relationship field.

**Relationship Name**
SkillLevelDefinition

**Relationship Type**
Lookup

**Refers To**
SkillLevelDefinition


-----

```
SkillMasterLabel
Status
TotalCount

##### Associated Objects

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The master label of the Skill associated with the associated SkillLevelDefinition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the progress.

Possible values are:

**•** `A—Approved`

**•** `R—Review`

**•** `S—Started`

The default value is 'S'.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The total number of modules that need to be completed.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelProgressOwnerSharingRule on page 64**
Sharing rules are available for the object.

**SkillLevelProgressShare on page 66**
Sharing is available for the object.
