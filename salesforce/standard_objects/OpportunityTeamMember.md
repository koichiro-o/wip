#### OpportunityTeamMember

Represents a User on the opportunity team of an Opportunity.

See also UserTeamMember, which represents a User who is on the default Opportunity team of another user.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
IsDeleted
Name
OpportunityAccessLevel

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not
(false). Label is Deleted.

Note: An OpportunityTeamMember that is deleted isn’t moved to the Recycle
Bin and can’t be undeleted, unless the record was cascade-deleted when deleting
a related Opportunity. For directly deleted OpportunityTeamMember records,
don't use the `isDeleted` field to detect deleted records in SOQL queries.
Instead, use `getDeleted().`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The team member name. This read-only field is available in API version 30.0 and later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Opportunity access level for this team member. Valid values:

**•** `Read`

**•** `Edit`

**•** `All`


-----

```
OpportunityId
PhotoURL
TeamMemberRole
Title
UserId

```

This field is supported in triggers, but not in workflows or validation rules. It’s editable
in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the Opportunity associated with this opportunity team. This field can’t
be updated.

**Type**
URL

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the users Chatter photo URL. This field is available in API version
32.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on the opportunity. The org’s admin sets the valid
values in the Opportunity Team Roles picklist. Label is Team Role.

**Type**
string

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the user’s title. This field is available in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the opportunity team. This field can’t
be updated.


-----

##### Usage

If you create a record for this object and the `OpportunityId` and `UserId` combination matches an existing record, the system
updates any modified fields and returns the existing record.

In the user interface, users can set up an opportunity team for the opportunities they own. The opportunity team includes other users
that are working on the opportunity with them. This object is available only in organizations that have enabled team selling.

Note: The behavior for changing ownership of opportunities is different using the user interface when the previous owner is on
an opportunity team. For example, when you change the owner of an opportunity using the API, the previous owner's access
becomes Read Only or the access specified in your organization-wide default for opportunities, whichever is greater. However,
performing this same action in the user interface allows you to select the access level for the previous owner when the previous
owner is on an opportunity team.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityTeamMemberHistory on page 62 (API version 59.0)**
History is available for tracked fields of the object.

SEE ALSO:

UserTeamMember
