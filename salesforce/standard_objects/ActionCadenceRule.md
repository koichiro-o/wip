#### ActionCadenceRule

Represents the logic that a branch step uses to determine which branch an action cadence tracker follows in an action cadence. Use
ActionCadenceRule to learn about a branch step, including its logic and what the next step is. This object is available in API version 48.0
and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ActionCadenceStep that this rule is associated with.

This field is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup


-----

```
ConditionLogic
GlobalEventType
GraphState

```

**Refers To**
ActionCadenceStep

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The logical operator used to evaluate the rule conditions. Possible values are:

**•** `AND`

If this rule has several conditions, all of them must be `true` for this step to be
```
   true.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the action cadence rule contains a global exit condition, this field contains the type
of event that the rule represents.

Possible values are:

**•** `EmailReply`

**•** `EmailHardBounce`

**•** `EmailSoftBounce`

**•** `CallMeaningfulConnect`

**•** `CallNotInterested`

**•** `CallUnqualified`

**•** `CallLeftVoicemail`

**•** `CallCallBackLater`

This field is available in API version 49.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the state of the `ActionCadenceRule` within the step graph, or
sequence, of the related action cadence. Available in API version 53.0 and later.

Possible values are:

**•** `Included—This step rule is part of the step graph.`


-----

```
OutcomeNextStepName
ParentRuleName
RuleName
RuleType

```


**•** `Orphaned—This step rule was removed from the step graph before the action`
cadence was activated. Orphaned step rules are deleted upon activation.

**•** `Pending—This step rule has been created but hasn’t been added to the step`
graph. Pending step rules can be added to the step graph in the future.

**•** `Retired—This step rule was previously part of an active action cadence step`
graph and was removed during an edit after activation. Retired step rules can have
associated step trackers.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next step in the action cadence if this rule evaluates as true. If this rule evaluates
as false, the next step is ActionCadenceStep.BranchDefaultStepName.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `RuleName` field of the previous rule in the action cadence. Must
contain a valid rule name value unless this rule is the root rule. null if this rule is a
root rule.

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name given to the rule. Every rule in an action cadence must have a unique name.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of step that this rule applies to. Possible values are:

**•** `BranchStep — The rule evaluates the condition of a branch step. A branch step`
is an ActionCadenceStep record with the field `type equal to` `Branch.`


-----

**•** `RepeatedStep— The rule evaluates the repeat steps for quick cadence. Available`
in API version 58.0 and later.

**•** `RootStep— The rule evaluates a global exit condition.`

**•** `SubRootStep—Available in API version 58.0 and later.`

This field is available in API version 49.0 and later.

##### Usage

Use ActionCadenceRule to see all the rules associated with a branch step:
```
select RuleName from ActionCadenceRule where ActionCadenceStep.ActionCadence.Name = "High
 Priority CFO"

```
SEE ALSO:

ActionCadence

ActionCadenceRuleCondition

ActionCadenceStep

ActionCadenceStepTracker
