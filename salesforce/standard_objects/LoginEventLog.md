#### LoginEventLog

Login event logs contain details about your Salesforce org's user login history. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ApiType

```

**Type**
string


-----

```
ApiVersion
AuthenticatedMethodReference
BrowserType

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of API request.

Possible values are:

**•** `D—Apex Class`

**•** `E—SOAP Enterprise`

**•** `I—SOAP Cross Instance`

**•** `M—SOAP Metadata`

**•** `O—Old SOAP`

**•** `P—SOAP Partner`

**•** `S—SOAP Apex`

**•** `T—SOAP Tooling`

**•** `X—XmlRPC`

**•** `f—Feed`

**•** `l—Live Agent`

**•** `p—SOAP ClientSync`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the API that’s being used. For example: 36.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The authentication method used by a third-party identification provider for an OpenID
Connect single sign-on protocol.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier string returned by the browser used at login.

Example values are:


-----

```
CipherSuite
ClientIp
CpuTime
DatabaseTotalTime
ForwardedForIp

```


**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv%3A50.0)`
```
   Gecko/20100101 Firefox/50.0

```
**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)`
```
   AppleWebKit/537.36 (KHTML, like Gecko)
   Chrome/51.0.2704.84 Safari/537.36

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The TLS cipher suite used for the login. Values are OpenSSL-style cipher suite names, with
[hyphen delimiters. For more information, see OpenSSL Cryptography and SSL/TLS Toolkit.](https://www.openssl.org/source/)

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
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and DatabaseTotalTime. Compare this field to `CpuTime`
to determine whether performance issues are occurring in the database layer or in your own
code.

**Type**
string


-----

```
LoginKey
LoginStatus
LoginSubType
LoginType

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

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
double

**Properties**
Filter, Nillable, Sort

**Description**
The status of the login attempt. For successful logins, the value is LOGIN_NO_ERROR. All
other values indicate errors or authentication issues. For details, see Login Event Type —
LOGIN_STATUS Values on page 2184.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login flow used. Possible values are:

**•** uiup—UI Username-Password

**•** oauthpassword—OAuth Username-Password

**•** oauthtoken—OAuth User-Agent

**•** oauthhybridtoken—OAuth User-Agent for Hybrid Apps

**•** oauthtokenidtoken—OAuth User-Agent with ID Token

**•** oauthclientcredential—OAuth Client Credential

**•** oauthcode—OAuth Web Server

**•** oauthhybridauthcode—OAuth Web Server for Hybrid Apps

**Type**
string


-----

```
RequestIdentifier
RequestStatus

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login used to access the session. Possible values are:

**•** 7—AppExchange

**•** A—Application

**•** s—Certificate-based login

**•** k—Chatter Communities External User

**•** n—Chatter Communities External User Third Party SSO

**•** r—Employee Login to Community

**•** z—Lightning Login

**•** l—Networks Portal API Only

**•** 6—Remote Access Client

**•** i—Remote Access 2.0

**•** I—Other Apex API

**•** R—Partner Product

**•** w—Passwordless Login

**•** 3—Customer Service Portal

**•** q—Partner Portal Third-Party SSO

**•** 9—Partner Portal

**•** 5—SAML Idp Initiated SSO

**•** m—SAML Chatter Communities External User SSO

**•** b—SAML Customer Service Portal SSO

**•** c—SAML Partner Portal SSO

**•** h—SAML Site SSO

**•** 8—SAML Sfdc Initiated SSO

**•** E—SelfService

**•** j—Third Party SSO

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
```
  3nWgxWbDKWWDIk0FKfF5DV.

```
**Type**
string


-----

```
RunTime
SessionKey
SourceIp
Timestamp

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the request for a page view or user interface action.

Possible values are:

**•** `S—Success. Salesforce handled the request successfully. If an Apex controller throws`
an exception, this status is also returned.

**•** `F—Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page`
took too long to render, page is read-only.

**•** `U—Undefined`

**•** `A—Authorization Error`

**•** `R—Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a`
Visualforce page.

**•** `N—Not Found. 404 error.`

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
When a user logs out and logs in again, a new session is started. For Login Event Type, this
field is usually null because the event is captured before a session is created. For example:
```
  d7DEq/ANa7nNZZVD.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source IP of the login request.

**Type**
dateTime


-----

```
TransportLayerSecurityProtocol
Uri
UserIdentifier
UserName
UserType

```

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
The TLS protocol used for the login.

Possible values are:

**•** `1.0`

**•** `1.1`

**•** `1.2`

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username that’s used for login.

**Type**
string


-----

```
Username
