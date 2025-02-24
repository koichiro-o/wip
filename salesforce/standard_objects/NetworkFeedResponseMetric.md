#### NetworkFeedResponseMetric

Represents an object that stores the date and time values of question posts. It captures information for question creation, answer creation,
and when an answer is marked as best answer This object is available in API version 51.0 and later.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
The NetworkFeedResponseMetric object is available only if both NetworksEnabled and ChatterEnabled org preferences are enabled.

##### Fields

```
BestCommentDateTime
BestCommentId
FeedItemCreatedById
FeedItemDateTime
FeedItemId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time a user created an answer that was later marked as best answer.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the comment that was marked as the best answer.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the user who created the feed item.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Represents the date and time when the feed Item was created.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
FirstCommentDateTime
FirstCommentId
MarkedAsBestCommentDateTime
NetworkId
ParentRecordId

```

**Description**
Represents the unique ID of the question post.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time when the first comment was created.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represent the first comment on a feed Item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time the user marked the answer as best answer.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents where the feed item was created.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the parent record. Parent records can include records like user, account, or group.


-----
