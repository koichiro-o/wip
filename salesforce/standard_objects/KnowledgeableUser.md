#### KnowledgeableUser

Represents a user identified as knowledgeable about a specific topic, and ranks them relative to other knowledgeable users. This object
is available in API version 31.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
NetworkId
RawRank
TopicId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site the topic exists in. This field is available only if
digigal experiences is enabled for your org.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank of this user’s knowledge on the topic relative to other users.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique ID for the topic in Salesforce.


-----

```
UserId
