#### TenantSecurityMobilePolicyTrend

Stores metrics related to changes in mobile security policies across all tenants in Security Center. This object is available to Security Center
subscribers in API version 54.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object can only be read and queried.


-----

##### Fields

**Field**
```
Action
ActionBy
ActionDate
ConnectedApp
DetailIdentifier
EffectiveDate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The change made to the mobile security policy. For example, a new policy was added,
updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The user who made the change.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the mobile security policy change.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The app that is associated with the mobile security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
IsEnabled
MetricIdentifier
MetricsType
MobilePlatform
Name
PolicyType

```

**Description**
The date a mobile security policy is enforced.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A value indicating whether the mobile security policy is enabled. The default is `false,`
which means policies are disabled.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The foreign key of the metric.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of mobile security policy data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The mobile operating system of the mobile security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for which data is collected.

**Type**
string


-----

```
RuleValue
RuleValueType
SeverityLevel
Tenant
TenantName

```

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of mobile security policy. For example, Block Calendar.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The value of the security notification rule.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of rule value. For example, boolean or text.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The severity level of the security threat. For example, `CRITICAL.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant.


-----

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPackageChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityPackageFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityPackageHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityPackageOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityPackageShare on page 66**
Sharing is available for the object.
