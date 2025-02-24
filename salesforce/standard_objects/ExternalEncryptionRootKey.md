#### ExternalEncryptionRootKey

Represents metadata about root keys stored in third-party key stores that are used to generate and secure keys that encrypt Salesforce
data. This object is available in API version 58.0 and later.


-----

Root keys are used to generate data encryption keys (DEKs) in Salesforce, which are in turn used to encrypt and decrypt data. Root keys
are also used as wrapping keys to secure DEKs in the Salesforce database.

##### Supported Calls
```
describeSObjects(), query(), update()

 Special Access Rules

```
This object is available as part of the Shield and Salesforce Platform Encryption add-on subscriptions. Access to this object also requires
the Cache-Only Key Service add-on subscription.

##### Fields

```
ActivatedDate
CreatedBy
Description
LastModifiedBy

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date the key was activated in Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who created the root key. For example,
```
  user@example.com.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The user-defined description of the root key.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


-----

```
Region
RootKeyIdentifier
RootKeyService
Status

```

**Description**
The email address of the user who most recently modified the key. For example,
```
  user@example.com.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The region for the customer managed key. For example, if the RootKeyService is AWS,
the region is an Amazon Web Services (AWS) region such as `us-east1.`

**Type**
string

**Properties**
Filter, Nillable, Sort, Update

**Description**
The unique key identifier from the external KMS, such as an AWS Amazon Resource Name
(ARN). For example,
```
  arn:aws:kms:us-west-2:123456789000:key/123ab456-7cd8-9012-3e4f-5gh678i901j2

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The external key management service connected to Salesforce. For example, `AWS.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The status of the key.

Possible values are:

**•** `Activation Pending—Salesforce is waiting for confirmation of a valid key policy`
in the external key store.

**•** `Active—Can be used to encrypt new DEKs and decrypt existing DEKs.`

**•** `Archived—Can’t encrypt new DEKs. Can be used to decrypt previously created DEKs.`

**•** `Canceled—Root key activation canceled by a user.`


-----

**•** `Inactive—The root key, and the DEKs that it encrypts, are inaccessible. Inaccessible`
DEKs can’t be used to decrypt data, which renders that data also inaccessible.
