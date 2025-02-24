#### UnifiedVoiceCallParticipant

Represents a participant in a voice call. This object is available for reports and dashboards in the Winter ’24 release and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```
Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

##### Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

##### Fields

```
ActivityId

```

**Type**
reference


-----

```
ChannelAddress
ListenRatio
ParticipantType

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the voice call the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedVoiceCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The phone number of the participant. The phone number is captured at the time of the
communication; it doesn’t change if the contact’s phone number is updated later.

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was listening versus talking in the voice call.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`


-----

```
PersonId
TalkRatio
