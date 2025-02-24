#### UiFormulaRule

```

**Relationship Name**
Operator

**Relationship Type**
Lookup

**Refers To**
null

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix of the parent ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the value used to evaluate the component’s visibility. For example, 1000000.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the formula rule ID.

This is a relationship field.

**Relationship Name**
Rule

**Relationship Type**
Lookup

**Refers To**
UiFormulaRule


Represents a set of one or more filters that define the conditions under which a component displays on a Lightning page. This object is
available in API version 47.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
AssociatedElementId
BooleanFilter
DeveloperName
Formula

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a parent component that UiFormulaRule is associated with, such as PromptVersion.

This is a relationship field.

**Relationship Name**
AssociatedElement

**Relationship Type**
Lookup

**Refers To**
PromptVersion

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the filter logic applied to UiFormulaRule. References the UI formula rule stored
by UiFormulaCriterion based on the sortIndex, such as ((1 && 3) || 2).

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Represents the API name of the UiFormulaRule.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
textarea

**Properties**
Nillable


-----

```
Language
MasterLabel
ParentKeyPrefix

```

**Description**
Represents the formula source string of UiFormulaRule.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the language of the UiFormulaRule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. Represents the label of the UiFormulaRule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the three-digit prefix for AssociatedElementId.

