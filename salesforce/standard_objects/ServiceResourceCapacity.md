#### ServiceResourceCapacity

Represents the maximum number of scheduled hours or number of service appointments that a capacity-based service resource can
complete within a specific time period. This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
CapacityInHours
CapacityInWorkItems

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of hours that the resource can work per time period. You must fill
out this field, the `CapacityInWorkItems` field, or both.

**Type**
int


-----

```
CapacityNumber
EndDate
LastReferencedDate
LastViewedDate
ServiceResourceId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of service appointments that the resource can complete per
time period. You must fill out this field, the CapacityInHours field, or both.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the capacity record.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the capacity ends; for example, the end date of a contract.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced (LastReferencedDate)
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
StartDate
TimePeriod

##### Usage

```

**Description**
The associated service resource. You can set multiple capacities for a resource as
long as their start and end dates do not overlap.

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
The date the capacity goes into effect.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Days, Hours, or Months. For example, if a resource can work 80 hours per month,
the capacity’s `Time Period` would be Month and `Hours per Time`
`Period` would be `80.`


Service resources who are capacity-based can only work a certain number of hours or complete a certain number of service appointments
within a specified time period. Contractors tend to be capacity-based. To indicate that a service resource is capacity-based, select
**Capacity-Based on the service resource record, then create a capacity record for the service resource.**

You must fill out at least one of these fields: `CapacityInWorkItems` and `CapacityInHours. If you’re using the Field Service`
managed package and would like to measure capacity both in hours and in number of work items, enter a value for both. The resource
is considered to reach their capacity based on whichever term is met first—hours or number of work items.

Important: If you aren’t using the Field Service managed package, capacity serves more as a suggestion than a rule. Resources
can still be as scheduled beyond their capacity, and you aren’t notified when a resource exceeds their capacity.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceResourceCapacityChangeEvent (API version 54.0)**
Change events are available for the object.

**ServiceResourceCapacityFeed**

Feed tracking is available for the object.

**ServiceResourceCapacityHistory**

History is available for tracked fields of the object.


-----
