#### DelegatedAccount

Represents the external managed account. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

```

-----

##### Special Access Rules

You must have a Partner or Customer Community Plus license. You can't edit the visibility of DelegatedAccount metadata on user profiles.

##### Fields

```
AccessBuyFor
AccessManageUsers
LastReferencedDate
LastViewedDate
ManagedById

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
The access that an admin authorizes for an external user to buy for other accounts. This field
is available in API version 50.0 and later. A B2B Commerce license is required to use
AccessBuyFor.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
The access that an admin authorizes for an external user to manage external users on other
accounts. This includes managing permission sets, membership, passwords, and activation.
This field is available in API version 50.0 and later. Delegated External User Administrator
permission is required to use AccessManageUsers.

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
reference


-----

```
Name
OwnerId
ParentId

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the managing user.

This is a relationship field.

**Relationship Name**
ManagedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the external managed account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the managing users account. This field is available in API version 50.0 and later.

This is a relationship field.


-----

```
TargetId
