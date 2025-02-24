#### CaseTeamRole

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the team member included in a predefined case team.

This is a relationship field.

**Relationship Name**
TeamTemplateMember

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplateMember


Represents a case team role. Every case team member has a role on a case, such as “Customer Contact” or “Case Manager.”

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only users with read access to the Case object can access this object.

##### Fields

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for cases. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`


-----

```
Name
PreferencesVisibleInCSP

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the case team role.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether or not the case team role is visible to Customer Portal users.

