#### HashtagDefinition

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date and time when one or more of the fields were modified

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date and time when one or more of the fields were viewed

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the guest buyer profile. Including a reference to the store helps with later
identification.


HashtagDefinition represents hashtag (#) topics in public Chatter posts and comments. Public posts and comments include those on
profiles and in public groups, but not those on records or in private groups. This object is available in API version 26.0 and later.

Important: Starting in Spring ’16, API access to HashtagDefinition is disabled across all API versions. Any integrations relying on
API queries to this object stop working. You can continue to use hashtags in posts and comments, and the hashtags continue to
create corresponding topics. We recommend that you redirect all API queries and reports using the HashtagDefinition object to
[use the Topic object instead. For more information, see Retiring the Legacy HashtagDefinition Object—FAQs.](https://help.salesforce.com/apex/HTViewSolution?urlname=Retiring-the-Legacy-HashtagDefinition-Object)

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Fields

**Field Name**
```
HashtagCount
Name
NameNorm
NetworkId

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a hashtag topic is used.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string of characters following the hashtag (#) in a hashtag topic.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string of characters following the hashtag (#) in a hashtag topic, normalized
to remove capitalization and punctuation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the community to which the HashtagDefinition belongs. This field
is available only if digital experiences is enabled in your org.


Use this object to identify public hashtag topics and see how often they’re used.

SEE ALSO:

Topic


-----
