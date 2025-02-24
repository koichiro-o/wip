#### TenantSecurityCredentialStuffing

[Stores when a user successfully logs in to Salesforce during an identified credential stuffing attack. For more information, see Threat](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
[Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

Note: Threat Detection is available only for Event Monitoring subscribers.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
AcceptLanguage
DetailIdentifier
EventDate
EventIdentifier
EventName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
List of HTTP headers that specify the natural language, such as English, that the client
understands.

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
Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event.

**Type**
string


-----

```
LoginType
LoginUrl
MetricIdentifier
MetricsType
Name

```

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Credential Stuffing.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login used to access the session. For the list of possible values, see the LoginType
[field of LoginHistory in the Object Reference.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the login page. For example, `login.salesforce.com.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.


-----

```
Score
Summary
Tenant
TenantName
UserAgent
UserIdentifier

```

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
Indicates that a user successfully logged in to Salesforce during an identified credential
stuffing attack. The value of this field is always 1.

**Type**
textarea

**Properties**
Nillable

**Description**
A summary of the threat that caused this event to be created.

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
textarea

**Properties**
Nillable

**Description**
UserAgent used in the HTTP request, post-processed by the server.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Username

##### Associated Objects

```

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time the event was created.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityCredentialStuffingChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityCredentialStuffingFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityCredentialStuffingHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityCredentialStuffingOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityCredentialStuffingShare on page 66**
Sharing is available for the object.
