#### TenantSecurityHealthCheckDetail

Stores the details of Health Check scores for a connected tenant. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get settings and risks per tenant on a selected date. This object is available
to Security Center subscribers in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
HealthCheckSettingIdentifier
HealthCheckTrendKey
Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Health Check setting. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Health Check trend related to the Health Check detail records.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant that was scored.


-----

```
OrgValue
RiskType
Setting
SettingGroup
SettingRiskCategory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org’s value for the security setting.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The level of risk of the org’s security setting value.

Possible values are:

**•** `HIGH_RISK`

**•** `MEDIUM_RISK`

**•** `MEETS_STANDARD`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the security setting. For example, Minimum Password Length.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the security setting group in Setup that this setting is in. For example, Password
Policies.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The level of risk of the org’s security settings.

Possible values are:

**•** `HIGH_RISK`


-----

```
StandardValue
Tenant

##### Associated Objects

```


**•** `INFORMATIONAL`

**•** `LOW_RISK`

**•** `MEDIUM_RISK`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The recommended standard value for the security setting.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the tenant that was scored.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityHealthCheckDetailChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityHealthCheckDetailFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityHealthCheckDetailHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityHealthCheckDetailOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityHealthCheckDetailShare on page 66**
Sharing is available for the object.
