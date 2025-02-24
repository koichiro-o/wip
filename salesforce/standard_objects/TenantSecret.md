#### TenantSecret

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax treatment’s parent tax policy. A tax policy is a group of tax treatments, where each
treatment represents a rule for how to invoice a customer for an order item. Tax policies are
related to products, which pass the policy on to the resulting order items. When you activate
an order, Subscription Management assigns a tax treatment to each order item based on
the tax policy's DefaultTaxTreatmentId, then uses the tax treatment to calculate tax.

This field is a relationship field.

**Relationship Name**
TaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy


This object stores an encrypted organization-specific key fragment that’s used with the primary secret (KDF seed) to produce org-specific
data encryption keys. This object is available in API version 34.0 and later.

You can rotate tenant secrets of the `Data` type once every four hours in a sandbox org or every 24 hours in production orgs. You can
rotate tenant secrets of the `SearchIndex` type one time every seven days.

Note: This information is about Shield Platform Encryption and not Classic Encryption.

##### Supported Calls
```
create(), query(), retrieve(), update()

 Fields

```
```
Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
KeyDerivationMode
RemoteKeyCertificate
RemoteKeyIdentifier
RemoteKeyServiceID

```

**Description**

The description of the tenant secret.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The key derivation mode applied to customer-supplied key material. Modes are:

**PBKDF2**
The customer-supplied key material is used by the Shield KMS to create a
derived data encryption key.

**NONE**
The customer-supplied key material is used by the Shield KMS as the final
data encryption key to directly encrypt and decrypt data.

Available in API version 43.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the certificate whose public key is used to encrypt the
`SecretValue` during a remote key callout.

Available in API version 45.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique key identifier for key material fetched from a remote key service.

Available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The named credential used to fetch remote key material from a remote key
service.


-----

```
SecretValue
SecretValueCertificate
SecretValueHash
Source

```

Available in API version 45.0 and later.

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**

The encrypted 256-bit secret value encoded in base64.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The certificate needed to upload a customer-supplied tenant secret. Each
certificate has a unique name.

**Type**
base64

**Properties**
Create

**Description**

The matching tenant secret hash for an uploaded customer-supplied tenant
secret.

**Type**
picklist

**Properties**
Create, Default on create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the encryption key material. Values are:

**HSM**
A Salesforce-generated tenant secret.

**Uploaded**
A customer-supplied tenant secret or data encryption key.

**Remote**
A tenant secret or data encryption key fetched from a key service outside of
Salesforce. Available in API version 44.0 and later.Tenant secrets with a
`Source` value of Remote are listed as Fetched on the Key Management
page in Setup.

Available in API version 43.0 and later.


-----

```
Status
Type
Version

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The status of the tenant secret. Values are:

**Active**
Can be used to encrypt and decrypt new or existing data.

**Archived**
Can’t encrypt new data. Can be used to decrypt data previously encrypted
with this key when it was active.

**Destroyed**
Can’t encrypt or decrypt data. Data encrypted with this key when it was active
can no longer be decrypted. Files and attachments encrypted with this key
can no longer be downloaded.

You can update the `Status` field through the API in versions 44.0 or later.

**Type**
picklist

**Properties**
Create, Default on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of tenant secret. The `Type` field is available in API version 39.0 and
later. The following values appear in the `Type` picklist:

**•** `Analytics—CRM Analytics data (available in API version 39.0 and later).`

**•** `Data—data stored in the Salesforce database. Includes data in encrypted`
fields, files, and attachments but not search index files. Tenant secrets created
in API version 34.0 and later default to the `Data` type.

**•** `Database—transactional database including standard and custom fields,`
metadata, and Apex (available in API version 62.0 and later).

**•** `DeterministicData—data stored in the Salesforce database. Includes`
data in encrypted fields, files, and attachments, but not search index files
(available in API version 39.0 and later).

**•** `EventBus—Change Data Capture event data (available in API version 43.0`
and later).

**•** `SearchIndex—search index files (available in API version 39.0 and later).`

**Type**
int

**Properties**
Filter, Group, idLookup, Sort


-----

**Description**

The version number of this secret. The version number is unique within your org.

##### Usage

Use this object to create or update an org-specific tenant secret or customer-supplied key material.

**Example 1: Build an automated tenant secret creation and activation solution similar to the following.**

**1. Start by creating an Apex class to create the tenant secret. Specify the value of the tenant secret to encrypt data of a particular type.**
```
  global class CreateNewSecret implements Schedulable {
    global void execute(SchedulableContext SC) {
      TenantSecret secret = new TenantSecret ();
      secret.description = 'Created new secret from scheduled job';
      secret.type= 'SearchIndex';
      insert secret;
    }
  }

```
Note: `Type` is available in API version 39.0 and later. `Type` is optional; all tenant secrets default to the `Data` type.

**2. Schedule the Apex class to run at the specified interval.**

This Apex code only needs to be run a single time to schedule the job. This code runs the job every 90 days.
```
  CreateNewSecret secret = new CreateNewSecret();
  String schedule = '0 0 0 1 JAN,APR,JUL,OCT ?';
  String jobID = system.schedule('Automated secret creation and activation', schedule,
  secret);

```
**3. Validate that the job is scheduled.**

**4. Validate that tenant secrets are created after the job is run.**

**Example 2: Upload a customer-supplied tenant secret or customer-supplied data encryption key.**

**[1. Create a certificate that’s compatible with customer-supplied key material. See Generate a BYOK-Compatible Certificate in Salesforce](https://help.salesforce.com/articleView?id=security_pe_byok_generate_cert.htm&language=en_US)**
Help.

**2. Then upload your matching key material and key material hash. Include the unique name of the compatible certificate. The key**
material is uploaded in encrypted form.


-----

[You can use this script to generate a customer-supplied tenant secret and tenant secret hash.](https://help.salesforce.com/articleView?id=byok-script&type=1&language=en_US)

**3. Validate that the key material is uploaded.**

**Example 3: Opt out of key derivation on a key-by-key basis when you upload key material. When you upload your key material, specify**
`'Source':Uploaded` and `'KeyDerivationMode':'NONE', and set non-null values for the SecretValueCertificate,`
SecretValue, and SecretValueHash.

**Example 4: Import a tenant secret of the** `Data` type.
```
TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];
secret.SecretValue = "<previously_exported_secret_as_a_String>";
update secret;

```
**Example 5: Export a tenant secret by writing the** `secret.SecretValue` to a file. Here’s an example that uses a tenant secret of
the `SearchIndex` type.
```
TenantSecret secret = [SELECT SecretValue FROM TenantSecret WHERE Type = 'TenantSecret'
AND Version = 2];
secret.SecretValue =...;
update secret;

```
**Example 6: Destroy a tenant secret of the** `Data` type.

Warning: Your tenant secret is unique to your organization and to the specific data to which it applies. When you destroy a
tenant secret, related data isn’t accessible unless you previously exported the key and then import the key back into Salesforce.
```
TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];
secret.SecretValue = NULL;
secret.Status = Destroyed;
update secret;

```
**Example 7: Change the Status** of a tenant secret from Archived to Destroyed. Include the SecretValue and new tenant secret Status.
```
TenantSecret secret = [SELECT Id FROM TenantSecret WHERE Type = 'Data' AND Version = 2];
secret.Status = Destroyed;
update secret;

```
Cache-Only Key Service customers can change the Status of cache-only key tenant secrets. For example, reactivate a cache-only key by
changing its Status from Destroyed to Active.

**Example 8: Create a callout connection that fetches a cache-only key tenant secret from a key service outside of Salesforce.**

**1. Make sure that your org has at least one active Data in Salesforce key, either Salesforce-generated or customer-supplied. Then turn**
on Allow Cache-Only Keys with BYOK from the Advanced Settings page in Setup.

**[2. Create a certificate that’s compatible with customer-supplied key material. See Generate a BYOK-Compatible Certificate in Salesforce](https://help.salesforce.com/articleView?id=security_pe_byok_generate_cert.htm&language=en_US)**
Help.

**[3. Create and assemble your key material.](https://help.salesforce.com/articleView?id=security_pe_byok_cache_create.htm&language=en_US)**

**4. Create a named credential to serve as your authenticated callout mechanism. You can define your named credential through Setup**
[or directly with Apex. Specify a BYOK-compatible certificate and an HTTPS endpoint.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)


-----

**5. Configure the connection to your remote key service. This connection uses a named credential and its associated certificate to fetch**
a specified cache-only key tenant secret.
```
  remote_params = { 'Source': 'Remote',
  'RemoteKeyIdentifier': ...,
  'RemoteKeyServiceId': ...,
  'RemoteKeyCertificate': ...}
  sf.TenantSecret.create(remote_params)

```
SEE ALSO:

System Fields
