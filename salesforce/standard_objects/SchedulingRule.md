#### SchedulingRule

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The record that the scheduling objective applies to.

Possible values are:

**•** `A—Appointment`

**•** `B—Shift`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of scheduling objective.

Possible values are:

**•** `AgentPreference—Scheduling tools consider agents’ service resource preferences.`
In the UI, this value appears as Maximized Preferences.

**•** `BalanceNonStandardShifts—Scheduling tools balance the number of shifts`
across available agents within a time period.

**•** `BalanceShifts—Scheduling tools balance the number of non-standard shifts`
across available agents within a time period.


Represents scheduling rules that are hard constraints in the scheduling logic engine. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user needs to have the Workforce
Engagement Planner permission set.


-----

##### Fields

**Field**
```
Description
DeveloperName
Language
MasterLabel
SchedulingCategory

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The scheduling rule description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name value of the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the scheduling rule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling rule name.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Shifts.

Possible values are:

**•** `A—Appointment`

**•** `B—Shift`


-----

```
SchedulingRuleType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The scheduling rule type.

Possible values are:

**•** `A—Active Resources`

**•** `B—Match Skills`

**•** `C—Availability`

**•** `LimitNonstandardShifts—Specifies a rule type that limits how many`
non-standard shifts can be assigned to each agent. This type is available in API version
54.0 and later.

**•** `M—Match Territory`

**•** `Q—Match Queues`

**•** `RestTimeMinutes—Specifies a rule type that requires the agent to have a minimum`
rest time between consecutive shifts. This type is available in API version 56.0 and later.

**•** `W—Work Limit`

