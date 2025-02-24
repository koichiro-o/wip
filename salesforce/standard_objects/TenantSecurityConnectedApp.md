#### TenantSecurityConnectedApp

Stores the details for a connected app that was added to or removed from a Security Center tenant. This object is available to Security
Center subscribers in API version 53.0 and later.

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
The action taken on the connected app within a tenant.

Possible values are:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who performed the action on the connected app.


-----

```
ActionDate
AppName
AuthorizedBy
AuthorizedDate
DetailIdentifier
LastUsedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the action was taken.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the connected app.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user who authorized the connected app to be installed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the connected app was authorized for installation.

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
The last date that the connected app was used for authentication.


-----

```
MetricIdentifier
MetricsType
Name
Publisher
Scope
Tenant

```

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents if the relevant tenant is the original publisher of the connected app for all
connected tenants in the org.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The scope or scopes assigned to the connected app. A scope defines the type of protected
resource that the connected app can access.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
TenantName
Version

##### Associated Objects

```

**Description**
The ID of the relevant tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that the connected app is connected to.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The current version of the connected app.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityConnectedAppChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityConnectedAppFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityConnectedAppHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityConnectedAppOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityConnectedAppShare on page 66**
Sharing is available for the object.
