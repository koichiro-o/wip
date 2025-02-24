#### TenantSecurityReportAnomaly

Stores anomalies in how users run or export reports, including unsaved reports, as detected by Threat Detection. For more information,
[see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

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
DetailIdentifier
EventDate
EventIdentifier
EventName
MetricIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the detail record. This field is unique within your org.

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
The name of the event, which is Report Anomaly.

**Type**
string


-----

```
MetricsType
Name
Report
Score
SecurityEventData

```

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

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
The ID for the report for which this anomaly event was detected. If the anomaly resulted
from a user executing an unsaved report, the value of this field is null.

**Type**
double

**Properties**
Filter, idLookup, Nillable, Sort

**Description**
A number from 0 through 100 that represents the anomaly score for the report execution
or export tracked by this event. The anomaly score indicates how the user’s current report
activity differs from their typical activity. A low score indicates that the current report activity
is similar to the user’s usual activity. A high score indicates that it’s different.

**Type**
textarea

**Properties**
Nillable


-----

```
Summary
Tenant
TenantName
UserIdentifier
Username

```

**Description**
The set of features about the report activity that triggered this anomaly event.

For example, a user typically downloads 10 accounts at a time, but then deviates from that
pattern and downloads 1,000 accounts. This event is triggered, and the contributing features
are captured in this field. Potential features include row count, column count, average row
size, day of week, and the browser’s user agent used for the report activity. The data captured
also shows as a percentage how much a particular feature contributed to this anomaly event.
The data is in JSON format.

**Type**
textarea

**Properties**
Nillable

**Description**
A text summary of the report anomaly that caused this event.

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


-----

**Description**
The origin username in the format of user@company.com at the time the event was created.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityReportAnomalyChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityReportAnomalyFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityReportAnomalyHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityReportAnomalyOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityReportAnomalyShare on page 66**
Sharing is available for the object.
