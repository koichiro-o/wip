#### UnifiedVoiceCall

Represents a voice call that is captured or synced from a VoiceCall or Task record. This object is available for reports and dashboards in
the Winter ’24 release and later.

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


-----

```
ActivityType
CallDurationInSeconds
DetailId
InternalEventKey
IsInsightAvailable

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The type of activity.

Possible value is `UnifiedVoiceCall.`

**Type**
int

**Properties**
Filter, Nillable

**Description**
The duration of the voice call in seconds.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

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
VoiceCall

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for internal use.

**Type**
boolean


-----

```
Snippet
Subject

```

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
An abbreviation of the voice call content. This field has a maximum length of 255 characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the voice call.

