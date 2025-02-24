#### ChatterAnswersActivity

Represents the reputation of a User in Chatter Answers zones.This object is available in API version 25.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field Name**
```
BestAnswerReceivedCount
BestAnswerSelectedCount
QuestionsCount
QuestionSubscrCount
QuestionSubscrReceivedCount
QuestionUpVotesCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of best answers the User has received from other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of best answers the User has selected.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records the User has selected to follow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of users following Question records posted by the User.

**Type**
int


-----

```
QuestionUpVotesReceivedCount
RepliesCount
ReplyDownVotesCount
ReplyDownVotesReceivedCount
ReplyUpVotesCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes the User has marked on Question records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Question
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Reply records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has marked on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ReplyUpVotesReceivedCount
ReportAbuseOnQuestionsCount
ReportAbuseOnRepliesCount
ReportAbuseReceivedOnQnCount
ReportAbuseReceivedOnReCount

```

**Description**

The number of up votes the User has marked on the Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Question records posted
by other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses reported by other users on the Question records posted
by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
UserId
CommunityId

##### Usage

```

**Description**

the number of abuses reported by other users on the Reply records posted by
the User.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The User ID associated with this reputation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID for the zone associated with this reputation.


Use this object to view metrics on User activity in Chatter Answers. For example, you can use the ChatterAnswersActivity object to view
the number of Question records a user is following in Chatter Answers zones.

SEE ALSO:

Question

Reply

User
