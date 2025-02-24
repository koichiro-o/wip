#### CollaborationRoom

```
Represents a collaboration room, which links Salesforce to a Slack channel used by applications with specific use cases, such as swarming
or reporting. This object is available in API version 55.0 and later.


-----

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), update(), upsert()

 Special Access Rules

```
To access this object, enable the Slack Terms of Service and one of:

**•** Sales Cloud for Slack App

**•** Service Cloud for Slack App

**•** CRM Analytics for Slack App

**•** Industries Cloud for Slack App

**•** Health Cloud for Slack App

##### Fields

```
IsArchived
IsAutoJoin
IsExternal

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the collaboration room is archived (true) or not (false).

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether new users automatically join the collaboration room. Used for Sales Cloud
for Slack App.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether external users are members of the Slack channel (true) or not (false).

The default value is `false.`


-----

```
LastReferencedDate
LastViewedDate
Name
PlatformKey
TeamKey

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of collaboration room.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack channel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack workspace.


-----
