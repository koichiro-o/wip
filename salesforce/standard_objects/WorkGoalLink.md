#### WorkGoalLink

Represents the relationship between two goals (many to many relationship). This object has been deprecated as of API version 35.0.
Use the GoalLink object to query information about the relationship between two WDC goals.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),

```
`retrieve(),` `undelete(),` `update()`, `upsert()`

##### Fields

```
IsActive
LinkType
Name
SourceGoalId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the WorkGoalLink is active (true) or not (false)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of link

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the goal link

**Type**
reference


-----

```
TargetGoalId
