#### Knowledge__Feed

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A type of group, indicating whether a queue is synchronous or asynchronous.

Possible values are:

**•** `A—Async`

**•** `S—Sync`

The default value is 'S'.


Represents the feed for a knowledge article. This object is available in API version 39.0 and later.

For additional information about feeds, see FeedItem on page 2408.

Note: By default, the prefix for this object name is `Knowledge` and that is the value shown in this reference. However, this
prefix can be modified by changing the Object Name for the Knowledge__kav object in Object Manager.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Lightning Knowledge must be enabled in your org.

##### Fields

```
BestCommentId
Body

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

**Type**
textarea


-----

```
CommentCount
InsertedById
IsRichText

```

**Properties**
Nillable, Sort

**Description**
The body of the feed item. Required when Type is TextPost or AdvancedTextPost.
Optional when `Type` is `ContentPost` or `LinkPost.`

Although a value for `Body` is not required for the `ContentPost` type, an attachment
is required. If an attachment isn’t present, the type changes to `TextPost` or
`AdvancedTextPost, depending on the API version.` `TextPost` and
`AdvancedTextPost` do require a value for `Body.`

Tip: See the IsRichText field for a list of HTML tags supported in the body of
rich text posts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.

Tip: In a feed that supports pre-moderation, `CommentCount` isn’t updated until a
comment is published. For example, say that you comment on a post that already has
one published comment and your comment triggers moderation. Now there are two
comments on the post, but the count says there's only one. In a moderated feed,
comments aren’t counted until approved by an admin or someone with Can Approve
Feed Post and Comment or Modify All Data.

Feed moderation has implications on how you retrieve feed comments. In a moderated
feed, rather than retrieving comments by looping through CommentCount, go through
pagination until the end of comments is returned.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
LikeCount
LinkUrl

```

**Description**
Indicates whether the feed item Body contains rich text. If you post a rich text feed comment
using SOAP API, set `IsRichText` to `true and escape HTML entities from the body.`
Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

**•** `<a>`

**•** `<b>`

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

Note: In API version 35.0 and later, the system replaces special characters in rich text
with escaped HTML. In API version 34.0 and prior, all rich text appears as a plain-text
representation.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Nillable, Sort

**Description**
The URL of a `LinkPost.`


-----

```
ParentId
RelatedRecordId
Title
Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Knowledge article to which the feed item is related.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost. For WDC thanks posts,`
it’s the ID of the WorkThanks object associated with a `RypplePost. This field is typically`
null for all posts except `ContentPost` and `RypplePost.`

For example, set this field to an existing ContentVersion ID and post it to a feed with `Type`
set to `ContentPost.`

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The title of the feed item. When the `Type` is `LinkPost, the` `LinkUrl` is the URL and
this field is the link name. The `Title` field can be updated on posts of `Type`
```
  QuestionPost.

```
**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost,` `LinkPost, and` `TextPost, don’t`
create feed items of other types directly from the API.

**•** `ActivityEvent—indirectly generated event when a user or the API adds a Task`
associated with a feed-enabled parent record (excluding email tasks on cases). Also
occurs when a user or the API adds or updates a Task or Event associated with a case
record (excluding email and call logging).

For a recurring Task with CaseFeed disabled, one event is generated for the series only.
For a recurring Task with CaseFeed enabled, events are generated for the series and each
occurrence.


-----

**•** `AdvancedTextPost—created when a user posts a group announcement and, in`
Lightning Experience as of API version 39.0 and later, when a user shares a post.

**•** `AnnouncementPost—Not used.`

**•** `ApprovalPost—generated when a user submits an approval.`

**•** `BasicTemplateFeedItem—Not used.`

**•** `CanvasPost—a post made by a canvas app posted on a feed.`

**•** `CollaborationGroupCreated—generated when a user creates a public group.`

**•** `CollaborationGroupUnarchived—Not used.`

**•** `ContentPost—a post with an attached file.`

**•** `CreatedRecordEvent—generated when a user creates a record from the publisher.`

**•** `DashboardComponentAlert—generated when a dashboard metric or gauge`
exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot—created when a user posts a dashboard`
snapshot on a feed.

**•** `LinkPost—a post with an attached URL.`

**•** `PollPost—a poll posted on a feed.`

**•** `ProfileSkillPost—generated when a skill is added to a user’s Chatter profile.`

**•** `QuestionPost—generated when a user posts a question.`

**•** `ReplyPost—generated when Chatter Answers posts a reply.`

**•** `RypplePost—generated when a user creates a Thanks badge in WDC.`

**•** `TextPost—a direct text entry on a feed.`

**•** `TrackedChange—a change or group of changes to a tracked field.`

**•** `UserStatus—automatically generated when a user adds a post. Deprecated.`

The following values appear in the `Type` picklist for all feed objects but apply only to
CaseFeed:

**•** `AttachArticleEvent—generated event when a user attaches an article to a case.`

**•** `CallLogPost—generated event when a user logs a call for a case through the user`
interface. CTI calls also generate this event.

**•** `CaseCommentPost—generated event when a user adds a case comment for a case`
object.

**•** `ChangeStatusPost—generated event when a user changes the status of a case.`

**•** `ChatTranscriptPost—generated event when Chat transcript is saved to a case.`

**•** `EmailMessageEvent—generated event when an email related to a case object is`
sent or received.

**•** `FacebookPost—generated when a Facebook post is created from a case. Deprecated.`

**•** `MilestoneEvent—generated when a case milestone is completed or reaches`
violation status.

**•** `SocialPost—generated when a social post is created from a case.`


-----

Note: If you set `Type` to `ContentPost, also specify` `ContentData` and
```
                   ContentFileName.
