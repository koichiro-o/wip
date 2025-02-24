#### AppointmentScheduleLog

Stores service appointments of each service Resource. This object is used to calculate the utilization of a service resource for the
AppointmentScheduleAggr object. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
AppointmentDate
AppointmentScheduleAggrId
IsUsedForResourceUtilization

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date of the appointment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The appointment scheduling aggregate associated with the appointment scheduling log.

This is a relationship field.

**Relationship Name**
AppointmentScheduleAggr

**Relationship Type**
Lookup

**Refers To**
AppointmentScheduleAggr

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the appointment scheduling log is used for deriving the appointment
scheduling aggregate.

The default value is 'false'.


-----

```
Name
RelatedRecordId
ResourceUtilization
ServiceResourceId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name or ID of the AppointmentScheduleLog object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service appointment, resource absence, event, or any other related record associated
with the appointment scheduling log.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Event, ServiceAppointment

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes the service resource already has scheduled appointments for.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service resource associated with the appointment scheduling log.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup


-----

```
UsageType

##### Associated Objects

```

**Refers To**
ServiceResource

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specify the product associated with the AppointmentScheduleLog object.

Possible values are:

**•** `FSL_Daily—FSL - Daily`

**•** `FSL_Monthly—FSL - Monthly`

**•** `FSL_Weekly—FSL - Weekly`

**•** `LightningScheduler—Lightning Scheduler`

The default value is 'LightningScheduler'.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentScheduleLogChangeEvent on page 67**
Change events are available for the object.

**AppointmentScheduleLogFeed on page 54**
Feed tracking is available for the object.

**AppointmentScheduleLogHistory on page 62**
History is available for tracked fields of the object.

**AppointmentScheduleLogOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AppointmentScheduleLogShare on page 66**
Sharing is available for the object.
