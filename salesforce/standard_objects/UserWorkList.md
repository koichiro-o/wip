#### UserWorkList

Represents a list of work items in the My Feed tab for Sales Engagement users.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
IsActive
ListType
Name
OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the work list is active or not.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of list, such as a call or email.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the work list.

**Type**
reference


-----

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the list.
