#### FlowRecord

Represents the details of a flow. This object is available in API version 58.0 and later.

##### Supported Calls
```
delete(), query(), update()

 Fields

```
```
ActiveVersionId
ApiVersion
AreMetricsLoggedToDataCloud

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active flow version. This field is available in API version 61.0 and
later.

This field is a relationship field.

**Relationship Name**
ActiveVersion

**Relationship Type**
Lookup

**Refers To**
FlowRecordVersion

**Type**
double

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the flow record. This field is available in API version 61.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value
is false. This field is available in API version 63.0 and later.


-----

```
AssociatedRecordId
Builder
CapacityCategory
Description

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record the flow is associated with.

This field is a polymorphic relationship field.

**Relationship Name**
AssociatedRecord

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Valid values are:

**•** `Cloud Flow Designer`

**•** `Flow Builder`

**•** `Swing Designer`

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the flow.


-----

```
ErrorCode
ErrorDetails

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The error code if the flow element run encountered an error. Valid values are:

**•** `ACTIVATING_USER_ACCOUNT_DEACTIVATED—We can't run this`
flow because the user who activated it has a deactivated user record.

**•** `ACTIVATING_USER_LOST_PERMISSIONS—We can't run this flow`
because the user that activated it no longer has permission to it.

**•** `CANNOT_PUBLISH_SEGMENT—We can't run this flow because we can't`
publish the segment it's using. Contact Salesforce Customer Support and
ask for help with the error ID.

**•** `CANNOT_QUERY_SEGMENT_MEMBER_DATA—We can't run this flow`
because we can't query the segment membership data it's using. Contact
Salesforce Customer Support and ask for help with the error ID.

**•** `CANNOT_REFRESH_DATA_STREAM—We can't run this flow because`
we can't refresh your data stream metadata. Contact Salesforce Customer
Support and ask for help with the error ID.

**•** `CANNOT_REFRESH_IDENTITY_RES_DATA—We can't run this flow`
because we can't refresh your identity resolution data. Contact Salesforce
Customer Support and ask for help with the error ID.

**•** `CANNOT_REFRESH_IDENTITY_RES_METADATA—We can't run this`
flow because we can't refresh your identity resolution metadata. Contact
Salesforce Customer Support and ask for help with the error ID.

**•** `CANNOT_UPDATE_DATASTREAM_METADATA—We can't run this flow`
because we can't update your DataStream metadata. Contact Salesforce
Customer Support and ask for help with the error ID.

**•** `CREATE_EXPERIMENT_ERROR—We can't run this flow because an`
error occurred while executing the Path Experiment element. To try again,
save and activate a new version of the flow.

**•** `DATA_ACTION_STATUS_ERROR—We can’t run this flow because we`
couldn’t create the data action. To try again, save and activate a new version
of the flow.

**•** `FLOW_FAILED_TO_START—This flow failed to start. Contact Salesforce`
Customer Support and ask for help with the error ID.

This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
FlowCategory
FlowDefinition
FlowSubcategory
FlowType

```

**Description**
The error ID. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of a category. Sharing rules assign permissions to view and edit
flows by category and subcategory. This field is available in API version 60.0 and
later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of a subcategory. Sharing rules assign permissions to view and
edit flows by category and subcategory. This field is available in API version 60.0
and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The label of a flow type. `FlowType consolidates` `ProcessType` and
`TriggerType` into one field. FlowType is used with permissions, so admins
can control access to each flow type. Valid values are:

**•** `Action Cadence Autolaunched Flow—Launches after a sales`
step is completed. This type of flow runs in the background without user
interaction.

**•** `Action Cadence Step Screen Flow—Launches from a cadence`
step. This type of flow collects or displays information and requires user
interaction.


-----

**•** `Action Plan Autolaunched Flow—Launches an action plan`
task from an action plan when conditions in the associated action plan
template process are met. This type of flow runs in the background without
user interaction.

**•** `Autolaunched Approval Orchestration—Launches when`
invoked by Apex, REST API, custom buttons, or custom links. An approval
orchestration lets you create a multi-step, multi-user approval process.

**•** `Autolaunched No Trigger Flow—Launches when invoked by`
processes or code such as Apex and REST API. This type of flow runs in the
background without user interaction.

**•** `Autolaunched No Trigger Orchestration—Launches when`
invoked by Apex, REST API, custom buttons, or custom links. An orchestration
lets you create a multi-step, multi-user process.

**•** `Automation Event-Triggered Flow—Launches when a user`
performs an automation event, like subscribing to SMS messages. This type
of flow runs in the background without user interaction.

**•** `Cart Async Autolaunched Flow—Launches when invoked by`
a cart change, such as an Add to Cart. This type of flow runs in the background
without user interaction.

**•** `Checkout Screen Flow—Create a screen flow that implements a`
Commerce Cloud checkout process. This type of flow collects or displays
information and requires user interaction.

**•** `CMS Workflow Orchestration Autolaunched—Launches`
when invoked from the Workflows component in a CMS workspace. This
type of orchestration lets you create a multi-step, multi-user process to create,
edit, organize, and manage digital content from a centralized location.

**•** `Contact Request Screen Flow—Launches when invoked by a`
customer, allowing them to enter contact details into a self-service form. This
type of flow collects or displays information and requires user interaction.

**•** `Customer Lifecycle Record-Triggered After Save`
```
  Flow—Launches after a customer lifecycle map is saved and changes

```
records related to the triggering record. This type of flow runs in the
background without user interaction.

**•** `Data Cloud Data Change Flow—Launches when a record from`
a Data Cloud data model object or a calculated insight object is changed and
meets the specified conditions. This type of flow runs in the background
without user interaction.

**•** `Digital Form Screen Flow—Launches from app extensions. This`
type of flow collects or displays information and requires user interaction.

**•** `Discovery Framework Data Capture Screen Flow`
```
  (Beta)—Launches when invoked by a user on a mobile device and

```
presents assessment questions from Discovery Framework. This type of flow
collects or displays information and requires user interaction.


-----

**•** `Employee Service Catalog Item Screen Flow—Launches`
when invoked by a user and allows them to browse and order items from
the Employee Service Catalog. This type of flow collects or displays information
and requires user interaction.

**•** `Evaluation Autolaunched Flow—Launches when invoked by`
an orchestration to evaluate custom criteria for a stage or step. To indicate
that the criteria are met, set the output variable
```
  isOrchestrationConditionMet to true. This type of flow runs

```
in the background without user interaction.

**•** `External System Change-Triggered Flow—Launches when`
an event is received from an external system. This type of flow runs in the
background without user interaction.

**•** `Event-Driven Flow—Launches when an event is received. This type`
of flow runs in the background without user interaction.

**•** `Field Service Mobile Screen Flow—Launches when invoked`
by a user in the Field Service mobile app. This type of flow collects or displays
information and requires user interaction.

**•** `Field Service Web Screen Flow—Launches from the Field`
Service app and lets users schedule, modify, or cancel an appointment in a
web browser. This type of flow requires user interaction.

**•** `Form-Triggered Flow—Launches when a web visitor submits a`
marketing form. This type of flow runs in the background without user
interaction.

**•** `Indicator Result Screen Flow—Launches a screen flow when`
initiated by a user to calculate and create indicator results for a selected
indicator performance period.

**•** `Individual-Object Linking Screen Flow—Launches when`
invoked by an agent to link a record like a case or messaging session to a
contact, lead, person account, or employee. This type of flow collects or
displays information and requires user interaction.

**•** `Login Screen Flow—Launches when a user tries to log in to`
Salesforce. This type of flow extends Salesforce's default authentication
process by sending users with certain profiles through a flow when they log
in and requires user interaction.

**•** `Loyalty Management Autolaunched Flow—Launches when`
invoked by a loyalty program process, and contains Assignment, Decision,
and Action elements. The Action element in this type of flow supports Apex
and quick actions. This type of flow runs in the background without user
interaction.

**•** `Managed Content Autolaunched Flow—Launches when`
invoked by the ManagedContentRelease translator. This type of flow runs in
the background without user interaction.


-----

**•** `Mortgage Lending Screen Flow—Launches when invoked by`
a user and allows them to provide Financial Service Cloud mortgage
application details. This type of flow requires user interaction.

**•** `Platform Event Triggered Flow—Launches when a platform`
event occurs. This type of flow runs in the background without user
interaction.

**•** `Process Builder Autolaunched Process—Launched when`
invoked from a Process Builder process. This type of flow runs in the
background without user interaction.

**•** `Process Builder Custom Event Process—A process created`
in Process Builder that launches when a custom event message is received.
This type of process runs in the background without user interaction.

**•** `Process Builder Workflow—Launches when a record is created`
or updated. This type of process runs in the background without user
interaction.

**•** `Prompt Template Capability-Triggered Flow—Launches`
from a prompt template. This type of flow adds prompt instructions to the
associated prompt template and runs in the background without user
interaction.

**•** `Recommendation Strategy Autolaunched Flow—Build a`
personalized list of recommendations. When a recommendation is selected,
it launches its assigned flow. Used by Einstein Next Best Action. Show
recommendations in Lightning App Builder with the Einstein Next Best Action
component and in Experience Builder with the Suggested Actions component.

**•** `Record-Triggered After Save Flow—Launches after a record`
is created or updated and has been saved. This type of flow can make changes
only to records related to the triggering record and runs in the background
without user interaction.

**•** `Record-Triggered After Save Approval`
```
  Orchestration—Launches when a record is created or updated. An

```
approval orchestration lets you create a multi-step, multi-user approval
process.

**•** `Record-Triggered After Save Orchestration—Launches`
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered Before Delete Flow—Launches when a`
record is deleted. This type of flow runs in the background without user
interaction.

**•** `Record-Triggered Before Save Flow—Launches after a record`
is created or updated, but hasn't been saved. This type of flow can make
changes only to the triggering record and runs in the background without
user interaction.


-----

```
Id
IsLightningAppEnabled

```


**•** `Routing Autolaunched Flow—Launches when a customer initiates`
a chat, voice, or messaging conversation and routes the work item to a queue,
skill, agent, or bot. This type of flow runs in the background without user
interaction.

**•** `Schedule-Triggered Flow—Launches at a specified time and`
frequency for each record that meets the flow criteria. This type of flow runs
in the background without user interaction.

**•** `Scheduler Appointments Screen Flow—Launches when`
invoked by a user and lets them schedule appointments in Salesforce
Scheduler. This type of flow collects or displays information and requires user
interaction.

**•** `Screen Flow—Launches from Lightning pages, Experience Cloud sites,`
quick actions and more. This type of flow collects or displays information and
requires user interaction.

**•** `Segment-Triggered Flow—Launches when activated or when`
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction.

**•** `Survey Enrich Autolaunched Flow—Launches in the context`
of a survey response and can't execute without a corresponding survey. Use
it to conditionally map a response to a record, create records, or send
notifications. This type of flow runs in the background without user
interaction.

**•** `Survey Screen Flow—Launches when invoked by an internal or`
external survey participant. This type of flow saves participant feedback as
survey response records and requires user interaction.

**•** `Transaction Security Autolaunched Flow—Used by`
Condition Builder to declaratively build customized security policies to protect
data. This type of flow runs in the background without user interaction.

**•** `User Provisioning Screen Flow—Launches when invoked by`
a user and allows them to create a user account and link it to a third-party
service or app. This type of flow requires user interaction.

This field is available in API version 60.0 and later.

**Type**
text

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow.

**Type**
boolean


-----

```
IsOverridable
IsTemplate
IsPaused
Manageable State

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s flow type has been enabled in Lightning Experience
apps. The default value is `false. This field is available in API version 61.0 and`
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is overridable. The default value is
```
  false. This field is available in API version 61.0 and later.

```
**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is a template. Template flow record
versions are automatically shared with all users in your Salesforce org. The default
value is `false. This field is available in API version 61.0 and later.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the segment-triggered flow is paused (true) or not (false).
When the value is `true, no additional records are processed until the flow is`
resumed. The default value is `false. This field is available in API version 60.0`
and later.

**Type**
boolean

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates the manageable state of the flow record that is contained in a package.
Valid values are:

**•** beta


-----

```
Name
NamespacePrefix
OverriddenById
OverriddenFlowId

```


**•** deleted

**•** deprecated

**•** deprecatedEditable

**•** installed

**•** installedEditable

**•** released

**•** unmanaged

This field is available in API version 60.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label of the flow.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the flow record. This field is available in
API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that’s overriding the current flow. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
reference


-----

```
OwnerId
ProgressStatus

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that the current flow is overriding. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user who owns the flow.

This field is a polymorphic relationship field.

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

**Description**
The progress status of the flow. Valid values are:

**•** `Canceled— Indicates a flow that has been deactivated by a user who`
doesn’t process previously added records. No additional records are added
to this flow.

**•** `Completed— Indicates a flow that is complete. No additional records are`
eligible to be processed in this flow.

**•** `Draft—Indicates a flow that is under construction and isn’t active yet. This`
status can be invalid because it needs additional information before it can
be activated by the user.


-----

```
ScheduledStartDate
SegmentId
SourceTemplateId

```


**•** `Error—Indicates a flow that has been deactivated because it encountered`
an error. When the error occurs, the error details are emailed to up to 5 users
with the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing— Indicates a flow that has been deactivated by a user, but is`
finishing previously added records that are eligible to run to completion. No
additional records are added to this flow.

**•** `InProgress— Indicates a flow that is running or ready to run.`

**•** `PreparingData— Indicates a flow that is preparing the necessary data`
to run. This process can take up to 2 hours.

**•** `Scheduled— Indicates a flow scheduled to start on the date and time`
selected by the user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the flow is scheduled to start.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the segment used in the flow.

This field is a relationship field.

**Relationship Name**
Segment

**Relationship Type**
Lookup

**Refers To**
MarketSegment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template from which the current flow was created. This field is
available in API version 61.0 and later.

This field is a relationship field.


-----

```
TriggerObjectOrEventLabel
Type

```

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow. This field is
available in API version 61.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The trigger type of the flow. Specifies what causes the flow to run. Valid values
are:

**•** `Automation Event—The flow starts when an automation event such`
as an SMS subscription occurs. This value is available in API version 62.0 and
later.

**•** `Capability—The flow starts when the specified capability that the flow`
integrates with is invoked. This value is available in API version 60.0 and later.

**•** `DataCloudDataChange—The flow starts when data model object`
(DMO) or calculated insight object (CIO) conditions are met. This value is
available in API version 59.0 and later.

**•** `DataGraphDataChange—The flow starts when conditions are met in`
the specified data graph field. This value is available in API version 63.0 and
later.

**•** `EventDrivenJourney—Reserved for internal use.`

**•** `ExternalSystemChange—The flow starts when an external system`
change event is received. This value is available in API version 61.0 and later.

**•** `FormSubmissionEvent—The flow runs when a user submits data via`
a webform. In Flow Builder, this value corresponds to `Form. This value is`
available in API version 60.0 and later.

**•** `PlatformEvent—The flow starts when a platform event message is`
received. This value is available in API version 49.0 and later.


-----

**•** `RecordAfterSave—The flow starts after a record is saved. This value`
is available in API version 49.0 and later.

**•** `RecordBeforeDelete—Deleting a record triggers an autolaunched`
flow before the record is deleted from the database. This value is available
in API version 50.0 and later.

**•** `RecordBeforeSave—Creating and/or updating a record triggers an`
autolaunched flow to make additional updates to that record before it's saved
to the database. This value is available in API version 48.0 and later.

**•** `Scheduled—The flow starts at the scheduled time. This value is available`
in API version 47.0 and later.

**•** `Segment—The flow runs at the scheduled time of a segment.`

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**FlowRecordChangeEvent (API version 62.0)**
Change events are available for the object.

**FlowRecordOwnerSharingRule**

Sharing rules are available for the object.

**FlowRecordShare**

Sharing is available for the object.
