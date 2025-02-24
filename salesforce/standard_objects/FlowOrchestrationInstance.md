#### FlowOrchestrationInstance

Represents a run-time instance of an orchestration. This object is available in API version 53.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
If sharing rules are defined for FlowOrchestrationInstance, they determine access to specific orchestration run records. Or the user must
have the View All Data permission.

##### Fields

```
CurrentStage
Duration
InterviewId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the stage that was running when the orchestration run was paused or failed
because of an error in an action called by a step. This field is available in API version 62.0 and
later.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration of the orchestration instance in seconds. Durations are incremented until the
orchestration is completed, canceled, or ends in an error. This field is available in API version
62.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The globally unique flow interview ID associated with the orchestration instance.

This field is a relationship field.

**Relationship Name**
Interview


-----

```
LastReferencedDate
LastViewedDate
Name
OrchestrationDeveloperName
OrchestrationLabel

```

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed a record related to the orchestration run. This field is
available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed the orchestration run. This field is available in API version
55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the orchestration instance.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The developer name of the flow definition associated with the orchestration run. This field
is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the orchestration. This field is available in API version 63.0 and later.


-----

```
OwnerId
Status
TriggeringRecordId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the orchestration run. Valid values are:

**•** `Canceled—The orchestration instance was canceled.`

**•** `Completed—The orchestration instance completed.`

**•** `Error—The orchestration instance, or a stage or step within the orchestration instance,`
encountered an error.

**•** `InProgress—The orchestration instance is in progress.`

**•** `Suspended—The orchestration instance was suspended.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record that triggered the record-triggered orchestration. This field is available
in API version 62.0 and later.

**Relationship Name**
TriggeringRecord

**Relationship Type**
Lookup

**Refers To**
Account, AccountContactRole, AiEvalCopilotTestCaseRslt, AiEvalTestCaseCritRslt,
AiEvalTestCaseResult, AiEvaluation, AiPromptBuilderGenResult, Announcement,
ApexTestQueueItem, AppAnalyticsQueryRequest, Asset, AssetRelationship, AssociatedLocation,


-----

AsyncApexJob, Attachment, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, BackgroundOperation, Benificiary__c,
BriefcaseAssignment, BusinessBrand, CalendarView, Case, CaseContactRole, CaseSolution,
CollaborationGroup, CollaborationGroupMember, CollaborationGroupMemberRequest,
CollaborationGroupRecord, CollaborationInvitation, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
ConferenceNumber, Contact, ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, ContactRequest, ContentBody,
ContentDistribution, ContentDocument, ContentDocumentLink,
ContentDocumentSubscription, ContentFolder, ContentFolderLink, ContentFolderMember,
ContentNotification, ContentVersion, ContentVersionComment, ContentVersionRating,
ContentWorkspaceDoc, Contract, ContractContactRole, Customer, Dashboard,
DashboardComponent, DataAssessmentFieldMetric, DataAssessmentMetric,
DataAssessmentValueMetric, DataUseLegalBasis, DataUsePurpose, DelegatedAccount,
DeleteEvent, Document, DuplicateRecordItem, DuplicateRecordSet, EmailMessage,
EmailMessageRelation, EmailStatus, EngagementChannelType, EnhancedLetterhead,
EntitySubscription, Event, EventRelation, EventRelayFeedback, ExternalEvent,
ExternalEventMapping, FeedAttachment, FeedComment, FeedItem, FeedLike, FeedPollChoice,
FeedPollVote, FeedRevision, FeedSignal, FeedTrackedChange, FileSearchActivity,
FlowInterviewLog, FlowInterviewLogEntry, FlowOrchestration, FlowOrchestrationInstance,
FlowOrchestrationLog, FlowOrchestrationStageInstance, FlowOrchestrationStepInstance,
FlowOrchestrationVersion, FlowOrchestrationWorkItem, FlowRecord, FlowRecordElement,
FlowRecordVersion, FlowRecordVersionOccurrence, FlowStageRelation, FlowTestResult,
ForecastingAdjustment, ForecastingCustomData, ForecastingFact, ForecastingItem,
ForecastingOwnerAdjustment, ForecastingQuota, Idea, Image, Individual, InstalledMobileApp,
Lead, ListEmail, ListEmailIndividualRecipient, ListEmailRecipientSource, Location,
LocationTrustMeasure, MLModel, MLModelFactor, MLModelFactorComponent,
MLModelMetric, ManagedContent, ManagedContentChannel, ManagedContentSpace,
ManagedContentVariant, MatchingInformation, MlFeatureValueMetric, NetworkActivityAudit,
NetworkDiscoverableLogin, NetworkFeedResponseMetric, NetworkSelfRegistration,
NetworkUserHistoryRecent, Note, ObjectDataImport, ObjectDataImportReference,
ObjectMetadataTag, ObjectRelatedUrl, Opportunity, OpportunityContactRole,
OpportunityLineItem, OpportunityRelatedDeleteLog, Order, OrderItem, OrgMetric,
OrgMetricScanResult, OrgMetricScanSummary, Partner, Partner__c, PartyConsent, Pricebook2,
PricebookEntry, ProcessException, ProcessInstance, ProcessInstanceNode, Product2, ProfileSkill,
ProfileSkillEndorsement, ProfileSkillUser, PromptAction, PromptError, PushTopic, QuickText,
QuickTextUsage, Recommendation, RecommendationResponse, RecordAction, Report,
Scorecard, ScorecardAssociation, ScorecardMetric, Seller, ServiceSetupProvisioning,
SetupAssistantStep, SocialPersona, SocialPost, Solution, StreamingChannel,
TableauHostMapping, Task, TodayGoal, Topic, TopicAssignment, UserAppInfo,
UserAppMenuCustomization, UserDefinedLabel, UserDefinedLabelAssignment,
UserEmailPreferredPerson, UserLocalWebServerIdentity, UserProvAccount,
UserProvAccountStaging, UserProvMockTarget, UserProvisioningLog, UserProvisioningRequest,
WorkAccess, WorkBadge, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkThanks


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationInstanceFeed on page 54**
Feed tracking is available for the object.

**FlowOrchestrationInstanceHistory on page 62**
History is available for tracked fields of the object.

**FlowOrchestrationInstanceOwnerSharingRule on page 64**
Sharing rules are available for the object. This object is available in API version 56.0 and later.

**FlowOrchestrationInstanceShare on page 66**
Sharing is available for the object. This object is available in API version 56.0 and later.
