#### TenantSecurityTenantInfo

Stores information on changes related to the tenant history. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read only.

##### Fields

```
DetailIdentifier
Instance

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique identifier for this record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
MyDomainName
Name
SandboxAlias
SandboxType
Status
Tenant

```

**Description**
The instance that the tenant is being hosted on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the domain for this tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which the data is being collected.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The alias specified by the user when the user creates a Sandbox.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type specified by the user when the user creates a Sandbox.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The status of the tenant. For example, active or inactive.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
TenantName
TenantType

##### Usage

 Associated Objects

```

**Description**
The ID of the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The type of tenant in this org.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityTenantInfoChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityTenantInfoFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityTenantInfoHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityTenantInfoOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityTenantInfoShare on page 66**
Sharing is available for the object.
