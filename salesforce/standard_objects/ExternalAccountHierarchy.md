#### ExternalAccountHierarchy

Represents the external account hierarchy, which works like a role-based hierarchy. Use ExternalAccountHierarchy to allow partner and
customer users to share data with other external accounts in their hierarchy.This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
You must have a Partner or Customer Community Plus license.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the account in the external account hierarchy.


-----

CurrencyISOCode
```
Description
HierarchyType
IsAccessibleToParent
IsActive

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `GBP— British Pound`

**•** `USD— U.S. Dollar`

The default value is `USD.`

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the external account hierarchy.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** `CustomerPortal` — Customer

**•** `Partner`

The default value is `Partner.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows data to be shared with parent account in the account hierarchy. The default value is
```
  true.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
ParentId

```

**Description**
When true, the hierarchy is turned on. The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the external account hierarchy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent account.


-----
