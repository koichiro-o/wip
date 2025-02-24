#### EntitlementContact

Represents a Contact eligible to receive customer support via an Entitlement. This object is available in API version 18.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete()

 Fields

```
```
ContactId
EntitlementId
IsDeleted
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Contact associated with the entitlement. Must be a valid ID.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the Entitlement associated with the entitlement contact. Must be a
valid ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not
(false). Label is Deleted.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Nillable

**Description**
Required. Name of the entitlement contact.


-----

##### Usage

Use to query and manage entitlement contacts.

SEE ALSO:

Entitlement
