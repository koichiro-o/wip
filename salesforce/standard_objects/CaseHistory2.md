#### CaseHistory2

Represents historical information about owner and status changes that have been made to the associated Case. This object is available
in API version 59.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is always read-only.

##### Fields

```
CaseId
IsDeleted
OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the contact who owns the case.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


-----

```
PreviousUpdate
Status

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was last updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the case, such as `New,` `Closed, or` `Escalated.`


CaseHistory2 entries are intended for case history reports.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseHistory2ChangeEvent on page 67**
Change events are available for the object in API version 60.0 or later.
