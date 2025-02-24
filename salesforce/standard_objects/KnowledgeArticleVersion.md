#### KnowledgeArticleVersion

Provides a global view of standard article fields across all types of articles depending on their version. This object is available in API version
18.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Use this object to:

**•** Query or search generically across multiple types of articles.

**•** Filter on a specific version.

**•** Update standard fields in draft versions.

When you query on the archived article, the results include both the article and the article’s archived versions.

Knowledge__kav on page 2849 is derived from this object.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve(), search()

```
Note:

**•** You can only update draft versions.


-----

**•** You can't update draft translations with the `knowledgeManagement` REST API.

**•** For Lightning Knowledge, to create, update, or delete a Knowledge article version, use the call on Knowledge__kav. For
example, to delete, use `Knowledge__kav.delete().`

**•** For Knowledge in Salesforce Classic, to create, update, or delete a Knowledge article version, use the call on
`ArticleType__kav, where ArticleType` is the name of the article’s type. For example, to delete, use
```
    ArticleType__kav.delete().

##### Special Access Rules

```
Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users, unlike
customer and partner users, must also be granted the `Knowledge User` feature license.

##### Fields

```
ArchivedById
ArchivedDate
ArticleArchivedById
ArticleArchivedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article version was archived.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was archived.


-----

```
ArticleCaseAttachCount
ArticleCreatedById
ArticleCreatedDate
ArticleMasterLanguage
ArticleNumber
ArticleTotalViewCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cases where this article is attached.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who created the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports
multiple languages.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't
change the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ArticleType
AssignedById
AssignedToId
AssignmentDate
AssignmentDueDate
AssignmentNote

```

**Description**
Total number of views for the article.

**Type**
string

**Properties**
Defaulted on createFilter

**Description**
Indicates the API Name of the article type. The `ArticleType` is assigned to the
article when it's created. You can't change the value of this field. This field is available
in orgs using Knowledge in Salesforce Classic in API version 26.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who assigned the article.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user assigned to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was assigned to a user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The due date when an article is assigned.

**Type**
textarea


-----

```
FirstPublishedDate
IsLatestVersion
IsMasterLanguage
IsOutOfDate

```

**Properties**
Filter, Nillable, Sort

**Description**
Notes to the assignee from the user who assigned the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article is the most current version. (true) or not (false).
This field can be `true` on the online or published version, a draft version in the
primary language, a draft version in a translation, and the latest archived version.
However, you can’t filter by (PublishState=’Online’) and (IsLatestVersion=false) because
the online version is also the latest version. This field is available in API version 24.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article has one or more translations associated with it (true)
or not (false). Only accessible if your knowledge base supports multiple languages.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the source article has been updated since this translated version
was created (true) or not (false). Only accessible if your knowledge base supports
multiple languages.


-----

```
IsVisibleInApp
IsVisibleInCsp
IsVisibleInPkb
IsVisibleInPrm
KnowledgeArticleId
Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Articles tab (true) or not
(false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Customer Portal (true) or
not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the public knowledge base (true)
or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the partner portal (true) or not
(false).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article independent from its version. The value for this field is retrieved
from the `Id field of the KnowledgeArticle object.`

**Type**
picklist


-----

```
LargeLanguageModel
LastPublishedDate
MasterVersionId
MigratedToFromArticleVersion

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as French or Chinese
```
  (Traditional).

```
Querying or searching articles in SOSL require that you specify the Language field
in the WHERE clause. The language must be the same for all article types.

Before API version 47.0, you must include the `Language` field to filter queries on
Knowledge article versions. In API version 47.0 and later, you can filter queries on
Knowledge article versions with or without Language depending on what you are
querying.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Shows the LLM used to create an article version. This object is available in API version
59.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source article, if the article is the translation of a source article. Only accessible
if your knowledge base supports multiple languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
NextReviewDate
OwnerId
PublishStatus
SourceId

```

**Description**
The ID for the corresponding pre- or post-migration article version. Contains values
only in orgs that migrate from Classic to Lightning Knowledge. Available in API version
43.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article must next be reviewed for accuracy. Available in API version
58.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article's owner.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The publication status for the article:

**•** `Draft: any draft articles.`

**•** `Online: articles published in Salesforce Knowledge.`

**•** `Archived: archived articles.`

A user must have the “Manage Articles” permission enabled to use `Online.`

Article queries and searches in SOQL or SOSL require that you specify either the
`PublishStatus` or the Id field in the WHERE clause. You can search for only
one publication status per article type in a single SOSL query. When searching for
articles with a PublishStatus of `Archived, also check that`
`IsLatestVersion` equals false in your WHERE clause.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
Summary
Title
TranslationCompletedDate
TranslationExportedDate
TranslationImportedDate

```

**Description**
ID of the source from which the article was created (Case or Reply).

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Summary of the article. Maximum size is 1000 characters.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Article's title. Maximum size is 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last translated. Only accessible if your knowledge
base supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last exported for translation. Only accessible if
your knowledge base supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last imported for translation. Only accessible if
your knowledge base supports multiple languages.


-----

```
UrlName
ValidationStatus
VersionNumber

##### Usage

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Represents the article's URL. Can contain alphanumeric characters and
hyphens but can't begin or end with a hyphen. This value must be unique regardless
of context. (For example, a unique value allows you to get expected results when
running an Apex test with SeeAllData set to false.) UrlName is case-sensitive
and its maximum size is 255 characters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group

**Description**

Shows whether the content of the article has been validated. Possible values are
`Validated` and `Not Validated. The default value is` `Not Validated.`
This field is available in API version 24.0 or later.

**Type**
int

**Properties**
Group, Sort

**Description**
The number assigned to a version of an article. This field is available in API version
24.0 and later.


Use this object to query, retrieve, or search for articles across all types of articles depending on their version. You can update draft primary
articles. Also, you can delete articles that aren’t drafts. Client applications can use KnowledgeArticleVersion with
`describeDataCategoryGroups()` and `describeDataCategoryGroupStructures()` to return the category
groups and the category structure associated with Salesforce Knowledge.

To access an article independent of its version, use the KnowledgeArticle object.

In Lightning Knowledge, the type of article is determined by the `RecordType` field on the concrete derived object (for example,
Knowledge__kav on page 2849). For Knowledge in Salesforce Classic, the type of article is determined by the ArticleType field and
the concrete derived object uses the prefix of the article type name (for example, FAQ__kav for the FAQ article type).


-----

##### SOQL Samples

The following SOQL clause uses KnowledgeArticleVersion to query all published articles from all articles complying with the classification
specified in the WITH DATA CATEGORY clause:
```
SELECT Title, Summary
FROM KnowledgeArticleVersion
WHERE PublishStatus='Online'
AND Language = 'en_US'
WITH DATA CATEGORY Geography__c ABOVE_OR_BELOW europe__c AND Product__c BELOW All__c

```
The following SOQL clause for Lightning Knowledge uses the `Offer` record type to limit the query to all draft articles:
```
SELECT Id, Title
FROM Knowledge__kav
WHERE PublishStatus='Draft'
AND Language = 'en_US'
AND RecordTypeId = '<specify RecordTypeId for Offer here>'
WITH DATA CATEGORY Geography__c AT (france__c,usa__c) AND Product__c ABOVE dsl__c

```
The following SOQL clause for Salesforce Classic uses the `Offer` article type to limit the query to all draft articles:
```
SELECT Id, Title
FROM Offer__kav
WHERE PublishStatus='Draft'
AND Language = 'en_US'
WITH DATA CATEGORY Geography__c AT (france__c,usa__c) AND Product__c ABOVE dsl__c

```
The following SOQL clause uses KnowledgeArticleVersion to query the IDs of all archived versions of a particular article:
```
SELECT Id
FROM KnowledgeArticleVersion
WHERE PublishStatus='Archived'
AND IsLatestVersion=false
AND KnowledgeArticleId='kA1D00000001PQ6KAM'

##### SOQL and SOSL with KnowledgeArticleVersion

```
**•** Filter on a single value of PublishStatus for best results. To find all versions of each article, omit the PublishStatus filter,
but do filter on one or more master key IDs. To retrieve all archived versions for a given article, specify a SOQL filter where
`IsLatestVersion` is `false.`

**•** In API version 46.0 and earlier, queries without a filter on PublishStatus return published articles by default. In API version
47.0 and later, draft, published, and archived articles are returned when Lightning Knowledge is enabled.

**•** To support security, only users with the “View Draft Articles” permission see articles whose `PublishStatus` value is Draft.
Similarly, only users with the “View Archived Articles” permission see articles whose PublishStatus value is `Archived`

**•** Archived article versions are stored in the `Knowledge__kav` object. To query archived article versions, specify the article `Id`
and set `IsLatestVersion='0'.`

**•** You can’t use binding variables in Apex SOQL statements with KnowledgeArticleVersion objects. For example, the following SOQL
statement causes a compilation error.


-----

[Instead, use dynamic SOQL as follows. See Dynamic SOQL in Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)
```
  final String PUBLISH_STATUS_ONLINE = 'Online';
  final String q = 'SELECT Id, PublishStatus FROM Knowledge__kav
  WHERE PublishStatus = :PUBLISH_STATUS_ONLINE';
  List<Knowledge__kav> articles = Database.query(q);

##### Other Usage for SOQL and SOSL with KnowledgeArticleVersion

```
To expose the migrated_to_from_id on KnowledgeArticle and KnowledgeArticleVersion to the sObject API: expose
**MigratedToFromArticleVersion in KnowledgeArticleVersion.**

**•** For SOQL:

**–** To filter by MigratedToFromArticleVersion, remove any other filters.

**–** When filtering by MigratedToFromArticleVersion, use the '=' or 'IN' operator.

**–** When filtering by MigratedToFromArticleVersion, the value can't be null or empty.

**•** SOSL doesn’t support MigratedToFromArticleVersion.

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**KnowledgeArticleVersionHistory**

History is available for tracked fields of the object.

SEE ALSO:

KnowledgeArticle

KnowledgeArticleViewStat

KnowledgeArticleVoteStat
