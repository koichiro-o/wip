#### IdeaReputation

Represents a collection of statistics and scores derived from a user’s activity within an Ideas zone or internal organization. This object is
available in API version 28.0 and later.

##### Supported Calls
```
query(), retrieve(),

 Fields

```
```
CommentCount
CommentsReceivedCount
ContextId
DownVotesGivenCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments a user has created in a zone or the internal organization. This
number excludes comments the user creates on his or her own idea.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments a user has received in a zone or the internal organization.

**Type**
reference

**Properties**
Filter, Group, Namepointing, Nillable, Sort

**Description**
The ID of the zone or internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of down votes a user has given in a zone or the internal organization.


-----

```
DownVotesReceivedCount
IdeaCount
ReputationLevel
Score
UpVotesGivenCount
UpVotesReceivedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of down votes a user has received in a zone or the internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of ideas a user has created in a zone or the internal organization.

**Type**
string

**Properties**
Nillable

**Description**
The reputation level that a user has achieved based on their score in a zone or within an
organization.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total score of a user’s activity within a zone or within an organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes a user has given in a zone or the internal organization. This number
doesn’t include the default vote the system applies when the user creates the idea.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
UserId

##### Usage

```

**Description**
The number of up votes a user has received in a zone or the internal organization.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID associated with the reputation.


Use to query a user’s reputation within a zone.
