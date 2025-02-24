#### Knowledge__kav

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports multiple
languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article. Contains values only in orgs that
migrate from Knowledge in Salesforce Classic to Lightning Knowledge. This field is available
in API version 45.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for this article. This field is available in API version 39.0 and later.


Provides access to the concrete object that represents a Knowledge article version. This object is available in API version 39.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note: By default, the prefix for this object name is `Knowledge` and that is the value shown in this reference. However, this
prefix can be modified by changing the Object Name for the Knowledge__kav object in Object Manager.

This object is derived from KnowledgeArticleVersion on page 2867.


-----

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), query(), retrieve(), search(), update(), upsert()

```
This object doesn’t retrieve `<ActionOverrides>.`

##### Special Access Rules

Lightning Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users,
unlike customer and partner users, must also be granted the `Knowledge User` feature license.

##### Fields

```
ArchivedById
ArchivedDate
ArticleArchivedById
ArticleArchivedDate
ArticleCaseAttachCount

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

**Type**
int


-----

```
ArticleCreatedById
ArticleCreatedDate
ArticleMasterLanguage
ArticleNumber
ArticleTotalViewCount

```

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
The article's original language. Only accessible if your knowledge base supports multiple
languages.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't change
the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for the article.


-----

```
AssignedById
AssignedToId
AssignmentDate
AssignmentDueDate
AssignmentNote
ExternalRef

```

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

**Properties**
Filter, Nillable, Sort

**Description**
Notes to the assignee from the user who assigned the article.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ExternalSourceId
ExternalUrl
FirstPublishedDate
IsExternalData
IsLatestVersion

```

**Description**
The ID of the item being referenced on the external system. For example, the ID of a document
on a Google Drive or a page on Confluence.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference to the external Knowledge data source object.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL of the knowledge content referenced in an external system. For example, the ID of
a document in Google Drive or a page in Confluence.

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
Indicates whether the data is external to the customer’s knowledge base (true) or not
(false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article is the most current version. (true) or not (false). This field
can be `true` on the online or published version, a draft version in the primary language, a
draft version in a translation, and the latest archived version. However, you can’t filter by


-----

```
IsMasterLanguage
IsOutOfDate
IsVisibleInApp
IsVisibleInCsp
IsVisibleInPkb

```

(PublishState=’Online’) and (IsLatestVersion=false) because the online version is also the
latest version. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article has one or more translations associated with it (true) or not
(false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the source article has been updated since this translated version was
created (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Articles tab (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the Customer Portal (true) or not
(false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the public knowledge base (true) or
not (false).


-----

```
IsVisibleInPrm
KnowledgeArticleId
Language
LastPublishedDate
MasterVersionId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the partner portal (true) or not (false).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article independent from its version. The value for this field is retrieved from
the `Id` field of the KnowledgeArticle object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as `French` or `Chinese`
```
  (Traditional).

```
Querying or searching articles in SOSL require that you specify the `Language` field in the
WHERE clause. The language must be the same for all article types.

Before API version 47.0, you must include the Language field to filter queries on Knowledge
article versions. In API version 47.0 and later, you can filter queries on Knowledge article
versions with or without `Language` depending on what you are querying.

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
ID of the source article, if the article is the translation of a source article. Only accessible if
your knowledge base supports multiple languages.


-----

```
MigratedToFromArticleVersion
NextReviewDate
OwnerId
PublishStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article version. Contains values only in
orgs that migrate from Classic to Lightning Knowledge. Available in API version 43.0 and
later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article must next be reviewed for accuracy. Available in API version 58.0
and later.

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
`PublishStatus` or the `Id field in the WHERE clause. You can search for only one`
publication status per article type in a single SOSL query. When searching for articles with a
`PublishStatus` of Archived, also check that IsLatestVersion equals false
in your WHERE clause.


-----

```
RecordTypeId
SourceId
Summary
Title
TranslationCompletedDate
TranslationExportedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the API Name that describes the type of article. Use the record type to determine
the article structure and other settings for different types of content.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source from which the article was created (Case or Reply). This field is only accessible
from the API and isn’t visible in the Salesforce UI.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Summary of the article. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Article's title. Maximum size is 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last translated. Only accessible if your knowledge base
supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
TranslationImportedDate
UrlName
ValidationStatus
VersionNumber

```

**Description**
Date and time when the article was last exported for translation. Only accessible if your
knowledge base supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last imported for translation. Only accessible if your
knowledge base supports multiple languages.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Represents the article's URL. Can contain alphanumeric characters and hyphens
but can't begin or end with a hyphen. Use a unique value regardless of context. (For example,
a unique value allows you to get expected results when running an Apex test with
`SeeAllData` set to `false.)` `UrlName` is case-sensitive and its maximum size is 255
characters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group

**Description**

Shows whether the content of the article has been validated. Possible values are
`Validated` and Not Validated. The default value is Not Validated. This field
is available in API version 24.0 or later.

**Type**
int

**Properties**
Group, Sort

**Description**
The number assigned to a version of an article. This field is available in API version 24.0 and
later.


-----
