#### NavigationMenuItem

```


**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th The Salesforce user interface is fully translated to Thai, but Help is`
in English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

Create and Update are available in API version 45.0 and later.

**Description**

Label for the navigation menu.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

Create is available in API version 45.0 and later. Update is available in API versions
45.0 to 47.0.

**Description**
ID of the Experience Cloud site.


Represents a single menu item in a NavigationLinkSet. Use this object to create, delete, or update menu items in your Experience Cloud
site’s navigation menu. This object is available in API version 35.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.


-----

##### Fields

**Field Name**
```
AccessRestriction
DefaultListViewId
DraftRowID
Label
NavigationLinkSetId
ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines if the menu item is available to guest users who aren’t required to
log in to the Experience Cloud site.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the value of the Type field is SalesforceObject, the value is the ID of the default
list view for the object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the draft navigation menu item. The ID is unique within your
organization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text that appears in the navigation menu for this item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The navigation menu that this item is included in.

**Type**
reference


-----

```
Position
Status
Target
TargetPrefs

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The parent navigation menu.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location of the menu item in the navigation menu.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Represents if the navigation menu item is published or not. The values can only
be DRAFT, LIVE, or null. In API versions 42 and earlier, if the Status field is not set,
the field defaults to LIVE. When queried and Status is not part of the query filter,
only the NavigationMenuItem objects with a status of LIVE return. In API versions
43 and later, if the Status field is not set, the field defaults to DRAFT. When queried
and Status is not part of the query filter, all NavigationMenuItem objects return
regardless of status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
If `Type` is ExternalLink or InternalLink, the target is the URL that the link points
to. For ExternalLink, your entry looks like this: https://salesforce.com.
For InternalLink, use a relative URL, such as /contactsupport.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
If Type is ExternalLink, determines whether a navigation menu item opens in
the same tab.


-----

```
Type

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of navigation menu item. The available values are:

**•** SalesforceObject—Available objects include accounts, cases, contacts, and
custom objects.

**•** ExternalLink—Links to a URL outside of your Experience Cloud site. For
example, https://salesforce.com.

**•** Event—An event, such as logging in, logging out, or switching accounts.
Event is internal only and can’t be used in custom components.

**•** GlobalAction—Enables users to create object records, but the new record
has no relationship with other records.

**•** InternalLink—Links to a relative URL inside your Experience Cloud site. For
example, /contactsupport.

**•** NavigationalTopic—A dropdown list with links to the navigational topics in
your Experience Cloud site.

**•** SystemLink—A system link, such as a link to Experience Builder, Workspaces,
or Salesforce setup.


You can add up to 20 navigation menu items. You can translate navigation menu items using the Translation Workbench.
