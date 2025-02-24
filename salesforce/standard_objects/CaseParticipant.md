#### CaseParticipant

Represents a junction between a case, and an account or a contact. This object stores the details of the participant associated with a
case. This participant could be the applicant, co-applicant, a household, or even a business account. This object is available in API version
54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

Fields and values added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.

##### Fields

```
AuthorizationProof
CaseId
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the participant communicated their consent. This field is available in API version 58.0
and later.

Possible values are:

**•** `Email Consent`

**•** `Joint Ownership`

**•** `Power of Attorney`

**•** `Verbal Consent`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The case associated with the case participant record.

This field is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


-----

```
LastViewedDate
Name
ParticipantId
PreferredCallTimeFrom
PreferredCallTimeTo

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
possibly the user only accessed this record or list view (LastReferencedDate) but
didn't view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the case participant record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The participant associated with the case participant record.

This field is a polymorphic relationship field.

**Relationship Name**
Participant

**Relationship Type**
Lookup

**Refers To**
Account, Contact

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

**Type**
time


-----

```
PreferredCommunicationMode
Role
Status

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the participant prefers to receive messages. This field is available in API version 58.0
and later.

Possible values are:

**•** `Email`

**•** `Phone`

**•** `SMS`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the case participant.

Possible values are:

**•** `Applicant`

**•** `Complainant Representative` (Available in API version 58.0 and later.)

**•** `Inspection Officer`

**•** `Lawyer`

**•** `Observer`

**•** `Perpetrator`

**•** `Primary Caretaker`

**•** `Victim`

The default value is `Applicant.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

**Description**
The status of the case participant.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `In Review` (Available in API version 58.0 and later.)

**•** `Pending` (Available in API version 58.0 and later.)

**•** `Submitted` (Available in API version 58.0 and later.)

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseParticipantFeed on page 54**
Feed tracking is available for the object.

**CaseParticipantHistory on page 62**
History is available for tracked fields of the object.
