#### TenantSecurityCertificate

Stores metric details related to public key certificate information. The certificate binds the public key to the identity of an entity. This
object is available in API version 63.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read only.

##### Fields

```
Action
ActionBy
ActionDate
CertCreatedDate

```

**Type**
String

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The action taken on this certificate. Possible values are:

**•** `Added`

**•** `Removed`

**•** `Updated`

**Type**
String

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The user who made this change.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action was taken.

**Type**
dateTime


-----

```
DetailIdentifier
ExpirationDate
IsActive
IsCaSigned
IsPlatformEncrypted
IsPrivateKeyExportable

```

**Properties**
Filter, Nillable, Sort

**Description**
When this certificate was created.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the individual detail record. This field is unique within your organization.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When this certificate expires.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate is active.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate is signed by the issuer (true) or not (false).

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Whether this certificate is encrypted with Platform Encryption.

**Type**
boolean


-----

```
KeySize
MetricIdentfier
MetricsType
Name
Tenant
TenantName

```

**Properties**
Filter, Group, Sort

**Description**
Indicates whether this certificate’s private key is exportable.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the public key.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
The type of data being collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A user-friendly name for the certificate.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant with this certificate.

**Type**
string


-----

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant with this certificate.
