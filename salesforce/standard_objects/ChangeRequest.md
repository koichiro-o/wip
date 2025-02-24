#### ChangeRequest

Represents a decision to implement a formal request for a change (RFC). This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
BusinessJustification
BusinessReason
Category

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the business reason to implement the change. This field can store up to 32
KB of data, but only the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The core reason for creating the change request.

Possible values are:

**•** `t2`

**Type**
picklist


-----

```
ChangeRequestNumber
ChangeType
Description
EstimatedEndTime
EstimatedStartTime

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of change request. Administrators set field values.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated change request number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of change request. Administrators set field values.

Possible values are:

**•** `Emergency`

**•** `Major`

**•** `Normal`

**•** `Standard`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request. This field can store up to 32 KB of data, but only the
first 255 characters display in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request is estimated to be implemented.

**Type**
dateTime


-----

```
FinalReviewDateTime
FinalReviewNotes
Impact
LastReferencedDate

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated date and time (in UTC) when the change request is implemented.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request was reviewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes left by the change request reviewer. This field can store up to 32 KB of data, but only
the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows the impact of a requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


-----

```
LastViewedDate
OwnerId
Priority
RemediationPlan

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A polymorphic relationship field that represents the user or group assigned as the change
reviewer.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of a requested change.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
ReviewerId
RiskImpactAnalysis
RiskLevel
Status

```

**Description**
A description of the steps required to resolve the incident. This field can store up to 32 KB
of data, but only the first 255 characters display in reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who reviewed the change request.

This is a relationship field.

**Relationship Name**
Reviewer

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An assessment of the risk involved with the implementation of the change request.
Administrators set field values, and each value can have up to 20 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The risk level associated with adopting the requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
picklist


-----

```
StatusCode
Subject

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents any custom or granular stages a customer may want to track. This will be a
dependent picklist.

Possible values are:

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the change.

Possible values are:

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

**Type**
string


-----

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the requested change.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestChangeEvent on page 67 (API version 59.0)**
Change events are available for the object.

**ChangeRequestFeed on page 54**
Feed tracking is available for the object.

**ChangeRequestHistory on page 62**
History is available for tracked fields of the object.

**ChangeRequestOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ChangeRequestShare on page 66**
Sharing is available for the object.
