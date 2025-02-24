#### TenantSecurityHealthCheckBaselineTrend

Stores metric details related to Health Check baseline settings. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get details about which metrics are collected and for which tenants, and
changes made to the Health Check baseline. This object is available to Security Center subscribers in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Action
ActionBy
ActionDate
ApiName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of action. For example, added, updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user or admin that made the change.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the change.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
BaselineDescription
BaselineIdentifier
BaselineName
DetailIdentifier
IsDefault
MetricIdentifier

```

**Description**
The name of the metric used by the API and managed packages.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For custom baselines, the name of the custom baseline file.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the baseline.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the baseline.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the baseline is default or custom. The default is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
MetricsType
Name
Tenant
TenantName

##### Associated Objects

```

**Description**
The ID of the type of metric collected.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of data collected. For example, SecurityHealthCheckBaselineMetric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant that was scored by the Security Health Check.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant that was scored by the Security Health Check.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckBaselineTrendChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityHealthCheckBaselineTrendFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityHealthCheckBaselineTrendHistory on page 62**
History is available for tracked fields of the object.


-----

**TenantSecurityHealthCheckBaselineTrendOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityHealthCheckBaselineTrendShare on page 66**
Sharing is available for the object.
