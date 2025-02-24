#### MacroInstruction

Represents an instruction in a macro. An instruction can specify the object that the macro interacts with, the context or publisher that
the macro works within, the operation or action that the macro performs, and the target of the macro’s actions.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
MacroId
Name
Operation
SortOrder

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the macro that contains this instruction.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Name of the instruction.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The action that the macro instruction performs. Valid values are:

**•** Select

**•** Set

**•** Insert

**•** Submit

**•** Close

To create macro instructions that execute conditionally, these values are available
in API version 46.0 and later.

**•** IF

**•** ELSEIF

**•** ELSE

**•** ENDIF

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Order of this instruction in the macro.


-----

```
Target
Value
ValueRecord

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The object that’s the target of the operation. For example, the target for the active
case tab (Tab.Case) or a quick action, like the Send Email action on the case object
(QuickAction.Case.SendEmail).

In Lightning Experience, macros are supported on standard and custom objects
that allow quick actions and have a customizable page layout.

In Salesforce Classic, macros are supported on objects with feed-based layouts
and quick actions.

You can specify relative dates and times for the following targets.

**•** DateTime

**•** Date

**•** Time

**•** DueDate

**•** Birthday

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Value of a field. If the operation is Select, then the value is null, because the
operation selects the object on which the macro performs an action. An
instruction can contain both a `Value` field and a `ValueRecord` field, but
only one of these fields can have a value. The other field value must be null.

To create relative dates and times, specify a valid Salesforce formula, prefaced
by `MacroFormula. For example, the following formula creates a date that is`
1 day from now:
```
  MacroFormula:NOW() + 1

```
You can’t edit custom relative formulas in the Macro Builder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the value or record. The ValueRecord can be either a value or a record,
but not both. An instruction can contain both a `Value` field and a


-----

`ValueRecord` field, but only one of these fields can have a value. The other
field value must be null.

##### Usage

MacroInstructions can specify objects, operations, conditions, and targets. For example, a macro containing these instructions performs
a quick action that sends an email.
```
    Select Email QuickAction
    Set Subject…
    Set To…
    Set Body…
    Submit

```
You can create conditional macros using IF, ELSEIF, ELSE, and ENDIF as operations. In a conditional statement, the ExpressionFilter
and ExpressionFilterCriteria objects are used to control which instructions execute. The ExpressionFilter object lets you define a logical
expression with one or more conditions. It uses a child object, ExpressionFilterCriteria, to represent each condition that is evaluated.

For example, consider the following conditional statement and macro instructions.
```
IF (Case.Status EQUALS New) AND (Case.Origin EQUALS Phone)
    Select Email QuickAction
    Set Subject…
    Set To…
    Set Body…
    Submit
ELSE
    Select Update Case Detail
    Update Case Description…
    Submit
ENDIF

```
The ExpressionFilter object includes a FilterConditionLogic field containing 1 AND 2, where 1 and 2 are ExpressionFilterCriteria
objects. The SortOrder field in the ExpressionFilterCriteria object maps condition 1 to `Case.Status EQUALS New, and condition`
2 to `Case.Origin EQUALS Phone. If the conditional statement evaluates to true, then the instructions in the` `IF` block are
executed; otherwise, the instructions in the `ELSE` block are executed.

Any number of macro instructions can be present inside an `IF,` `ELSEIF, or` `ELSE` block. In addition, conditions can be nested.

##### Data Model


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MacroInstructionChangeEvent (API version 48.0)**
Change events are available for the object.
