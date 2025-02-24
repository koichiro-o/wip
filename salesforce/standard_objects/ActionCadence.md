#### ActionCadence

Represents the definition of a 1 cadence. This object is available in API version 45.0 and later.

Use ActionCadence and its related objects to learn about an action cadence, including:


-----

**•** The current state of the action cadence.

**•** The steps that the action cadence contains.

**•** Which leads, contacts, or person accounts are assigned to the action cadence.

The ActionCadence, ActionCadenceStep, ActionCadenceRule, and ActionCadenceRuleCondition objects define an action cadence and
the steps that it contains. ActionCadenceTracker and ActionCadenceStepTracker track a prospect's movement through an active action
cadence.

By learning when the action cadence objects are created and deleted, you can make the most of the action cadence API.

**•** An ActionCadence record is created when you use the Sales Engagement app to create a cadence.

**•** An ActionCadenceStep record is created to represent a step. If the step is a branch step, then corresponding ActionCadenceRule
and ActionCadenceRuleCondition records are also created.

**•** An ActionCadenceTracker record is created when you assign a prospect to an action cadence.

**•** An ActionCadenceStepTracker record is created each time the prospect moves to a new step.

All of these action cadence records exist until you use the Sales Engagement app to delete an action cadence. If many prospects have
been assigned to the action cadence, there can be many associated ActionCadenceTracker and ActionCadenceStepTracker records. In
this case, deleting the action cadence can take some time. While the action cadence is being deleted, the value for the State field is
`Deleting` on the ActionCadence record.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Fields

```
```
ActivatedDate
ActiveTargets

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the user activated the action cadence. ActionCadence objects are created in
a draft state and must be manually activated before they’re used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of active targets that are currently assigned with this cadence. Available
in API version 58.0 and later.


-----

```
Description
ErrorMessage
FolderId
FolderName
IsWaitAllowedBeforeDaisyChain

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of this action cadence.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If there was an error when activating the action cadence, this field contains the error message.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the folder that contains the action cadence. Available in API version 49.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name of the folder that contains the action cadence. Available in API version 49.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
LastEditedDateTime
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Description**
Whether the cadence is allowed to have a wait step before a daisy chain step (true) or not
(false).

The default value is `false.`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time this object was last edited.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this object was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this action cadence was last viewed in the Sales Engagement app.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this action cadence. Every action cadence in an org must have a unique name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the action cadence (typically the user who created it).

Note: To change the owner of an action cadence, the new owner must have read
access to action cadences enabled in their user profile.


-----

```
State
SuccessfulCompletions

```

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This entity's state.

Possible values are:

**•** `Active`

The user finished modifying the action cadence and has activated it. At this point, you
can't make any more changes to the steps in the action cadence.

**•** `Deleting`

All records associated with this action cadence, including the ActionCadence record and
all its related records, are being deleted. While in this state, the ActionCadence can’t be
attached to a prospect.

**•** `Draft`

ActionCadence objects are in the draft state when they’re created. In this state, the
ActionCadence can’t be assigned to any prospect.

**•** `Error`

An error occurred while trying to activate the action cadence.

**•** `Inactive`

The user deactivated the action cadence. New targets can’t be added to the action
cadence. Existing targets continue in the action cadence until completion.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of successful dispositions this cadence has upon completion. For example,
customer engaged or customer connected. Available in API version 58.0 and later.


-----

```
TotalSteps
TotalTargets
Type

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of total steps associated with this cadence. This value doesn’t include special
step types such as root, branch, and daisy chain. Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of targets that have been assigned with this cadence. Available in API
version 58.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the type of ActionCadence. Available in API version 56.0 and later.

Possible values are:

**•** `Standard`

Standard cadences can contain multiple steps and are usually built by sales managers
in the Cadence Builder.

**•** `Quick`

Quick cadences can contain only one step, are built by reps for their personal use, and
don't require the Cadence Builder.


Use ActionCadence to learn how many action cadences are currently active:
```
select COUNT() from ActionCadence where State="Active"

```
Retrieve all ActionCadence records that have "West Coast" in their name:
```
SELECT ActionCadenceId FROM ActionCadence WHERE NAME LIKE '[West Coast Cadence]%'

```
Retrieve all ActionCadence records owned by a specific user:


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceChangeEvent (API version 48.0)**
Change events are available for the object.

**ActionCadenceOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ActionCadenceShare on page 66**
Sharing is available for the object.

SEE ALSO:

ActionCadenceRule

ActionCadenceRuleCondition

ActionCadenceStep

ActionCadenceStepTracker
