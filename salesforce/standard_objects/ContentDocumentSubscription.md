#### ContentDocumentSubscription

Represents a subscription for a user following or commenting on a file in a library. This object is available in API version 42.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Only users with Modify All Data permission have access to this object.

##### Fields

```
ContentDocumentId
IsCommentSub
IsDocumentSub

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the user made comments on the file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the user follows the file.


-----

```
UserId
