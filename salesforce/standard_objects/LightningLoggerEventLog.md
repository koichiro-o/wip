#### LightningLoggerEventLog

Lightning Logger Event Log provides information from observed Lightning component logs. This object is available in API version 61.0
and later.

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
AppName
BrowserName
BrowserVersion
ClientGeolocation
ClientIdentifier
ClientIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s browser version in major.minor format. Some browsers don’t provide a minor
version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of <Country>/<State|Province>.

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
ConnectionType
DeviceModel
DevicePlatform

```

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.Possible values are:

**•** CDMA1x

**•** CDMA

**•** EDGE

**•** EVDO0

**•** EVDOA

**•** EVDOB

**•** GPRS

**•** HRPD

**•** HSDPA

**•** HSUPA

**•** LTE

**•** WIFI

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the device model. For example: iPad, iPhone.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in name:experience:form format. Possible values are:

Name

**•** APP_BUILDER

**•** CUSTOM

**•** S1


-----

```
DeviceSessionIdentifier
LoginKey
Message
MobileSdkAppType

```


**•** SFX

Experience

**•** BROWSER

**•** HYBRID

Form

**•** DESKTOP

**•** PHONE

**•** TABLET

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session is based on page load time. When the user reloads
a page, a new session starts. For example: 321a1ddfaf924803a075f1e69fc87bc06f53ccd0

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
Filter, Nillable, Sort

**Description**
The message is passed to the lightning/logger log() method. The message can
be a JSON object or a string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application type. Possible Values:

**•** HYBRID


-----

```
MobileSdkVersion
OperatingSystemName
OperatingSystemVersion
PageContext
PageObjectIdentifier

```


**•** HYBRIDLOCAL

**•** HYBRIDREMOTE

**•** NATIVE

**•** REACTNATIVE

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile SDK application version number. For example, 5.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from the `User Agent. For example:`

**•** Android

**•** iOS

**•** OSX

**•** Windows

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from the `User Agent.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page. For example:
clients:cardsContainer.

**Type**
string


-----

```
PageObjectType
PageUrl
RequestIdentifier
SdkAppVersion
SessionKey

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique entity identifier of the event. For example: 0013000000I3zJAAAZ.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event. For example: task, contacts.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PageUrl. For example: /sObject/0064100000JXITSAA5/view.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app version used in this request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Timestamp
UiEventRelativeTimestamp
UiEventTimestamp
UiRootActivityIdentifier
UserIdentifier

```

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
double

**Properties**
Filter, Nillable, Sort

**Description**
Difference in milliseconds between when the message was logged and when the browser
tab was opened.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds when this event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the root activity, if any, when this message was logged.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
  00530000009M943.

```

-----

```
UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of user employing Salesforce services, whether through the UI or API.

