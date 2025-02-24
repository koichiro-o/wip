#### CaseTeamMember

Represents a case team member, who works with a team of other users to help resolve a case.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Spring ’20 and later, only users with read access to the Case object can access this object.

When accessing from Apex code, use the `WITH SECURITY_ENFORCED` clause to enable field-level and object-level security
permissions checking for `SOQL SELECT queries, including subqueries and cross-object relationships. To learn more, see Filter SOQL`
[Queries Using WITH SECURITY_ENFORCED.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_classes_with_security_enforced.htm)

##### Fields

```
MemberId
ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a member on a case team.

This is a polymorphic relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
reference


-----

```
TeamRoleId
TeamTemplateId

```

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team member is associated.

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
Create, Filter, Group, Sort, Update

**Description**
The ID of the case team role with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamRole

**Relationship Type**
Lookup

**Refers To**
CaseTeamRole

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the predefined team with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate


-----

```
TeamTemplateMemberId
