#### CaseTeamTemplateRecord

The CaseTeamTemplateRecord object is a linking object between the Case and CaseTeamTemplate objects. To assign a predefined case
team to a case (customer inquiry), create a CaseTeamTemplateRecord record and point the `ParentId` to the case and the
`TeamTemplateId` to the predefined case team.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only users with read access to the Case object can access this object.

##### Fields

```
ParentId
TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

**Description**
The ID of the predefined case team with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate
