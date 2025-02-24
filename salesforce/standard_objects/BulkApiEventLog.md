#### BulkApiEventLog

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
The URI of the page that’s receiving the request. For example: `/home/home.jsp.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943.`


Bulk API event logs contain details about Bulk API requests. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
BatchIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ClientIp
CpuTime
FailureCount
IsSuccess
JobIdentifier
LoginKey

```

**Description**
The 15-character ID of the Bulk API batch.

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
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of failures that were returned with the request.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the callout request was successful.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Bulk API job.

**Type**
string


-----

```
Message
ObjectType
OperationType
RequestIdentifier
RowsProcessed

```

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
Filter, Nillable, Sort

**Description**
Any success or error message that’s associated with the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of entity that the Bulk API used.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Bulk API operation that was performed.

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


-----

```
RunTime
SessionKey
Timestamp
Uri
UserIdentifier

```

**Description**
The number of rows that were processed in the request. For example: `150.`

**Type**
double

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
The URI of the page that’s receiving the request. For example: `/home/home.jsp.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943.`


-----
