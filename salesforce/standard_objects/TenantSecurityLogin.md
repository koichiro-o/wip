#### TenantSecurityLogin

Stores the login details of a single user to a tenant, grouped by date and type. You can query this object to find out how many times the
user logged in to a specific tenant using a specific login type (for example, username/password or SSO). This object is available to Security
Center subscribers in API version 53.0 and later.

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
LastLoginDate
LoginCount
MetricIdentifier
MetricsType

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
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The number of times the user has logged in to the tenant.

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
The type of data collected.

The supported metric types are:

**•** LOGIN_PWLESS

**•** LOGIN_PWLESS2FA

**•** LOGIN_UNPW

**•** LOGIN_UNPW2FA


-----

```
Name
Tenant
TenantName
UserEmail
Username

```


**•** LOGIN_SSO

**•** LOGIN_SSO2FA

**•** LOGIN_OAUTH

**•** LOGIN_OAUTH2FA

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that was scored.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that was scored.

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
The user’s org username.


-----

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityLoginChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityLoginFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityLoginHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityLoginOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityLoginShare on page 66**
Sharing is available for the object.
