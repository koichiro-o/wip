#### ApexExecutionEventLog

Apex Execution event logs contain details about Apex classes that are used. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
CalloutTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Time spent waiting on webservice callouts, in milliseconds.


-----

```
ClientIp
CpuTime
DatabaseTotalTime
EntryPoint
ExecutionTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.

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
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entry point for this Apex execution. For example,
```
  GeneralCloner.cloneAndInsertRecords or VF- /apex/CloneUser.

```
**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The end-to-end Apex execution time (in milliseconds).


-----

```
IsLongRunningRequest
LoginKey
Quiddity

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the request is counted against your org’s concurrent long-running Apex
request limit (true) or not (false).

Asynchronous Apex jobs (batch, queueable, scheduled, and future), background processes,
and bulk API requests are not counted against the concurrent long-running limit.

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
The type of outer execution associated with this event. For example:

**•** `A–ACS Batch Apex`

**•** `C–Scheduled Apex`

**•** `E–Inbound Email Service`

**•** `F–Future`

**•** `H–Apex REST`

**•** `I–Invocable Action`

**•** `K–Quick Action`

**•** `L–Lightning`

**•** `M–Remote Action`

**•** `P–Bulk Apex jobs running in parallel`

**•** `Q–Queueable`

**•** `R–Synchronous uncategorized (which is where all transactions not specified elsewhere`
end up)


-----

```
RequestIdentifier
RunTime
SessionKey
SoqlQueryCount

```


**•** `S–QueryLocator Batch Apex (Batch Apex jobs run faster when the start method returns`
a QueryLocator object that doesn't include related records via a subquery. See Batch
[Apex Best Practices in Using Batch Apex.)](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_batch_interface.htm#apex_batch_best_practices)

**•** `T–Tests Apex`

**•** `V–Visualforce`

**•** `W–SOAP Webservices`

**•** `X–Execute Anonymous`

Implementations of the Process.Plugin interface use the quiddity value `R.`

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
The amount of time the request took, as measured by SFDC code.

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
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of SOQL queries that were executed during the event.

This value is the aggregate across all namespaces, and can exceed the per-namespace limits.
For test executions, the aggregate total value across all test methods executed in the request


-----

```
Timestamp
Uri
UserIdentifier

```

is used. If you are using this value to track limit consumption, consider filtering out test
execution quiddities (indicated by the `Quiddity` field).

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

