#### UserRole

Represents a user role in your organization.

Note: This object was called “Role” in previous versions of the API documentation.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

```

-----

##### Special Access Rules

As of Summer ’20 and later, only users with the View Roles and Role Hierarchy permission can access this object, and only users with
the Manage Roles permission can edit this object.

##### Fields

```
CaseAccessForAccountOwner
ContactAccessForAccountOwner
DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The case access level for the account owner.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The contact access level for the account owner.

Note: When DefaultContactAccess is set to Controlled
```
    by Parent, you can’t create or update this field.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org.
It must begin with a letter, not include spaces, not end with an underscore,
and not contain two consecutive underscores. In managed packages, this
field prevents naming conflicts on package installations. With this field, a
developer can change the object’s name in a managed package and the
changes are reflected in a subscriber’s organization. Corresponds to Role
**Name in the user interface.**

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one
for each record.


-----

```
ForecastUserId
IsPartner
MayForecastManagerShare
Name
OpportunityAccessForAccountOwner
ParentRoleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the forecast manager associated with this role. Label is User ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user role is a partner who has access to the partner
portal (true) or not (false). This field is not available for release 9.0 and
later. Instead, use `PortalType` with the value `Partner.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecast manager can manually share their own
forecast.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the role. Corresponds to Label on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The opportunity access level for the account owner. Note that you
can’t set a user role with an opportunity access less than that specified in
organization-wide defaults.

**Type**
reference


-----

```
PortalAccountId
PortalAccountOwnerId
PortalRole
PortalType
RollupDescription

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent role.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the role’s associated portal account. This field is read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the role’s associated portal account’s owner. This field is read-only.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The portal role: Executive, Manager, User, or PersonAccount.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This value indicates the type of portal for the role:

**•** None: Salesforce application role.

**•** CustomerPortal: Customer portal role.

**•** Partner: partner portal role. The field `IsPartner` used in release 8.0
will map to this value.

This field replaces IsPartner beginning with release 9.0.

**Type**
string


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the forecast rollup. Label is Description.

##### Usage

Use this object to query the set of currently configured user roles in your organization. Use it in your client application to obtain valid
UserRole IDs to use when querying or modifying a User record.

Users with the View Roles and Role Hierarchy permission can query or describe this object. If your client application logs in with the
“Manage Users” permission, it can query, create, update, or delete UserRole records.

Note: You can’t update any field for a portal role.

For example, the following code finds all roles that are not assigned to any users.
```
SELECT Id, Name, DeveloperName
FROM UserRole
WHERE Id NOT IN (SELECT UserRoleId
           FROM User
           WHERE UserRoleId !='000000000000000')

```
SEE ALSO:

Overview of Salesforce Objects and Fields
