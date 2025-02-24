#### UnifiedEmail

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity insight associated with the keyword.

This field is a relationship field.

**Relationship Name**
Insight

**Relationship Type**
Lookup

**Refers To**
UnifiedActivityInsight

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Keyword mentioned in the communication.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Number of times the keyword was mentioned in the communication.


Represents an email that was captured or synced from an EmailMessage or Task record. This object is available for reports and dashboards
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
DetailId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the email in the Coordinated Universal Time (UTC) time zone.

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

Possible value is `UnifiedEmail.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object that contains detailed activity-specific information. The object depends
on the activity type. For example, the detail for a Task activity is a Task object. The detail for
an Event activity is an Event object. If the email was captured from Einstein Activity Capture,
this field returns a blank value.

This field is a relationship field.

**Relationship Name**
Detail

**Relationship Type**
Lookup

**Refers To**
EmailMessage


-----

```
Direction
InternalEventKey
IsInsightAvailable
IsPrivate
Snippet

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
The direction in which the email was sent or received.

Possible values are:

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

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
boolean

**Properties**
Defaulted on create Filter

**Description**
Indicates whether the activity's sensitive fields (Subject and `Snippet) are masked`
(true) or visible (false) for non-owners.

The default value is `false.`

**Type**
string

**Properties**
Nillable


-----

```
Subject

```

**Description**
An abbreviation of the email content. This field has a maximum length of 255 characters.

**Type**
string

**Properties**
None

**Description**
Contains the subject of the email.

