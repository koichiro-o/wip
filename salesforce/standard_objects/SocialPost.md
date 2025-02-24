#### SocialPost

Represents a snapshot of a post on a social network such as a Facebook or Twitter. This object is available in API version 23.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AnalyzerScore
AssignedTo
AttachmentType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Score set on the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
User in Social Studio that the social post is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the first attachment on the social post. Values are:

**•** `APPLICATION`

**•** `AUDIO`

**•** `IMAGE`

**•** `LINK`


-----

```
AttachmentUrl
Classification
CommentCount
Content
DeletedById

```


**•** `TEXT`

**•** `UNKNOWN`

**•** `VIDEO`

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the first attachment on the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Classification for the social post, such as inquiry or customer case.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of comments on the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the social post is deleted, ID of the person who deleted the social post.

This is a relationship field.

**Relationship Name**
DeletedBy


-----

```
EngagementLevel
ExternalPostId
Handle
HarvestDate
Headline
HiddenById

```

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Engagement level of the social post, such as reviewed or resolved.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social post in its social network.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Handle of the person who posted the social post.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when Social Studio collected the social post.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Headline of the social post.

**Type**
reference


-----

```
InboundLinkCount
IsOutbound
KeywordGroupName
Language

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the social post is hidden, ID of the person who hid it.

This is a relationship field.

**Relationship Name**
HiddenBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of links on the inbound social post.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social post is outbound or not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field that is no longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Language of the social post.


-----

```
LastReferencedDate
LastViewedDate
LikedBy
LikesAndVotes
MediaProvider
MediaType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the managed social account in the social network that liked the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 number of likes and votes on the social post.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social post.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of social network of the social post.


-----

```
MessageType
Name
Notes
OutboundSocialAccountId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of message. Values are:

**•** `Comment—Facebook comment`

**•** `Direct—Twitter direct message`

**•** `Post—Facebook post`

**•** `Private—Facebook private message`

**•** `Reply—Twitter or Facebook reply`

**•** `Retweet—Twitter retweet`

**•** `Tweet—Twitter tweet`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes added by Social Hub actions for the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the social account used for outbound social posts.

This is a relationship field.

**Relationship Name**
OutboundSocialAccount

**Relationship Type**
Lookup


-----

```
OwnerId
ParentId
PersonaId

```

**Refers To**
ExternalSocialAccount

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the social post.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent record of the social post, for example, the ID of a case.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona who made the post.

This is a relationship field.

**Relationship Name**
Persona


-----

```
PostPriority
PostTags
PostUrl
Posted
Provider
R6PostId

```

**Relationship Type**
Lookup

**Refers To**
SocialPersona

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of the social post set in Social Studio.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of tags on the social post.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the social post.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Sort, Update

**Description**
Date and time when the social post was made.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Social network of the social post.

**Type**
string


-----

```
R6SourceId
R6TopicId
Recipient
RecipientType
ReplyToId

```

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique ID of the post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the author in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for either the topic profile or the managed account in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recipient of the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the recipient of the social post, such as a person.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Dynamically generated from replyToExternalPostId in Social Studio.

This is a relationship field.


-----

```
ResponseContextExternalId
ReviewScale
ReviewScore
ReviewedStatus
Sentiment

```

**Relationship Name**
ReplyTo

**Relationship Type**
Lookup

**Refers To**
SocialPost

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External ID, such as a conversation ID, author ID, or post ID, for the item you’re
responding to.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review scale for the social post.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review score for the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the social post review.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
Shares
SourceTags
SpamRating
Status

```

**Description**
Sentiment of the social post. Values are:

**•** `Negative`

**•** `Neutral`

**•** `Positive`

**•** `SomewhatNegative`

**•** `SomewhatPositive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post has been shared.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of author type tags.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Spam rating of the social post. Values are:

**•** `NotSpam`

**•** `Spam`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the social post. Values are:

**•** `DELETED`

**•** `FAILED`

**•** `HIDDEN`


-----

```
StatusMessage
ThreadSize
TopicProfileName
TopicType
TruncatedContent

```


**•** `PENDING`

**•** `PENDING_APPROVAL`

**•** `RECALL_APPROVAL`

**•** `REJECTED_APPROVAL`

**•** `REPLIED`

**•** `SENT`

**•** `UNKNOWN`

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status message for the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the topic profile for the social post in Social Studio.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of topic. Values are:

**•** `Keyword`

**•** `Managed`

**Type**
string


-----

```
UniqueCommentors
ViewCount
WhoId

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Truncated content of the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of unique people who commented on the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post was viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Polymorphic ID of a person such as a lead or a contact.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead


The fields on a SocialPost object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected the post from the social network. Many of the Radian6-related fields are no longer accurate or used.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SocialPostChangeEvent (API version 48.0)**
Change events are available for the object.

**SocialPostFeed (API version 26.0)**
Feed tracking is available for the object.

**SocialPostHistory (API version 26.0)**
History is available for tracked fields of the object.

**SocialPostOwnerSharingRule**

Sharing rules are available for the object.

**SocialPostShare**

Sharing is available for the object.
