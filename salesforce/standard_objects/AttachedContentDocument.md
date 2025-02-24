#### AttachedContentDocument

This read-only object contains all `ContentDocument` objects associated with an object.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ContentSize
ContentUrl
ExternalDataSourceName
ExternalDataSourceType

```

**Description**

ID of the attached `ContentDocument.`

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the document in bytes.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL for links and Google Docs. This field is set only for links and Google Docs,
and is one of the fields that determine the `FileType.`

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the external data source in which the document is stored. This field is
set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
FileExtension
FileType
LinkedEntityId

```

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in APIAPI version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the attached `ContentDocument.`

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, determined by the file extension.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the record the `ContentDocument` is attached to.

This is a relationship field.

**Relationship Name**
LinkedEntity

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,


-----

```
SharingOption

```

CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CollaborationGroup,
CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentWorkspace, Contract, ConversationEntry,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria,
Event, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingSession,
MktCalculatedInsight, OperatingHours, Opportunity, Order, OrderItem,
Organization, OtherComponentTask, PartyConsent, PersonEducation,
PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit, PlanBenefitItem,
Product2, ProductFulfillmentLocation, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report,
ReportAnomalyEventStore, ResourceAbsence, ResourcePreference, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SessionHijackingEventStore, Shift, Shipment, ShipmentItem, Site, SkillRequirement,
SocialPost, Solution, Task, ThreatDetectionFeedback, User, Visit, VisitedParty,
Visitor, VoiceCall, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Controls whether or not sharing is frozen for a file. Only administrators and file
owners with Collaborator access to the file can modify this field. Default is
```
  Allowed, which means that new shares are allowed. When set to
  Restricted, new shares are prevented without affecting existing shares.

```
This field is available in API versions 35.0 and later.


-----

```
Title

##### Usage

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Title of the attached `ContentDocument.`


Use this object to list all `ContentDocument` objects attached to an object via a feed post.

To retrieve `ContentDocument` objects, issue a describe call on an object, which returns a query result for each activity since the
record was created. You can’t directly query this object.
