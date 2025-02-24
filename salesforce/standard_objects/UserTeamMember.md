#### UserTeamMember

Represents a single User on the default opportunity team of another User.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
**•** This object is available only in organizations that have enabled the team selling functionality.

**•** Customer Portal users can’t access this object.

##### Fields

```
OpportunityAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. Level of access that the team member has to opportunities for which the user has
added his or her default opportunity team. The possible values are:

**•** `Read`

**•** `Edit`


-----

```
 OwnerId
 TeamMemberRole
 UserId

##### Usage

```

This field must be set to an access level that is higher than the organization’s default access
level for opportunities.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who owns the default opportunity team. This field can’t be updated.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on opportunities for which the User has added his or her
default opportunity team. The valid values are set by the organization’s administrator in the
Opportunity Team Roles picklist. Label is Team Role.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the default opportunity team. This field can’t
be updated.


If you attempt to create a record that matches an existing record, the create request updates any modified fields and returns the existing
record.

Users can set up their default opportunity team to include other users that typically work with them on opportunities.

SEE ALSO:

OpportunityTeamMember
