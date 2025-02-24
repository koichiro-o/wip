#### FlowOrchestrationWorkItem

Represents a work item associated with a run-time instance of an interactive step in a run-time instance of an orchestration. This object
is available in API version 54.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update()

```

-----

##### Special Access Rules

An assignee can see all work item records assigned to them. If sharing rules are defined for FlowOrchestrationWorkItem, they determine
access to specific orchestration work item records for users other than the assignee. Or the user must have the View All Data permission.

##### Fields

```
AssigneeId
Description
ElapsedTimeSinceAsgntInSec
ElapsedTimeSinceCreationInSec

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user, group, or queue assigned to the orchestration work item.

This field is a polymorphic relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
Group (Type = Regular), Group (Type = Queue), User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the orchestration work item.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
When status is Assigned, the number of seconds that have passed since the work item was
last assigned. When status is Completed, this value is null. This field is available in API version
63.0 and later.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort


-----

```
Label
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Description**
When status is Assigned, the number of seconds that have passed since the work item was
created. When status is Completed, this value is null. This field is available in API version 63.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the orchestration work item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed a record related to the orchestration work item. This
field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed the orchestration work item. This field is available in API
version 55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the orchestration work item.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**

**•** When the assignee is an internal user: the ID of the internal user


-----

```
RelatedRecordId

```


**•** When the assignee is a credentialed Experience Cloud site visitor: the ID of the
credentialed Experience Cloud site visitor

**•** When the assignee is a group or queue: the ID of the automated process user

This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the context record, such as an account, case, or expense, that the orchestration
work item is related to. An assigned user completes the associated orchestration work item
on the page for this record.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
All objects except AccountContactRelation, AccountTeamMember, ActiveScratchOrg,
ActivityMetric, ActivityMetricRollup,CampaignMember, CartCheckoutSession,
CartDeliveryGroup, CartDeliveryGroupMethod, ChatterActivity,CollaborationGroupMember,
ContentDesignKit, ContentDesignKitVersion, ConversationBroadcastEntry,ConversationReason,
ConversationReasonExcerpt, ConversationReasonGroup,
CustomPersonDataTemplate,ElectronicMediaGroup, EngagementScore, Event, FeedItem,
FlowOrchestrationWorkItem, FtestDelPlatform1,FtestDelPlatform2,
FtestFormulaFieldRefSql,HighScaleSample, HighScaleSampleItem, LegalEntity, LocationWaitlist,
LocationWaitlistedParty,LocWaitlistMsgTemplate, ManagedContentVersion,
MessagingEndUser, MessagingSession, MLModel,MLModelFactor, MLModelFactorComponent,
NetworkMember, NetworkMemberChunk, OpportunityContactRole,OpportunityLineItem,
OpportunityScore, OpportunityTeamMember, OrgSnapshot,
PaymentTermItem,RequestsForAccessSIQ, ScoreIntelligence, ScratchOrgInfo,
SharingRecordCollection, SharingRecordCollectionItem,SharingRecordCollectionMember,
StreamActivityAccess, Survey, SurveyMessagingChannel, SurveyPage,SurveyQuestionChoice,
SurveyVersion, Task, TenantSecurityAlertRuleSelectedTenant,
TenantSecurityApiAnomaly,TenantSecurityConnectedApp, TenantSecurityCredentialStuffing,
TenantSecurityHealthCheckBaselineTrend,TenantSecurityHealthCheckDetail,


-----

```
ScreenFlow

```

TenantSecurityHealthCheckTrend, TenantSecurityLogin,
TenantSecurityMetricDetail,TenantSecurityMetricDetailLink, TenantSecurityMobilePolicyTrend,
TenantSecurityMonitorMetric,TenantSecurityNotification, TenantSecurityNotificationRule,
TenantSecurityPackage, TenantSecurityPolicy,TenantSecurityPolicyChangeLog,
TenantSecurityPolicyDeployment,
TenantSecurityPolicySelectedTenant,TenantSecurityReportAnomaly,
TenantSecuritySessionHijacking, TenantSecurityTenantChangeLog,TenantSecurityTenantInfo,
TenantSecurityTrustedIpRangeTrend, TenantSecurityUserActivity,
TenantSecurityUserPerm,TenantSecurityWebsite, TopicAssignment, UserExternalCredential,
VoiceCall

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The screen flow associated with the orchestration work item.

Possible values are:

**•** `healthcloud_pm_flows__AcceptSlots`

**•** `industries_automotive__AutoIV`

**•** `industries_mfg_service__MfgIv`

**•** `omnichannel_chat__QueuesChat`

**•** `omnichannel_chat__SkillsChat`

**•** `omnichannel_messaging__MsgRouting`

**•** `omnichannel_voice__VoiceRouting`

**•** `opencti__SCV_Basic_Routing_Flow`

**•** `runtime_appointmentbooking__Flow`

**•** `runtime_appointmentbooking__Guest_Flow`

**•** `runtime_appointmentbooking__In_Cancel`

**•** `runtime_appointmentbooking__In_Modify`

**•** `runtime_appointmentbooking__In_New`

**•** `runtime_appointmentbooking__Inv_Book`

**•** `runtime_appointmentbooking__Inv_Gen`

**•** `runtime_appointmentbooking__Out_Modify`

**•** `runtime_commerce_adj__Discount_Item`

**•** `runtime_commerce_exc__Exchange_Flow`

**•** `runtime_commerce_oms__Cancel_Item`

**•** `runtime_commerce_oms__Create_OS`

**•** `runtime_commerce_oms__Create_PE`

**•** `runtime_commerce_oms__Return_Item`


-----

```
ScreenFlowInputs

```


**•** `runtime_commerce_rma__Create_CO`

**•** `runtime_commerce_rma__Return_Item_RMA`

**•** `runtime_commerce_rs__Reship_FO`

**•** `runtime_industries_recurrence__Orch`

**•** `runtime_industries_recurrence__Schdlr`

**•** `sales_channel__BroadcastArchive`

**•** `sales_channel__DealWon`

**•** `sales_channel__DealsToWatch`

**•** `sales_channel__HighPriorityCaseNotif`

**•** `sales_channel__NotificationsSubflow`

**•** `sales_channel__OpptyChgNotif`

**•** `sales_channel__OpptyCloseDateNotif`

**•** `sales_channel__OpptyCreateMatchAct`

**•** `sales_channel__OpptyNextStepNotif`

**•** `sales_channel__OpptyStageNotChgNotif`

**•** `sales_channel__SelectFeaturedChannels`

**•** `sales_channel__SetupBroadcastChannel`

**•** `sales_channel__filter_users`

**•** `sales_channel__get_single_user`

**•** `sales_channel__invite_to_channel`

**•** `sales_channel__slack_sales_AccountRoom`

**•** `sales_channel__slack_sales_DealRoom`

**•** `setup_bot__IntroBotAddCaseComment`

**•** `setup_bot__IntroBotCreateCase`

**•** `setup_bot__IntroBotCreateLead`

**•** `setup_bot__IntroBotLookupCase`

**•** `setup_bot__IntroBotPreChatContext`

**•** `setup_order_bot__IntroBotLookupOrder`

**•** `setup_service_experience__Create_Case`

**•** `setup_service_experience__Reset_Pwd`

**•** `setup_service_experience__Verify_Cust`

**Type**
textarea

**Properties**
Nillable

**Description**
The input parameters required by the screen flow.


-----

```
Status
StepInstanceId

##### Associated Objects

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the work item.

Valid values are:

**•** `Assigned`

**•** `Completed`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow orchestration step associated with the orchestration work item.

This field is a relationship field.

**Relationship Name**
StepInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationStepInstance


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationWorkItemFeed on page 54**
Feed tracking is available for the object.

**FlowOrchestrationWorkItemHistory on page 62**
History is available for tracked fields of the object.

**FlowOrchestrationWorkItemOwnerSharingRule on page 64**
Sharing rules are available for the object.

**FlowOrchestrationWorkItemShare on page 66**
Sharing is available for the object.


-----
