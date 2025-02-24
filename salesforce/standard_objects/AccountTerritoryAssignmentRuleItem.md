#### AccountTerritoryAssignmentRuleItem

A row of selection criteria for an AccountTerritoryAssignmentRule object. Available if Sales Territories has been enabled.

AccountTerritoryAssignmentRuleItem can be created or deleted if the `BooleanFilter` field on its corresponding
AccountTerritoryAssignmentRule object is a null value.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Users with the View Setup and Configuration permission can access this object. Users with the Manage Territories permission can edit
this object.

##### Fields

```
Field
Operation

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The standard or custom account field to use as a criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The criteria to apply, such as “equals” or “starts with.”


-----

```
 RuleID
 SortOrder
 Value

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
ID of the associated AccountTerritoryAssignmentRule.

**Type**
int

**Properties**
Create, Filter, Update

**Description**
The order in which this row is evaluated compared to other
AccountTerritoryAssignmentRuleItem objects for the given AccountTerritoryAssignmentRule.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The field value(s) to evaluate, such as `94105` if the Field is `Billing Zip/Postal`
```
  Code.

```


**•** Both standard and custom account fields can be used as criteria for account assignment rules.

**•** A territory will not have any accounts (with the exception of manually assigned accounts) unless at least one account assignment
rule is active for the territory.

SEE ALSO:

AccountTerritoryAssignmentRule

Territory

UserTerritory
