#### ShiftSegmentType

```

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the shift in which the segment is scheduled.

This is a relationship field.

**Relationship Name**
Shift

**Relationship Type**
Lookup

**Refers To**
Shift

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment starts.


Represents a type of activity scheduled within a shift. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license and Workforce Engagement must be enabled. The user requires the Workforce
Engagement Planner or Workforce Engagement Admin permission set.

##### Fields

```
AdherenceThreshold

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Category
Color
Description
DeveloperName

```

**Description**
A threshold, in minutes. If the agent starts the scheduled activity within this threshold, the
shift segment activity is in adherence.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A category for the type of shift segment.

Possible values are:

**•** `Break—Break times, such as a coffee or lunch break.`

**•** `NonWork—Non-working activities, such as training or meetings.`

**•** `Work—Work activities, such as answering calls, responding to chats, or handling cases.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shift activities of this type are displayed in the UI. Use a 3- or
6-digit hexadecimal format, for example #FF00FF.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the shift segment type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.


-----

```
IsActive
Language
MasterLabel
ServicePresenceStatusId

```

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the shift segment type is active (true) or not (false).

The default value is `true.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the shift segment type.

Possible values are the languages that Workforce Engagement supports.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label of the shift segment type.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the associated service presence status for segments of this type.

This is a relationship field.

**Relationship Name**
ServicePresenceStatus

**Relationship Type**
Lookup


-----

**Refers To**
ServicePresenceStatus
