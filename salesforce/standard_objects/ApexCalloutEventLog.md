#### ApexCalloutEventLog

Apex Callout event logs contain details about callouts (external requests) during Apex code execution. This object is available in API
version 55.0 and later.

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
IsSuccess
LoginKey
Method

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
The HTTP method of the callout. For example: `GET,` `POST,` `PUT, and so on.`


-----

```
RequestIdentifier
RequestSize
RequestTime
ResponseSize
RunTime
SessionKey

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
The size of the callout request body, in bytes.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Not used for this event type. Use the `RequestTime` field instead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
StatusCode
Timestamp
Type
Uri
Url

```

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
```
  d7DEq/ANa7nNZZVD.

```
**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The returned status code of the request.

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
The type of Apex callout. For example: `REST` or `AJAX.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp.`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The callout endpoint URL. For example, `www.salesforce.com.`


-----

```
UserIdentifier
