#### PermissionSetAssignment

Represents a user’s assignment to a permission set or permission set group. This object is available in API version 22.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update()

 Special Access Rules

```
As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Assign Permission Sets

**•** Manage User

##### Fields

```
AssigneeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that is assigned the permission set indicated in `PermissionSetId`
or the permission set group indicated in `PermissionSetGroupId.`

This is a relationship field.

**Relationship Name**
Assignee


-----

```
ExpirationDate
IsActive

```
`IsRevoked` (Beta)
```
LastCreatedByChangeId

```
(Beta)


**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the assignment of the permission set or permission set group expires for the
specified user. This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the assignment is active (true) or not (false). Defaults to `false.`
This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the assignment was revoked (true) or not (false). Defaults to false.
This field is available in API version 57.0 and later.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its
sole discretion. Any use of the Beta Service is subject to the applicable Beta Services
[Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user access change record related to this permission set or permission set group
assignment. This field is available in API version 57.0 and later.

This field is a relationship field.


-----

```
LastDeletedByChangeId

```
(Beta)
```
PermissionSetGroupId

```

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its
sole discretion. Any use of the Beta Service is subject to the applicable Beta Services
[Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user access change record related to this permission set or permission set group
assignment being revoked. This field is available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its
sole discretion. Any use of the Beta Service is subject to the applicable Beta Services
[Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the permission set group assigned to the user specified in `AssigneeId. This`
field is available in API version 45.0 and later.

This is a relationship field.

**Relationship Name**
PermissionSetGroup

**Relationship Type**
Lookup


-----

```
PermissionSetId

##### Usage

```

**Refers To**
PermissionSetGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the permission set assigned to the user specified in `AssigneeId.`

This is a relationship field.

**Relationship Name**
PermissionSet

**Relationship Type**
Lookup

**Refers To**
PermissionSet


**Finding Permission Set Assignments**
Use the PermissionSetAssignment object to query permission set assignments to find out which permission sets are assigned to
which users. Because each user can be assigned to many permission sets and each permission set can be assigned to many users,
each PermissionSetAssignment ID represents the association of a single user and single permission set.

For example, to search for all permission sets assigned to a particular user:
```
  SELECT Id, PermissionSetId
  FROM PermissionSetAssignment
  WHERE AssigneeId = '005600000017cKt'

```
To search for all users assigned to a particular permission set:
```
  SELECT Id, AssigneeId
  FROM PermissionSetAssignment
  WHERE PermissionSetId = '0PS30000000000e'

```
You can also create a new permission set assignment, or use delete to remove a permission set that's assigned to a user. To update
an assignment, delete an existing assignment and insert a new one.

**User Licenses**
When assigning a permission set, if the PermissionSet has a `UserLicenseId, its` `UserLicenseId` and the Profile
`UserLicenseId` must match. To determine a user's license assignment, query the user's profile and then query the profile's
license.


-----

For example, to find a user's profile ID:
```
  SELECT Id, ProfileId
  FROM User
  WHERE Id = '005D0000001GMAT'

```
To find a permission set's `UserLicenseId:`
```
  SELECT Id, LicenseId
  FROM PermissionSet
  WHERE Id = '0PS30000000000e'

```
If the IDs match, the assignment succeeds.

To find all the permission sets with no license that are assigned to any user:
```
  SELECT Id, Assignee.Name, PermissionSet.Name
  FROM PermissionSetAssignment
  WHERE PermissionSet.LicenseId = null

```
SEE ALSO:

PermissionSet
