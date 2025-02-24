#### ActivePermSetLicenseMetric

Represents the number of active, assigned, and purchased permission set licenses in the org. This object is available in API version 52.0
and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field**
```
ActiveUserCount
AssignedUserCount
DeveloperName
MasterLabel
MetricsDate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this permission set license who have logged in within the last 30
days.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this permission set license.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of this permission set license object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the permission set license.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that permission set license metrics were collected.


-----

```
PermissionSetLicenseId
TotalLicenses
