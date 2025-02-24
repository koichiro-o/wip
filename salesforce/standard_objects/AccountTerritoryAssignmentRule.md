#### AccountTerritoryAssignmentRule

An account assignment rule that assigns accounts to territories based on account fields. Available if Sales Territories has been enabled.

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
BooleanFilter

```

**Type**
string

**Properties**
Create, Filter, Nillable, Update


-----

```
IsActive
IsInherited
Name
TerritoryId

```

**Description**
Advanced filter conditions that were specified for the rule in the online application. For
example, “(1 AND 2) OR 3.”

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the rule is active (true) or inactive (false). Via the API, active rules run
automatically when new accounts are created and existing accounts are edited. The exception
is when the IsExcludedFromRealign field on an account is true, which prevents
account assignment rules from evaluating that account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the rule is an inherited rule (true) or a local rule (false). An inherited
rule also acts upon territories below it in the territory hierarchy. A local rule is created at the
immediate territory and only impacts the immediate territory.

**Type**
string

**Properties**
Create, Filter, Update

**Description**
A name for the rule. Limit is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
ID of the territory where accounts that satisfy this rule are assigned.


-----

##### Usage

A territory will not have any accounts (with the exception of manually assigned accounts) unless at least one account assignment rule
is active for the territory.

SEE ALSO:

AccountTerritoryAssignmentRuleItem

Territory

UserTerritory
