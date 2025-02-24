#### UserAppMenuCustomization

Represents an individual user’s settings for items in the app menu or App Launcher. This object is available in API version 35.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ApplicationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 15-character ID for the application associated with the menu item.


-----

```
OwnerId
SortOrder

##### Usage

```

This is a relationship field.

**Relationship Name**
Application

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user for these specific settings.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The index value that controls where this item appears in the menu. For example,
a menu item with a sort order value of 5 will appear between items with sort
order values of 3 and 9.


See the AppMenuItem object for the organization-wide default settings This object contains the fields representing any changes the
user made to the menu.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**UserAppMenuCustomizationOwnerSharingRule**

Sharing rules are available for the object.

**UserAppMenuCustomizationShare**

Sharing is available for the object.
