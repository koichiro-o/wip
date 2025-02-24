#### TenantSecurityHealthCheckTrend

Stores the history of Security Health Check scores for a connected tenant within Security Center. Health Check in Security Center displays
Health Check scores and the average risk settings for all your tenants in one place. This object belongs to the parent tenant and stores
Health Check data pushed from child tenants. This object is available for Security Center subscribers in API version 53.0 and later.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Baseline
HighRisk
Informational
LowRisk
MediumRisk

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The definition of an org’s security settings standards.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data highly sensitive to your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data that isn't sensitive for your company.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data with low sensitivity for your company.

**Type**
int

**Properties**
Filter, Group, Sort


-----

```
Name
ProcessedTime
Score
ScoreDelta
Tenant
TenantOriginalIdentifier

```

**Description**
Indicates that fields with this picklist value contain data with moderate sensitivity for your
company.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant that was scored.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time when the Health Check score was calculated.

**Type**
double

**Properties**
Filter, Sort

**Description**
The summary score that shows how your org measures against a security baseline.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The percentage amount that the Health Check score changed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant that was scored.

**Type**
string


-----

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Health Check Trend record for a tenant. This field is unique within your org.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckTrendChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityHealthCheckTrendFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityHealthCheckTrendHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckTrendOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityHealthCheckTrendShare on page 66**
Sharing is available for the object.
