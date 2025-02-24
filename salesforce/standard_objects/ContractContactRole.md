#### ContractContactRole

Represents the role that a Contact plays on a Contract.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
ContactId

```

**Type**
reference


-----

```
ContractId
IsDeleted
IsPrimary

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Contact associated with this Contract.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Contract.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort,Update

**Description**
Specifies whether this Contact plays the primary role on this Contract (true) or not (false).
Each contract has one primary contact role. Default is `false. Labels is Primary.`


-----

```
 Role

```
SEE ALSO:

ContractStatus
