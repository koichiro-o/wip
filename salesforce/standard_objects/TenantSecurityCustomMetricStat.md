#### TenantSecurityCustomMetricStat

Represents custom metric data within Security Center. This object is available in API version 61.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
ChangeCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this metric was changed.


-----

```
CustomMetricIdentifier
EndProcessTime
MetricCount
MetricIdentifier
MetricName
Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the custom metric.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The end time of the metric being processed.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of times this metric was recorded.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique identifier of the metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the custom metric.


-----

```
PreviousMetricIdentifier
StartProcessTime
Tenant

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The previous unique identifier of this metric.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The start time of the metric being processed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant with the custom metric.

