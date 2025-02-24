#### CaseTeamTemplateMember

Represents a member on a predefined case team, which is a group of users that helps resolve cases.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Spring ’20 and later, only users with read access to the Case object can access this object.

##### Fields

```
MemberId
TeamRoleId
TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a team member on a predefined case team.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the predefined case team member's case team role.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

**Description**
The ID of the predefined case team's template.
