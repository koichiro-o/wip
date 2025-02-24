#### NetworkUserHistoryRecent

Represents an Experience Cloud site user’s history of accessed records. This object is available in API version 42.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(),query(), undelete()

 Special Access Rules

```
Only users with the Modify All Data permission can view and delete these data.

##### Fields

```
AccessTimestamp

```

**Type**
datetime

**Properties**
Create, Filter, Sort

**Description**
The time at which the record was accessed.


-----

```
ActionType
DomainName
FeedCommentId
FeedItemId
NetworkId
NetworkUserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the action type taken by the user. The possible values are:

**•** Read

**•** Write

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain used to access the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Feed comment accessed by the user.

**Type**
reference

**Properties**
Create, Filter, Group,Sort, Update

**Description**
Feed item accessed by the user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Experience Cloud site used to access the record or comment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
RecordId
RecordKeyPrefix
Url
UserType

```

**Description**
User’s Experience Cloud site user ID to access the record or comment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that was accessed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Record’s ID key prefix.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The URL from which the user accessed the record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of user who accessed this record. The possible values include:

**•** Standard

**•** Partner

**•** Customer Portal Manager

**•** Customer Portal User

**•** Guest

**•** High Volume Portal

**•** CSN Only

**•** Self Service


-----

##### Usage

Use the NetworkUserHistoryRecent object to delete comments, posts, or record access by Experience Cloud site users who would like
all such activity to be removed.
