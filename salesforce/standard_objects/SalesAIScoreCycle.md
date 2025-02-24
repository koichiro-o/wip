#### SalesAIScoreCycle

```

**Description**
Indicates whether the rule is an inherited rule (true) or a local rule (false).
Rule inheritance flows from the parent territory where the rule is created to the
rule’s descendent territories (if any) in the territory model hierarchy. A local rule
is created within a single territory and affects that territory only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory where the rule was created.


Represents the cycle type and ID used to score records. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To see score cycle information, users need a Sales Cloud Einstein license with the View Scoring Model Factors permission enabled. The
permission isn’t enabled by default. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

##### Fields

```
CycleType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

```
Name

```

**Description**
The cycle used to create scores on opportunity records can be one of two types.

**•** `OpportunityScoreModeling—Provides model factors, which Sales Cloud`
Einstein uses to build a scoring model.

**•** `OpportunityScoreScoring—Provides scores and key factors to individual`
records, which are based on Sales Cloud Einstein’s scoring model.

Note: When the value `OpportunityScoreModeling` is returned, use the
Sales AI Score Model Factor object to get information about the model factors.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the cycle. Currently, the name is a system-generated unique value.

