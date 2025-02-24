#### feedSignal

Attach feed signals, like `UpDownVote,` `UserVerified, and` `Verified, to a feed post or comment. This object is available in`
API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects()

 Fields

```
```
FeedEntityId
FeedItemId
InsertedById

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Feed entity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the feed post or comment.

Possible values are:

**•** `FeedItem`

**•** `FeedComment`

**Type**
reference


-----

```
SignalType
SignalValue

```

**Properties**
Filter, Group, Sort

**Description**
ID of user who inserted the signal.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of signal.

Possible values are:

**•** `UpDownVote`

**•** `UserVerified`

**•** `Verified`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The value of the signal. For example, for `UpDownVote, the value specifies whether the`
signal is an upvote or a downvote.

