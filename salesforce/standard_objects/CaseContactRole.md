#### CaseContactRole

Represents the role that a given Contact plays on a Case.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
CasesId
ContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cases associated with this contact.

This is a relationship field.

**Relationship Name**
Cases

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference


-----

```
 IsDeleted
 Role

##### Usage

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the role played by the contact on this case, such as Technical Contact, Business
Contact, Decision Maker, and so on. Must be unique—there can't be multiple records in
which the CaseId, ContactId, and Role values are identical. Different contacts can
play the same role on the same case. A contact can play different roles on the same case.


Use this object to define the role that a given Case plays on a given Contact. For example, you can use this object to be able to see all
contacts who are associated to a case, or, given a contact, be able to query all cases that they are associated with, even if they are not
the primary contact on the case.
