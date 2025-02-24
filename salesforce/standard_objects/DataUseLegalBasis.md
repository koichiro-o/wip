#### DataUseLegalBasis

Represents the legal basis for contacting a customer, such as billing or contract. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Data Protection and Privacy is enabled.

##### Fields

```
Description

```

**Type**
string


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the data use legal basis.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate)
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Specifies a name for the legal basis. For example, “billing” or “contract”.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


-----

```
Source

##### Associated Objects

```

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the source of the legal basis. For example, the URL of a contract.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DataUseLegalBasisChangeEvent (API version 62.0)**
Change events are available for the object.

**DataUseLegalBasisHistory**

History is available for tracked fields of the object.

**DataUseLegalBasisOwnerSharingRule**

Sharing rules are available for the object.

**DataUseLegalBasisShare**

Sharing is available for the object.
