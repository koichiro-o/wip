#### TenantSecurityApiAnomaly

[Stores detected anomalies in how users typically make API calls. Fore more information, see Threat Detection. This object is available to](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
Security Center subscribers in API version 53.0 and later.

Note: Threat Detection is available only for Event Monitoring subscribers.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.


-----

##### Fields

**Field**
```
DetailIdentifier
EventDate
EventIdentifier
EventName
MetricIdentifier
MetricsType

```

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
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique ID of the event, which is shared with the corresponding storage object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event, which is Api Anomaly.

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


-----

```
Name
Operation
QueriedEntities
RequestIdentifier
RowsProcessed
Score

```

**Description**
The type of data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API call that generated the event. For example, Query.

**Type**
textarea

**Properties**
Nillable

**Description**
The type of entities associated with the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total row count for the current operation.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort


-----

```
SecurityEventData
Summary
Tenant
TenantName
Uri

```

**Description**
A number from 0 through 100 that represents the anomaly score for the API execution or
export tracked by this event. The anomaly score shows how the current API activity differs
from the user’s typical activity. A low score indicates that the user’s current API activity is
similar to the usual activity, and a high score indicates that it’s different.

**Type**
textarea

**Properties**
Nillable

**Description**
The set of features about the API activity that triggered this anomaly event.

For example, a user typically downloads 10 accounts at a time but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows how much as a percentage that the feature contributed to triggering this anomaly
event. The data is in JSON format.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the API anomaly that caused this event.

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


-----

```
UserAgent
UserIdentifier
Username

##### Associated Objects

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp.`

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

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The origin username in the format of user@company.com at the time that the event was
created.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityApiAnomalyChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityApiAnomalyFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityApiAnomalyHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityApiAnomalyOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityApiAnomalyShare on page 66**
Sharing is available for the object.


-----
