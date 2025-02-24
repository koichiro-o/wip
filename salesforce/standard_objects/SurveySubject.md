#### SurveySubject

Represents a relationship between a survey and another object, such as an account or a case.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
LastReferencedDate
LastViewedDate
Name
ParentId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the SurveySubject record was last referenced by another
object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the SurveySubject record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the SurveySubject record.

**Type**
reference


-----

```
SubjectEntityType

```

**Properties**
Create, Filter, Group, Sort

**Description**
Unique identifier of the SurveyInvitation object or SurveyResponse object that is
associated with this survey-object relationship.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
SurveyInvitation, SurveyResponse

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object that the survey is associated with. Possible values include:

**•** `Account`

**•** `Asset`

**•** `Banker`

**•** `BranchUnit`

**•** `BranchUnitBusinessMember`

**•** `BranchUnitCustomer`

**•** `BusinessLicenseApplication`

**•** `BusinessMilestone`

**•** `Campaign`

**•** `CareProgram`

**•** `Case`

**•** `Claim`

**•** `ClaimParticipant`

**•** `Contact`

**•** `Employee`

**•** `Event`

**•** `Incident`

**•** `IndividualApplication`

**•** `InsurancePolicy`

**•** `InsurancePolicyParticipant`

**•** `Lead`


-----

```
SubjectId
SurveyId

```


**•** `LearningItemSubmission—Available in API version 58.0 and later.`

**•** `LiveChatTranscript`

**•** `LoyaltyProgram`

**•** `LoyaltyProgramMember`

**•** `LoyaltyProgramPartner`

**•** `MaterialityStakeholder`

**•** `MessagingSession`

**•** `Opportunity`

**•** `Order`

**•** `PersonalLifeEvent`

**•** `Producer`

**•** `Product2`

**•** `Promotion`

**•** `RebateProgram`

**•** `RetailStore`

**•** `ServiceAppointment`

**•** `ServiceResource`

**•** `Solution`

**•** `Task`

**•** `TransactionJournal`

**•** `User`

**•** `VideoCall`

**•** `Visit`

**•** `VoiceCall`

**•** `VolunteerProject`

**•** `WorkOrder`

**•** Custom Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the object that’s associated with the survey.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
SurveyInvitationId
SurveyResponseId

##### Associated Objects

```

**Description**
Unique identifier of the survey that’s associated with the record that’s represented
by SubjectId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation that's associated with another object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey response that's associated with another object.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveySubjectChangeEvent (API version 62.0)**
Change events are available for the object.
