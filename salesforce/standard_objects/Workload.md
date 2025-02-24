#### Workload

Represents the time series for work item volume and average handle time from aggregation and forecasting processes. This object is
available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license. To view, create, edit, or delete records, the user must have the Workforce
Engagement Analyst permission set.

##### Fields

```
Description
EndDateTime
IsOmni
Name

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the workload

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The end date and time of the time series represented by the Workload object.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the workload is Omni-based.

The default value is 'false'.

**Type**
string


-----

```
OwnerId
StartDateTime
TimeZone
WorkloadType

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The workload name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the workload.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The start date and time of the time series represented by the Workload object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone associated with the workload. Possible values are the time zones supported
by Workforce Engagement.

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the workload.


-----

Possible values are:

**•** `F—Forecasted`

**•** `H—Historical`

**•** `IH—Intraday History. This value is available in API version 55.0 and later.`

The default value is 'H'.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkloadOwnerSharingRule on page 64**
Sharing rules are available for the object.

**WorkloadShare on page 66**
Sharing is available for the object.
