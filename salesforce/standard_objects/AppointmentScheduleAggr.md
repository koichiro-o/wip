#### AppointmentScheduleAggr

Records the utilization of a service resource, by date, for the Load Balancing appointment assignment policy. This object is available in
API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
AppointmentDate
Name
ResourceUtilizationCount
ServiceResourceId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date of the appointment.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name or ID of the AppointmentScheduleAggr object.

**Type**
integer

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of appointments scheduled for a service resource. Available in API version 53.0
and later.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service resource associated with the appointment scheduling aggregate.


-----

```
TotalResourceUtilization
UsageType

##### Associated Objects

```

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of minutes for which the service resource has scheduled appointments.

This is a calculated field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specify the usage type of the AppointmentScheduleAggr object.

Possible values are:

**•** `FSL_Daily`

**•** `FSL_Monthly`

**•** `FSL_Weekly`

**•** `LightningScheduler`

The default value is 'LightningScheduler'.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentScheduleAggrOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AppointmentScheduleAggrShare on page 66**
Sharing is available for the object.


-----
