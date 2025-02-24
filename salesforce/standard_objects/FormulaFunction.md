#### FormulaFunction

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows forecast quantity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows the guided tour.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows a quota column.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows changes in the last 7 days.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows quota attainment information.


Represents a function used when building a formula, including examples and uses. This object is available in API version 47.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
CategoryId
Description
DurableId
ExampleString

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FormulaFunctionCategory.

This is a relationship field.

**Relationship Name**
Category

**Relationship Type**
Lookup

**Refers To**
FormulaFunctionCategory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the formula function.

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
Describes the function and what arguments you can use with it.


-----

```
IsAllowedInEntityContext
IsAllowedInFlowContext
IsAllowedInVisualforceContext
Label
Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether you can use the formula function on an Entity (true) or not (false).
For example, you cannot use the PRIORVALUE function in a custom Account formula field.
The default value is `false. This field is removed in API version 48.0 and later. Use the`
FormulaFunctionAllowedType on page 2661 object instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the formula function is allowed in a Flow (true) or not (false). The
default value is `false. This field is removed in API version 48.0 and later. Use the`
FormulaFunctionAllowedType on page 2661 object instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the formula function is allowed in Visualforce (true) or not (false).
The default value is `false. This field is removed in API version 48.0 and later. Use the`
FormulaFunctionAllowedType on page 2661 object instead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The formula function label that appears in the user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the formula function.


-----

##### Usage

Query FormulaFunction to search for available formula functions, such as `AND(),` `ISBLANK(),` `MAX(),` `MIN(), and others.`
