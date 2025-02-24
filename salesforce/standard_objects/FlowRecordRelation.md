#### FlowRecordRelation

Represents a relationship between a record and a flow interview. When a flow interview is paused, Salesforce uses the $Flow.CurrentRecord
global variable in the flow to associate the interview with a record. Available in API version 42.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
Name
ParentId
RelatedRecordId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this relation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The flow interview that the record is related to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that the flow interview is related to. Make sure that this field contains
only one ID, and that the ID is for a valid object.

Custom objects and most standard objects are supported.

This is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, AccountContactRole, AccountPartner, Accreditation, ActivationTarget,
ActivationTrgtIntOrgAccess, Address, AlternativePaymentMethod, Announcement,
ApexTestQueueItem, AppAnalyticsQueryRequest, AppUsageAssignment,
AssessmentIndicatorDefinition, AssessmentTask,


-----

AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, AssociatedLocation, AsyncApexJob, Attachment,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BackgroundOperation, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, CalendarView, Campaign,
CampaignMember, CardPaymentMethod, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth,
CarePreauthItem, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct,
CareProgramProvider, CareProgramTeamMember, CareProviderAdverseAction,
CareProviderFacilitySpecialty, CareProviderSearchableField, CareRegisteredDevice,
CareRequest, CareRequestDrug, CareRequestExtension, CareRequestItem,
CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CaseContactRole,
CaseSolution, CodeSet, CodeSetBundle, CollaborationGroup,
CollaborationGroupMember, CollaborationGroupMemberRequest,
CollaborationGroupRecord, CollaborationInvitation, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConferenceNumber, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, ContactRequest,
ContentDistribution, ContentDocument, ContentDocumentLink,
ContentDocumentSubscription, ContentFolder, ContentFolderLink,
ContentFolderMember, ContentNotification, ContentVersion,
ContentVersionComment, ContentVersionRating, ContentWorkspaceDoc,
Contract, ContractContactRole, ConversationEntry, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, Dashboard,
DashboardComponent, DataAssessmentFieldMetric, DataAssessmentMetric,
DataAssessmentValueMetric, DataStream, DataUseLegalBasis, DataUsePurpose,
DelegatedAccount, DeleteEvent, DialerCallUsage, DigitalSignature, DigitalWallet,
Document, DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet,
EmailMessage, EmailMessageRelation, EngagementChannelType,
EnhancedLetterhead, EnrollmentEligibilityCriteria, EntitySubscription, Event,
EventRelation, ExternalEvent, ExternalEventMapping, FeedAttachment,
FeedComment, FeedItem, FeedPollChoice, FeedPollVote, FeedRevision,
FileSearchActivity, FlowInterviewLog, FlowInterviewLogEntry, FlowStageRelation,
HealthCareDiagnosis, HealthCareProcedure, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument, Image, Individual,
IndividualApplication, InstalledMobileApp, Invoice, InvoiceLine, Lead, ListEmail,
ListEmailIndividualRecipient, ListEmailRecipientSource, Location,
LocationTrustMeasure, MarketSegment, MarketSegmentActivation,


-----

MatchingInformation, MemberPlan, MessagingDeliveryError, MessagingEndUser,
MktCalculatedInsight, MktSgmntActvtnAudAttribute,
MktSgmntActvtnContactPoint, Note, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, OpportunityPartner, Order,
OrderItem, OrgMetric, OrgMetricScanResult, OrgMetricScanSummary,
OtherComponentTask, Partner, PartyConsent, Payment, PaymentAuthAdjustment,
PaymentAuthorization, PaymentGateway, PaymentGatewayLog, PaymentGroup,
PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry,
ProcessException, ProcessInstance, ProcessInstanceNode, Product2,
ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, PromptAction, ProviderSearchSyncLog, PurchaserPlan,
PurchaserPlanAssn, PushTopic, QuickText, QuickTextUsage, ReceivedDocument,
Recommendation, RecordAction, Refund, RefundLinePayment, ReplyText, Report,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment,
ReturnOrderItemTax, ReturnOrderLineItem, SearchPromotionRule,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SetupAssistantStep,
SharingRecordCollection, SharingRecordCollectionItem,
SharingRecordCollectionMember, Shift, Shipment, ShipmentItem,
SkillRequirement, SocialPersona, SocialPost, Solution, StreamingChannel, Task,
ThreatDetectionFeedback, TimeSlot, TodayGoal, Topic, TopicAssignment,
UnitOfMeasure, UserAppInfo, UserAppMenuCustomization,
UserEmailPreferredPerson, UserProvAccount, UserProvAccountStaging,
UserProvMockTarget, UserProvisioningLog, UserProvisioningRequest, VideoCall,
VideoCallParticipant, VideoCallRecording, Visit, VisitedParty, Visitor, VoiceCall,
VoiceCallRecording, VoiceVendorLine, VolunteerProject, WaveAutoInstallRequest,
WaveCompatibilityCheckItem, WorkAccess, WorkBadge, WorkBadgeDefinition,
WorkOrder, WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup,
WorkTypeGroupMember
