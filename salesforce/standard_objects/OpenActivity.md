#### OpenActivity

This read-only object is displayed in a related list of open activities—future events and open tasks—related to an object. It includes
activities for all contacts related to the object. OpenActivity fields for phone calls are only available if your organization uses Salesforce
CRM Call Center.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the related account, which is determined as follows:

**•** The account associated with the `WhatId, if it exists; or`

**•** The account associated with the `WhoId, if it exists; otherwise`

**•** `null`

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account


-----

```
ActivityDate
ActivityDateTime
ActivitySubtype
ActivityType

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates one of the following:

**•** The due date of a task

**•** The date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time Coordinated
(UTC) time zone. The time stamp doesn’t represent the time of the activity; don’t attempt
to alter it to accommodate time zone differences. Label is `Date.`

**Type**
dateTime

**Properties**
Aggregate, Filter, Nillable, Sort

**Description**
Contains the event’s due date if the `IsAllDayEvent flag is set to` `false. The time`
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate. Label is Due Date Time.

The value for this field and StartDateTime must match, or one of them must be null.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.
This field isn’t updateable.

Possible values are:

**•** Task

**•** Email

**•** Call

**•** Event

**•** LinkedIn —Available in API version 56.0 and later.

**•** List Email

**Type**
picklist


-----

```
AlternateDetailId
CallDisposition
CallDurationInSeconds

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents one of the following values: `Call,` `Email,` `Meeting, or` `Other. Label is`
```
  Type. These are default values, and can be changed.

```
`ActivityType` is the union of TaskType and EventType. If the same activity appears
in both dynamic picklists, duplicate activities appear.

`TaskType` and `EventType` can each have a `Call` type. Internally, they are distinct from
each other.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a record the activity is related to which contains more details about the activity.
For example, an activity can be related to an EmailMessage record.

This is a relationship field.

**Relationship Name**
AlternateDetail

**Relationship Type**
Lookup

**Refers To**
EmailMessage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Duration of the call in seconds.


-----

```
CallObject
CallType
CompletedDateTime
ConnectionReceivedId
ConnectionSentId

```

**Type**
string

**Properties**
Filter, Group,Nillable, Sort

**Description**

Name of a call center. Limit is 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of call being answered: Inbound, Internal, or Outbound.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status. This value is always null.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that shared this record with your
organization. This field is available only if your organization has enabled Salesforce to
Salesforce and only in API versions 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that your organization shared this record
with. This field is available only if your organization has enabled Salesforce to Salesforce, and
only in API versions 28.0 and later. The value is always `null. You can use the`
PartnerNetworkRecordConnection object to forward records to connections.


-----

```
Description
DurationInMinutes
EndDateTime
IsAllDayEvent
IsClosed

```

**Type**
textarea

**Properties**
Nillable

**Description**
Contains a description of the event or task. Limit is 32 KB.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the duration of the event or task.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the end date and time of the event or task. Available in versions 27.0 and later. This
field is optional, depending on the following:

**•** If IsAllDayEvent is true, you can supply a value for either DurationInMinutes
or `EndDateTime. Supplying values in both fields is allowed if the values add up to`
the same amount of time. If both fields are `null, the duration defaults to one day.`

**•** If `IsAllDayEvent is false, a value must be supplied for either`
`DurationInMinutes` or EndDateTime. Supplying values in both fields is allowed
if the values add up to the same amount of time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true, then the activity is an event spanning a full day, and`
the ActivityDate defines the date of the event. If the value of this field is set to false,
then the activity may be an event spanning less than a full day, or it may be a task. The default
value of this field is `false. Label is` `All-Day Event.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsDeleted
IsHighPriority
IsReminderSet
IsTask
IsVisibleInSelfService

```

**Description**
Indicates whether a task is closed (true) or not closed (false). The default value of this
field is `false. This field is set indirectly by setting` `Status` on the task—each picklist
value has a corresponding `IsClosed` value. Label is `Closed.`

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has been moved to the Recycle Bin (true) or not (false).
Label is `Deleted.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a high-priority task. The default value of this field is `false. This field is derived`
from the `Priority` field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a reminder is set for an activity (true) or not (false). The default value
of this field is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to true, then the activity is a task; if the value is set to false,
then the activity is an event. The default value of this field is `false. Label is` `Task.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Location
OwnerId
PrimaryAccountId
PrimaryWhoId

```

**Description**
If the value of this field is set to `true, then the activity can be viewed in the self-service`
portal. The default value of this field is false. Label is Visible in Self-Service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the activity is an event, then this field represents the location of the event. If the activity is
a task, then the value is `null.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the user or group who owns the activity.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the AccountId value from the activity record. Available in API versions 30.0 and
later to organizations that use Shared Activities.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `WhoId` value from the activity record. Available in API versions 30.0 and later
to organizations that have enabled Shared Activities.


-----

```
Priority
ReminderDateTime
Status
Subject

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the priority of a task, such as high, normal, or low. The default value of this field is
```
  Normal.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the time at which a reminder is scheduled to fire if IsReminderSet is set to
`true. If` `IsReminderSet` is set to `false, then either the user has deselected the`
reminder checkbox in the user interface or the reminder has already fired at the time indicated
by the value.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the current status of a task. The default value of this field is `Not Started. Each`
predefined status field sets a value for `IsClosed. To obtain picklist values, query the`
TaskStatus object.

Possible values are:

**•** Completed

**•** Deferred

**•** In Progress

**•** Not Started

**•** Waiting on someone else

**Type**
combobox

**Properties**
Filter, Nillable, Sort

**Description**
Contains the subject of the task or event.


-----

```
WhatId
WhoId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The `WhatId` represents nonhuman objects such as accounts, opportunities, campaigns,
cases, or custom objects. `WhatIds are polymorphic. Polymorphic means a` `WhatId` is
equivalent to the ID of a related object. The label is `Related To ID.`

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant, ContactRequest,
Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo, DelegatedAccount,
DocumentChecklistItem, EnrollmentEligibilityCriteria, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
ListEmail, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**

The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
```
                ID.

```
If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID.`

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

##### Usage

**Query activities that are related to an object**

**1. Optionally, issue a describe call against the object whose activities you want to query, to get a suggestion of the correct SOQL**
query to use.

**2. Issue a SOQL relationship query with a main clause that references the object and an inner clause that references the activity**
history. For example:
```
    SELECT
     (SELECT ActivityDate, Description
      FROM OpenActivities)
    FROM Account
    WHERE Name Like 'XYZ%'

```
The user interface enforces sharing rules, filtering out related-list items that a user doesn’t have permission to see.

The following constraints on users who don’t have the “View All Data” permission help prevent performance issues.

**•** In the main clause of the relationship query, you can reference only one record. For example, you can’t filter on all records where
the account name starts with “A.” Instead, you must reference a single account record.
```
    SELECT
     (SELECT ActivityDate, Description
      FROM OpenActivities
      ORDER BY ActivityDate ASC NULLS LAST, LastModifiedDate DESC
      LIMIT 500)
    FROM Account
    WHERE Name = 'Acme'
    LIMIT 1

```
**•** In the inner clause of the query, you can’t use `WHERE.`


-----

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.

**•** In the inner clause of the query, you must sort on `ActivityDate` in ascending order and `LastModifiedDate` in
descending order. You can optionally display nulls last. For example: `ORDER BY ActivityDate ASC NULLS LAST,`
```
   LastModifiedDate DESC.

```
SEE ALSO:

Task
