#### ActionCadenceStep

Represents a step in a cadence. Use ActionCadenceStep to learn which steps belong to a cadence, and how the steps are connected to
each other. This object is available in API version 48.0 and later.

An ActionCadenceStep record is created to represent a step. If the step is a branch step, then corresponding ActionCadenceRule and
ActionCadenceRuleCondition records are also created.

Note: An ActionCadenceStep with `IsOrphan` equal to `true` can be part of a cadence but is never executed. To retrieve the
steps that can be executed by the cadence, query for ActionCadenceStep records with `IsOrphan` equal to `false.`
ActionCadenceStep records with IsOrphan equal to `true` are deleted.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
ActionCadenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ActionCadence that this step belongs to.

This field is a relationship field.

**Relationship Name**
ActionCadence


-----

```
AllCallsCallBackLater
AllCallsLeftVoicemail
AllCallsMeaningfulConnect
AllCallsNotInterested
AllCallsUncategorized
AllCallsUnqualified

```

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where the call outcome isn’t categorized.

**Type**
int


-----

```
AllEmailsBouncedCount
AllEmailsDeliveredCount
AllEmailsHardBouncedCount
AllEmailsLinkClickedCount
AllEmailsOpenedCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls having the call outcome Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that weren’t delivered successfully.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails delivered.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails returned for a permanent reason — for example, the email address
doesn’t exist. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of links inside an email that the target clicked during this step. Multiple clicks
on the same link count towards this total. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
AllEmailsOutOfOfficeCount
AllEmailsRepliedCount
AllEmailsSentCount
AllEmailsSoftBouncedCount
AllEmailsTrackedSentCount

```

**Description**
The number of emails that the target opened while working on this step. Multiple opens of
the same email count towards this total.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were returned because the recipient set an out-of-office responder.
Multiple replies count towards this total. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that targets replied to as part of this step. Multiple replies to the same
email count towards this total, This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were returned for temporary reasons — for example, the email
is too large. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled.


-----

```
AllEmailsUntrackedSentCount
AllManuallyCompletedCount
AllOnTimeCompletedCount
AllOverdueCompletedCount
AllSkippedCount
AllTotalCallsCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps manually completed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps completed on time.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of overdue steps that were completed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of steps skipped.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls that the sales rep made during this step.


-----

```
BranchDefaultStepName
ChainedCadenceId
GoToStepIntervalInMinutes
GoToStepIterationLimit
GoToStepName

```

This field is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the default step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ActionCadence for the linked action cadence. Available only if the step type is
`DaisyChain` (meaning that another action cadence is connected to this action cadence).

This field is a relationship field.

**Relationship Name**
ChainedCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains information about when the step should be repeated next, in minutes. Available
in API version 58.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the maximum number of repeat (goto) step iterations allowed. Available in API
version 58.0 and later.

**Type**
string


-----

```
GraphState
HasVariant
IsImmediateWakeUp

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If this step’s original next step was removed during an edit after activation, this field specifies
the updated next step.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the state of the `ActionCadenceStep` within the step graph, or sequence,
of the action cadence.

Possible values are:

**•** `Included—This step is part of the step graph.`

**•** `Orphaned—This step was removed from the step graph before the action cadence`
was activated. Orphaned steps are deleted upon activation.

**•** `Pending—This step has been created but hasn’t been added to the step graph.`
Pending steps can be added to the step graph in the future.

**•** `Retired—This step was previously part of an active action cadence step graph and`
was removed during an edit after activation. Retired steps can have associated step
trackers.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is valid for email and call step types. If true, the step has email or call template
variants. The template variants are defined in ActionCadenceStepVariant records. Available
in API version 53.0 and later.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a listener branch is immediate wake up (true) or not (false).

The default value is `false.`


-----

```
IsOrphan
IsScheduledDueDateLocked
IsScreenFlowActive
IsStepAutomationActive
IsThreaded

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true, this step isn’t executed by the action cadence and will be deleted. Steps with`
`IsOrphan` equal to `true` have ParentStepName equal to `null.`

Note: To retrieve the active steps in an action cadence, include IsOrphan=false
in your query.

The default value is `false.`

This field is available in API version 49.0 and later.

This field is a calculated field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether assignees can change the due date (true) or not (false). Available in
API version 58.0 and later.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is active and can be executed (true) or not (false).

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the flow referenced in the StepAutmationReference field is active. If false, the flow
isn’t active. Only active flows can be executed. The default value isfalse. This field is
available in API version 56.0 and later.

**Type**
boolean


-----

```
ParentStepName
RootStepId
ScheduledDaysUntilDue

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is valid for email steps. Email steps have ActionCadence.StepType equal to
```
  SendAnEmail. If true, the email for this email step is sent as a reply to the email

```
conversation from the previous email step. By sending the email as a reply to a previous
email, customers see a "conversation" view of the emails. Only emails from the same action
cadence are grouped as conversations.

This field can’t be true for the first email step in an action cadence, because the first email
from an action cadence must start a new conversation with the prospect.

The default value is `false. This field is available in API version 49.0 and later.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The step name (ActionCadenceStep.StepName) of the previous step in the action
cadence. Must contain a valid step name value unless this step is the root step. null if this
step is a parent step.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the root step for this action cadence. Every action cadence has exactly one root
step (so that the Salesforce API can find all the steps for this cadence).

This field is a relationship field.

**Relationship Name**
RootStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ScheduledDaysUntilStart
ScheduledStartDelayInMinutes
ScheduledStartTimeInMinutes
ScreenFlowReference
StepAutomationReference

```

**Description**
The number of days after which this current step is due. Available in API version 58.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days when this step starts after the previous step completes. For delays of
greater than one day from ScheduledStartTimeInMinutes. Available in API version
58.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Any hard waits in minutes is captured in this field. Waits greater than 1 day need to set
```
  ScheduledDaysUntilStart. Available in API version 58.0 and later.

```
**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The specific time of day when the step starts. The time represents minutes after 00:00.
Available in API version 58.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The `namespace__fullname` of the screen flow. Used to describe flow objects and
launch flows client side.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
StepComments
StepName
StepTitle
TemplateId

```

**Description**
The name of the flow that the step uses. Cadence steps can launch a cadence step flow as
the step or as a cadence autolaunched flow when a rep completes the step. The format is
```
  namespace__fullName. This field is available in API version 56.0 and later.

```
**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A comment that provides additional information about this step.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier for this step. Generated by Salesforce.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title given to the step when it was created.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If a template was added to this step, this field contains the template's ID. For example, if this
step is a call step it can contain a template for a call script. Or, if this step is an email step, it
can contain a template for an email.

This field is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate


-----

```
Type
TypeDetail
UniqueEmailsLinkClickedCount
UniqueEmailsOpenedCount

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of step. Possible values are:

**•** `AutoSendAnEmail` — Salesforce automatically sends the specified email.

**•** `Branch — A branch step in the action cadence.`

**•** `CreateTask — Used for custom steps.`

**•** `DaisyChain — A daisy chain step. A daisy chain step connects this action cadence`
to another action cadence. It must be the last step in the path.

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch` — A branch step for emails.

**•** `MakeACall — The sales rep must call the prospect at this step.`

**•** `PlatformScreenFlow`

**•** `Root — This step is the root step for the action cadence.`

**•** `SendAnEmail — The sales rep must send the prospect an email at this step.`

**•** `Wait — A wait step tells the sales rep not to do anything at this point in the action`
cadence.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
More detail about the step type. If the step is a cadence step flow, this field contains the flow
name. Otherwise, this field contains the same value as the Type field. This field is available
in API version 56.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of links inside an email that the target clicked during this step. Multiple clicks
on the same link aren’t counted. This field is available in API version 50.0 and later.

**Type**
reference


-----

```
UniqueEmailsRepliedCount
WaitTimeInSeconds

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that the target opened as part of this step. Multiple openings of the
same email aren’t counted. This field is available in API version 50.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that targets replied to as part of this step. Multiple replies to the same
email aren’t counted. This field is available in API version 50.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required if the step type is `Wait. The time in seconds for this step to wait.`


Use ActionCadenceStep to see what steps your action cadence has:
```
select StepTitle from ActionCadenceStep where ActionCadence.ID= <the id of an action
cadence> and IsOrphan=false

##### Associated Objects

```
This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ActionCadenceStepChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

ActionCadence

ActionCadenceRule

ActionCadenceRuleCondition

ActionCadenceStepTracker


-----
