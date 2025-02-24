#### ReputationLevel

Represents a reputation level defined for an Experience Cloud site. This object is available in API version 32.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is available only if digital experiences is enabled in your org. Only users with permissions to create or manage an Experience
Cloud site can view the ReputationPointsRule records.

##### Fields

```
Label
LevelNumber
ParentId
Threshold

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the reputation level.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The rank of the reputation level.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent Experience Cloud site the reputation level applies to.

**Type**
double

**Properties**
Filter, Sort

**Description**
The lower limit of reputation points associated with this reputation level. The
maximum number of reputation points a user can accrue is 999,999,999,999,999.


-----
