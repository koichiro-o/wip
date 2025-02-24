#### FeedComment

Represents a comment added to a feed by a user. This object is available in API version 18.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

```

-----

##### Special Access Rules

Note the following when working with feed comments.

**•** You must have read access to the feed’s parent type to see a FeedComment record.

**•** You must be able to access the feed to add a comment.

**•** If the comment is related to a user record, the user can delete the comment. For example, if John Smith makes a comment on Sasha
Jones’ profile feed, Sasha can delete the comment.

**•** If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create field property is available on`
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s
author and creation date. The fields can’t be updated after migration.

You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**•** Modify All Data

**•** Modify All Records on the object associated with the feed and delete permission on the parent feed

**•** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments they can see.

**•** Manage Unlisted Groups

Only users with this permission can delete items in unlisted groups.

##### Fields

```
CommentBody
CommentType

```

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The text in the comment.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of comment:

**•** `ContentComment—an uploaded file on a comment`

**•** `TextComment—a direct text entry on a comment`

Before API version 24.0, a text entry was required on a comment. As of version 24.0, a text
entry is optional if the `CommentType` is `ContentComment.`


-----

```
FeedItemId
HasEntityLinks
InsertedById
IsRichText

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the feed item containing the comment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed `CommentBody` includes at least one link to a record.

Note: This field is available starting in API version 43.0.

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

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the feed `CommentBody` contains rich text. If you post a rich text feed
comment using SOAP API, set `IsRichText` to `true` and escape HTML entities from
the body. Otherwise, the comment is rendered as plain text.

Rich text supports the following HTML tags:


-----

**•** `<p>`

**•** `<a>`

**•** `<b>`


Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

```
IsVerified
LastEditById
LastEditDate

```


**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The <img> tag is accessible only through the API and must reference files in Salesforce
similar to this example: `<img src="sfdc://069B0000000omjh"></img>`

Note: This attribute is available as of API version 38.0. In API version 38.0 and later,
the system replaces special characters in rich text with escaped HTML. In API version
37.0 and prior, all rich text appears as a plain-text representation.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a comment on a question is marked as Company Verified.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the user who last edited the feed comment.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort


-----

```
ParentId
RelatedRecordId
Revision
Status

```

**Description**
The date the feed comment was last edited.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of a record associated with the feed comment. For example, if you are commenting on a
change to a field on Account, `ParentId is set to the account ID.`

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a ContentComment. This field is null for
all comments except `ContentComment.`

For example, set this field to an existing ContentVersion ID and set the `CommentType` to
```
  ContentComment.

```
**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of times the comment was revised.

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed comment is published and visible to all who can access the parent
feed item. To change a comment’s status, the comment’s parent feed item must be in a
published state. This field is available in API version 38.0 and later.

Possible values are:

**•** `Published—The comment is visible to all who can access the parent feed item.`

**•** `PendingReview—The comment is visible to its author. Users see the parent feed`
item and have View All Data or Can Approve Feed Post and Comment permission also
see the comment. The author can delete the comment as can users who see the comment
and have Can Approve Feed Post and Comment or Modify All Data permission. If the


-----

```
SystemModstamp
ThreadChildrenCount
ThreadLastUpdatedDate

```

parent feed item is published, the author can edit the comment. Users who see the
comment and have Can Approve Feed Post and Comment or Modify All Data permission
can also edit the comment. Users with Can Approve Feed Post and Comment or Modify
All Data permission can change comment status from Published to PendingReview and
from PendingReview to Published.

Some actions are blocked when a feed comment is pending review:

**–** Select as Best—When a feed comment that is marked as best answer becomes
unpublished, it’s removed as the best answer. If the comment is published, its best
answer status is not restored.

**–** Like and unlike

**•** `Isolated—The comment is visible only to admins. After an item is isolated, the author`
no longer has view or edit access. The admin user can edit, view, and delete isolated
feed comments.

**Type**
datetime

**Properties**
Defaulted on create, Filter

**Description**
Date and time when a user or automated process (such as a trigger) last modified this record.
In this context, "trigger" refers to Salesforce code that runs to implement standard
functionality, and not an Apex trigger. `SystemModstamp` [is a read-only system field,](http://www.salesforce.com/developer/docs/api/Content/system_fields.htm)
available in FeedComment as of API version 37.0.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The count of comments associated with this parent feed object. The feed object can be
either a Feed Item or a Feed Comment. The count shows how many comments are directly
subordinate to the parent. This field is available on the object when Allow discussion
**threads is selected in the Administration Workspace. This field is available in API version**
44.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time the thread on this comment was last updated. This field is available on
the object when Allow discussion threads is selected in the Administration Workspace.
This field is available in API version 44.0 and later.


-----

```
ThreadLevel
ThreadParentId

##### Usage

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier that shows the level of this Feed Comment in a thread. By default, there are a
maximum of three levels in a thread. The `ThreadLevel` value shows in which of the
three levels this comment falls. This field is available on the object when Allow discussion
**threads is selected in the Administration Workspace. This field is available in API version**
44.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier of the feed item that is the parent of this comment. This field is available on
the object when Allow discussion threads is selected in the Administration Workspace.
This field is available in API version 44.0 and later.

This is a relationship field.

**Relationship Name**
ThreadParent

**Relationship Type**
Lookup

**Refers To**
FeedComment



**•** As of API version 23.0 and later, if you have View All Data permission, you can query FeedComment records directly without an ID
filter. If you don’t have View All Data permission, you can’t query FeedComment records directly, with or without an ID filter.

For example, the following query returns general information about a feed:
```
  SELECT ID, CreatedDate, CreatedById, CreatedBy.FirstName,
         CreatedBy.LastName, ParentId, Parent.Name, Body
  FROM FeedItem
  WHERE CreatedDate > LAST_MONTH
  ORDER BY CreatedDate DESC, Id DESC

```
**•** You can search for text in comments using SOSL. For example, the following Java class uses `search()` to find the string “foo” in
any field of a record:


-----

**•** If you use an Apex trigger to modify the `Body` of a FeedComment object, all mentions hyperlinks are converted to plain text. The
mentioned users don't get email notifications.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.

SEE ALSO:

Custom Object__Feed
