#### CryptoProdCatgWalletGroup

Specifies if CryptoWalletGroup is in the allowlist or airdrop for the ProductCategory. A custom object between ProductCategory and
CryptoWalletGroup adding the CryptoWalletGroup to allowlist or airdrop. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object has read, create, update, delete, modify all, and view all access.


-----

##### Fields

**Field**
```
CryptoWalletGroupId
LastReferencedDate
LastViewedDate
Name
ProductCategoryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The CryptoWalletGroup ID.

This field is a relationship field.

**Relationship Name**
CryptoWalletGroup

**Relationship Type**
Lookup

**Refers To**
CryptoWalletGroup

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the record.

**Type**
reference


-----

```
Status
Type
