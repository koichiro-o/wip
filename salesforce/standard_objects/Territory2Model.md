#### Territory2Model

Represents a territory model. Available if Sales Territories has been enabled.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
Standard and partner users can access this object. If a territory model is in Active state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned


-----

records and assigned users subject to your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or Archived).

##### Fields

```
ActivatedDate
DeactivatedDate
Description
DeveloperName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory model was activated.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory model was archived.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the territory model.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is Territory Model Name.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.


-----

```
LastOppTerrAssignEndDate
LastRunRulesEndDate
Name
State

##### Associated Objects

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. The date when the opportunity territory assignment filter was last
run. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15
/ API version 33).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the last rules run was completed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The territory model name. The field label in the user interface is `Label.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The state of the territory model. Values are: Planning, Activating,
```
  Activation Failed, Active, Archiving, Archiving Failed,
  Archived, Deleting, and Deletion Failed.

```

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**Territory2ModelChangeEvent (API version 62.0)**
Change events are available for the object.

**Territory2ModelFeed**

Feed tracking is available for the object.

**Territory2ModelHistory**

History is available for tracked fields of the object.


-----
