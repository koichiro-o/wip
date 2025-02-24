#### PermissionSetTabSetting

Represents a permission set tab setting. Requires the View Setup permission. Use this object to query all tab settings of the permission
set. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only users with "View Setup and Configuration" permission can access this object.

##### Fields

```
Name

```

**Type**
string


-----

```
ParentId
Visibility

##### Usage

```

**Properties**
Create, Filter, Group, Sort

**Description**
The tab name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The permission set Id.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the tab is visible by default. Possible values are:

**•** `DefaultOff`

**•** `DefaultOn`


Use the PermissionSetTabSetting object to find tab setting visibility settings, parent permission sets, and so forth.

For example, to find the visibility setting of a tab named “standard-Lead,” do something like the following.


-----
