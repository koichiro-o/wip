#### UserAuthCertificate

Represents a user authentication certificate in your org. A user certificate is a unique PEM-encoded X.509 digital certificate to authenticate
individual users to your org. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is only available in orgs with Let users authenticate with a certificate enabled in Identity Verification.
Only users with the Manage Internal Users permission can access this object.


-----

##### Fields

**Field**
```
CertificateChain
CertificateChainLength
DeveloperName
ExpirationDate
Fingerprint

```

**Type**
base64

**Properties**
Create, Update

**Description**
The uploaded PEM files can contain a single certificate or up to 10 certificates in a certificate
chain. Uploaded PEM files can’t be larger than 1 MB.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-generated length of the certificate or certificate chain in the uploaded PEM file.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
When creating large sets of data, always specify a unique `DeveloperName for each`
record. If no `DeveloperName is specified, Salesforce generates one for each record,`
which slows performance.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The expiration date of the uploaded certificate.

**Type**
string

**Properties**
Filter. Group, idLookup, Sort


-----

```
Language
MasterLabel
SerialNumber

```

**Description**
The unique fingerprint of the uploaded certificate.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language in which to display the certificate.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexico)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazil)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A descriptive name for the certificate.

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
UserID

```

**Description**
The serial number of the uploaded certificate.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The user associated with the certificate.

