#### FeedLike

Indicates that a user has liked a feed item. This object is available in API version 21.0 and later.

FeedLike records represent likes on posts and not likes on comments. Likes on comments can’t be queried via the API. A FeedLike is a
child object of an associated FeedItem, FeedTrackedChange, or object feed, such as AccountFeed.

##### Supported Calls
```
create(), delete(), describeSObjects()

 Special Access Rules

```
If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

##### Fields

```
FeedItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the feed item that the user liked.


-----

```
FeedEntityId
InsertedById

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of a feed item or feed comment the user liked.

If the user liked a comment, `FeedEntityId` is set to the ID of the comment. If the user
liked a feed item, `FeedEntityId` is set to the ID of the feed item.

This field is optional. The default value is the ID of the feed item.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User


You can't query FeedLike records directly. They can only be queried via the entity feed, such as AccountFeed.

FeedLike records represent likes on posts and not likes on comments. Likes on comments can’t be queried via the API.
