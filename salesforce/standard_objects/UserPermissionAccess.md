#### UserPermissionAccess

Represents the permissions accessibility for a current user. Available in API version 41.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
LastCacheUpdate
Permissions<PermissionName>

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date and time of either the user info or org info, whichever is later.

**Type**
boolean


-----

**Properties**
Filter

**Description**
The name of the permission, such as `PermissionsActivateContract or`
`PermissionsAuthorApex` and whether it’s available to the user (true) or not
(false).

##### Usage

API users without `PermissionsViewSetup` can use this object to check if their own sessions have access to a feature.

SEE ALSO:

Profile

PermissionSet
