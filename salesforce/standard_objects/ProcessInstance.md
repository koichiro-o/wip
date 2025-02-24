#### ProcessInstance

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the package containing the process flow migration object.


Represents an instance of a single, end-to-end approval process. Use this and the node, step, and workitem process instance objects to
create approval history reports.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

For approval process instances that were completed before the Summer '14 rollout, all Process Instance fields are automatically populated,
with one exception: CompletedDate is never populated for approval process instances that were completed before January 1, 2013.
For approval process instances that were pending during the Summer '14 rollout, all ProcessInstance fields are automatically populated,
with two exceptions: `CompletedDate` and `LastActorId` are populated only after the approval process instance is complete.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
CompletedDate
ElapsedTimeInDays

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The completion date and time of the approval process. The `ElapsedTimeDay,`
`ElapsedTimeHours, and ElapsedTimeMinutes` field values are calculated using
```
  CompletedDate.

```
**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
ElapsedTimeInHours
ElapsedTimeInMinutes
LastActorId
ProcessDefinitionId

```

**Description**
The total elapsed time in days between when the approval process instance was started and
now.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total elapsed time in hours between when the approval process instance was started
and now.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total elapsed time in minutes between when the approval process instance was started
and now.

**Type**
reference

**Properties**
Group, Filter, Nillable, Sort

**Description**
The last actor that approved, rejected, or recalled the process.

This is a relationship field.

**Relationship Name**
LastActor

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Group, Filter, Sort

**Description**
The ID of this approval process instance.

This is a relationship field.


-----

```
Status
SubmittedById
TargetObjectId

```

**Relationship Name**
ProcessDefinition

**Relationship Type**
Lookup

**Refers To**
ProcessDefinition

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of this approval process instance, for example Started, Pending, or Approved.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who submitted the approval process.

This is a relationship field.

**Relationship Name**
SubmittedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the object affected by this approval process instance.

This is a polymorphic relationship field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup


-----

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
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
PurchaserPlan, PurchaserPlanAssn, QuickTextUsage, Quote, ReceivedDocument,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment,
ReturnOrderItemTax, ReturnOrderLineItem, ServiceAppointment, ServiceResource,
ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SharingRecordCollection, SharingRecordCollectionItem, SharingRecordCollectionMember,
Shift, Shipment, ShipmentItem, SkillRequirement, SocialPost, Solution, StreamingChannel,
UnitOfMeasure, UserProvisioningRequest, VideoCall, VideoCallParticipant, VideoCallRecording,
Visit, VisitedParty, Visitor, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember


-----

##### Usage

Use this object to query or retrieve an approval process.

The following SOQL query returns details for all the ProcessInstanceStep records related to individual ProcessInstance records. The nested
query references `Steps, which is the child` `relationshipName` for ProcessInstanceStep in the ProcessInstance object.
```
SELECT Id, (SELECT Id, StepStatus, Comments FROM Steps)
FROM ProcessInstance

```
The following SOQL query returns details for all the ProcessInstanceWorkItem records related to individual ProcessInstance records. The
nested query references Workitems, which is the child relationshipName for ProcessInstanceWorkItem in the ProcessInstance
object.
```
SELECT Id, (SELECT Id, ActorId, ProcessInstanceId FROM Workitems)
FROM ProcessInstance

```
ProcessInstanceHistory can help provide a unified read-only view of the ProcessInstanceStep and ProcessInstanceWorkItem objects.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProcessInstanceHistory**

History is available for tracked fields of the object.

**ProcessInstanceChangeEvent (API Version 58.0)**
Change events are available for the object.

SEE ALSO:

ProcessInstanceHistory

ProcessInstanceStep

ProcessInstanceWorkitem
