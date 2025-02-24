#### TenantSecurityLicense

Stores license usage information within Security Center. This object is available in API version 59.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available only for Security Center subscribers. This object is read-only.

##### Fields

```
Action

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
ActionDate
DetailIdentifier
ExpirationDate
MetricIdentifier
MetricsType

```

**Description**
The type of change made to the license. Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

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
The unique identifier for this detail record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which this license expires.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of license collected by this metric.


-----

```
Name
Status
Tenant
TenantName
TotalLicenses
UsedLicenses

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the license.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The status of the license.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this license.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant with this license.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The total number of licenses.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of used licenses.


-----

```
UsedLicensesLastUpdated

##### Associated Objects

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the used licenses were last updated for this tenant.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityLicenseChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityLicenseFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityLicenseHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityLicenseOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityLicenseShare on page 66**
Sharing is available for the object.
