#### SessionPermSetActivation

The SessionPermSetActivation object represents a permission set assignment activated during an individual user session. When a
SessionPermSetActivation object is inserted into a permission set, an activation event fires, allowing the permission settings to apply to
the user’s specific session. This object is available in API versions 37.0 and later.


-----

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

```
Note: If you include session-based permission sets in a permission set group, the permissions in them do not require session-based
activation for users assigned to the group.

##### Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

##### Fields

```
AuthSessionId
Description
PermissionSetGroupId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The session ID related to this permission set assignment for its duration.

This is a relationship field.

**Relationship Name**
AuthSession

**Relationship Type**
Lookup

**Refers To**
AuthSession

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session details, such as device used and browser.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
PermissionSetId
UserId

```

**Description**
The permission set group ID related to this permission set group assignment and
user for its duration. This field is available in API version 53.0 and later.

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
Filter, Group, Sort

**Description**
The permission set ID related to this permission set assignment and user for its
duration.

This is a relationship field.

**Relationship Name**
PermissionSet

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID of the user to whom this permission set assignment applies for its
duration.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


-----

##### Usage

Use SessionPermSetActivation to create a permission set available only for a specified session’s duration. For example, create permission
sets that provide access to specific applications only during authenticated sessions.

In the following Apex example, an identified session is activated after session information is submitted via a button. Successful activation
results in a confirmation message displayed to the user.


-----
