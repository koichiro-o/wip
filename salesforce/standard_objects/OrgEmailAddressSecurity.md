#### OrgEmailAddressSecurity

Defines the assignment of a user profile to an org-wide email address. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Only authenticated users with the View Setup and Configuration permission can access this object.

##### Fields

```
OrgWideEmailAddressId
ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of an organization-wide email address.

This field is a relationship field.

**Relationship Name**
OrgWideEmailAddress

**Relationship Type**
Lookup

**Refers To**
OrgWideEmailAddress

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The profile ID that’s allowed to use an organization-wide email address.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


-----

**Refers To**
Profile

##### Usage

You can use this object with OrgWideEmailAddress and Profile objects to retrieve user profiles that have access to a specific org-wide
email address. To find specific users, use the `ProfileId` field on the User object.

You can also retrieve the org-wide email addresses that a specific user can access. Note that any users assigned to those org-wide email
addresses via permission set aren’t returned.
