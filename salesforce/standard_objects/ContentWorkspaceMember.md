#### ContentWorkspaceMember

Represents a member of a content library. This object is available in API version 40.0 and later.

Manage library membership from the API.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
A user can create/update/delete memberships if they have the Manage Salesforce CRM Content admin perm or the Manage Library
permission for the library concerned.


-----

##### Fields

**Field**
```
ContentWorkspaceId
ContentWorkspacePermissionId
MemberId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the library.

This is a relationship field.

**Relationship Name**
ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
ContentWorkspace

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The id of the library permission or role.

This is a relationship field.

**Relationship Name**
ContentWorkspacePermission

**Relationship Type**
Lookup

**Refers To**
ContentWorkspacePermission

**Type**
reference

**Properties**
Create, Filter, Group,Namepointing, Sort

**Description**
ID of the library member (the member is either a user or a group).

This is a polymorphic relationship field.

**Relationship Name**
Member


-----

```
MemberType

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable,Restricted picklist, Sort

**Description**
The type of library member. Valid values are:

**•** G - Group

**•** U - User


Use this object to create, update, or delete members from a library.
