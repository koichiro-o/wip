#### Question

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds set for push timeout. 0 is returned when push timeout isn’t enabled.
Available in API version 36.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The routing type that determines how work items are routed (pushed) to agents. Possible
values are `Least Active` and `Most Available.`

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority in which work items from the service channels that are related to this routing
configuration are routed to agents. Work items from routing configurations that have lower
priority values (for example, `0) are routed to agents first.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service channel that’s associated with this configuration. This field is available
in API version 32.0 and earlier.


Represents a question in a zone that users can view and reply to.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is only available if the Answers permission and AnswersEnabled preference or PortalFeed permission and PortalFeedEnabled
preference are enabled in your org.

##### Fields

```
BestReplyId
BestReplySelectedById
Body
CommunityId
CreatorFullPhotoUrl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the reply that has been identified as the best answer to the question. Use
the user interface to identify the best answer for a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who selected the best answer to the question.

This field is available in API version 24.0 and later. In API version 24.0 through version
29.0, you must update this field using the UI. In API version 30.0 and later, you can
update this field using the API.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the question.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The zone ID associated with the question. After you create a question, you can’t
change the zone ID associated with that question.

**Type**
string


-----

```
CreatorName
CreatorSmallPhotoUrl
HasSingleFieldForContent
LastReferencedDate

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to
view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal
users (agents) appears to portal users in the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the content of a Chatter Answers question is:

**•** Included in only one field: `Title` if the content is unformatted and less than
255 characters; or Body if the content is formatted or more than 255 characters
(true)

**•** Included in two fields: `Title` and `Body` (false)

This field also determines if content displays in one or two fields in Chatter Answers
question feeds.

This field is available in API version 25.0 and later.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


-----

```
LastReplyDate
LastReplyId
LastViewedDate
MostReportAbusesOnReply
NumReplies

```

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the last reply (child Reply object) was posted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The ID of the last reply (child Reply object) posted to the question.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is null,
this record might only have been referenced (LastReferencedDate) and not
viewed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The most number of user-reported abuses on a Reply associated with the question.

This field is available in API version 24.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies (child Reply object) that users have submitted for the question.


-----

```
NumReportAbuses
NumSubscriptions
Origin
Title
UpVotes
VoteScore

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of user-reported abuses on the question.

This field is available in API version 24.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of users following the question.

This field is available in API version 24.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the question, such as `Chatter Answers.`

This field is available in API version 24.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The descriptive title of the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of up votes for the question.

**Type**
double


-----

**Properties**
Filter, Nillable, Sort

**Description**
The internal score of the question, used to sort questions and articles on the Popular
tab in the application user interface. The internal algorithm that determines the score
gives older votes less weight than newer votes, simulating exponential decay. The
score itself doesn’t display in the application user interface.

Note: Unlike other fields of type double, you can't use a SOQL aggregate
function with this field.

##### Usage

Use this object to track questions in a zone.
