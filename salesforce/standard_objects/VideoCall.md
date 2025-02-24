#### VideoCall

```
Represents a video call.


**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly—Users whose access to the application is limited to Chatter. This user type`
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal—CSP Lite Portal license. Users whose access is limited because`
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess—Customer Success license. Users whose access is limited`
because they’re organization customers and access the application through a customer
portal.

**•** `Guest—Users whose access is limited so that your customers can view and interact`
with your site without logging in.

**•** `PowerCustomerSuccess—Power Customer Success license. Users whose access`
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner—Power Partner license. Users whose access is limited because they’re`
partners and typically access the application through a partner portal or site.

**•** `SelfService—Users whose access is limited because they’re organization customers`
and access the application through a self-service portal.

**•** `Standard—Standard user license. This user type also includes Salesforce Platform`
and Salesforce Platform One user licenses, and admins for this org.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of the Visualforce view state in bytes.


One `VideoCall` record can be related to several `VideoCallRecording` records — for example, a video call can have several
video recordings and a transcript. As well, one video call record can be associated with several video call participant records.


-----

This object is available in API version 51.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), update()

 Fields

```
```
Description
DurationInSeconds
EndDateTime
EventId

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the video call. Typically, the sales rep enters the description.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The video call duration in seconds.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time the video call ended, in universal time coordinated (UTC).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the event record associated with this video call. Reserved for future use.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup


-----

```
ExternalId
HostId
IntelligenceScore
IsCallCoachingIncluded

```

**Refers To**
Event

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the video call, sent by the video call provider.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who hosted the meeting.

This is a relationship field.

**Relationship Name**
Host

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Einstein Intelligence score for the video call. Video calls with higher scores are likely to
contain more relevant information. For example, video calls where product names and
competitor names are mentioned tend to have a higher score.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether Einstein Conversation Insights is available for this org and this user
`(true)` or not `(false).`


-----

```
IsDiarizationOptIn
IsRecorded
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether optimal speaker separation (diarization) is opted in `(true)` or not
`(false)` for the call.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the video call was recorded `(true)` or not `(false).`

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

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
```
  null, the user might have only accessed this record or list view (LastReferencedDate)

```
but not viewed it.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the video call. Typically entered by the sales rep.

**Type**
reference


-----

```
RelatedRecordId
StartDateTime
TranscribedLanguage

```

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user who created the video call.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the account or opportunity related to this video call.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Opportunity

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the video call started, in universal time coordinated (UTC).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The language that is transcribed for this video call.


-----

```
VendorMeetingKey
VendorMeetingUuid
VendorName

##### Associated Objects

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The vendor's ID for this video call.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The vendor's unique identifier for this video call.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the vendor providing the video call software.

Possible values are:

**•** `ZOOM`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VideoCallChangeEvent (API version 51.0)**
Change events are available for the object.

SEE ALSO:

VideoCallParticipant

VideoCallRecording
