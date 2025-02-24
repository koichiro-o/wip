#### UserTerritory

Represents a User who has been assigned to a Territory.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
**•** Only available if territory management has been enabled for your organization.

**•** As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with
the Manage Territories permission can edit this object.

##### Fields

```
IsActive
IsDeleted
TerritoryId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is active in the given territory (true), or inactive in the
given territory (false):

**•** Users who are active in a territory are explicitly assigned to the territory and can
have open opportunities, closed opportunities, or no opportunities associated
with that territory.

**•** Users who are inactive in a territory are not explicitly assigned to the territory, but
own an open or closed opportunity that is associated with the territory. For
example, a user may have been transferred out of a territory, but still own
opportunities in his or her old territory.

Until a user is deleted from a territory (not simply removed from the territory), the
record is not returned in a `getDeleted() call.`

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not
(false). Label is Deleted.

**Type**
reference

**Properties**
Create, Filter


-----

```
UserId

##### Usage

```

**Description**
ID of the Territory to which the user has been assigned. This field is required when
creating a record in API version 20.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the user. This field is required when creating a record.


If a user is inactive in a territory, and the opportunities they own that are associated with the territory are all closed, the user is not returned
in the Territories related list on the User page in Setup. Regardless of whether the user is inactive or the opportunities are closed, the
user is returned in the Quotas related list.

SEE ALSO:

Territory

AccountTerritoryAssignmentRule

AccountTerritoryAssignmentRuleItem
