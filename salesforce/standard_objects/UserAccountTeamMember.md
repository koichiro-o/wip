#### UserAccountTeamMember

Represents a User on the default account team of another User.

See also OpportunityTeamMember, which represents a User on the opportunity team of an Opportunity

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal and Chatter Free users can't access this object.

##### Fields

```
AccountAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update


-----

```
CaseAccessLevel
ContactAccessLevel
OpportunityAccessLevel

```

**Description**
Required. For Account records that the user has added to his or her default account
team, the level of access the account team member has. . The possible values are:

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default
access level for accounts.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. Level of access that the account team member has to Case records related
to the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization's default
access level for cases.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
Required. ForContact records related to the account, the level of access that the
account team member has. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization's default
access level for contacts.

Note: When `DefaultContactAccess` is set to `Controlled by`
```
    Parent, you can’t create or update this field.

```
**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update


-----

```
 OwnerId
 TeamMemberRole
 UserId

##### Usage

```

**Description**
Required. Level of access that the team member has to Opportunity records related
to the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is higher than the organization’s default
access level for opportunities.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who owns the default account team.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on opportunities for which the user has added his
or her default account team. The valid values are set by the organization’s administrator
in the Account Team Roles picklist. Label is Team Role.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the default account team. This field
cannot be updated.


This object is available only in organizations that have enabled the account teams functionality, which can be done using the user
interface.

If you attempt to create a record that matches an existing record, the create call updates any modified fields and returns the existing
record.

You can set up a User record so the default account team includes the others who typically work with them on accounts.


-----
