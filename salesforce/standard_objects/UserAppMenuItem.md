#### UserAppMenuItem

Represents the organization-wide settings for items in the app menu or App Launcher that the requesting user has access to in Setup.
This object is available in API version 35.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), search()

 Fields

```
```
AppMenuItemId
ApplicationId
Description
IconUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the menu item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the application associated with the menu item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A description of this menu item.

**Type**
url


-----

```
InfoUrl
IsUsingAdminAuthorization
IsVisible
Label
LogoUrl

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon for the menu item’s application.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL for more information about the application.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true, the app is pre-authorized for certain users by the administrator.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true, the app is visible to the user.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The app’s name.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The logo for the menu item’s application. The default is the initials of the Label
value.


-----

```
MobileStartUrl
Name
SortOrder
StartUrl
Type

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The location mobile users are directed to after they’ve authenticated. This is only
used with connected apps.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The API name of the item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that controls where this item appears in the menu. For example,
a menu item with a sort order value of 5 will appear between items with sort
order values of 3 and 9.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

The location users are directed to after they’ve authenticated. For a connected
app, this is the location specified by the StartUrl. Otherwise it’s the
application’s default start page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of application represented by this item. The types are:

**•** ConnectedApplication


-----

```
UserSortOrder

##### Usage

```


**•** Network

**•** ServiceProvider

**•** TabSet

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that represents where the user set this item in the menu (or App
Launcher). For example, an item with a sort order value of 5 will appear between
items with sort order values of 3 and 9.

This value is separate from SortOrder so you can create logic incorporating both
values. For example, if you want the user-sorted items to appear first, followed
by the organization order for the rest, use:


See the AppMenuItem object for the organization-wide default settings This object contains the fields the requesting user has permission
to see.
