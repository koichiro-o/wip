#### UnifiedMeetingParticipant

Represents a participant in a meeting. This object is available for reports and dashboards in the Winter ’24 release and later.

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

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the meeting that the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedMeeting

**Type**
string

**Properties**
Filter, Nillable


-----

```
ParticipantType
PersonId
