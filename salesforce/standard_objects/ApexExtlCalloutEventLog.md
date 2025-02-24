#### ApexExtlCalloutEventLog

Apex Extl Callout EventLog represent external data callouts via custom adapters for Salesforce Connect. This object is available in API
version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.


-----

##### Fields

**Field**
```
Action
ExecutionTime
FetchTime
IsSuccess
Message
ObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Action performed by the callout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time in milliseconds.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Duration (in milliseconds) it takes to retrieve the query results from the external system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the query was successful (true) or not (false).

The default value is `false.`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Error or warning message associated with the failed call.

**Type**
string


-----

```
QueryFilter
QueryLimit
QueryOffset
QueryOrderBy
QuerySelect

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of event. The value is always BulkApi2.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field expressions to filter the rows to return. Corresponds to `WHERE` in SOQL queries.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of rows to skip when paging through a result set. Corresponds to OFFSET in SOQL
queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Comma-delineated list of fields being queried. Corresponds to `SELECT` in SOQL queries.


-----

```
RequestIdentifier
RowCount
RowsFetched
Subqueries
Throughput
Timestamp

```

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
Total number of records in the result set.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of rows fetched by the callout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of subqueries this query has been split into.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of records retrieved in one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
TotalTime
UserIdentifier
