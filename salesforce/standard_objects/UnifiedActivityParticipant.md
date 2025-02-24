#### UnifiedActivityParticipant

Represents a participant in an activity. For example, a participant in a voice call is someone who initiated the call or someone who
received the call.This object is available for reports and dashboards in the Winter ’24 release and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```
Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

##### Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.


-----

##### Fields

**Field**
```
ActivityId
ChannelAddress
ParticipantType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity that the person participated in.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedEmail, UnifiedMeeting, UnifiedTask, UnifiedVideoCall, UnifiedVoiceCall

**Type**
string

**Properties**
Filter, Nillable

**Description**
The channel-specific address used to identify the participant in an external communication.
For example, an email address in an email or a phone number in a voice call. The value is
captured at the time of the communication; it doesn’t change if the contact’s email address
or phone number is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The role of the participant in the activity.

Possible values are:

**•** `AssignedTo`

**•** `Attendee`

**•** `BCC`

**•** `CC`

**•** `From`

**•** `OptionalAttendee`

**•** `Organizer`


-----

```
PersonId

```


**•** `To`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person who participated in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

