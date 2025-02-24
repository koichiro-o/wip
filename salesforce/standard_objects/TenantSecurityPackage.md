#### TenantSecurityPackage

Stores details about managed and unmanaged packages that are added, updated, or removed from a tenant in Security Center. Use this
object to identify whether new packages are installed, upgraded, or uninstalled from your connected tenants. This object is available to
Security Center subscribers in API version 53.0 and later.

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
ActionDate
AppExchangeReady
DetailIdentifier
InstalledBy
MetricIdentifier

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on a package within a tenant. The options are:

**•** `Added`

**•** `Removed`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the action was taken.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the package has passed AppExchange review.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the individual detail record. This field is unique within your org.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user that installed the package.

**Type**
string


-----

```
MetricsType
Name
NamespacePrefix
PackageName
Publisher
ReleaseStatus

```

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
The namespace prefix associated with the package.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the package being added to or removed from the tenant.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the publisher that created the package.

**Type**
string


-----

```
Tenant
TenantName
Version

##### Associated Objects

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The release status of the package. The options are:

**•** `Beta`

**•** `Released`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant that the package was added to or removed from.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that the package was added to or removed from.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The current version of the package.


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


-----

**TenantSecurityPackageShare on page 66**
Sharing is available for the object.
