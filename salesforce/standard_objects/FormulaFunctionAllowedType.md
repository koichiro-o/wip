#### FormulaFunctionAllowedType

Represents the functions that are supported in the given formula context. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
DurableId
FunctionId
Type

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
Unique identifier for the supported function.

This is a relationship field.

**Relationship Name**
Function

**Relationship Type**
Lookup

**Refers To**
FormulaFunction

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

**Description**
The name of the formula type in which the function is supported.

Possible values are:

**•** `FLOW`

**•** `VALIDATION`

**•** `VISUALFORCE`
