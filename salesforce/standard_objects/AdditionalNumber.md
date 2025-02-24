#### AdditionalNumber

Represents an optional additional number for a call center. This additional number is visible in the call center's phone directory.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
CallCenterId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Description
Name
Phone

##### Usage

```

**Description**
System field that contains the ID of the user who created the call center associated with this
additional number. If value is null, this additional number is displayed in every call center's
phone directory.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the additional number, such as Conference Room B.

Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the additional number.

Limit: 80 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
The phone number that corresponds to this additional number.


Create an additional number for a call center directory. Use this object if the number is not easily categorized as a User, Contact, Lead,
Account, or the other object. Examples include phone queues or conference rooms.
