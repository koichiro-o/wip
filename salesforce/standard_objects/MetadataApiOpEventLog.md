#### MetadataApiOpEventLog

MetadataApiOpEventLog stores details of Metadata API retrieval and deployment requests. This object is available in API version 62.0
and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ApiVersion
ClientIdentifier
ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the API that’s being used.

For example: `60.0.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
CpuTime
LoginKey
OperationType
RequestIdentifier

```

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26.`

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
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
RunTime
SessionKey
Timestamp
Uri
UserIdentifier

```

**Description**
Globally unique id for a given request.

For example: `3nWgxWbDKWWDIk0FKfF5DV.`

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
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`
