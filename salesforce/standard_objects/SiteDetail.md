#### SiteDetail

Represents the details of a Salesforce site or Experience Cloud site. Available in API Version 38.0 and later.

##### Supported SOAP Calls
```
describeSObjects(), query()

 Supported REST HTTP Methods
GET

```

-----

##### Fields

**Field**
```
DurableId
IsRegistrationEnabled
SecureUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Site object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the site allows users to sign up.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the website.


Note: SiteDetail fields are exposed in SOAP API version 45.0 and later. You can use Tooling API to query for SiteDetail fields in
guest user mode in API version 44.0 and earlier. In API version 45.0 and later, use SOAP API to get this data in guest user mode.
SiteDetail is still exposed in Tooling API to User Profiles with the ViewSetup permission.

SiteEventLog
SiteEventLog stores details of Site.com requests. Requests can originate from the browser (UI). This object is available in API version
62.0 and later.

##### SiteEventLog

SiteEventLog stores details of Site.com requests. Requests can originate from the browser (UI). This object is available in API version 62.0
and later.

###### Supported Calls
```
describeSObjects(), query()

```

-----

###### Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

###### Fields

```
ClientIp
CpuTime
DatabaseTotalTime
HttpHeaders
HttpMethod

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and DB_CPU_TIME. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP headers that were sent in the request.

**Type**
string


-----

```
IsApi
IsError
IsFirstRequest
IsGuest
IsSecure

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: GET, POST, PUT, and so on.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was an error page.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page is the first Visualforce transaction in the request.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was a guest (unauthenticated) request.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
LoginKey
PageName
QueryString
RequestIdentifier
RequestStatus

```

**Description**
True if this request is secure.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
GeJCsym5eyvtEK2I.

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
The SOQL query, if one was performed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
RequestType
RunTime
SessionKey

```

**Description**
The status of the request for a page view or user interface action. This field can have a blank
value.

For example:

**•** `S— Success. Salesforce handled the request successfully. If an Apex controller throws`
an exception, this status is also returned.

**•** `F— Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page`
took too long to render, page is read-only.

**•** `U— Undefined.`

**•** `A—Authorization error.`

**•** `R— Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a`
Visualforce page.

**•** `N—Not Found. 404 error.`

**Type**
String

**Description**
The request type.

Possible values are:

**•** `page—a normal request for a page`

**•** `content_UI—a content request for a page that originated in the user interface`

**•** `content_apex—a content request initiated by an Apex call`

**•** `PDF_UI—a request for a page in PDF format through the user interface`

**•** `PDF_apex—a request for PDF format by an Apex call (usually a Web Service call)`

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

-----

```
SiteIdentifier
Timestamp
Uri
UserIdentifier
UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Site.com site.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: `20130715233322.670.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `home/home.jsp.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943YAS.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly—Users whose access to the application is limited to Chatter. This user type`
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal—CSP Lite Portal license. Users whose access is limited because`
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.


-----

**•** `CustomerSuccess—Customer Success license. Users whose access is limited`
because they’re organization customers and access the application through a customer
portal.

**•** `Guest—Users whose access is limited so that your customers can view and interact`
with your site without logging in.

**•** `PowerCustomerSuccess—Power Customer Success license. Users whose access`
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner—Power Partner license. Users whose access is limited because they’re`
partners and typically access the application through a partner portal or site.

**•** `SelfService—Users whose access is limited because they’re organization customers`
and access the application through a self-service portal.

**•** `Standard—Standard user license. This user type also includes Salesforce Platform`
and Salesforce Platform One user licenses, and admins for this org.
