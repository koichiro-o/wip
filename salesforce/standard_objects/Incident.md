#### Incident

An Incident is any unplanned business interruption that has wide-sweeping impacts and requires an urgent fix. This object contains the
details of the incident, documenting the history of the incident from registration to closure. This object is available in API version 53.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Category
Description
DetectedDateTime
EndDateTime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the incident. This field can store up to 32 KB of data, but only the first 255
characters appear in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident was first detected.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident ended.


-----

```
Impact
IncidentNumber
IsMajorIncident
LastReferencedDate
LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The incident's impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated number for the incident.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the incident is business-critical. If set to true, the incident is widespread
and business-critical. The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last accessed this record, a list view, or
another related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
OwnerId
ParentIncidentId
Priority

```

**Description**
The date and time (in UTC) when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A polymorphic relationship field that represents the user or group assigned to resolve the
incident.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of an incident above one or more related incidents in an incident hierarchy.

This is a relationship field.

**Relationship Name**
ParentIncident

**Relationship Type**
Lookup

**Refers To**
Incident

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of the incident.

Possible values are:

**•** `Critical`


-----

```
PriorityOverrideReason
ReportedMethod
ResolutionDateTime
ResolutionSummary
ResolvedById

```


**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why a priority should be changed or edited.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates how the incident was reported to customer service.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident was resolved.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of possible steps to resolve the incident.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the user who resolved the incident.

This is a relationship field.


-----

```
StartDateTime
Status
StatusCode

```

**Relationship Name**
ResolvedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident began.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any custom or granular stages a customer may want to track.

Possible values are:

**•** `Completed`

**•** `In Progress`

**•** `New`

**•** `Open`

**•** `Problem Created`

**•** `Resolved`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The incident's status.

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `Open`


-----

```
SubCategory
Subject
Type
Urgency

```


**•** `ProblemCreated`

**•** `Resolved`

The default value is 'New'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident. One level deeper than Category. Administrators set field values.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the incident.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident, for example, question or problem. Administrators set field values.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A measure of how long the resolution can be delayed until an incident, problem, or change
has a significant business impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IncidentChangeEvent on page 67**
Change events are available for the object.

**IncidentFeed on page 54**
Feed tracking is available for the object.

**IncidentHistory on page 62**
History is available for tracked fields of the object.

**IncidentOwnerSharingRule on page 64**
Sharing rules are available for the object.

**IncidentShare on page 66**
Sharing is available for the object.
