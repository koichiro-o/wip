#### ExpressionFilterCriteria

```
Represents a condition in an expression that’s used to control the execution of macro instructions. This object is available in API version
46.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
ExpressionFilterId
FilterTarget
FilterTargetValue
Name
Operation

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the ExpressionFilter object that references this condition.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The target object or field used in the condition. For example, to create a condition
that applies to new cases, use `Case.Status` as the `FilterTarget.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The value that’s compared to the value of the FilterTarget. For example, to create
a condition that applies to new cases, use `New` as the `FilterTargetValue.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Optional. A label for the condition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the operator used to compare the target field and the target value. For
example, to create a condition that applies to new cases, use EQUALS for the Operation
field, as in `Case.Status EQUALS New.`

**•** `EQUALS`


-----

```
SortOrder

##### Usage

```


**•** `NOTEQUALS`

**•** `CONTAINS`

**•** `NOTCONTAIN`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The order in which the criteria are evaluated.


ExpressionFilterCriteria is a child object of the ExpressionFilter object. Use these objects with the `IF` and `ELSEIF operations in a`
MacroInstruction to control instruction execution. Each condition in a ExpressionFilterCriteria compares a target object or field to a value
using a condition operator; for example, `Case.Status EQUALS New.`
