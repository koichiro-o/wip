#### SenderEmailAddress

Represents a From address in a marketing email. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
DisplayName
EmailDomainKeyId
Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive name that makes the sender email address easier to identify.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique system ID of the domain associated with the sender email address.

This field is a relationship field.

**Relationship Name**
EmailDomainKey

**Refers To**
EmailDomainKey

**Type**
string


-----

```
OwnerId
Username

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A unique identifier for the sender email address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique user ID of the user who owns the sender email address object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The part of the email address that comes before the @ symbol.

