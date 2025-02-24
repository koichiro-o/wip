#### FeedPollVote

Shows how users voted on a poll posted in the feed. This object is available in API version 29.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ChoiceId
FeedItemId

##### Usage

```

**Type**
reference

**Properties**
Filter, Group

**Description**
Indicates which choice a user selected on a poll posted in a feed.

This is a relationship field.

**Relationship Name**
Choice

**Relationship Type**
Lookup

**Refers To**
FeedPollChoice

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed item for the poll.


Use this object to query how users voted on a particular poll.
