#### LoginAsEventLog

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The size of the queued party.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The state of a party in the queue.

Possible values are:

**•** `canceled`

**•** `entered`

**•** `exited`

**•** `ready`

**•** `waiting`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a party signed up for the queue.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID for the queue.


LoginAsEventLog contains details about when a user logs in as another user in your org. This object is available in API version 56.0 and
later.

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
ClientIp
CpuTime
DelegatedUserIdentifier
DelegatedUserName

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID that identifies the user who’s logging in as, or impersonating, another user. For
example: `00530000009M943.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the user who’s logging in as, or impersonating, another user.


-----

```
LoginKey
RequestIdentifier
RunTime
SessionKey
Timestamp

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
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier. For example:`
```
  3nWgxWbDKWWDIk0FKfF5DV.

```
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
The impersonated user’s unique session ID. You can use this value to identify all user events
within a session. When a user logs out and logs in again, a new session is started. For Login
Event Type, this field is usually null because the event is captured before a session is created.
For example: `d7DEq/ANa7nNZZVD.`

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
Uri
UserIdentifier
