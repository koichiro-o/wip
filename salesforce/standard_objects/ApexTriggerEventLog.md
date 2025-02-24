#### ApexTriggerEventLog

Apex Trigger event logs contain details about triggers that fire in an organization. This object is available in API version 55.0 and later.


-----

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

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
DatabaseTotalTime
ExecutionTime

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
double

**Properties**
Filter, Nillable, Sort

**Description**
Time (in milliseconds) spent waiting for database processing in aggregate for all operations
in the request. Compare this field to `CpuTime` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
LoginKey
ObjectName
RequestIdentifier
RequestStatus

```

**Description**
The end-to-end Apex execution time (in milliseconds).

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
The name of the object affected by the trigger.

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


-----

```
RunTime
SessionKey
Timestamp
TriggerIdentifier
TriggerName

```

This field can have a blank value.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered long-running requests for the purposes
of the Concurrent Long-Running Apex Limit.

HTTP callout processing time isn't included when calculating the 5-second limit. We pause
the timer for the callout and resume it when the callout completes.

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
The 15-character ID of the trigger that was fired.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
TriggerType
Uri
UserIdentifier
UserType

```

**Description**
For triggers coming from managed packages, TriggerName includes a namespace prefix
separated with a `.` character. If no namespace prefix is present, the trigger is from an
unmanaged trigger. For example:

**•** `examplePackage.managedExampleTrigger—Managed trigger from the`
examplePackage namespace

**•** `unmanagedExampleTrigger—Unmanaged trigger`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of this trigger.

Possible values are:

**•** AfterInsert

**•** AfterUpdate

**•** BeforeInsert

**•** BeforeUpdate

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
The category of user license.


-----

Possible values are:

**•** `CsnOnly—Users whose access to the application is limited to Chatter. This user type`
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal—CSP Lite Portal license. Users whose access is limited because`
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

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
