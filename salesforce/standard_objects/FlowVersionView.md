#### FlowVersionView

Represents the version of a flow definition. This object is available in API version 46.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
ApiVersion
ApiVersionRuntime
AreMetricsLoggedToDataCloud

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for the flow definition. Every flow version has an API version specified
at creation.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for running the flow. This value determines which versioned run-time
behavior improvements are adopted by the flow version.

If not specified when the flow or flow version is created, the latest available API version
is used as the API version for running the flow. When an existing flow is saved as a
new flow or flow version, the existing flow’s run-time API version is used in the new
flow or flow version.

This field is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
CapabilityType
CapacityCategory
Description
DurableId
FlowDefinitionViewId

```

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value is
false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The capability that integrates with the flow. An example value is
```
  PromptTemplateType://SalesEmail.

```
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
Flow version information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition.


-----

```
IsSwingFlow
IsTemplate
Label
ProcessType

```

This field s a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is built with Desktop Flow Designer.

This field is available in API version 49.0 and later.

Default: false

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the process or flow is a template. When installed from managed
packages, processes and flows can’t be viewed or cloned by subscribers because of
intellectual property (IP) protection. But when those processes and flows are templates,
subscribers can open them in a builder, clone them, and customize the clones.
Available in API version 46.0 and later.

Default: false

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow—A flow that triggers an actionable`
event orchestration process in the background and automatically executes
different types of actions based on the event type. This value is available in API
version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow—A flow executed when a user`
completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow—A screen flow used as a cadence step. This`
value is available in API version 56.0 and later.

**•** `Appointments—A flow for Lightning Scheduler. This value is available in API`
version 44.0 and later.

**•** `ApprovalWorkflow—An orchestration for approvals. This value is available`
in API version 62.0 and later.

**•** `AutoLaunchedFlow—A flow that doesn’t require user interaction.`

**•** `CheckoutFlow—A flow used in Lightning B2B Commerce to create a checkout`
in a store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow—A flow that lets customers request that customer`
support get back to them. This flow is used to create contact request records.
This value is available in API version 45.0 and later.

**•** `CustomerLifecycle—A Salesforce Surveys flow that lets you associate`
survey questions with different stages in customer lifecycles. This value is available
in API version 49.0 and later and only when the Customer Lifecycle Designer
license is enabled.

**•** `CustomEvent—A process that is invoked when it receives a platform event`
message. In the UI, it’s an event process. This value is available in API version 41.0
and later.

**•** `DataCaptureFlow—A flow that configures the Form tab on Work Order`
Overview or the related list for a service appointment or a work order line item.
This value is available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow—A screen flow that presents`
assessment questions from Discovery Framework. Launches when invoked by a
user on a mobile device. This type of flow collects or displays information, requires
user interaction, and works offline or online. This value is available in API version
62.0 and later.

**•** `FieldServiceMobile—A flow for the Field Service mobile app. This value`
is available in API version 39.0 and later.

**•** `FieldServiceWeb—A flow for embedded Appointment Booking. Its UI`
label is Field Service Embedded Flow. This value is available in API version 41.0
and later.

**•** `Flow—A flow that requires user interaction because it contains one or more`
screens or local actions, choices, or dynamic choices. In the UI and Salesforce


-----

Help, it’s a screen flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.

**•** `FSCLending—A flow for Financial Services Cloud Mortgage. This value is`
available in API version 46.0 and later.

**•** `FSCLending—A flow for login. This value is available in API version 51.0 and`
later.

**•** `IndicatorResultFlow—A flow for Outcome Management that calculates`
and creates indicator results for a selected indicator performance period. This
value is available with the Outcome Management license in API version 60.0 and
later.

**•** `IndividualObjectLinkingFlow—A screen flow that helps search for`
contacts, leads, person accounts, and employees and links them to support
interactions. This value is available in API version 58.0 and later.

**•** `InvocableProcess—A process that can be invoked by another process or`
the Invocable Actions resource in REST API. This value is available in API version
38.0 and later.

**•** `LoyaltyManagementFlow—A flow for the Loyalty Management app and`
can be invoked by loyalty program processes. This value is available in API version
54.0 and later.

**•** `PromptFlow—A flow for Prompt Builder. Pass data between Prompt Builder`
and the flow. This value is available in API version 60.0 and later.

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

These values are reserved for future use.

**•** `ActionCadenceFlow`

**•** `ActionPlan`

**•** `ActivitySmartMatchingFlow`

**•** `AppProcess`

**•** `CartAsyncFlow`

**•** `DigitalForm`

**•** `Journey`

**•** `JourneyBuilderIntegration`

**•** `LoginFlow`

**•** `ManagedContentFlow`


-----

```
RunInMode
Status
VersionNumber

```


**•** `OrchestrationFlow`

**•** `RecommendationStrategy`

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

This value has significant impact on validation when saving the flow and on the flow’s
runtime behavior. Don’t change this value unless you understand the flow properties
of the specified type.

Across flow versions, you can change the type only from `Flow` to
`AutoLaunchedFlow` or vice versa. Before you change the flow type, make sure that
the flow contains only elements, resources, and functionality that the new flow type
supports.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the flow runs in. Valid values are:

**•** DefaultMode — The flow version runs in system or user context, depending on
how the flow is launched.

**•** SystemModeWithSharing — The flow version always runs in system mode with
sharing. The flow respects org-wide default settings, role hierarchies, sharing
rules, manual sharing, teams, and territories. But it doesn’t respect object
permissions, field-level access, or other permissions of the running user.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The flow’s status.

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The flow’s version number.

##### Usage

Use this object to query information about flow versions. A query must be filtered by DurableId or `FlowDefinitionViewId`
to get results.
