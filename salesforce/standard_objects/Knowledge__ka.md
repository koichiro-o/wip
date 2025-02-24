#### Knowledge__ka

```
Provides access to the concrete object that represents a Knowledge article, the parent object for article versions. This object is available
in API version 39.0 and later.

Note: By default, the prefix for this object name is `Knowledge` and that is the value shown in this reference. However, this
prefix can be modified by changing the Object Name for the Knowledge__kav object in Object Manager.

This object is derived from KnowledgeArticle on page 2861.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), query(), retrieve(), undelete()

 Special Access Rules

```
Lightning Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users,
unlike customer and partner users, must also be granted the `Knowledge User` feature license.

##### Fields

```
ArchivedById
ArchivedDate
ArticleNumber

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
The date when the article was archived.

**Type**
string


-----

```
CaseAssociationCount
FirstPublishedDate
LastPublishedDate
LastReferencedDate
LastViewedDate

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't change
the format or value for this field.

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
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
MasterLanguage
MigratedToFromArticle
TotalViewCount
