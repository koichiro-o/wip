#### ContentNotification

Represents a notification for a file. This object is available in API version 42.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Only users with Modify All Data permission have access to this object.

##### Fields

```
EntityIdentifierId
EntityType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object with the notification.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of object with the notification. One of the following.

**•** `ContentDocument`

**•** `ContentTagName`

**•** `ContentVersion`

**•** `ContentWorkspace`

**•** `ContentWorkspacePermission`

**•** `User`


-----

```
Nature
Subject
Text
UsersId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of notification.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Subject of the notification.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Text of the notification.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who received the notification.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

