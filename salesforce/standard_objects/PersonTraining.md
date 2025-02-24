#### PersonTraining

```


**•** `ContentDocument`

**•** `ManagedContent`

**•** `Report`

**•** `Dashboard`

**•** Custom objects

You can have up to 2,500 `ExperienceVariation` targets and 25,000 record targets.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Value of the target. For ExperienceVariation, this is the developer name of the Experience
Variation or the record ID for the object.


Represents an assignment of a learning module in Workforce Engagement. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The org requires a Workforce Engagement license and an Enablement Sites (myTrailhead) license. The user requires at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Admin, Workforce Engagement Analyst, Workforce Engagement
Planner, or Workforce Engagement Agent.

Workforce Engagement Management uses this object to route training to agents. To assign modules to agents, users with the Learning
Manager profile require Read, Create, and View All Records access to this object. To receive routed modules, users with the Learner profile
require Read access to this object.

##### Fields

```
AssigneeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Name
OwnerId
Status

```

**Description**
A valid user ID for the user who’s assigned the training. `AssigneeId` can’t be empty if
the `Status` field is Assigned. We recommend that you set `AssigneeId` to the value
in `OwnerId.`

This is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the learning module.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the person training.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the training.

Possible values are:

**•** `A—Assigned; when the Status` is assigned, the AssigneeId field can’t be empty.


-----

```
TrainingId
TrainingType

##### Usage

```


**•** `C—Completed`

**•** `I—In Progress`

**•** `N—New`

**•** `P—Paused`

The default value is 'N'.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the learning module.

This is a relationship field.

**Relationship Name**
Training

**Relationship Type**
Lookup

**Refers To**
LearningContent

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of training.

Possible values are:

**•** `T—Trailhead`


In version 54.0 and later releases, Workforce Engagement uses this object instead of the AgentTraining object to route learning modules
to agents. If you set up agent engagement in your org in an earlier release, we rename AgentTraining records as PersonTraining records.
