#### GoalLink

Represents the relationship between two goals. This is a many-to-many relationship, meaning that each goal can link to many other
goals.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated name of the goal link.


-----

```
ParentGoalId
SubgoalId
