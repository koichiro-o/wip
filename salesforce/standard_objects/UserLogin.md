#### UserLogin

Represents the settings that affect a user’s ability to log into an organization. To access this object, you need the
`UserPermissions.ManageUsers` permission. This object is available in API version 29.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update()

 Fields

```
```
IsFrozen
IsPasswordLocked
UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
[If true, the user account associated with this object is frozen. If a user's account](https://help.salesforce.com/s/articleView?id=platform.users_freeze.htm&language=en_US)
is frozen, they can't log in, but their account isn't deactivated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, the user account associated with this object is locked because of too`
many login failures. From the API, you can set this field to false, but not true.

Note: If the Lockout effective period is set to Forever (must be reset by
admin) in your org’s Password Policies Setup page, this field isn’t set to
```
    false.

```
**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated user account. This field can’t be updated.


-----

##### Usage

To query for all frozen users in your organization:
```
SELECT Id, UserId
FROM UserLogin
WHERE IsFrozen = true

```
[To freeze or unfreeze multiple users, use Data Loader.](https://help.salesforce.com/s/articleView?id=000387522&type=1&language=en_US)
