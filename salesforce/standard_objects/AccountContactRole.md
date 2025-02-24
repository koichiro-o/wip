#### AccountContactRole

Represents the role that a Contact plays on an Account.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
AccountId
ContactId
IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Account.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Contact associated with this account.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean


-----

```
 IsPrimary
 Role

##### Usage

```

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the Contact plays the primary role on the Account (true) or not (false).
Note that each account has only one primary contact role. Label is Primary. Default value
is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the role played by the Contact on this Account, such as Decision Maker, Approver,
Buyer, and so on. Must be unique—there can't be multiple records in which the
`AccountId,` `ContactId, and` `Role` values are identical. Different contacts can play
the same role on the same account. A contact can play different roles on the same account.


Use this object to define the role that a Contact plays on a given Account within the context of a specific Opportunity.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountContactRoleChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

Account

Contact


-----
