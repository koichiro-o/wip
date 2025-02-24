#### UnifiedVideoCall

```


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
ID of the contact, lead, or user participating in the activity.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


Represents a video call that is captured or synced from the VideoCall or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.

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
ActivityDateTime
ActivitySubType
ActivityType
CallDurationInSeconds
DetailId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the activity in the Coordinated Universal Time (UTC) time zone.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.

Possible values are:

**•** `Captured`

**•** `LegacyCall`

**•** `Streamed`

**•** `VoiceCall`

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedVideoCall.`

**Type**
int

**Properties**
Filter, Nillable

**Description**
The duration of the video call in seconds.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
InternalEventKey
IsInsightAvailable
Snippet
Subject

```

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
VideoCall

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has an insight associated with it.

The default value is `false.`

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the activity body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the video call.


-----
