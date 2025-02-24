#### CaseArticle

Represents the association between a Case and a KnowledgeArticle. This object is available in API version 20.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

Access to this object is controlled by the parent Case and KnowledgeArticle. However, when querying, access is only controlled by the
parent Case.

Customer Portal users can't access this object.

##### Fields

```
ArticleLanguage
ArticleVersionNumber
CaseId
IsSharedByEmail
KnowledgeArticleId

```

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
The language of the article associated with the case.

**Type**
int

**Properties**
Create, Group, Nillable

**Description**
The number assigned to a version of an article. This field is available in API version 24.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Case associated with the KnowledgeArticle.

**Type**
int

**Properties**
Create, Group, Nillable

**Description**
Indicates that the article has been shared with the customer through an email.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

**Description**
ID of the KnowledgeArticle associated with the Case.

##### Usage

This object represents the association of a knowledge article with a Case. An article is associated with a case when it’s relevant to a
specific issue, when it helps an agent solve the case, or when the agent sends the article to a customer.

You can use this object to include case-article associations in Apex and Visualforce.

You can't update this object via the API. If you attempt to create a record that matches an existing record, the create request simply
returns the existing record.

SEE ALSO:

Case

KnowledgeArticle
