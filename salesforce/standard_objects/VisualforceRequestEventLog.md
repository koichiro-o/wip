#### VisualforceRequestEventLog

```
Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI). This object is available
in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
[is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)


-----

##### Fields

**Field**
```
ClientIp
ControllerType
CpuTime
DatabaseBlocks

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of controller that’s used by the requested Visualforce page.

Possible values are:

**•** `0—Not Specified`

**•** `1—Standard`

**•** `2—Standard Set`

**•** `3—Custom`

**•** `4—Java`

**•** `5—Spring`

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
Indicates how much activity is occurring in the database. A high value for this field suggests
that adding indexes or filters on your queries benefits performance.


-----

```
DatabaseCpuTime
DatabaseTotalTime
HttpMethod
IsAjaxRequest
IsFirstRequest
LoginKey

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds to complete the request. Indicates the amount of activity taking
place in the database layer during the request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseCpuTime. Compare this field to` `CpuTime` to
determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: `GET,` `POST,` `PUT, and so on.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The value is `true` if the request is a partial page request. The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`1` if this page is the first Visualforce transaction in the request, or `0` if it isn't. The default
value is `0.`

**Type**
string


-----

```
ManagedPackageNamespace
PageName
QueryString
RequestIdentifier

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
Filter, Group, Nillable, Sort

**Description**
If the page is part of a managed package, the namespace of that package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Visualforce page that was requested.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The query string used to access the requested Visualforce page.

**Example**
Let’s assume that the requested Visualforce page
(/apex/myAccountDetailPage?id=001xx000003GYv6AAG) shows details
of the account whose ID is in the URL. The value of `QueryString` in this case is
```
  ?id=001xx000003GYv6AAG.

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

-----

```
RequestSize
RequestStatus
RequestType
ResponseSize

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the callout response, in bytes.

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The request type.

Possible values are:

**•** `page—A normal request for a page`

**•** `content_UI—A content request for a page that originated in the user interface`

**•** `content_apex—A content request initiated by an Apex call`

**•** `PDF_UI—A request for a page in PDF format through the user interface`

**•** `PDF_apex—A request for PDF format by an Apex call (usually a Web Service call)`

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
The size of the callout request body, in bytes.

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

```
UserType
ViewStateSize
