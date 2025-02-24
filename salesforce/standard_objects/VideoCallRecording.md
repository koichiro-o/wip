#### VideoCallRecording

Represents a recording from a video call, such as a video recording, a voice recording, or a transcript.

Video call recordings aren’t saved in Salesforce.

This object is available in API version 51.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
undelete()

 Fields

```
```
DurationInSeconds

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The video call duration in seconds, not the recording duration.


-----

```
EndDateTime
ExpirationDateTime
ExternalRecordingKey
FileSizeInByte
FileType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time the call ended, in universal time coordinated (UTC).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Reserved for internal use. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the video call recording, from the recording provider. For example, the Zoom ID
of the recording. This value is unique.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the video call recording, in bytes.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The file type of the video call recording.

Possible values are:

**•** `MP4—Video file`

**•** `M4A—Audio-only file`

**•** `TIMELINE—Time stamp file in JSON format.`

**•** `TRANSCRIPT—Transcription files in VTT format.`

**•** `CHAT—Text file containing chat messages from the video call.`


-----

```
LastReferencedDate
LastViewedDate
Name
StartDateTime
VideoCallRecordId

```


**•** `CC—File containing closed captions of the video call recording. The file is in VTT format.`

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
  null, the user only accessed this record or list view (LastReferencedDate) but not

```
viewed it.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the video call recording, entered by the sales rep.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start time of the video call recording.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the VideoCall record (the parent record).

This is a relationship field.

**Relationship Name**
VideoCallRecord


-----

**Relationship Type**
Lookup

**Refers To**
VideoCall

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**VideoCallRecordingChangeEvent (API version 51.0)**
Change events are available for the object.

SEE ALSO:

VideoCallParticipant

VideoCall
