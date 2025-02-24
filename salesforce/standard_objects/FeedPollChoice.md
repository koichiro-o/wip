#### FeedPollChoice

Shows the choices for a poll posted in the feed. This object is available in API version 29.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

To delete feed items they didn’t create, users must have one of these permissions:

**•** Modify All Data

**•** Modify All Records on the parent object, for example on Account for a poll on an AccountFeed

**•** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments they can see.

Only users with this permission can delete items in unlisted groups.

##### Fields

```
ChoiceBody
FeedItemId
Position

##### Usage

```

**Type**
textarea

**Properties**
Group

**Description**
A choice in the poll.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed item for the poll.

**Type**
int

**Properties**
Group, Sort

**Description**
Shows the position of the poll choice.


Use this object to query all of the choices associated with a particular poll. To view how people voted on the poll, see the FeedPollVote
object.


-----
