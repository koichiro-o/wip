#### FlowNavMetricEventLog

Flow Navigation Metric event logs contain metric data for flow interviews such as total execution time, number of interviews, and number
of errors. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.


-----

##### Fields

**Field**
```
ErrorCount
FlowLoadTime
FlowVersionIdentifier
InterviewCount
ProcessType

```

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of errors for all flow interviews after the flow version was executed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds to load the flow’s metadata.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version that was executed.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of flow interviews that started after the flow version was executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow—A flow that triggers an actionable event`
orchestration process in the background and automatically executes different types of
actions based on the event type. This value is available in API version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow—A flow that’s executed when a user`
completes a cadence step. This value is available in API version 56.0 and later.


-----

**•** `ActionCadenceStepFlow—A screen flow used as a cadence step. This value is`
available in API version 56.0 and later.

**•** `Appointments—A flow for Lightning Scheduler. This value is available in API version`
44.0 and later.

**•** `ApprovalWorkflow—An orchestration that’s used for an approval process. This`
value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow—A flow that doesn’t require user interaction.`

**•** `CheckoutFlow—A flow used in Lightning B2B Commerce to create a checkout in a`
store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow—A flow that lets customers request to be contacted by`
customer support. This flow is used to create contact request records. This value is
available in API version 45.0 and later.

**•** `CustomerLifecycle—A Salesforce Surveys flow that lets you associate survey`
questions with different stages in customer lifecycles. This value is available in API version
49.0 and later and only when the Customer Lifecycle Designer license is enabled.

**•** `CustomEvent—A process that is invoked when it receives a platform event message.`
In the UI, it’s an event process. This value is available in API version 41.0 and later.

**•** `DataCaptureFlow— In the UI, Data Capture flows configure the Form tab in the`
Field Service mobile app. When the Data Capture flow is launched, its Flow metadata is
publicly available in JavaScript format. This value is available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow—A screen flow that presents assessment`
questions from Discovery Framework. Launches when invoked by a user on a mobile
device. This type of flow collects or displays information, requires user interaction, and
works offline or online. This value is available in API version 62.0 and later.

**•** `EvaluationFlow—A flow for evaluating custom entry and exit conditions in an`
orchestration. Uses the `isOrchestrationConditionMet` output variable and
discards values from any other output variables. This value is available in API version 54.0
and later.

**•** `FieldServiceMobile—A flow for the Field Service mobile app. This value is`
available in API version 39.0 and later.

**•** `FieldServiceWeb—A flow for embedded Appointment Booking. Its UI label is`
Field Service Embedded Flow. This value is available in API version 41.0 and later.

**•** `Flow—A flow that requires user interaction because it contains one or more screens`
or local actions, choices, or dynamic choices. In the UI and Salesforce Help, it’s a screen
flow. Screen flows can be launched from the UI, such as with a flow action, Lightning
page, or web tab.

**•** `FSCLending—A flow for Financial Services Cloud Mortgage. This value is available`
in API version 46.0 and later.

**•** `IndicatorResultFlow—A flow for Outcome Management that calculates and`
creates indicator results for a selected indicator performance period. This value is available
with the Outcome Management license in API version 60.0 and later.


-----

**•** `IndividualObjectLinkingFlow—A flow that associates individuals with`
interactions such as voice calls, messaging sessions, or case-related emails. This value is
available in API version 58.0 and later.

**•** `InvocableProcess—A process that another process or the Invocable Actions`
resource in REST API invokes. This value is available in API version 38.0 and later.

**•** `Journey—An audience-driven flow for Marketing Cloud. This value is available in API`
version 57.0 and later.

**•** `LoginFlow—A flow for login. This value is available in API version 51.0 and later.`

**•** `LoyaltyManagementFlow—A flow for the Loyalty Management app that’s`
invokable by loyalty program processes. This value is available in API version 54.0 and
later.

**•** `Orchestrator—An orchestration that organizes flows into groups of steps contained`
in a series of stages. This value is available in API version 53.0 and later.

**•** `PromptFlow—A flow for Prompt Builder. Pass data between Prompt Builder and the`
flow. This value is available in API version 60.0 and later.

**•** `RecommendationStrategy—Build recommendations for your users. A`
recommendation launches its assigned flow. This value is available in API version 54.0
[and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=sf.nba_building_flow_builder_strategy.htm&language=en_US)

**•** `RoutingFlow—A flow for Salesforce Omni-Channel routing and other business logic.`
This value is available in API version 52.0 and later.

**•** `Survey—A flow for Salesforce Surveys. From the UI, this type of flow is created in`
Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich—A Salesforce Surveys flow that uses the Survey Data Mapper. From`
the UI, this type of flow is created in the Survey Builder and requires an associated survey
flow type. This value is available in API version 49.0 or later and only when the Customer
Lifecycle Designer license is enabled.

**•** `Workflow—A process that is invoked when a record is created or edited. In the UI`
and Salesforce Help, it’s a record change process.

These values are reserved for future use.

**•** `ActionCadenceFlow`

**•** `ActionPlan`

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


-----

```
RequestIdentifier
Timestamp
TotalExecutionTime
UserIdentifier
