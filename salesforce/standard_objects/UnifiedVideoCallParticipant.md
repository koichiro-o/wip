#### UnifiedVideoCallParticipant

Represents a participant in a video call. This object is available for reports and dashboards in the Winter ’24 release and later.

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
ChannelAddress
ListenRatio

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the video call the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedVideoCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
double


-----

```
ParticipantType
PersonId
TalkRatio

```

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was listening versus talking in the video call.

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

**•** `Organizer`

**•** `To`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person participating in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
double

**Properties**
Filter, Nillable


-----

**Description**
Ratio of time the participant was talking versus listening in the video call.
