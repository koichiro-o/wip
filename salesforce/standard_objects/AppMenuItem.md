#### AppMenuItem

Represents the organization’s default settings for items in the app menu or App Launcher.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve(), update()

```

-----

##### Fields

**Field**
```
ApplicationId
CanvasAccessMethod
CanvasEnabled
CanvasOptions
CanvasReferenceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID for the menu item.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The access method for the canvas app. Values can be:

**•** `Get—OAuth Webflow`

**•** `Post—Signed Request`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the app menu item is a canvas app (true) or not (false). The default setting
is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the options enabled for a canvas connected app. The options are:

**•** `PersonalEnabled—The app is enabled as a canvas personal app.`

**•** `HideHeader—The publisher header, which contains the “What are you working on?”`
text, is hidden.

**•** `HideShare—The publisher Share button is hidden.`

This field is available in API version 34.0 and later.

**Type**
string


-----

```
CanvasSelectedLocations
CanvasUrl
Description
IconUrl
InfoUrl

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The canvas app unique identifier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The selected locations for the canvas app which define where the canvas app can appear in
the user interface. For example:
```
  Chatter,ChatterFeed,Publisher,ServiceDesk

```
**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the canvas app.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of this menu item.

**Type**
url

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


-----

```
IsAccessible
IsRegisteredDeviceOnly
IsUsingAdminAuthorization
IsVisible
Label
LogoUrl

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true, the current user is authorized to use the app. The default setting is` `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true, indicates that the app is available to registered devices only. The default setting is`
```
  false. Available in API version 49.0 and later.

```
**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the app is pre-authorized for certain users by the administrator. The default setting
is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**

If `true, the app is visible to users of the organization. The default setting is` `false.`

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


-----

```
MobileAppBinaryId
MobileAppInstallUrl
MobileAppInstalledDate
MobileAppInstalledVersion
MobileAppVer
MobileDeviceType

```

**Description**
The logo for the menu item’s application. The default is the initials of the `Label value.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for the Mobile App Binary file.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location mobile users are directed to install the app. Available in API version 49.0 and
later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a user installed a mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the user’s installed mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the mobile app. Available in API version 49.0 and later.

**Type**
string


-----

```
MobileMinOsVer
MobilePlatform
MobileStartUrl
Name
NamespacePrefix

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The supported device form factors for the mobile app. Available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The minimum version required for the app. Available in API version 49.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mobile platform for the app. Possible values include:

**•** `android – Android`

**•** `ios – iOS`

Available in API version 49.0 and later.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location mobile users are directed to after they’ve authenticated. This field is used with
connected apps and Experience Builder sites. For sites only, this location is a fully qualified
domain name. For other apps, it’s a relative URL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the item.

**Type**
string


-----

```
SortOrder
StartUrl
Type

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values:

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The index value that controls where this item appears in the menu. For example, a menu
item with a sort order of 5 appears between items with sort order values of 3 and 9.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
For a connected app, the location users are directed to after they’ve authenticated. Otherwise,
the application’s default start page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of application represented by this item. The types are:

**•** `ConnectedApplication`

**•** `Network`

**•** `ServiceProvider`


-----

```
UserSortOrder

##### Usage

```


**•** `TabSet`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The index value that represents where the user set this item in the menu (or App Launcher).
For example, an item with a sort order value of 5 appears between items with sort order
values of 3 and 9.

This value is separate from SortOrder so you can create logic incorporating both values. For
example, if you want the user-sorted items to appear first, followed by the organization order
for the rest, use:


Use this read-only object to view an entry in the Lightning Platform app menu or the App Launcher. You can create a SOQL query to
retrieve all items, even items the user does not see from the user interface.

There are many ways you can use AppMenuItem. Here are some examples:

**•** Build your own App Launcher or app menu in Salesforce. Create a custom page showing all the apps you have access to and that
lets you run them using single sign-on.

**•** Build your own App Launcher or app menu on a tablet or mobile app. You can have your own app for launching applications on
various mobile devices.

**•** Build an app launcher into your company’s intranet. There’s no need to have it run on Salesforce because Salesforce APIs let you
integrate with Salesforce programmatically and build an app launcher.

Tip: To get metadata information about apps and their tabs, use the Apex Schema.describeTabs() method, REST API
`/vXX.X/tabs/` resource, or SOAP API `describeTabs()` call.
