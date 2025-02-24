#### ChatterActivity

ChatterActivity represents the number of posts and comments made by a user and the number of comments and likes on posts and
comments received by the same user. This object is available in API version 23.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
CommentCount

```

**Type**
int

**Properties**
Filter, Group, Sort


-----

```
CommentReceivedCount
InfluenceRawRank
LikeReceivedCount
NetworkId
ParentId

```

**Description**
The number of FeedComments made by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments received by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number indicating the ParentId’s Chatter influence rank, which is calculated based
on the ParentId’s ChatterActivity statistics, relative to the other users in the
organization. This field is available in API version 26.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedLikes received by the ParentId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site to which the ChatterActivity belongs. This field is
available only if digital experiences is enabled in your org. This field is available in API
version 26.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object type to which the ChatterActivity is related. In API version 63.0, the
`ParentId` must be a `UserId` or SelfServiceUser ID.


-----

```
PostCount

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedItems made by the ParentId.



**•** Use this object to reference the Chatter activity statistics, which include the number of posts and comments made by a user and
the number of comments and likes on posts and comments received by the same user.

**•** You can directly query for ChatterActivity.
```
  SELECT Id, PostCount, LikeReceivedCount
  FROM ChatterActivity
  WHERE ParentId = UserId

```
Note: To query ChatterActivity, you must provide the ParentId. In API version 63.0, the ParentId must be a UserId
or SelfServiceUser ID.

**•** A ChatterActivity record is created for users the first time they post or comment. Users who have never posted or commented don’t
have ChatterActivity records. If users make only one post and then delete it, they do have ChatterActivity records. In both cases, the
user interface displays zeros for their Chatter activity.

**•** Use the InfluenceRawRank field to reference a user’s Chatter influence rank. This field is available in API version 26.0 and later.

SEE ALSO:

FeedItem

FeedComment

FeedLike
