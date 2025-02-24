#### TenantSecuritySessionHijacking

Stores information about session hijacking events as detected by Threat Detection within connected tenants in Security Center. For
[more information, see Threat Detection. This object is available for Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
CurrentIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
CurrentPlatform
CurrentScreen
CurrentUserAgent
CurrentWindow

```

**Description**
The IP address of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the IP address didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousIp` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The platform of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the platform didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousPlatform` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The screen of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the screen didn’t contribute to the observed fingerprint deviation, the
value of this field is the same as the `PreviousScreen field.`

**Type**
textarea

**Properties**
Nillable

**Description**
The user agent of the observed fingerprint that deviates from the previous fingerprint. The
difference between the current and previous values is one indicator that a session hijacking
attack has occurred. If the user agent didn’t contribute to the observed fingerprint deviation,
the value of this field is the same as the `PreviousUserAgent field.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser window of the observed fingerprint that deviates from the previous fingerprint.
The difference between the current and previous values is one indicator that a session


-----

```
DetailIdentifier
EventDate
EventIdentifier
EventName
MetricIdentifier
MetricsType

```

hijacking attack has occurred. If the window didn’t contribute to the observed fingerprint
deviation, the value of this field is the same as the `PreviousWindow field.`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the hijacking event was reported. For example, 2020-01-20T19:12:26.965Z.
The most granular setting is milliseconds.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Session Hijacking.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist


-----

```
Name
PreviousIp
PreviousPlatform
PreviousScreen
PreviousUserAgent

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the `CurrentIp`
field for the newly observed IP address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The platform of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentPlatform` field for the newly observed platform.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The screen of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentScreen` field for the newly observed screen.

**Type**
textarea


-----

```
PreviousWindow
Score
SecurityEventData

```

**Properties**
Nillable

**Description**
The user agent of the previous fingerprint. The difference between the current and previous
values is one indicator that a session hijacking attack has occurred. See the
`CurrentUserAgent` field for the newly observed user agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The browser window of the previous fingerprint. The difference between the current and
previous values is one indicator that a session hijacking attack has occurred. See the
`CurrentWindow` field for the newly observed window.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Specifies how much the new fingerprint deviates from the previous one. The score is from
6.0 through 21.0. The event exposes five field pairs (such as `CurrentIp` and
```
  PreviousIp) to view the before and after data for browser features that contributed to

```
this anomaly. See the `SecurityEventData` field for all contributing features in JSON
format. A large deviation score (6.0 or more) between two intra-session fingerprints indicates
that two different browsers are active in the same session. The presence of two active browsers
usually means that session hijacking has occurred.

**Type**
textarea

**Properties**
Nillable

**Description**
[The set of browser fingerprint features that triggered this event. See the Threat Detection](https://help.salesforce.com/articleView?id=real_time_em_threat_session.htm&type=5&language=en_US)
[documentation for the possible features. For example, a user’s current browser fingerprint](https://help.salesforce.com/articleView?id=real_time_em_threat_session.htm&type=5&language=en_US)
diverges from the previously known fingerprint. If Salesforce concludes the user’s session
was hijacked, it fires this event, and the contributing features are captured in this field in
JSON format. Each feature describes a browser fingerprint property, such as the browser user
agent, window, or platform. The data includes the current and previous values for each
feature.


-----

```
Summary
Tenant
TenantName
UserIdentifier
Username

```

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the threat that caused this event. The summary lists the browser fingerprint
features that most contributed to the threat detection, along with their contribution to the
total score.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was targeted in the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time that the event was
created.


-----

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecuritySessionHijackingChangeEvent on page 67**
Change events are available for the object.

**TenantSecuritySessionHijackingFeed on page 54**
Feed tracking is available for the object.

**TenantSecuritySessionHijackingHistory on page 62**
History is available for tracked fields of the object.

**TenantSecuritySessionHijackingOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecuritySessionHijackingShare on page 66**
Sharing is available for the object.
