#### BulkApi2EventLog

Bulk API 2 event logs contain details about Bulk API 2.0 requests. This object is available in API version 61.0 and later.

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
ClientIp
CpuTime
FailedRecordCount
ErrorMessage
JobIdentifier
JobStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The total number of records that failed. For example: `150.`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The error message returned on failure.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API 2.0 job.

**Type**
string


-----

```
LoginKey
ObjectType
OperationType
ProcessedRecordCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The job’s current status.

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
The type of event. The value is always `BulkApi2.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Bulk API 2.0 operation that was performed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of records processed for this event. For example: `980.The number of records`
processed is reported differently for ingest and query jobs.

For ingest jobs:

**•** Events with a status of `InProgress` report (if applicable) the number of records
processed.

For query jobs:

**•** Events with a status of `JobComplete` or `InProgress` report (if applicable) the
number of records processed.


-----

```
RequestIdentifier
ResultSize
RunTime
SessionKey
Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId. For example:`
```
  3nWgxWbDKWWDIk0FKfF5DV.

```
**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

Number of megabytes returned in query. Empty for ingest jobs. For example: `670.`

ResultSizeMb currently does not emit events, but is shown here as a placeholder for future
enhancement.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestId. For example:`
```
  3nWgxWbDKWWDIk0FKfF5DV.

```
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
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Uri
UserIdentifier
