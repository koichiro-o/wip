#### TenantSecurityEncryptionPolicy

Stores tenant encryption policy status. This object is available in API version 58.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

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
The action taken on the encryption policy within a tenant. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
ActionDate
DetailIdentifier
MetricIdentifier
MetricsType
Name
PolicyName

```

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the change to the tenant encryption policy status was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of encryption policy collected by this metric.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
PolicyStatus
Tenant
TenantName

```

**Description**
The name of the policy.

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Status of the policy. Possible values are:

**•** `-1—No license.`

**•** `0—Not Enabled.`

**•** `-1—Enabled`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with Shield Encryption.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant that this record is for.

