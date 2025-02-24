#### AIRecordInsight

Represents an Einstein prediction insight. This object is available in API version 47.0 and later.

An Einstein insight is created every time an Einstein feature, such as Prediction Builder, makes a prediction. An insight is represented by
a root AIRecordInsight and the following child objects: AIInsightAction, AIInsightFeedback, AIInsightReason, and AIInsightValue.

AIRecordInsight contains information on the Einstein prediction, the AI prediction field where results were written, and other details
such as the type of prediction.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete()

 Special Access Rules

```
Prediction insight objects are available in orgs that have Einstein features, such as Prediction Builder or Case Classification, enabled.

##### Fields

```
AiApplicationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the AiApplication that generated this prediction.

This is a relationship field.

**Relationship Name**
AiApplication

**Relationship Type**
Lookup

**Refers To**
AIApplication


-----

```
Confidence
MlPredictionDefinitionId
ModelId
Name

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Relative confidence strength of the generated prediction insight, from 0.0 to 1.0. Higher
values (near 1.0) indicate stronger confidence.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is a relationship field.

**Relationship Name**
MlPredictionDefinition

**Relationship Type**
Lookup

**Refers To**
MLPredictionDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the model to use when generating the insight.

This field is a polymorphic relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the AIRecordInsight.


-----

```
PredictionField
RunGuid
RunStartTime
Status
TargetField

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the field that Einstein is making predictions for, such as “Case.IsEscalated”.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A unique identifier for the Einstein process that made the prediction.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the Einstein prediction process was started.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of this insight. Possible values are:

**•** `Defunct—The insight has been consumed by the Einstein feature that owns the`
prediction. For example, Case Classification marks an insight as defunct if a predicted
recommendation was presented to a user and the user either accepted or ignored the
recommendation. This behavior ensures that the same recommendation isn’t presented
multiple times to the user.

**•** `New—The insight hasn’t been consumed by the Einstein feature.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The field to which prediction results are written. Case Classification doesn’t use this field.


-----

```
TargetId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the record Einstein is making predictions for.

This is a relationship field.

**Relationship Name**
Target

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


-----

```
TargetSobjectType
Type
ValidUntil

```

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
Filter, Group, Restricted picklist, Sort

**Description**
The type of the target object, such as Account or Case.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values are:

**•** `Action—An insight that indicates a suggested action, such as sending an email.`

**•** `Lookup—An insight that indicates a related value not directly related to the target`
object and field.

**•** `MultiValue—An insight with multiple values, such as a multi-class classification.`

**•** `SimilarRecord—An insight that indicates similar or duplicate records.`

**•** `SingleValue—A single value insight, such as a regression number or a score.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The day and time this insight is valid until. After this day and time, the insight might no longer
be valid due to new prediction results from new or changed data. If this field is `null, this`
insight never expires.


-----

##### Usage

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

##### Considerations for Case Classification

To generate reports on the effectiveness of Einstein Case Classification predictions, use the root AIRecordInsight object and its child
[objects, AIInsightFeedback and AIInsightValue. For example, you can determine how many cases received predictions, or how often](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_aiinsightfeedback.htm)
agents accepted or rejected them.

**•** To determine how many cases received recommendations, the AIRecordInsight table identifies the case and contains a row for each
field and each recommendation. In AIRecordInsight, the TargetId field contains the case ID. The PredictionField indicates which case
field is being predicted. Each field value recommendation is contained in a separate AIInsightValue object with AIRecordInsight as
the parent. For a picklist field, Einstein creates AIInsightValue objects with up to 10 field value recommendations. However, just the
top three predictions appear to agents in the Einstein Field Recommendations component.

**•** To learn whether agents acted on any of the top three predictions, use the AIInsightFeedback object. When an agent updates fields
after viewing Einstein’s recommendations, or when Einstein applies a recommendation automatically, the object’s
AiInsightFeedbackType field contains Explicit. If the agent updates fields without viewing the predictions, such as on the case details
tab, AiInsightFeedbackType is set to Implicit. When the agent applies the recommended value, the object’s AiFeedback field is set
to Positive; if the agent applies a different value, AiFeedback is Negative.
