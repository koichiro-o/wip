#### TenantSecurityTrustedIpRangeTrend

Stores details of changes related to trusted IP ranges in Security Center.This object is available for Security Center subscribers in API
version 54.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Action

```

**Type**
string


-----

```
ActionBy
ActionDate
Description
DetailIdentifier
IpEndAddress

```

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Stores information on a change to the policy. Available options include:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this change was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A description of the trusted IP range. For example, "Trusting the IP addresses from NA-West
region".

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
IpRangeIdentifier
IpStartAddress
MetricIdentifier
MetricsType
Name
Tenant

```

**Description**
The end IP address of a trusted IP range. For example, 10.0.0.0 – 10.255.255.255.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the IP range.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The start IP address of a trusted IP range. For example, 10.0.0.0 – 10.255.255.255.

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


-----

```
TenantName
UsageOptions

##### Associated Objects

```

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityTrustedIpRangeTrendChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityTrustedIpRangeTrendFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityTrustedIpRangeTrendHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityTrustedIpRangeTrendOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityTrustedIpRangeTrendShare on page 66**
Sharing is available for the object.
