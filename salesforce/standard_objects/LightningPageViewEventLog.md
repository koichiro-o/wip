#### LightningPageViewEventLog

Lightning Page View event logs represent information about the page on which the event occurred in Lightning Experience and the
Salesforce mobile app. A Lightning Page View event log tracks the page a user visited, how long the user spent on the page, and the
load time for the page. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

```

-----

##### Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
AppName
BrowserName
BrowserVersion
ClientGeolocation
ClientIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the application that the user accessed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the browser that the user accessed. For example: Chrome, IE, Safari, Gecko.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The geolocation of the client in the form of <Country>/<State|Province>. For example:
```
  United States/California.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.


-----

```
ClientIp
ConnectionType
DeviceIdentifier
DeviceModel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
IP address of the client employing salesforce.com services.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of connection.

Possible values are:

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier used to identify a device when tracking events. DeviceIdentifier
is a generated value that’s created when the mobile app is initially run after installation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DevicePlatform
DeviceSessionIdentifier
DoesEffectivePageTimeDeviate

```

**Description**
The name of the device model. For example: `iPad,` `iPhone.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of application experience in name:experience:form format. Possible values
are:

Name

**•** `APP_BUILDER`

**•** `CUSTOM`

**•** `S1`

**•** `SFX`

Experience

**•** `BROWSER`

**•** `HYBRID`

Form

**•** `DESKTOP`

**•** `PHONE`

**•** `TABLET`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started. For example:
```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0.

```
**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When a deviation is detected, `DoesEffectivePageTimeDeviate` records `true.`
The default value is `false.`


-----

```
Duration
EffectivePageTime
EffectivePageTimeErrorType
EffectivePageTimeReason
GrandparentUiElement

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The duration in milliseconds since the page start time.

This field is being deprecated. Use `EffectivePageTime` instead.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how many milliseconds it took for the page to load before a user could interact
with the page’s functionality. Multiple factors can affect effective page time, such as network
speed, hardware performance, or page complexity. If an effective page time greater than 60
seconds is detected, the value of this field is set to `null` or `0.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the origin of an error. This field is populated when
EFFECTIVE_PAGE_TIME_DEVIATION_REASON contains the PAGE_HAS_ERROR value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason for deviation in page loading time.

Examples of possible values include:

**•** `PageInDom- The page was loaded from a cache`

**•** `PageHasError- An undefined page loading error occurred.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
LoginKey
MobileSdkAppType
MobileSdkVersion
OperatingSystemName
OperatingSystemVersion

```

**Description**
The grandparent scope of the page element where the event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring. For example:
```
  GeJCsym5eyvtEK2I.

```
**Type**
String

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
String

**Description**
The mobile SDK application version number.

**Example**
5.0

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system name, derived from `UserAgent. For example:` `Android,` `iOS,`
```
  OSX, Windows.

```
**Type**
string


-----

```
PageAppName
PageContext
PageObjectIdentifier
PageObjectType
PageStartTime

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating system version, derived from `UserAgent.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the application that the user accessed from the App Launcher. For
example: `LightningSales.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the component hosting the main content of the page. For example:
```
  clients:cardsContainer.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique entity identifier of the event. For example: `0013000000I3zJAAAZ.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object type of the event. For example: `task,` `contacts.`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time when the page was initially loaded, measured in milliseconds. For example:
```
  1471564788642.

```

-----

```
PageUrl
ParentUiElement
PreviousPageAppName
PreviousPageContext
PreviousPageObjectIdentifier
PreviousPageObjectType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PageUrl. For example:`
```
  /sObject/0064100000JXITSAA5/view.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent scope of the page element where the event occurred.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The internal name of the previous application that the user accessed from the App Launcher.
For example: `LightningSales.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context of the previous page where the event occurred. For example:
```
  clients:cardsContainer.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique previous page object identifier of the event.

**Type**
string


-----

```
PreviousPageUrl
RequestIdentifier
SdkAppVersion
SessionKey
TargetUiElement

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The previous page object type of the event. For example: `task,` `contacts.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened. For example: `/sObject/006410000.`

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SDK application version number. For example: `5.0.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started. For example: `cdd09305cb6babf34059e27f70e47f1b11dec868.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Timestamp
UiEventSequenceNumber
UiEventTimestamp
UserAgent
UserIdentifier

```

**Description**
The target page element where the event occurred. For example: `label bBody`
```
  truncate, tabitem-link.

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
An auto-incremented sequence number of the current event since the session started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The numeric code for the type of client used to make the request (for example, the browser,
application, or API) as a string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API. For
example: `00530000009M943.`


-----

```
UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

Possible values are:

**•** `A: Automated Process`

**•** `b: High Volume Portal`

**•** `C: Customer Portal User`

**•** `D: External Who`

**•** `F: Self Service`

**•** `G: Guest`

**•** `L: Package License Manager`

**•** `N: Salesforce to Salesforce`

**•** `n: CSN Only`

**•** `O: Power Custom`

**•** `o: Custom`

**•** `P: Partner`

**•** `p: Customer Portal Manager`

**•** `S: Standard`

**•** `X: Salesforce Administrator`

