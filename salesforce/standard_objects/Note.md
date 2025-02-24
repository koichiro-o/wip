#### Note

Represents a note, which is text associated with a custom object or a standard object, such as a Contact, Contract, or Opportunity.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Body
IsDeleted
IsPrivate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the note. Limited to 32 KB.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, only the note owner or a user with the “Modify All Data” permission can view the`
note or query it via the API. Note that if a user who does not have the “Modify All Data”
permission sets this field to `true` on a note that they do not own, then they can no longer
query, delete, or update the note. Label is Private.


-----

```
OwnerId
ParentId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the note.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the object associated with the note.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EngagementChannelType,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, Lead, Location, MemberPlan,


-----

```
 Title

##### Usage

```

Opportunity, Order, OtherComponentTask, PersonEducation, PersonLifeEvent, Product2,
ProductRequest, ProductRequestLineItem, PurchaserPlan, ReceivedDocument,
ServiceAppointment, ServiceResource, Shift, SocialPost, Visit, VisitedParty, Visitor,
VolunteerProject, WorkOrder, WorkOrderLineItem

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Title of the note.


Use this object to manage notes for an object.

SEE ALSO:

Overview of Salesforce Objects and Fields
