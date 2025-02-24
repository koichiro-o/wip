#### ActionCadenceTracker

```
Represents an active cadence target. This object is available in API version 45.0 and later.

An ActionCadenceTracker record is created when you add a target to a cadence. Use ActionCadenceTracker to learn about a running
cadence target, including its state, current step, assigned prospect, and reason for completion.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
ActionCadenceId
CompletionDisposition

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related ActionCadence.

**Relationship Name**
ActionCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort


-----

```
CompletionReason
CurrentStepId

```

**Description**
The target’s disposition when it exited the action cadence. This field contains a value if the
target’s `State` is Complete. Sales reps can set this value when removing a target from
a cadence. This field is available in API version 51.0 and later. Possible values are:

**•** `Bad Data — some of the target’s data is incorrect or invalid.`

**•** `Contact Later` — the target asked to be contacted at a later date.

**•** `Customer Connected` — the sales rep contacted the target.

**•** `Customer Engaged` — the target engaged with an email.

**•** `Disqualified— a sales rep determined that the target isn’t qualified.`

**•** `Duplicate — the target has a duplicate lead, contact, or person account record.`

**•** `No Response — the target didn’t reply to any outreach.`

**•** `Not Interested` — the target stated a lack of interest.

**•** `Success — the cadence outreach was successful.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason that the target completed the cadence. This field contains a value if the target’s
`State` is `Complete. Possible values are:`

**•** `AutomaticallyExited` — the target completed because a global exit condition
occurred. This value is available in API version 49.0 and later.

**•** `AutomaticallyExitedDeletedStep`

**•** `AutomaticallyExitedInvalidParentStep`

**•** `DaisyChained` — the target completed because it’s connected to another action
cadence.

**•** `LeadConverted` — the target completed because the lead converted.

**•** `ManuallyRemoved` — the target completed because the sales rep removed it from
the cadence.

**•** `ManuallyRemovedNoAccess— reserved for future use.`

**•** `NoMoreSteps — the target completed the action cadence because all the action`
cadence steps were completed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the current ActionCadenceStepTracker.


-----

```
DaisyChainIteration
ErrorMessage
ExitGlobalRuleId
IsTrackerActive

```

**Relationship Name**
CurrentStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of this action cadence in a sequence of linked action cadences followed by this
target. This value starts at 1 with the initial action cadence. A target can follow a sequence
of up to 10 linked action cadences. Available in API version 53.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If an error occurs while this target is being completed, this field contains the error message.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If a global exit condition occurs, a target completes. One example of a global exit condition
is an email returned because of an invalid address. If the target completed because a global
exit condition occurred, this field contains the ID of the ActionCadenceRule record that
evaluated as `true.`

This field is available in API version 49.0 and later.

**Relationship Name**
ExitGlobalRule

**Relationship Type**
Lookup

**Refers To**
ActionCadenceRule

**Type**
boolean


-----

```
LastCompletedStepId
OwnerId
RelatedToAttributionType

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action cadence target is active `(true)` or not `(false). The`
default value is false. An action cadence target is active if the state is Running, Paused,
```
  Processing, or Initializing. Only active targets count against the org limit of

```
150,000 trackers.

This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the last completed ActionCadenceStepTracker.

**Relationship Name**
LastCompletedStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who is assigned to complete the cadence steps for the target.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
RelatedToId
ScheduledResumeDateTime
State

```

**Description**
Defines when the cadence is related to an opportunity or invoice. Available in API version
51.0 and later.

Possible values are:

**•** `Activation—Attribute the opportunity to the cadence when the opportunity is`
created.

**•** `Collected—Attribute the value to the cadence after payment for the invoice is`
collected.

**•** `Collection Advancement—Attribute the value to the cadence when the invoice`
is out for collection.

**•** `Maturation—Attribute the opportunity to the cadence only when the opportunity`
stage advances.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related opportunity if there’s one. Available in API version 51.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
RelatedTo

**Relationship Type**
Lookup

**Refers To**
Opportunity, Invoice

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. Available in API version 53.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. Possible values are:


-----

```
TargetId

##### Usage

```


**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing—Salesforce is working on changing the state of this action cadence`
tracker. We recommend that you filter out steps that have this state from your dashboards.

**•** `Running`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the target that is assigned to this action cadence.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


Use ActionCadenceTracker to see what targets are currently assigned to an active action cadence.
```
select TargetId from ActionCadenceTracker where ActionCadenceId=<Id of the action cadence>
 and State= "Running"

##### Associated Objects

```
This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceTrackerChangeEvent (API version 48.0)**
Change events are available for the object.

**ActionCadenceTrackerOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ActionCadenceTrackerShare on page 66**
Sharing is available for the object.


-----
