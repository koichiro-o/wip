#### WorkDemographic

Represents the field values used to specify slices in the workload forecasting and capacity planning. This object is available in API version
49.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user must have the Workforce
Engagement Analyst permission set.

##### Fields

```
Channel
CustomWorkType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The channel value.

**Type**
string


-----

```
GroupIdentifier
JobProfileId
Region
ServiceChannelId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Custom dimension value that the user can define other than the channel, region, and skill
dimensions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The group or queue associated to a slice when creating an Omni-based workload.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The foreign key to the JobProfile object.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The region value.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The foreign key to the ServiceChannel object.

This is a relationship field.


-----

```
ServiceTerritoryId
SkillSet
