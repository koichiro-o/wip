#### UserCustomBadge

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the Chat configuration; agents associated with this configuration can
transfer chats to the chat button indicated by the `LiveChatButtonId.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the skill group that agents can transfer chats to.


Represents a custom badge for a user. This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
BadgeType
CustomText
ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of badge. Valid values are:

**•** `Customer`

**•** `Partner`

**•** `Employee`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Custom text for the badge.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site or org that the badge is in.

