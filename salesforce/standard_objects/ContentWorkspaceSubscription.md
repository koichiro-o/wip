#### ContentWorkspaceSubscription

Represents a subscription for a user following a library. This object is available in API version 42.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Only users with Modify All Data permission have access to this object.

##### Fields

```
ContentWorkspaceId
UserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

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
Filter, Group, Sort

**Description**
ID of the user following the library.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


-----

**Refers To**
User
