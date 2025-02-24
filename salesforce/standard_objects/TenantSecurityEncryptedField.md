#### TenantSecurityEncryptedField

Represents fields encrypted under your Shield Platform Encryption policy. This object is available in API version 61.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Action

```

**Type**
string


-----

```
ActionBy
ActionDate
DetailIdentifier
EncryptionType
FieldName

```

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

**Description**
This field is reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the change to the tenant encryption policy status was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of encryption for the field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
FieldType
MetricIdentifier
MetricsType
Name
ObjectName
Tenant

```

**Description**
The name of the encrypted field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of field being encrypted.

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
Filter, Group, Nillable, Sort

**Description**
The name of the object for this encrypted field.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
TenantName

```

**Description**
The ID of the tenant with Shield Encryption.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tenant that this record is for.

