#### TenantSecurityUserPerm

Stores information on permissions assigned to a user. Use this object to see which tenants a user is assigned to. This object is available
to Security Center subscribers in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object can only be read and queried.

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
The action taken regarding the user’s permission. The options are:

**•** `Added`

**•** `Removed`

**Type**
string


-----

```
ActionDate
Context
ContextType
DetailIdentifier
MetricIdentifier

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the permission action was taken.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the profile or permission set assigned to the user.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Indicates the method through which the permission was granted. The options are:

**•** `Permission Set`

**•** `Profile`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted.


-----

```
MetricsType
Name
Tenant
TenantName
UserEmail
UserLicense

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of metric that the assigned permission represents.

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
The ID of the tenant where the user permission was applied.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the connected tenant where the user permission was applied.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s email address.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The license assigned to the user.


-----

```
Username

##### Associated Objects

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user’s org username.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityUserPermChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityUserPermFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityUserPermHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityUserPermOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityUserPermShare on page 66**
Sharing is available for the object.
