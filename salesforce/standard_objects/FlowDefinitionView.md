#### FlowDefinitionView

```
Represents the description of a flow definition. This object is available in API version 46.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
ActiveVersionId
ApiName
ApiVersion

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active flow version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow definition.

**Type**
string


-----

```
AreMetricsLoggedToDataCloud
Builder
CapacityCategory
Description

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the flow definition.

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value is
false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Possible values are:

**•** Cloud Flow Designer

**•** Flow Builder

**•** Swing Designer

This field is available in API version 47.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow definition information, specified by the org’s admin.


-----

```
DurableId
Environments
HasAsyncAfterCommitPath
InstalledPackageName
IsActive

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow definition.

**Type**
multipicklist

**Properties**
Filter, Nillable

**Description**
The environment in which the flow can run. Valid values are:

**•** `Default—The flow can run from a Visualforce component, Lightning page,`
flow action, or custom Aura component.

**•** `Offline—The flow can run only offline. Flow types that support offline flows`
must set this value. This value is available in API version 62.0 and later.

**•** `Slack—The flow can run in Slack and the default environment. You specify`
the Slack flow environment when you save the flow.

This field is available in API version 55.0 to 62.0. This field is deprecated in API version
63.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the scheduled path runs asynchronously after a save. The default
value is false. This field is available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the installed package that includes this flow definition.

This field is available in API version 47.0 and later.

**Type**
boolean


-----

```
IsOutOfDate
IsOverridable
IsSwingFlow
IsTemplate

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the latest version of the flow definition is the active flow version.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the active flow version is the latest version of the flow definition.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is overridable. The default value is false. This field is available
in API version 53.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is built with Desktop Flow Designer.

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the process or flow is a template. The default value is `false.`
When installed from managed packages, subscribers can’t view or clone processes
or flows because of intellectual property (IP) protection. But when those processes
and flows are templates, subscribers can open them in a builder, clone them, and
customize the clones.

This field is available in API version 47.0 and later.


-----

```
Label
LastModifiedBy
LatestVersionId
ManageableState

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who last updated this flow definition.

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the latest flow version, regardless of the flow’s status.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the manageable state of the flow that is contained in a package. Possible
values are:

**•** `beta`

**•** `deleted`

**•** `deprecated`

**•** `deprecatedEditable`

**•** `installed`

**•** `installedEditable`

**•** `released`

**•** `unmanaged`

This field is available in API version 47.0 and later.


-----

```
NamespacePrefix
OverriddenById
OverriddenFlowId
ProcessType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the flow definition.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The flow that’s overriding the current flow. This is a relationship field. This field is
available in API version 53.0 and later.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The flow that the current flow is overriding. This is a relationship field. This field is
available in API version 53.0 and later.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the flow. Valid values are:


-----

**•** `ActionableEventManagementFlow—A flow that triggers an actionable`
event orchestration process in the background and automatically executes
different types of actions based on the event type. This value is available in API
version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow—A flow that’s executed when a`
user completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow—A screen flow used as a cadence step. This`
value is available in API version 56.0 and later.

**•** `Appointments—A flow for Lightning Scheduler. This value is available in API`
version 44.0 and later.

**•** `ApprovalWorkflow—An orchestration that’s used for an approval process.`
This value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow—A flow that doesn’t require user interaction.`

**•** `CheckoutFlow—A flow used in Lightning B2B Commerce to create a checkout`
in a store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow—A flow that lets customers request to be contacted`
by customer support. This flow is used to create contact request records. This
value is available in API version 45.0 and later.

**•** `CustomerLifecycle—A Salesforce Surveys flow that lets you associate`
survey questions with different stages in customer lifecycles. This value is available
in API version 49.0 and later and only when the Customer Lifecycle Designer
license is enabled.

**•** `CustomEvent—A process that is invoked when it receives a platform event`
message. In the UI, it’s an event process. This value is available in API version 41.0
and later.

**•** `DataCaptureFlow— In the UI, Data Capture flows configure the Form tab`
in the Field Service mobile app. When the Data Capture flow is launched, its Flow
metadata is publicly available in JavaScript format. This value is available in API
version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow—A screen flow that presents`
assessment questions from Discovery Framework. Launches when invoked by a
user on a mobile device. This type of flow collects or displays information, requires
user interaction, and works offline or online. This value is available in API version
62.0 and later.

**•** `EvaluationFlow—A flow for evaluating custom entry and exit conditions`
in an orchestration. Uses the `isOrchestrationConditionMet` output
variable and discards values from any other output variables. This value is available
in API version 54.0 and later.

**•** `FieldServiceMobile—A flow for the Field Service mobile app. This value`
is available in API version 39.0 and later.

**•** `FieldServiceWeb—A flow for embedded Appointment Booking. Its UI`
label is Field Service Embedded Flow. This value is available in API version 41.0
and later.


-----

**•** `Flow—A flow that requires user interaction because it contains one or more`
screens or local actions, choices, or dynamic choices. In the UI and Salesforce
Help, it’s a screen flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.

**•** `FSCLending—A flow for Financial Services Cloud Mortgage. This value is`
available in API version 46.0 and later.

**•** `IndicatorResultFlow—A flow for Outcome Management that calculates`
and creates indicator results for a selected indicator performance period. This
value is available with the Outcome Management license in API version 60.0 and
later.

**•** `IndividualObjectLinkingFlow—A flow that associates individuals`
with interactions such as voice calls, messaging sessions, or case-related emails.
This value is available in API version 58.0 and later.

**•** `InvocableProcess—A process that another process or the Invocable`
Actions resource in REST API invokes. This value is available in API version 38.0
and later.

**•** `Journey—An audience-driven flow for Marketing Cloud. This value is available`
in API version 57.0 and later.

**•** `LoginFlow—A flow for login. This value is available in API version 51.0 and`
later.

**•** `LoyaltyManagementFlow—A flow for the Loyalty Management app that’s`
invokable by loyalty program processes. This value is available in API version 54.0
and later.

**•** `Orchestrator—An orchestration that organizes flows into groups of steps`
contained in a series of stages. This value is available in API version 53.0 and later.

**•** `PromptFlow—A flow for Prompt Builder. Pass data between Prompt Builder`
and the flow. This value is available in API version 60.0 and later.

**•** `RecommendationStrategy—Build recommendations for your users. A`
recommendation launches its assigned flow. This value is available in API version
[54.0 and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=sf.nba_building_flow_builder_strategy.htm&language=en_US)

**•** `RoutingFlow—A flow for Salesforce Omni-Channel routing and other business`
logic. This value is available in API version 52.0 and later.

**•** `Survey—A flow for Salesforce Surveys. From the UI, this type of flow is created`
in Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich—A Salesforce Surveys flow that uses the Survey Data Mapper.`
From the UI, this type of flow is created in the Survey Builder and requires an
associated survey flow type. This value is available in API version 49.0 or later and
only when the Customer Lifecycle Designer license is enabled.

**•** `Workflow—A process that is invoked when a record is created or edited. In`
the UI and Salesforce Help, it’s a record change process.

These values are reserved for future use:

**•** `ActionCadenceFlow`

**•** `ActionPlan`


-----

```
RecordTriggerType
SourceTemplateId

```


**•** `AppProcess`

**•** `ApprovalWorkflow`

**•** `CartAsyncFlow`

**•** `DigitalForm`

**•** `JourneyBuilderIntegration`

**•** `LoginFlow`

**•** `ManagedContentFlow`

**•** `OrchestrationFlow`

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

This value has significant impact on validation when saving the flow and on the flow’s
runtime behavior. Don’t change this value unless you understand the flow properties
of the specified type.

Across flow versions, you can change the type only from `Flow` to
`AutoLaunchedFlow` or vice versa. Before you change the flow type, make sure that
the flow contains only the elements, resources, and functionality that the new flow type
supports.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies what type of record changes can start the flow. Possible values are:

**•** `Create`

**•** `CreateAndUpdate`

**•** `Delete`

**•** `None`

**•** `Update`

Available only when `triggerType` is RecordBeforeSave. This field is
available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The template that the current flow was created from. This is a relationship field. This
field is available in API version 53.0 and later.


-----

```
SupportedEnvironments
TriggerObjectOrEventId
TriggerObjectOrEventLabel

```

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Nillable

**Description**
The environment in which the flow can run. Valid values are:

**•** `Default—The flow can run from a Visualforce component, Lightning page,`
flow action, or custom Aura component.

**•** `Offline—The flow can run only offline. Flow types that support offline flows`
must set this value.

**•** `Slack—The flow can run in Slack and the default environment. You specify`
the Slack flow environment when you save the flow.

This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
ID of the object or platform event that triggers this flow. This field is available in API
version 53.0 and later.

This is a relationship field.

**Relationship Name**
TriggerObjectOrEvent

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
TriggerOrder
TriggerType

```

**Description**
The label of the object or platform event that triggers this flow. This field is available
in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
[The run order of a record-triggered flow, from 1 to 2,000. See "Guidelines for Defining](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
[the Run Order of Record-Triggered Flows for an Object" in Salesforce Help. Available](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
in API version 54.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies what causes the flow to run. If you exclude this field, the flow has no trigger
and starts only when a user or app launches the flow. Valid values are:

**•** `AutomationEvent—The flow starts when an automation event such as an`
SMS subscription occurs. This value is available in API version 62.0 and later.

**•** `Capability—The flow starts when the specified capability that the flow`
integrates with is invoked. This value is available in API version 60.0 and later.

**•** `DataCloudDataChange—The flow starts when data model object (DMO)`
or calculated insight object (CIO) conditions are met. This value is available in API
version 59.0 and later.

**•** `DataGraphDataChange—The flow starts when conditions are met in the`
specified data graph field. This value is available in API version 63.0 and later.

**•** `EventDrivenJourney—Reserved for internal use.`

**•** `ExternalSystemChange—The flow starts when an external system change`
event is received. This value is available in API version 61.0 and later.

**•** `FormSubmissionEvent—The flow runs when a user submits data via a`
webform. In Flow Builder, this value corresponds to Form. This value is available
in API version 60.0 and later.

**•** `PlatformEvent—The flow starts when a platform event message is received.`
This value is available in API version 49.0 and later.

**•** `RecordAfterSave—The flow starts after a record is saved. This value is`
available in API version 49.0 and later.

**•** `RecordBeforeDelete—Deleting a record triggers an autolaunched flow`
before the record is deleted from the database. This value is available in API version
50.0 and later.


-----

```
VersionNumber

##### Usage

```


**•** `RecordBeforeSave—Creating and/or updating a record triggers an`
autolaunched flow to make additional updates to that record before it's saved to
the database. This value is available in API version 48.0 and later.

**•** `Scheduled—The flow starts at the scheduled time. This value is available in`
API version 47.0 and later.

**•** `Segment— At the scheduled time, the flow send emails to individuals included`
in the chosen segment. This value is available in API version 56.0 and later.

Available only when `processType` is `AutoLaunchedFlow` or `PromptFlow.`
This field is available in API version 47.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow’s version number. This field is available in API version 54.0 and later.


Use this object to query information about flow definitions.
