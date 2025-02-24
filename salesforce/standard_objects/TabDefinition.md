#### TabDefinition

Represents a custom tab. Returns only the tabs that the current user has access to. This object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query(), search()

 Fields

```
```
DurableId
IsAvailableInAloha
IsAvailableInDesktop

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Unique identifier for the tab. Always retrieve this value before using it, because
the value isn’t guaranteed to stay the same from one release to the next. Simplify
queries by using this field instead of making multiple queries.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Salesforce Classic.

**Type**
boolean


-----

```
IsAvailableInLightning
IsAvailableInMobile
IsCustom
Label
MobileUrl

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available on desktop.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Lightning Experience.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in the Salesforce mobile app.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is a custom tab created by admins in the org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The localized label corresponding to the `MasterLabel` field in the Tooling
API object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab in the Salesforce mobile app.


-----

```
Name
SobjectName
Url
