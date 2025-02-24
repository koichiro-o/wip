#### SearchClickEventLog

Search Click Event Log contains details about the user’s interaction with the search results. This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

```

-----

##### Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ClickedRecordIdentifier
QueryIdentifier
Rank
RequestIdentifier
Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the result the user clicked in the search results page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID of the search query.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Ranking of the result clicked in the search results page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
UserIdentifier

##### Usage

```

**Description**
The access time of Salesforce services in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
  00530000009M943.

```

All searches within the app, including Experience Cloud sites, are included. However, unauthenticated guest users don’t have a unique
Salesforce user ID.
