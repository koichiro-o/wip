#### KnowledgeArticle

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique ID for the user in Salesforce.


Provides read-only access to an article and the ability to delete the primary article. This object is available in API version 19.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Unlike KnowledgeArticleVersion, the ID of a KnowledgeArticle record is identical irrespective of the article's version (status).

Knowledge__ka on page 2847 is derived from this object.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users, unlike
customer and partner users, must also be granted the `Knowledge User` feature license.

##### Fields

```
ArchivedById
ArchivedDate

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


-----

```
ArticleNumber
CaseAssociationCount
FirstPublishedDate
IsGeneratedByLlm
LastPublishedDate
LastReferencedDate

```

**Description**
The date when the article was archived.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't
change the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of cases attached to the article.

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
True if the first version of an article was created with an LLM. This object is available
in API version 59.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
dateTime


-----

```
LastViewedDate
MasterLanguage
MigratedToFromArticle
TotalViewCount

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value
is null, the user has not viewed this record or list view, though they might have
accessed it (LastReferencedDate)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports
multiple languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article. Contains values only in
orgs that migrate from Knowledge in Salesforce Classic to Lightning Knowledge. This
field is available in API version 45.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for this article. This field is available in API version 39.0 and
later.


-----

##### Usage

Use this object to query or retrieve articles. KnowledgeArticle can be used in a SOQL clause, but doesn’t provide access to the fields from
the article. Provides read-only access to an article and the ability to delete the primary article.

##### Usage for SOQL with KnowledgeArticle

To expose the `migrated_to_from_id` column on KnowledgeArticle and KnowledgeArticleVersion to the sObject API: expose
`MigratedToFromArticle` in KnowledgeArticle.

For SOQL:

**•** To filter by `MigratedToFromArticle, remove any other filters.`

**•** When filtering by `MigratedToFromArticle, use the '=' or 'IN' operator.`

**•** When filtering by `MigratedToFromArticle, the value can't be null or empty.`

SEE ALSO:

KnowledgeArticleVersion
