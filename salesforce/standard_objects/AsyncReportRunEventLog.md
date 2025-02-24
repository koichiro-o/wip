#### AsyncReportRunEventLog

Async Report Run Event Log is used for reporting scheduled requests. This category includes dashboard refreshes, asynchronous reports,
schedule reports, and analytics snapshots. This object is available in API version 61.0 and later.

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
AverageRowSize
BucketCount
ClientIp
ColumnCount
CpuTime
DashboardIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The average row size (in bytes) of all rows in the Asynchronous Report Run event.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of buckets used in the report.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of columns in the report.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string


-----

```
DatabaseBlocks
DatabaseCpuTime
DatabaseTotalTime
DisplayType
ExceptionFilterCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the dashboard that was run.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
How much activity is occurring in the database.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time (in milliseconds) to complete the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total time spent in OracleJdbc calls, counting the Jdbc driver, Network, and Oracle time for
execs, fetches, and get-connection.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Possible values are:

**•** D—Dashboard

**•** S—Show Details

**•** H—Hide Details

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
IsPreview
LoginKey
ObjectName
Origin
RenderingType

```

**Description**
The number of exception filters used in the report.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is reserved for future use.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
```
  GeJCsym5eyvtEK2I.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object affected by the trigger.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Where the report is being executed, such as from a UI (Classic, Lightning, Mobile), through
an API (synchronous, asynchronous, Apex), or through a dashboard.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the format of the report output in Salesforce Classic. If the report was exported in
Lightning Experience, this field is blank.


-----

```
ReportIdentifier
RequestIdentifier
RequestStatus
RowCount
RunTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The report’s ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
String

**Description**
The status of the request for a page view or user interface action.

For example:

**•** `S—Success. Salesforce handled the request successfully. If an Apex controller throws`
an exception, this status is also returned.

**•** `F—Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page`
took too long to render, page is read-only.

**•** `U—Undefined`

**•** `A—Authorization Error`

**•** `R—Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a`
Visualforce page.

**•** `N—Not Found. 404 error.`

This field can have a blank value.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows that were processed in the Asynchronous Report Run event.

**Type**
double


-----

```
SessionKey
SortOrder
Timestamp
Uri
UserIdentifier

```

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
```
  d7DEq/ANa7nNZZVD.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The sort column and order that was used in the report.

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

**Description**
The URI of the page that’s receiving the request. For example: /home/home.jsp.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
UserType
