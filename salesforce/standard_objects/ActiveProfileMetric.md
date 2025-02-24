#### ActiveProfileMetric

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the permission set license.

This is a relationship field.

**Relationship Name**
PermissionSetLicense

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicense

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of this permission set licenses that are available to your org.


Represents the profile associated with the active, assigned, and purchased user licenses. This object is available in API version 52.0 and
later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ActiveUserCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this profile who have logged in within the last 30 days.


-----

```
AssignedUserCount
MetricsDate
ProfileId
UserLicenseId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this profile.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that profile metrics were collected.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the profile.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user license.

This is a relationship field.

**Relationship Name**
UserLicense

**Relationship Type**
Lookup

**Refers To**
UserLicense


-----
