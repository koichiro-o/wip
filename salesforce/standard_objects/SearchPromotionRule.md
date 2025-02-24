#### SearchPromotionRule

Represents a promoted search term, which is one or more keywords that you associate with a Salesforce Knowledge article. When a
user’s search query includes these keywords, the associated article is returned first in search results. This object is available in API version
31.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
A user must have the “Manage Promoted Search Terms” permission.

##### Fields

```
PromotedEntityId
Query

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the KnowledgeArticleVersion that the promoted search term is
associated with. The article must be in published status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

**Description**
The text of the promoted search term. Maximum length: 100 characters.

You can associate the same promoted search term with multiple articles. If the
user’s search matches the promoted term, all associated articles are promoted
in search results, ordered by relevancy. For best results, create promoted search
terms selectively and limit the number of articles that are promoted per term.

##### Usage

Use this object to optimize article search results in Salesforce Knowledge.
