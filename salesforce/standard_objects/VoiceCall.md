#### VoiceCall

Represents a call in Service Cloud Voice, Sales Dialer, or other supported voice connectors. For Service Cloud Voice, this can be a phone
or Voice over Internet Protocol (VoIP) call. This object is available in API version 40.0 and later.

[To manage VoiceCall records when using Service Cloud Voice, see the Telephony Integration REST API.](https://developer.salesforce.com/docs/atlas.en-us.254.0.voice_developer_guide.meta/voice_developer_guide/voice_rest_overview.htm)

The fields in the VoiceCall object apply to the Sales Dialer and Service Cloud Voice features unless otherwise stated in the field description.

In addition to the standard fields listed in this page, you can define up to 50 custom fields for the VoiceCall object. As an alternative to
using custom fields, consider creating a custom object with lookup fields that look up to the VoiceCall object.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
Only users with the Modify All Data permission can delete call records.

To edit voice call records, Sales Dialer or Service Cloud Voice permissions are required. This includes the Dialer Outbound permission set
for Sales Dialer, or the Contact Center Agent or Contact Center Admin permission sets for Service Cloud Voice.


-----

##### Fields

**Field Name**
```
ActivityId
AgentSentimentScore
CallAcceptDateTime
CallCenterId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the activity record. Available in API version 48.0 and later.

This is a relationship field.

**Relationship Name**
Activity

**Refers To**
Task

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
[If Sentiment Journey in Service Cloud Voice is set up, this field represents the](https://help.salesforce.com/s/articleView?id=sf.voice_conversation_sentiments.htm&language=en_US)
rep’s overall sentiment score post-call in a conversation event. The value must
be between -5 (lowest negative sentiment score) and 5 (highest positive
sentiment score), with 0 being a neutral sentiment score. Available in API version
59.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the date and time (in UTC)
when an agent accepts the call. Available in API version 48.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the call
center (CallCenter Id) where the activity took place. Available in API version 48.0
and later.

This is a relationship field.


-----

```
CallConnectDateTime
CallDisposition
CallDurationInSeconds
CallEndDateTime

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
For Sales Dialer, this field represents the date and time (in UTC) when the call
was connected.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The status of the phone call.

For Sales Dialer, possible values are:

**•** `in progress`

**•** `busy`

**•** `failed`

For Service Cloud Voice, possible values are:

**•** `new—The voice call record has been created.`

**•** `in-progress—The call has been accepted (or, for outbound messages,`
initiated) by an agent.

**•** `completed—The call has ended. This includes calls that are transferred.`
(If a call is transferred, another voice call record is created to track the state
of the transferred call.) If After Conversation Work (ACW) is enabled, that work
begins after the call completes.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total duration (in seconds) of the call.

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The date and time (in UTC) when the call ended.


-----

```
CallerId
CallerIdType
CallOrigin

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, this field represents the unique ID of the participant who
initiated the call. If “Match Callers to End User Records” is enabled in Lightning
Experience, the value is null and the EndUserId field is used instead to
determine the end user associated with this voice call. Available in API version
48.0 and later.

This is a relationship field.

**Relationship Name**
Caller

**Relationship Type**
Lookup

**Refer To**
ConversationParticipant

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Sales Dialer, this field represents the number displayed for outbound calls.
Possible values are:

**•** `VendorLine—User.`

**•** `CompanyNumber—Company.`

**•** `LocalPresence—Local Presence.`

**•** `CustomCallerId—Custom Caller ID.`

Available in API version 41.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Information about how this call originated. For Service Cloud Voice, possible
values are:

**•** `Preview—Preview dialer.`

**•** `Progressive—Progressive dialer.`

**•** `Voicemail—Voicemail call.`


-----

```
CallQueuedDateTime
CallRecordingId
CallResolution
CallStartDateTime

```

Available in API version 56.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the date and time (in UTC)
when the call was added to a queue to be routed to an agent. Available in API
version 48.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, this field represents the unique ID of the call recording
for the voice call. Available in API version 41.0 and later.

This is a relationship field.

**Relationship Name**
CallRecording

**Relationship Type**
Lookup

**Refers To**
VoiceCallRecording

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The resolution outcome of the call. The default value is Resolved, meaning
the call has been resolved. Available in API version 48.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The date and time (UTC) when the call started.


-----

```
CallSubtype
CallType
CoachingDurationInSeconds

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Service Cloud Voice, this field represents the network or protocol over which
the phone or Voice over Internet Protocol (VoIP) call is made. Possible values are:

**•** `PSTN`

**•** `WebRTC`

Available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The types of call.

For Sales Dialer, possible values are:

**•** `Bridge`

**•** `Coach`

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

For Service Cloud Voice, possible values are:

**•** `Callback`

**•** `Consult`

**•** `Inbound`

**•** `InternalCall`

**•** `Outbound`

**•** `Transfer`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the total duration (in seconds) of the coaching
session. This field only appears if call coaching is enabled. Available in API version
41.0 and later.


-----

```
ConferenceKey
ConversationId
CurrencyCode
CustomerHoldDuration
CustomerSentimentScore

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the related conference key. This field is only
available if call monitoring is enabled. Available in API version 41.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the
conversation. This field is only available if call monitoring is enabled. Available in
API version 48.0 and later.

This is a relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup

**Refers To**
Conversation

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Sales Dialer, this field represents the ISO currency code used to bill the call.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the total duration (in
seconds) of all the holds that occurred during the voice call. Available in API
version 49.0 and later.

**Type**
double


-----

```
Description
DisconnectReason
EndUserId

```

**Properties**
Filter, Nillable, Sort

**Description**
[If Sentiment Journey in Service Cloud Voice is set up, this field represents the](https://help.salesforce.com/s/articleView?id=sf.voice_conversation_sentiments.htm&language=en_US)
customer’s overall sentiment score post-call in a conversation event. The value
must be between -5 (lowest negative sentiment score) and 5 (highest positive
sentiment score), with 0 being a neutral sentiment score. Available in API version
59.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
If Service Cloud Voice is enabled, this field represents a text field where the agent
can enter a summary of the call. Available in API version 48.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable

**Description**
If Service Cloud Voice is enabled, this field represents the reason why the voice
call was disconnected. The reason is provided by the partner telephony. For
Amazon Connect instances, this value is automatically populated through the
Contact Trace Record (CTR) if you have Contact Center version 13.0 or later. See
[DisconnectReason in the Amazon Connect contact records data model page for](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html)
a list of possible reasons why a voice call may be disconnected. For all other
partner telephony models, configure this feature through
the disconnectReason parameter in the Update a Voice Call Record
Telephony Integration API. Available in API version 59.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Service Cloud Voice, if “Match Callers to End User Records” is enabled in
Lightning Experience, this field represents the unique ID of the messaging end
user (MessagingEndUser `ID) associated with this voice call. Available in API`
version 53.0 and later.

This is a relationship field.


-----

```
RecipientContactInfo
IsDiarizationOptIn
IsRecorded
LastReferencedDate
LastViewedDate

```

**Relationship Name**
EndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser

**Type**
phone

**Properties**
Create, Filter, Group, Sort

**Description**
The number of the user who initiated the call. This field was renamed from
`FromPhoneNumber` to RecipientContactInfo in API version 62.0.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether optimal speaker separation (diarization) is opted in (true) or
not (false) for the call.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a Voice Call Recording record was created (true) or not
(false) for this voice call. The default value is `false. Available in API version`
44.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last viewed a record related
to this voice call.

**Type**
dateTime


-----

```
LongestHoldDuration
MediaProviderId
Name
NextCallId

```

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last viewed this voice call. If
the record has not been viewed before, this value is null. Referencing a record
(LastReferencedDate) doesn’t count as viewing it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the longest hold duration
(in seconds) that occurred during the call. Available in API version 49.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique ID of the related media provider. Available in API version 49.0 and
later.

This is a relationship field.

**Relationship Name**
MediaProvider

**Relationship Type**
Lookup

**Refers To**
CallCoachingMediaProvider

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the voice call record. For example, `VC-00000001. Available in`
API version 60.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
NumberOfHolds
OwnerId
PreviousCallId

```

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the next
call if the call was transferred to another agent. If there is no other agent, this
value is null. Available in API version 48.0 and later.

This is a relationship field.

**Relationship Name**
NextCall

**Relationship Type**
Lookup

**Refers To**
VoiceCall

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the number of times the
customer was put on hold. Available in API version 49.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID of the user who owns the voice call record.

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
Create, Filter, Group, Nillable, Sort


-----

```
Price
QualityScore
QueueName
RecipientId

```

**Description**
If Service Cloud Voice is enabled, this field represents the unique ID of the previous
call if the call was transferred from another agent. When there is no previous call,
this value is null. Available in API version 48.0 and later.

This is a relationship field.

**Relationship Name**
PreviousCall

**Relationship Type**
Lookup

**Refers To**
VoiceCall

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
For Sales Dialer, this field represents the cost of the phone call.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
If Service Cloud Voice is enabled, this field represents the value of the Mean
Opinion Score (MOS) that measures voice call quality. This algorithm is based on
packet loss percentage, average latency, and average jitter. Available in API version
53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If Service Cloud Voice is enabled, this field represents the name of the agent
queue. Available in API version 49.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
RecordyTypeId
RelatedRecordId

```

**Description**
For Service Cloud Voice, this field represents the unique ID of the participant who
received the call. If “Match Callers to End User Records” is enabled in Lightning
Experience, this value is null and the EndUserId field is used instead to
determine the end user associated with this voice call.

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
ConversationParticipant

**Type**
reference

**Properties**
Create, Filter, Nillable, Updates

**Description**
The ID of the voice call record type assigned to this voice call. If a record type
isn't assigned to this voice call, the value is null. Available in API version 59.0 and
later.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the related record. Associates the VoiceCall record to a standard
or custom object record. For Service Cloud Voice, supported related records
include the standard objects Account, Case, Contact, Lead, and Opportunity. For
Sales Dialer, supported related records include custom objects.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord


-----

```
SourceType
CallerContactInfo
TranscribedLanguage
UserId

```

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact, Lead, Opportunity

**Type**
picklist

**Properties**
Create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The general purpose of the call. The permission sets assigned to the voice call
owner determine the value. A call’s source type controls which insights Einstein
Conversation Insights applies during analysis.

Possible values are:

**•** Sales

**•** Service

Available in API version 52.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Sort

**Description**
The recipient of the call. For inbound, transfer, and callback calls, this value is the
agent's number. For outbound calls, this value is the customer's number. This
field was renamed from ToPhoneNumber to CallerContactInfo in
API version 62.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The language that is transcribed for this voice call.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
VendorCallKey
VendorParentCallKey
VendorType
VoiceVendorLineId

```

**Description**
The unique ID of the Salesforce user who initiates an outbound call or accepts
an inbound call. If no one takes the call, this value defaults to null.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, idLookup, Sort

**Description**
The unique ID of the child leg of the call that’s provided by the Sales Dialer vendor
or Service Cloud Voice telephony provider.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For Sales Dialer, this field represents the unique ID of the parent leg of the call
that’s provided by the Dialer vendor.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For Sales Dialer, this field represents the type of Dialer vendor. For Service Cloud
Voice, this field is always set to ContactCenter. Available in API version 41.0
and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

**Description**
For Sales Dialer, this field represents the unique ID of the associated Dialer vendor
line.

This is a relationship field.

**Relationship Name**
VoiceVendorLine

**Relationship Type**
Lookup

**Refers To**
VoiceVendorLine

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**VoiceCallChangeEvent (Available in API version 48.0 and later)**
Change events are available for the object.

**VoiceCallFeed (Available in API version 50.0 and later.)**
Feed tracking is available for the object.

**VoiceCallOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCallShare**

Sharing is available for the object.
