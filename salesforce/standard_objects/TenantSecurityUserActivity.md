#### TenantSecurityUserActivity

Stores details related to how a user interacts with a tenant. Use this object to determine whether to reevaluate a user’s access to your
org for security purposes. You can check whether a user has never logged in, hasn’t been active for 90 days, has a frozen account, or
isn’t using multi-factor authentication. This object is available to Security Center subscribers in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

This object can only be read and queried.

##### Fields

```
DetailIdentifier
LastLoginDate
MetricIdentifier
MetricsType
Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last time the user logged in.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.


-----

```
Tenant
TenantName
UserCreatedDate
UserEmail
UserLicense
Username

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant where the user activity happened.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the user was created.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The license assigned to the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.


-----

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityUserActivityChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityUserActivityFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityUserActivityHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityUserActivityOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityUserActivityShare on page 66**
Sharing is available for the object.
