#### Reply

Represents a reply that a user has submitted to a question in an answers zone.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Body

```

**Type**
textarea


-----

```
CommunityId
CreatorFullPhotoUrl
CreatorName
CreatorSmallPhotoUrl
DownVotes

```

**Properties**
Create, Update

**Description**
Body of this reply.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The zone ID associated with the question and its reply. This field is available in API
version 27.0 and later.

**Type**
string

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
to view this field. This field is available in API version 26.0 and later

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled
to view this field. This field is available in API version 26.0 and later.

**Type**
int


-----

```
Name
NumReportAbuses
QuestionId
UpVotes
VoteTotal

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of down votes for a reply.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
When creating a Reply, the `Name` field is automatically populated with a truncated,
plain text version of the Reply `Body` field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the number of reported abuses on the reply by users.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Question to which this reply was made.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of up votes for a reply.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of all votes for a reply, including up and down votes.


-----

##### Usage

Use this object to track replies to a Question.
