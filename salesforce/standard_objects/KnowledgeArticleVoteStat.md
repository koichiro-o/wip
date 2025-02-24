#### KnowledgeArticleVoteStat

Provides the weighted rating for the specified article on a scale of 1 to 5 across all article types. This object is read-only and available in
API version 20.0 and later.

Knowledge__VoteStat is derived from this object.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Knowledge must be enabled in your org. Users must have access to the published version of an article to retrieve its votes. For more
information on published article version, see the `PublishStatus` field in KnowledgeArticleVersion

##### Fields

```
Channel

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The channel where the article is rated:

**•** `AllChannels` for article views across all channels.

**•** `App` for the internal Salesforce Knowledge application.

**•** `Pkb` for article views in public knowledge base.

**•** `Csp` for Customer Portal.

**•** `Prm` for article view in partner portal.


-----

```
NormalizedScore
ParentId

##### Usage

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Article's weighted score on a scale of 1 to 5. A higher score means more votes. Articles
without recent votes trend towards an average rating of three stars.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The rated article. This corresponds to a KnowledgeArticle record.


Use this object to query or retrieve the rating for an article.

Alternatively, client applications can use the article type `API Name` followed by `__VoteStat` to query or retrieve the rating for an
article for a specific article type.

##### SOQL Samples

See KnowledgeArticleViewStat.

SEE ALSO:

KnowledgeArticle

KnowledgeArticleVersion

KnowledgeArticleViewStat
