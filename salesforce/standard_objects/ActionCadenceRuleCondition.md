#### ActionCadenceRuleCondition

Represents the logic for a branch step. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
ActionCadenceRuleId
Operator

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ActionCadenceRule that this condition is associated with.

**Type**
picklist


-----

```
Resource
RuleConditionName
Value

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The conditional operator for this rule. Possible values are:

**•** `Equal`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field to evaluate. Possible values are:

**•** `CallDispositionCategory`

Use by branch steps.

**•** `EmailEngagement`

Used by ListenerBranch steps.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the rule condition. Every rule condition in a cadence must have a unique name.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The event that your cadence rule condition listens for to decide when the event is complete.

Possible values for emails are:

**•** `EmailOpen`

**•** `EmailLinkClick`

Possible values for calls are:

**•** `CallMeaningfulConnect`

**•** `CallUnqualified`

**•** `CallLeftVoicemail`

**•** `CallNotInterested`

**•** `CallCallBackLater`


-----

##### Usage

Use ActionCadenceRuleContion to see all the rule conditions associated with a branch step:
```
select RuleConditionName from ActionCadenceRuleCondition where ActionCadenceStepId= <ID
of a branch step>

```
SEE ALSO:

ActionCadence

ActionCadenceRule

ActionCadenceStep

ActionCadenceStepTracker
