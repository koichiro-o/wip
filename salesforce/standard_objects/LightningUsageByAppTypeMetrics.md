#### LightningUsageByAppTypeMetrics

Represents number of users on Lightning Experience and Salesforce Mobile. This object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Not available in sandbox orgs.

##### Fields

```
AppExperience
MetricsDate
UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User’s app (Lightning Experience or Salesforce Mobile).

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user accessed Lightning Experience or Salesforce Mobile.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId for user accessing Lightning Experience or Salesforce Mobile.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


-----
