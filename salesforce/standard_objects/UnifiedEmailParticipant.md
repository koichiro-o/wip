#### UnifiedEmailParticipant

Represents a participant in an email. This object is available for reports and dashboards in the Winter ’24 release and later.

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email the person is participating in.

This field is a relationship field.

**Relationship Name**
Activity

**Relationship Type**
Lookup


-----

```
ChannelAddress
ParticipantType
PersonId

```

**Refers To**
UnifiedEmail

**Type**
string

**Properties**
Filter, Nillable

**Description**
Email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Participant’s role in the email.

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
ID of the person participating in the email.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


-----
