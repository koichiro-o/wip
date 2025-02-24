#### NoteAndAttachment

This read-only object contains all notes and attachments associated with an object.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
IsDeleted
IsNote

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean


-----

```
IsPrivate
OwnerId
ParentId

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object contains a note (true) or an attachment (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true, only the note owner or a user with the “Modify All Data” permission can view the`
note or query it via the API. Note that if a regular user who does not have “Modify All Data”
permission sets this field to `true` on a note that they do not own, then they can no longer
query, delete, or update that note. Label is Private.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns the note and attachment.

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
Filter, Group, Sort

**Description**
ID of the parent object.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


-----

```
 Title

##### Usage

```

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
Opportunity, Order, OtherComponentTask, PersonEducation, PersonLifeEvent, Product2,
ProductRequest, ProductRequestLineItem, PurchaserPlan, ReceivedDocument,
ServiceAppointment, ServiceResource, Shift, SocialPost, Visit, VisitedParty, Visitor,
VolunteerProject, WorkOrder, WorkOrderLineItem

**Type**
string

**Properties**
Filter, Nillable, Group, Sort

**Description**
Title of the note.


Use this object to list all notes and attachments for an object.

To retrieve notes and attachments, issue a describe call on an object, which returns a query result for each activity since the record was
created. You can’t directly query this object.

SEE ALSO:

Note

Attachment
