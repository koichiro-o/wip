#### ProcessInstanceHistory

This read-only object shows all steps and pending approval requests associated with an approval process (ProcessInstance).

##### Supported Calls
```
describeSObjects()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Fields

```
ActorId

```

**Type**
reference


-----

```
Comments
ElapsedTimeInDays
ElapsedTimeInHours
ElapsedTimeInMinutes

```

**Properties**
Filter, Group, Sort

**Description**
ID of the user who is assigned to this ProcessInstance.

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Comments for a ProcessInstanceStep . This field doesn't apply to ProcessInstanceWorkitem
records.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days between when the approval process instance was started and when
it was completed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours between when the approval process instance was started and when
it was completed.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
IsPending
OriginalActorId
ProcessInstanceId
ProcessNodeId

```

**Description**
The total time in minutes between when the approval process instance was started and
when it was completed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the ProcessInstance is pending (true) or not (false).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who was originally assigned this ProcessInstance.

This is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ProcessInstance.

This is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance

**Type**
reference


-----

```
RemindersSent
StepStatus
TargetObjectId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this step.

This is a relationship field.

**Relationship Name**
ProcessNode

**Relationship Type**
Lookup

**Refers To**
ProcessNode

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of reminders that have been sent. Default is 0 (zero).

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the ProcessInstanceStep.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object being approved.

This is a polymorphic relationship field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,


-----

AssetRelationship, AssignedResource, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, Award, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, Campaign, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CodeSetBundle, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
ConsumptionRate, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, DataStream, DataUseLegalBasis,
DataUsePurpose, DelegatedAccount, DigitalSignature, DocumentChecklistItem,
DuplicateRecordItem, DuplicateRecordSet, EmailMessage, EngagementChannelType,
EnrollmentEligibilityCriteria, ExternalEventMapping, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, IdentityDocument,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, LocationTrustMeasure,
MarketSegment, MarketSegmentActivation, MemberPlan, MessagingEndUser,
MessagingSession, MktCalculatedInsight, Opportunity, Order, OrgMetricScanResult,
OrgMetricScanSummary, OtherComponentTask, PartyConsent, PaymentAuthAdjustment,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, ProcessException, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PromptAction,
PurchaserPlan, PurchaserPlanAssn, QuickTextUsage, ReceivedDocument, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType, SharingRecordCollection,
SharingRecordCollectionItem, SharingRecordCollectionMember, Shift, Shipment,
ShipmentItem, SkillRequirement, SocialPost, Solution, StreamingChannel, UnitOfMeasure,
UserProvisioningRequest, VideoCall, VideoCallParticipant, VideoCallRecording, Visit,
VisitedParty, Visitor, VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem,
WorkType, WorkTypeGroup, WorkTypeGroupMember

##### Usage

This object helps you replicate the related list functionality of the Salesforce user interface for approval processes. Use ProcessInstanceHistory
for a unified read-only view of the ProcessInstanceStep and ProcessInstanceWorkItem objects. You can’t query ProcessInstanceHistory.
Instead, you can query ProcessInstanceHistory by including it in a nested query on the parent ProcessInstance object. For example, this


-----

SOQL query returns all the ProcessInstanceHistory records related to individual ProcessInstance records. The nested query references
`StepsAndWorkitems, which is the child` `relationshipName` for ProcessInstanceHistory in the ProcessInstance object.
```
SELECT Id, (SELECT Id, StepStatus, Comments FROM StepsAndWorkitems)
  FROM ProcessInstance

```
This object respects field-level security on the parent object.

SEE ALSO:

ProcessInstance

ProcessInstanceStep

ProcessInstanceWorkitem
