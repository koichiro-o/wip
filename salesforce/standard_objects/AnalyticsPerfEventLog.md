#### AnalyticsPerfEventLog

Analytics Perf Event Log helps track trends in your Analytics performance. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


-----

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
AnalyticsSessionIdentifier
AnalyticsTimestamp
ClientIp
CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line is generated.

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


-----

```
EffectivePageTime
IsInitialLoad
LoginKey
QueriedName
RecordIdentifier
RequestIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The experienced page time in milliseconds.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is for the initial load of the Dashboard (true) or not (false).

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
The asset title or query string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the CRM Analytics object.

**Type**
string


-----

```
RunTime
SessionKey
TabIdentifier
Timestamp
Uri

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
3nWgxWbDKWWDIk0FKfF5DV.

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the particular Analytics tab in the UI.

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

```
UserIdentifier
ViewMode
