#### ContentUserSubscription

Represents a subscription for a user following another user. This object is available in API version 42.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Only users with Modify All Data permission have access to this object.

##### Fields

```
SubscribedToUserId
SubscriberUserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who is followed by another user.

This is a relationship field.

**Relationship Name**
SubscribedToUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who follows another user.

This is a relationship field.

**Relationship Name**
SubscriberUser

**Relationship Type**
Lookup


-----

**Refers To**
User
