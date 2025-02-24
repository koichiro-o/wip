#### KnowledgeArticleEventLog

Knowledge Article View event logs contain user activity with your knowledge base. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ArticleIdentifier
ArticleStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The id of the article. For example: `00Dxx0000001gEb.`

**Type**
string


-----

```
ArticleVersion
ArticleVersionIdentifier
Context
IsLargeLanguageModel
IsLastVersion

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the article.

Possible values are:

**•** `D—Draft`

**•** `O—Online`

**•** `A—Archived`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The article version number. For example: `2.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the article version. For example: `ka0R00000005rt6.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Context of the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Whether the article was written with an LLM.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Language
ObjectType
RequestIdentifier
SessionIdentifier
Timestamp

```

**Description**
True if it is the last version of the article.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO code of the language. For example: `en_US/`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object requested. For example: `Knowledge__kav.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier. For example:`
```
  3nWgxWbDKWWDIk0FKfF5DV.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Session ID of the request. For example:
```
  gV7pCSW2vGaaJNFi3GSpuPIjNbKVbSxRvx34LJsIvuc=.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```

-----

```
UserIdentifier
UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User type of the request.

Possible values are:

**•** `A—App`

**•** `C—Customer Portal`

**•** `P—Partner Portal`

**•** `G—Guest`

