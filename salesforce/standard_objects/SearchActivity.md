#### SearchActivity

Represents search activity on a Knowledge article. Also known as KnowledgeSearchActivity. This object is available in API version 38.0
and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
The Knowledge Base Search Dashboard permission must be enabled in your org.


-----

##### Fields

**Field**
```
AvgNumResults
ClickRank
ClickedRecordId
ClickedRecordName
CountQueries

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The number of search results returned for the search term. If Period is also included, this
value is aggregated based on the time period specified.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that the article appeared in the search results when the user sorted the results by
relevance and clicked it from the list of results.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the clicked article.

This field is a polymorphic relationship field.

**Relationship Name**
ClickedRecord

**Relationship Type**
Lookup

**Refers To**
Knowledge__kav

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the clicked article taken when the user sorts the search results by relevance.

**Type**
int


-----

```
CountUsers
KbChannel
Name
Period

```

**Properties**
Filter, Group, Sort

**Description**
The number of searches for the period (day, month, or year).

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of individual users who clicked the article.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The channel that’s applicable to the article.

Possible values are:

**•** `AllChannels—All Channels`

**•** `App—Internal App`

**•** `Csp—Customer`

**•** `Pkb—Public Knowledge Base`

**•** `Prm—Partner`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of search activity.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The time period that the search count is applied to. For example, a record where the Count
is 70 and the Period is Monthly indicates that 70 searches took place over the past month.
Totals are aggregated daily for the current month, monthly from the past full month through
the past full year, and yearly beyond that.


-----

```
QueryDate
QueryLanguage
SearchTerm

```

Activity totals are collected nightly and aren’t in real time.

Possible values are:

**•** `DAY`

**•** `MONTH`

**•** `YEAR`

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date of the search.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language filter that’s applied to the user’s search.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first 100 characters of the search term that was used to search published articles in the
knowledge base.

