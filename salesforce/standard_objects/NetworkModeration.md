#### NetworkModeration

```
Represents a flag on an item in a community. This object is available in API version 30.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is available only when your org has digital experiences enabled.


-----

##### Fields

**Field Name**
```
EntityId
ModerationType
NetworkId
Visibility

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the post, comment, or file that was flagged.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Determines the type of flag applied to an item. Values are:

**•** FlagAsInappropriate

**•** FlagAsSpam

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the community in which the item was flagged.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Nillable, Sort

**Description**
Determines visibility of a flagged item. Values are:

**•** SelfAndModerators—The user who flagged the item and any moderators
can see the flagged item. This is the default value.

**•** ModeratorsOnly—Only moderators can see the flagged item. If
ModeratorsOnly is selected, only moderators can set flags using the API.


Use this object to view the items flagged for moderation within a community. Additionally, users with “Moderate Feeds” and “Modify
All Data” can remove flags.


-----

Flags on items are created either when a member manually flags an item in a community (if flagging is enabled for that community),
or when a trigger automatically flags an item because the item met the trigger criteria.
