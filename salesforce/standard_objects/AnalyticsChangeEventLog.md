#### AnalyticsChangeEventLog

Analytics Change Event Logs represent route or page changes made in the CRM Analytics. This object is available in API version 61.0 and
later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
AnalyticsMode
AnalyticsSessionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location where the dashboard is displayed. In the Salesforce mobile app, embedded
dashboards are logged as embedded first.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
AnalyticsTimestamp
ClientIp
CpuTime
IsMobile
IsNew

```

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the dashboard is displayed in mobile (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The field indicates that this action opens a new tab (true) or goes back to a previously
opened tab (false).

The default value is `false.`


-----

```
LoginKey
PageContext
PageIdentifier
RecordIdentifier
ReopenCount
RequestIdentifier

```

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
The name of the component hosting the main content of the page. For example:
clients:cardsContainer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CRM Analytics dashboard page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the CRM Analytics object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If `IsNew` is `false, the number of times that an existing page opens.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
RunTime
SavedViewIdentifier
SessionKey
TabIdentifier
Timestamp

```

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
The ID of the CRM Analytics dashboard saved view.

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
The ID of the particular Analytics tab in the user interface.

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
Type
Uri
UserIdentifier
ViewMode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of Apex callout. For example: REST or AJAX.

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

**Description**
The 15-character Identifier of the user who’s using Salesforce services through the UI or the
API. For example: `00530000009M943.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The view mode for the CRM Analytics asset. Possible values include `view`

**•** `edit`

**•** `present`

**•** `JSON`

**•** `print`

