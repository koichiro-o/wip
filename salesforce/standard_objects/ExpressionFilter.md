#### ExpressionFilter

Represents a logical expression that’s used to control the execution of macro instructions. This object is available in API version 46.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ContextId
FilterConditionLogic

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the MacroInstruction object that contains the expression.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The filter conditions to use and the order in which to apply them. For example, ‘1
AND 2’ evaluates condition 1 and then condition 2.


-----

```
FilterDescription
Name

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. A description of the filter expression that helps to explain the logic to users. For
example, ‘Applies to New cases.’

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Optional. A label for the expression.


The ExpressionFilter object is used with the `IF` and `ELSEIF` operations in a MacroInstruction. It lets you specify a logical expression
that determines whether macro instructions are executed. The object indicates whether any or all conditions must be true.

To represent the conditions that are evaluated, this object uses one or more ExpressionFilterCriteria child objects. The ExpressionFilter
to be used with each criteria is specified in the ExpressionFilterCriteria’s ExpressionFilterId field.

For example, to represent the following conditional statement, the ExpressionFilter object specifies the FilterConditionLogic
field as 1 AND 2, where 1 and 2 are ExpressionFilterCriteria objects. In this example, condition 1 is Case.Status EQUALS New,
and condition 2 is `Case.Origin EQUALS Phone.`
```
IF (Case.Status EQUALS New) AND (Case.Origin EQUALS Phone)
    Select Email QuickAction
    Set Subject…
    Set To…
    Set Body…
    Submit
ENDIF
