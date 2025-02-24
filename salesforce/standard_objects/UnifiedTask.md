#### UnifiedTask

```

**Description**
The email address of the participant. The email address is captured at the time of the
communication; it doesn’t change if the contact’s email address is updated later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The participant’s role in the meeting.

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
ID of the contact, lead, or user participating in the meeting.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


Represents a business activity such as a to-do item. This object is available for reports and dashboards in the Winter ’24 release and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```
Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

##### Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

##### Fields

```
ActivityDateTime
ActivitySubType
ActivityType
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
Always blank for this object.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedTask.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object.

This field is a relationship field.


-----

```
InternalEventKey
IsInsightAvailable
Snippet
Subject

```

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
Task

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
Indicates whether the activity has an insight associated with it (true) or not (false).

The default value is `false.`

**Type**
string

**Properties**
Nillable

**Description**
An abbreviation of the task body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
The subject line of the task.

