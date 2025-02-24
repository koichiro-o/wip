#### AnalyticsDownloadEventLog

AnalyticsDownloadEventLog represent downloads made from lens and dashboard in the CRM Analytics. This object is available in API
version 61.0 and later.


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
AssetIdentifier
AssetType
ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a particular session of CRM Analytics. Use this field to determine which log lines
originated from a particular session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when this log line was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset ID from the user download.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset type from the user download.

**Type**
string


-----

```
CpuTime
DatasetIdentifiers
DownloadFormat
LoginKey
RecordCount

```

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
A comma-separated list of used dataset IDs.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The format of the data for export.

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
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
RequestIdentifier
RunTime
SessionKey
Timestamp
Uri

```

**Description**
The number of records exported.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Globally unique identifier for a given request.

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
The URI of the page that’s receiving the request. For example: /home/home.jsp.


-----

```
UserIdentifier
UserType

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

