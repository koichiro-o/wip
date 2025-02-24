#### VoiceCallRecording

Represents a call recording in Service Cloud Voice and Sales Dialer. Call recordings for Service Cloud Voice with Amazon Connect and
for Service Cloud Voice with Partner Telephony from Amazon Connect are stored in S3 buckets on your Amazon Web Services (AWS)
account and can be accessed via AWS. Call recordings for Sales Dialer are saved as files in Salesforce.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
DurationInSeconds

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The total length (in seconds) of the voice call recording.

This value depends on which parameters are passed to the `PATCH`
`/telephony/v1/voiceCalls/{CALL ID}` API.

**•** If the totalRecordingDuration parameter is passed, then
`DurationInSeconds` = `totalRecordingDuration.`

**•** If the agentInteractionDuration and totalHoldDuration parameters are passed,
then DurationInSeconds = agentInteractionDuration +
```
   totalHoldDuration.

```
**•** If the agentInteractionDuration, totalHoldDuration, and
totalRecordingDuration parameters are passed, then
`DurationInSeconds` = totalRecordingDuration.


-----

```
IntelligenceScore
IsConsented
MediaContentId
Name
OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The intelligence score of the recording.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the call recording was indicated as consented or not.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related media content, a ContentDocument. The record counts
toward your org’s file storage quota.

This is a relationship field.

**Relationship Name**
MediaContent

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the call recording file.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
UploadDateTime
VoiceCallId

##### Associated Objects

```

**Description**
The ID of the owner of the call recording.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time and date that the recording was uploaded.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the related phone call. The property nillable has been
removed in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
VoiceCall

**Relationship Type**
Lookup

**Refers To**
VoiceCall


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VoiceCallRecordingChangeEvent (API version 48.0)**
Change events are available for the object.

**VoiceCallRecordingOwnerSharingRule**

Sharing rules are available for the object. Removed in API version 50.0 and later.


-----

**VoiceCallRecordingShare**

Sharing is available for the object. Removed in API version 50.0 and later.
