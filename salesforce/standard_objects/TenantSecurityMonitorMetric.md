#### TenantSecurityMonitorMetric

Stores the daily count and daily count change for a metric within Security Center. This object is available to Security Center subscribers
in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
ChangeCount
Count

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
How much the relevant metric changed.

**Type**
int

**Properties**
Filter, Group, Sort


-----

```
EndProcessTime
MetricIdentifier
MetricsType
Name
PreviousMetricIdentifier
StartProcessTime

```

**Description**
The current metric count.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the metric count process ended.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the type of metric counted. This field is unique within your organization.

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
The name of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The previous ID of the type of metric that was counted. This field is unique within your
organization.

**Type**
dateTime


-----

```
Tenant

##### Associated Objects

```

**Properties**
Filter, Sort

**Description**
The date and time that the metric count process started.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was scored.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityMonitorMetricChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityMonitorMetricFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityMonitorMetricHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityMonitorMetricOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityMonitorMetricShare on page 66**
Sharing is available for the object.
