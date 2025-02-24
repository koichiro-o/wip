#### AutomatedActionCondition

Represents the logical operator details for evaluating conditions in an automated action. This object is available in API version 57.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
AutomatedActionId
ConditionNumber
IsLocked

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference number of the condition containing advanced filter logic.

**Type**
boolean


-----

```
MayEdit
Operator
ReferenceField

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record is locked or not.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record can be edited or not.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The logical operator for this condition.

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equal`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `IsChanged`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotEqual`

**•** `StartsWith`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field to use for this condition.


-----

```
Type
Value

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of condition.

Possible values are:

**•** `ExtraFilterCondition`

**•** `PrimaryFilterCondition`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value to compare to the `ReferenceField.`

