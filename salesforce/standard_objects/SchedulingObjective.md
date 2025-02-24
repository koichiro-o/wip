#### SchedulingObjective

Represents business goals that the scheduling tools consider. This object is available in API version 53.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user needs to have the Workforce
Engagement Planner permission set.

##### Fields

```
Description
DeveloperName
Language
MasterLabel

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The scheduling objective description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are the supported languages for Workforce Engagement.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The scheduling objective name.


-----

```
SchedulingCategory
SchedulingObjectiveType
