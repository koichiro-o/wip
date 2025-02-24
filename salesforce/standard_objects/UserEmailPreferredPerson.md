#### UserEmailPreferredPerson

```
Represents a mapping for a user’s preferred record for an email address when multiple records match an email field.This object is available
in API version 44.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
As of Summer ‘20 and later, only authenticated internal and external users can access this object.

##### Fields

```
Email

```

**Type**
email


-----

```
Name
OwnerId
PersonRecordId

```

**Properties**
Create, Filter,Group, idLookup, Sort, Update

**Description**
Required. The unique email the mapping applies to. This field is unique for each user.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto-generated field.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The userId that owns the record. Each record is only accessible to the owner.

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
Create, Filter, Group, Sort, Update

**Description**
Required. The recordId of a contact, lead, or user that represents the preferred record for the
email address. Use cascade delete for contact and lead, and delete if the personId is a
deactivated user record.

This is a polymorphic relationship field.

**Relationship Name**
PersonRecord

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**UserEmailPreferredPersonChangeEvent (API version 62.0)**
Change events are available for the object.

**UserEmailPreferredPersonShare**

Sharing is available for the object.
