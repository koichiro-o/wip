#### WorkforceCapacity

Represents the time series for actual or forecasted workforce allocation. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
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
Additional information about the planning.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The end date and time of the planning.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived from isOmni field on Workload object. Indicates that the workload is Omni-based.
If workload is null, the field value defaults to `false.`

The default value is `false.`

**Type**
string


-----

```
OwnerId
PlanType
StartDateTime
TimeZone

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of capacity plan. Possible values are:

**•** `Intraday—The plan shows intraday management.`

**•** `LongTerm—The plan predicts the required number of full-time employees (FTEs).`

**•** `ShortTerm—The plan predicts the required number of shifts.`

This field is available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date and time of the planning.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
WorkloadId

##### Associated Objects

```

**Description**
The time zone associated with the capacity plan. Possible values are the time zones supported
by Workforce Engagement.

This field is available in API version 56.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The foreign key to the Workload object.

This is a relationship field.

**Relationship Name**
Workload

**Relationship Type**
Lookup

**Refers To**
Workload


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkforceCapacityOwnerSharingRule on page 64**
Sharing rules are available for the object.

**WorkforceCapacityShare on page 66**
Sharing is available for the object.
