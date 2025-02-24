#### FormulaFunctionCategory

Represents the category to which a formula belongs when building a formula. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
DurableId
Label
Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label of the FormulaFunctionCategory that appears in the user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the FormulaFunctionCategory.


-----

##### Usage

Query FormulaFunctionCategory to search for categories of available formula functions, such as Math, Logical, Date and Time,
and others.
