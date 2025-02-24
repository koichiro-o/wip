#### TenantSecurityFeature

Stores org features across all tenants in Security Center. This object is available in API version 57.0 and later.

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
FeatureDescription
FeatureName
IsEnabled
MetricIdentifier
MetricsType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique across all tenants.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the feature.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the feature.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feature is enabled or disabled.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
picklist


-----

```
Name
Tenant
TenantName

##### Associated Objects

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of feature collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the feature for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant where the feature was applied.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the connected tenant where the feature was enabled or disabled.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityFeatureChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityFeatureFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityFeatureHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityFeatureOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityFeatureShare on page 66**
Sharing is available for the object.


-----
