#### UiFormulaCriterion

Represents a filter that helps define component visibility on a Lightning page. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
LeftHandSide
OperatorId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Represents the field that the filter is based on. For example, `AMOUNT.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the filter operator. Valid values are:

**•** `CONTAINS`

**•** `EQUAL`

**•** `GE—greater than or equal`

**•** `GT—greater than`

**•** `LE—less than or equal`

**•** `LT—less than`

**•** `NE—not equal`

This is a relationship field.


-----

```
ParentKeyPrefix
RightHandSide
RuleId
