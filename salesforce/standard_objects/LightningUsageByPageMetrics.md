#### LightningUsageByPageMetrics

Represents standard pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Not available in sandbox orgs.

##### Fields

```
MetricsDate
PageName
TotalCount
UserId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date user viewed page in Lightning Experience.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of page user viewed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of pages viewed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of user who viewed page.


-----

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User
