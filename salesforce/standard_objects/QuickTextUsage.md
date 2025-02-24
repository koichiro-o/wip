#### QuickTextUsage

Represents the usage of quick text on a record, including which quick text was used, who used it, and how they used it. Quick text is a
snippet of text that allows users to send a quick response to a customer. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is always read-only.

##### Fields

```
AppContext

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Context in which the quick text was used. Possible values are:

**•** `Aloha—Salesforce Classic`

**•** `Lightning—Lightning Experience`

**•** `Unknown`


-----

```
Channel
FolderId
LaunchSource

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The channel in which the quick text was used. Possible values are:

**•** `Email`

**•** `Event`

**•** `Generic`

**•** `Internal`

**•** `Knowledge`

**•** `Live Agent`

**•** `Messaging`

**•** `Phone`

**•** `Portal`

**•** `Social`

**•** `Task`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the folder containing the quick text at the time it was used.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the user started the quick text. Possible values are:

**•** `Floater`

**•** `Keyboard shortcut`


-----

```
LoggedTime
Name
OwnerId
QuickTextID

```


**•** `Macro`

**•** `Toolbar`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the quick text was used.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the quick text.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the group or user that owns the quick text.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the quick text.

This is a relationship field.

**Relationship Name**
QuickText


-----

```
UserId

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
QuickText

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user that used the quick text.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**QuickTextUsageChangeEvent (API version 62.0)**
Change events are available for the object.

**QuickTextUsageOwnerSharingRule**

Sharing rules are available for the object.

**QuickTextUsageShare**

Sharing is available for the object.
