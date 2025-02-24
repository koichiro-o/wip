#### PermissionSetGroupComponent

A junction object that relates the PermissionSetGroup and PermissionSet objects via their respective IDs; enables permission set group
recalculation to determine the aggregated permissions for the group. This object is available in API version 45.0 and later.

PermissionSetGroupComponent is a child object of PermissionSet and PermissionSetGroup.

##### Supported Calls
```
create(), delete(), describeSObject(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only users with the "View Setup and Configuration" permission can access this object.

##### Fields

```
PermissionSetGroupId
PermissionSetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique permission set group ID.

This is a relationship field.

**Relationship Name**
PermissionSetGroup

**Relationship Type**
Lookup

**Refers To**
PermissionSetGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique permission set ID of a permission set in a permission set group.


-----

This is a relationship field.

**Relationship Name**
PermissionSet

**Relationship Type**
Lookup

**Refers To**
PermissionSet

##### Usage

Use the PermissionSetGroupComponent object to add members to or delete members from a permission set group, or to query for
group members.
