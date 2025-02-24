#### ObjectTerritory2AssignmentRuleItem

A single row of selection criteria for an ObjectTerritory2AssignmentRule object. ObjectTerritory2AssignmentRuleItem can only be created
or deleted if the `BooleanFilter` field on its corresponding ObjectTerritory2AssignmentRule object is a `null` value. Available if
Sales Territories has been enabled.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories and assignment rules. For territories in an active model, any standard user can view assigned records and assigned users subject
to your Salesforce sharing settings. Users cannot view territory models in other states (such as `Planning` or `Archived).`


-----

##### Fields

**Field Name**
```
Field
Operation
RuleId
SortOrder
Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The standard or custom object field that the rule item will operate on.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The criterion to apply for the rule item. For example: `equals` or `starts`
```
  with.

```
**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated ObjectTerritory2AssignmentRule.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order in which this row is evaluated in relation to other
ObjectTerritoryAssignmentRuleItem objects for the given
ObjectTerritoryAssignmentRule. This field is required for assignment rule items,
which are used in the Boolean conditions in assignment rule formulas.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The field value or values to evaluate. For example: if the field is `Billing`
```
  ZIP/Postal Code, a value might be 94105. .

```

-----
