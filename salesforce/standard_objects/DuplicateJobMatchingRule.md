#### DuplicateJobMatchingRule

Represents a MatchingRule to be used with a DuplicateJob sharing the corresponding DuplicateJobMatchingRuleDefinition.

This object is available in API versions 42.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

```
DuplicateJobId
DuplicateJobMatchRuleDefId
MatchingRuleBooleanFilter
MatchingRuleDescription

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding DuplicateJob.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the matching rule defined for the corresponding
DuplicateJobMatchingRuleDefinition.

**Type**
textarea

**Properties**
Filter, Sort

**Description**
Boolean logic of the MatchingRule for this DuplicateJobMatchingRule.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


-----

```
MatchingRuleName

```

**Description**
Description of the matching rule for this DuplicateJobMatchingRule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the matching rule defined for this particular DuplicateJob invocation.

