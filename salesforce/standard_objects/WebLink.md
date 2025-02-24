#### WebLink

Represents a custom link to a URL or Scontrol.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
**•** To create a custom link, the client application must be logged in with the “Customize Application” permission.

**•** Customer Portal users can’t access this object.

##### Fields

```
Availability
Description
DisplayType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the custom link. Limit is 1,000 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


-----

```
EncodingKey
HasMenubar
HasScrollbars
HasToolbar
Height
IsProtected

```

**Description**
Type of display: button, link, or mass-action button.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Encoding of parameters on the URL link.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows a menu bar (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows scroll bars (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows browser toolbars (true) or not
(false). Toolbars normally contain navigation buttons like Back, Forward, and
Print.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Height of the popup in pixels.

**Type**
boolean


-----

```
IsResizable
LinkType
MasterLabel
Name

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is protected (true) or not (false). Protected
components that have been installed in other organizations can’t be linked to
or referenced by components created in the subscriber organization. A developer
can easily delete a protected component contained in a managed package in a
future release of the package without worrying about failing installations.
However, once a component is marked as unprotected and is released globally,
the developer can’t delete it.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users are allowed to resize the popup window (true) or not
(false).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Type of link (S-control or URL).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Master label for the link. Limit is 240 characters. This display value is the internal
label that is not translated.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name to display on page.


-----

```
NamespacePrefix
OpenType
PageOrSobjectType
Position

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

This field can’t be accessed unless the logged-in user has the Customize
Application permission.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. How the custom link opens when clicked in a browser—NewWindow,
Sidebar, or NoSidebar.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. For standard objects, the name of the page on which to display the
custom link. For custom objects, the name of the object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
RequireRowSelection
ScontrolId
ShowsLocation
ShowsStatus
Url

```

**Description**
Location on the screen where the popup should open—TopLeft, FullScreen, or
None.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the custom link requires a row selection (true) or not
(false).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the custom s-control object (Scontrol) to link to. Can include fields as tokens
within the custom s-control object. Label is Custom S-Control ID.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the popup window shows the browser’s address bar containing
the URL (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Show the status bar at the bottom of the browser.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Required. URL of the page to link to. Can include fields as tokens within the URL.
Limit: 1,024 KB.


-----

```
Width

##### Usage

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Width of the popup in pixels.


Use this object to programmatically manage custom links, which allow client applications to integrate data with external URLs, an
organization’s intranet, or other back-end office systems. A custom link can point to:

**•** An external URL, such as `www.google.com` or your company's intranet.

**•** A custom s-control, such as a Java applet or Active-X control.

Custom links can include fields as tokens within the URL or custom s-control.

SEE ALSO:

Scontrol
