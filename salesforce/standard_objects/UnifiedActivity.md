#### UnifiedActivity

Represents an activity that is automatically captured from Einstein Activity Capture (EAC) or other activity data, such as calls, manually
logged tasks, and emails. This object consists of fields common to all types of activity-related objects such as Event, Task, EmailMessage,
VoiceCall, VideoCall, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

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

```

**Type**
dateTime

**Properties**
Filter, Sort


-----

```
ActivitySubType
ActivityType
DetailId

```

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

Possible values are:

**•** `UnifiedActivity`

**•** `UnifiedEmail`

**•** `UnifiedMeeting`

**•** `UnifiedTask`

**•** `UnifiedVideoCall`

**•** `UnifiedVoiceCall`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object.

This field is a polymorphic relationship field.

**Relationship Name**
Detail


-----

```
InternalEventKey
IsInsightAvailable
Snippet
Subject

```

**Relationship Type**
Lookup

**Refers To**
EmailMessage, Event, Task, VideoCall, VoiceCall

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
An abbreviation of the activity body or description. This field has a maximum length of 255
characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the task or event.

