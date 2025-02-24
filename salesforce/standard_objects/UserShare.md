#### UserShare

Represents a sharing entry on a user record. This object is available in API version 26.0 and later.


-----

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, only standard users or users with the Customize Application permission can access this object.

##### Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

```
IsActive
RowCause

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the User has access to log in (true) or not (false).
You can modify a User's active status from the user interface or via the API.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual. If no value is specified, the field defaults to` `Manual.`
All other `RowCause` values are read-only. After the sharing entry is created, this
field can’t be edited.

Possible values include:

**•** `Manual—The User or Group has access to the user record because a User with`
“All” access manually shared the User with them.

**•** `Rule—The User or Group has access to the user record via a User sharing rule.`

**•** `GuestRule—The User or Group has access via a User guest user sharing rule.`


-----

```
UserAccessLevel
UserId
UserOrGroupId

```


**•** `LpuImplicit—The User has access to records owned by high-volume`
Experience Cloud site users via a share group.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the specified user. The specified user is
denoted by the `UserId. The possible values are:`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s
default `UserAccessLevel.`

`UserAccessLevel` can be updated only if `RowCause` is set to `Manual`
```
  Sharing.

```
**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User being shared.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the User. This field can’t be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup


-----

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Usage

This object allows you to determine which users and groups can view or edit User records owned by other users.
