#### CustomNotificationType

Stores information about custom notification types. This object is available in API version 47.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
CustomNotifTypeName
Description
Desktop
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Unique, Update

**Description**
Specifies a notification type name. The notification type name is unique within your
organization. The notification type name isn’t namespaced, so it can’t be duplicated across
installed packages. Maximum number of characters: 80.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies a general description of the notification type, which is displayed with the notification
type name. Maximum number of characters: 255.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the desktop delivery channel is enabled (true) or not (false). The
default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
IsSlack
Language
MasterLabel
Mobile
NamespacePrefix

```

**Description**
Specifies the API name of the notification type.

**Type**
boolean

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the language of the custom notification type. The value for this field is the language
value of the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the notification type label.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the mobile delivery channel is enabled (true) or not (false). The
default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the notification type, if installed with a managed package.


-----
