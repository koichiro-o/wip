#### VideoCallParticipant

Represents a participant in a video call.

Participant information can come from the video call provider (for example, Zoom), or Salesforce.

This object is available in API version 51.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Email
IsAllowed
JoinDateTime
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The email address of the participant, from the video call provider.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the participant is admitted into the video call (true) or not (false).

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the participant joins the video call.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LeaveDateTime
Name
RelatedPersonId
VideoCallId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
```
  null, the user might have only accessed this record or list view (LastReferencedDate)

```
but not viewed it.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the participant leaves the video call.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The participant's name or phone number. This information is provided by the video call
provider.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the user, lead, or contact record for this participant.

This is a polymorphic relationship field.

**Relationship Name**
RelatedPerson

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the video call record.

This is a relationship field.


-----

**Relationship Name**
VideoCall

**Relationship Type**
Lookup

**Refers To**
VideoCall

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VideoCallParticipantChangeEvent (API version 55.0)**
Change events are available for the object.

SEE ALSO:

VideoCall

VideoCallRecording
