#### Territory2AlignmentLog

```

**Description**
The ID of the territory model that the territory belongs to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the territory type that the territory belongs to.


Represents the start and end status of a territory assignment rule run job. This object is available in API version 54.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available if Sales Territories has been enabled.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users can’t view territory models in other states (such as Planning
or `Archived).`

##### Fields

```
EndTime
Filter

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the assignment rule run job finished.

**Type**
textarea

**Properties**
Nillable


-----

```
RunAsId
StartTime
Status
Territory2Id

```

**Description**
Criteria to filter the rule jobs. For example, {RULE_LAST_MOD_DATE_FORM=2021-08-31,
RULE_LAST_MOD_DATE_TO=2021-09-15}.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Salesforce user who started the assignment rule run job.

This is a relationship field.

**Relationship Name**
RunAs

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user started the assignment rule run job.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the assignment rule run job.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the territory for which the assignment rule run was performed. If the assignment
rule run was for the territory model, this value is null.

This is a relationship field.


-----

```
Territory2ModelId

##### Associated Objects

```

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the territory model for which the assignment rule run was performed.

This is a relationship field.

**Relationship Name**
Territory2Model

**Relationship Type**
Lookup

**Refers To**
Territory2Model


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**Territory2AlignmentLogChangeEvent**

Change events are available for the object.
