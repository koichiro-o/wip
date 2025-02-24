#### LightningToggleMetrics

Represents users who switched from Lightning Experience back to Salesforce Classic. This object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Not available in sandbox orgs.


-----

##### Fields

**Field Name**
```
Action
MetricsDate
RecordCount
UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User switched from Lightning Experience to Salesforce Classic or from Salesforce
Classic to Lightning Experience.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user switched.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of user switches.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of user who switched.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


-----
