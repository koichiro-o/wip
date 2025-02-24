#### AIInsightValue

Represents an Einstein prediction insight value. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

AIInsightValue is a one-to-many child of AIRecordInsight. AIInsightValue represents a predicted value of a predicted insight.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available when Einstein features such as Prediction Builder or Case Classification are enabled. To access an AIInsightValue record, you
must have access to the related AIRecordInsight record. To grant a user the right to create an AIInsightValue record, you can use the
AICreateInsightObjects or the CreateAIInsights permission.

##### Fields

```
AiInsightActionId

```

**Type**
reference


-----

```
AiRecordInsightId
Confidence
Field

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the associated AIInsightAction.

This is a relationship field.

**Relationship Name**
AiInsightAction

**Relationship Type**
Lookup

**Refers To**
AIInsightAction

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the associated AIRecordInsight.

This is a relationship field.

**Relationship Name**
AiRecordInsight

**Relationship Type**
Lookup

**Refers To**
AIRecordInsight

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight. Higher values (near 1.0)
indicate stronger confidence.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the target field Einstein is making predictions for, such as “AnnualRevenue”.


-----

```
FieldValueLowerBound
FieldValueUpperBound
Name
SobjectLookupValueId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The lower bound value.

**Type**
textarea

**Properties**
Nillable

**Description**
The upper bound value.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIInsightValue.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the value object, if this insight value references an object.

This is a relationship field.

**Relationship Name**
SobjectLookupValue

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, Address, AlternativePaymentMethod,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskIndDefinition,
AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, AssociatedLocation,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CampaignMember, CardPaymentMethod, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareInterventionType, CareMetricTarget, CareObservation,


-----

```
SobjectType

```

CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem,
CareProgram, CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CodeSetBundle, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, ContactRequest, ContentVersion, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo, CreditMemoLine,
DataUseLegalBasis, DataUsePurpose, DelegatedAccount, DigitalWallet,
DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet, EmailMessage,
EngagementChannelType, EnrollmentEligibilityCriteria, Event, HealthCareDiagnosis,
HealthCareProcedure, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument,
Image, Individual, IndividualApplication, Invoice, InvoiceLine, Lead, Location,
LocationTrustMeasure, MemberPlan, MessagingEndUser, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, Order, OrderItem, OtherComponentTask,
PartyConsent, Payment, PaymentAuthAdjustment, PaymentAuthorization, PaymentGateway,
PaymentGroup, PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry, ProcessException,
Product2, ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, PurchaserPlan,
PurchaserPlanAssn, QuickText, ReceivedDocument, Recommendation, Refund,
RefundLinePayment, ReportAnomalyEventStore, ResourceAbsence, ResourcePreference,
ReturnOrder, ReturnOrderItemAdjustment, ReturnOrderItemTax, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore,
SharingRecordCollection, Shift, Shipment, ShipmentItem, SkillRequirement, SocialPersona,
SocialPost, Solution, Task, TimeSlot, UnitOfMeasure, UserProvisioningRequest, VideoCall, Visit,
VisitedParty, Visitor, VoiceCall, VolunteerProject, WorkBadge, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup, WorkTypeGroupMember

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the value object, such as Account or Case, if this insight value references an
object.


-----

```
 Value
 ValueType

##### Usage

```

**Type**
textarea

**Properties**
Nillable

**Description**
The prediction result insight value.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The data type of the prediction result insight value. Possible values are:

**•** `Boolean—Boolean`

**•** `Currency—Currency`

**•** `DateTime—DateTime`

**•** `Enum—Enum`

**•** `Lookup—Lookup`

**•** `Number—Number`

**•** `String—String`


When an Einstein feature makes a prediction and saves the results, the following events happen in a single atomic operation:

**•** An AIRecordInsight record is created and populated with information about the prediction insight. AIInsightAction, AIInsightReason,
and AIInsightValue records are also created and made children of the AIRecordInsight record.

**•** If the Einstein feature uses AI prediction fields, prediction result values are written to the target AI prediction field.

**•** An AIPredictionEvent platform event is created, and any subscriber to AIPredictionEvent is notified.

When Einstein writes prediction results back to AI prediction fields, record save custom logic, such as Apex triggers, workflow rules, and
assignment rules, aren’t run. To add custom logic based on Einstein prediction results, use a platform event subscriber, such as Process
Builder, to get notifications for AIPredictionEvents that contain references to Einstein insight objects.

Custom fields can’t be added to Einstein insight objects.

Einstein insights contain information about target fields and predicted value. Your org may have created Einstein predictions that are
associated with target fields with field-level security restrictions. To control how users access Einstein insights records, use Salesforce
data access features such as user profiles and permission sets.
