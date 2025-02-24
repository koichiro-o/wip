#### DuplicateJobMatchingRuleDefinition

Setup object specifying a MatchingRule to use with DuplicateJob instances that share a DuplicateJobDefinition.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This object is available in API versions 42.0 and later.

##### Supported Calls
```
describeSObjects(), query(), search()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

```
DuplicateJobDefinitionId
MatchingRuleId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of DuplicateJobDefinition (master) for this DuplicateJobMatchingRuleDefinition
(detail).

**Type**
reference


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the MatchingRule to be used with this DuplicateJobMatchingRuleDefinition.
