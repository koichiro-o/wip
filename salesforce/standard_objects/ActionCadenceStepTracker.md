#### ActionCadenceStepTracker

Represents a step in an active cadence for a specific cadence target. This object is available in API version 48.0 and later.

An ActionCadenceStepTracker record is created when a target moves to a new step in a cadence. Use ActionCadenceStepTracker to
find information such as the step's current state, the reason it completed, and its type.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
ActionCadenceId
ActionCadenceName
ActionCadenceStepId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ActionCadence that is related to the ActionCadenceStep.

This field is a relationship field.

**Relationship Name**
ActionCadence

**Relationship Type**
Lookup

**Refers To**
ActionCadence

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the related ActionCadence object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ActionCadenceStepTracker is the runtime version of an ActionCadenceStep. This field contains
the ID of the related ActionCadenceStep.

This field is a relationship field.


-----

```
ActionCadenceTrackerId
ActionTakenDateTime
CompletedById

```

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related ActionCadenceTracker.

This field is a relationship field.

**Relationship Name**
ActionCadenceTracker

**Relationship Type**
Lookup

**Refers To**
ActionCadenceTracker

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the action described in this step was taken.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user ID of the sales rep who completed this step. A step can be assigned to several users
before it’s completed. This field is available in API version 50.0 and later.

This field is a relationship field.

**Relationship Name**
CompletedBy

**Relationship Type**
Lookup


-----

```
CompletionDate
CompletionReason
DueDateTime
ErrorCode

```

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date this step completed. A step is completed either when the action is taken, or the
step is skipped.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason that this step completed: Possible values are:

**•** `AutomaticallyCompleted` — The sales rep successfully completed this step
and moved to the next one. Salesforce automatically marks this step as completed.

**•** `AutomaticallyExited` — The step exited because a global exit condition
occurred. This value is available in API version 49.0 and later.

**•** `ManuallyCompleted` — The sales rep manually marked this step as completed.

**•** `ManuallySkipped` — The sales rep skipped this step.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Some steps have a due date to indicate when they must be completed. If this step has been
assigned a due date, this field contains the date and time it is due.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `AUTO_EMAIL_DAILY_LIMIT_REACHED`

**•** `AUTO_EMAIL_ORG_SETTING_OFF`

**•** `AUTO_LIST_MQ_MAX_RETRIES_FAILED`


-----

**•** `BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED`

**•** `EAC_GLOBAL_DATA_SOURCE_ERROR—EAC data source error`

**•** `EMAIL_ORG_SETTING_OFF`

**•** `EXCHANGE_MAX_MAILBOX_SIZE—Max Exchange mailbox size reached`

**•** `EXCHANGE_SEND_AS_DENIED`

**•** `FIX_WITH_RECONNECT—Data connection failed`

**•** `GOOGLE_MAIL_SERVICE_NOT_ENABLED—Gmail service not enabled`

**•** `INVALID_DRAFT—Invalid email draft`

**•** `INVALID_TARGET_EMAIL`

**•** `INVALID_TEMPLATE_ID`

**•** `INVALID_USER_EMAIL`

**•** `MAIL_PROVIDER_RATE_LIMIT_REACHED—Email provider rate limit reached`

**•** `NON_EMAIL_UNKNOWN_ERROR—Unknown error`

**•** `NO_ATTACHMENT_ACCESS`

**•** `NO_CONTENT_VERSION_ACCESS`

**•** `NO_LIST_EMAIL_PERMISSION`

**•** `NO_TARGET_ACCESS`

**•** `ORG_WIDE_AUTO_EMAIL_LIMIT_REACHED`

**•** `ORG_WIDE_DAILY_EMAIL_LIMIT_REACHED`

**•** `OTHER_REQ_FIELD_MISSING—Other required field missing`

**•** `PARDOT_MERGE_FIELD_RENDERING_ERROR`

**•** `POST_SEND_EXCEPTION`

**•** `RETRIES_MAX_EXCEEDED—Maximum retries exceeded`

**•** `RETRY_LATER`

**•** `SCHEDULED_EMAIL_FAILED—Unknown error`

**•** `SENDER_MAILBOX_NOT_FOUND`

**•** `TARGET_DO_NOT_CONTACT_ON—Target has Do Not Contact on`

**•** `TARGET_EMAIL_BOUNCED`

**•** `TARGET_EMAIL_EMPTY`

**•** `TEMPLATE_DELETED`

**•** `TEMPLATE_EMPTY—Email subject or body missing`

**•** `TEMPLATE_HAS_INVALID_MERGE_FIELD`

**•** `TEMPLATE_MERGE_FIELD_RENDERING_ERROR`

**•** `TEMPLATE_NOT_PUBLIC—No access to template`

**•** `TEMPLATE_TOO_LARGE`

**•** `UNKNOWN—Email unknown error`

**•** `USER_HAS_LOST_HVS_ACCESS`

**•** `USER_IS_INACTIVE`


-----

```
GoToStepIterationCount
IsActionTaken
ScheduledStartDateTime
SecondsOverdue
State

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the action cadence step tracker was created for the same step in a
cadence. Available in API version 58.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the sales rep completed an action during this step, such as making a phone call,
otherwise `false.`

The default value is `false.`

This field is a calculated field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the step starts. Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this step has a due date that has passed, this field contains the number of seconds that
has elapsed since the due date. Once a sales rep takes action on the cadence step, the value
of this field is the number of seconds elapsed between the due date and the time the action
was taken.

This field is a calculated field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
StepTitle
StepType

```

**Description**
The current state of this step. Possible values are:

Possible values are:

**•** `Active` — The current step that the sales rep is performing. There can only be one
active step for a given target.

**•** `Cancelled` — The sales rep canceled the step. Salesforce doesn’t run any canceled
steps.

**•** `Completed` — This step is finished. Either the work in the step completed, or the step
was skipped.

**•** `Error` — An error occurred while executing this step.

**•** `InProgress` — The sales rep has started the step, but it isn’t yet completed.

**•** `Paused` —The sales rep paused the step.

**•** `Queued` — Used for automated email steps. The email step has started but the email
is waiting in the queue to be sent.

**•** `Scheduled` — Used for email steps. An email can be scheduled to be sent later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the related step.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of step to execute. Possible values are:

**•** `AutoSendAnEmail`

**•** `Branch`

**•** `CreateTask`

**•** `DaisyChain`

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`

**•** `MakeACall`

**•** `PlatformScreenFlow`

**•** `Root`

**•** `SendAnEmail`


-----

```
TargetId
WasEverPaused

##### Usage

```


**•** `SubRoot`

**•** `Wait`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the prospect that is assigned to this cadence.

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the sales rep had ever paused this step (true), or not (false). This field
is available in API version 50.0 and later.


List all the steps that this prospect has completed in a given cadence:
```
select StepTitle from ActionCadenceStepTracker where TargetID = <target ID>
      and ActionCadenceId=<action cadence id> and StepType="Completed"

##### Associated Objects

```
This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**ActionCadenceStepTrackerChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

ActionCadence

ActionCadenceRule

ActionCadenceStep

ActionCadenceRuleCondition
