#### TenantSecurityLoginIpRangeTrend

Stores details of changes related to login IP ranges in Security Center. This object is available in API version 59.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available only for Security Center subscribers. This object is read-only.

##### Fields

```
Action
ActionBy

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of change made to the login IP range. Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string


-----

```
ActionDate
Description
DetailIdentifier
IpEndAddress
IpRangeIdentifier
IpStartAddress

```

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when this change was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The description of the login IP range record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The end IP address of the login IP range. For example, 10.0.0.0 – 10.255.255.255.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the IP range.

**Type**
string


-----

```
MetricIdentifier
MetricsType
Name
ProfileIdentifier
ProfileName
Tenant

```

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The start IP address of the login IP range. For example, 10.0.0.0 – 10.255.255.255.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the profile that is assigned to this login IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the profile that is assigned to this login IP range.

**Type**
string


-----

```
TenantName

##### Associated Objects

```

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityLoginIpRangeTrendChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityLoginIpRangeTrendFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityLoginIpRangeTrendHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityLoginIpRangeTrendOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityLoginIpRangeTrendShare on page 66**
Sharing is available for the object.
