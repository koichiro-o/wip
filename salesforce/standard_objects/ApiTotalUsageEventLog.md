#### ApiTotalUsageEventLog

API Total Usage Event Log contains details about Platform SOAP API, Platform REST API, and Bulk API requests. This object is available in
API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ApiFamily
ApiResource
ClientIp
ClientName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API family. For example, REST, SOAP, or Bulk.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API method or resource. For example, `describeSObjects` for SOAP.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
string


-----

```
ConnectedAppIdentifier
HttpMethod
IsApiLimitCounted
ObjectName
RequestIdentifier

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the client making the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the connected app making the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method. For example, `GET.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the request counted against the API limit (true) or not (false).

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
StatusCode
Timestamp
UserIdentifier

```

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP response status code for the request.

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
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
  00530000009M943.

```
