#### SearchEventLog

Search Event Log provides details about the user’s search query. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
PrefixesSearched

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A space-delineated list of key prefixes that are searched.


-----

```
QueryIdentifier
RequestIdentifier
ResultCount
SearchQuery
Timestamp
UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID of the search query.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of results returned by the search query.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first 100 characters of the search query.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
                00530000009M943.

##### Usage

```
All searches within the app, including Experience Cloud sites, are included. However, unauthenticated guest users don’t have a unique
Salesforce user ID.
