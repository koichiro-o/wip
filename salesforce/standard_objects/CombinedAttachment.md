#### CombinedAttachment

This read-only object contains all notes, attachments, Google Docs, documents uploaded to libraries in Salesforce CRM Content, and
files added to Chatter that are associated with a record.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
ContentSize
ContentUrl
ExternalDataSourceName

```

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


-----

```
ExternalDataSourceType
FileExtension
FileType
ParentId

```

**Description**
Name of the external data source in which the document is stored. This field is
set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

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

The ID of the parent object.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


-----

```
RecordType

```

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
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier,
IdentityDocument, Image, IndividualApplication, Invoice, InvoiceLine, Lead,
ListEmail, Location, MarketSegment, MarketSegmentActivation, MemberPlan,
MessagingSession, MktCalculatedInsight, OperatingHours, Opportunity, Order,
OrderItem, Organization, OtherComponentTask, PartyConsent, PersonEducation,
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
string


-----

```
 SharingOption
Title

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

The parent object type.

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the attached file.


Use this object to list all notes, attachments, documents uploaded to libraries in Salesforce CRM Content, and files added to Chatter for
a record, such as a related list on a detail page.

To determine if an object supports the CombinedAttachment object, call `describeSObject()` on the object. For example,
`describeSObject('Account')` returns all the child relationships of the Account object, including CombinedAttachment.
You can then query the CombinedAttachment child relationship.
```
SELECT Name, (SELECT Title FROM CombinedAttachments)
FROM Account

```
You can’t directly query CombinedAttachment.
