#### AssignedResource

Represents a service resource who is assigned to a service appointment in Field Service and Lightning Scheduler. Assigned resources
appear in the Assigned Resources related list on service appointments. This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
ActualTravelTime

```

**Type**
double


-----

```
ApptAssistantInfoUrl
AssignedResourceNumber
EstimatedTravelTime
LocationStatus

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes that the service resource needs to travel to the assigned
service appointment. You can enter a value with up to two decimal places.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The URL that contains the status of the mobile worker approaching the service
appointment, the Community URL, and the expiry of the URL. Available in version
51.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the resource assignment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated number of minutes needed for the service resource to travel to
the service appointment they’re assigned to. You can enter a value with up to
two decimal places.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the mobile worker approaching the service appointment. When
the location status changes to one of these values, a status update containing
`ApptAssistantInfoUrl` is sent to the customer. Available in version 51.0
and later.

Possible values are:

**•** `EnRoute`


-----

```
IsPrimaryResource
ServiceAppointmentId
ServiceCrewId

```


**•** `LastMile`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the service resource is a primary resource or not. The default
value is false. Available in API version 47.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service appointment that the resource is assigned to.

This is a relationship field.

**Relationship Name**
ServiceAppointment

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
reference

**Properties**
Create, Update, Filter, Group, Sort, Nillable

**Description**
The service crew that the resource is assigned to.

Note: Since service resources can represent crews or individuals,
appointments are typically assigned to crews in the following way:

**1. Create a service resource of the Crew type that represent the crew.**

**2. Create an assigned resource on the service appointment and select**
the crew resource in the ServiceResourceId field.

As an alternative, you can assign appointments to crew members
separately. This lets you track each member’s travel time and see a list of
the crew members in the Assigned Resources related list. To take this
approach, create an assigned resource for each crew member. List the
crew member in the ServiceResourceId field and the crew they
belong to in the ServiceCrewId field.


-----

```
ServiceResourceId

##### Usage

```

**Type**
reference

**Properties**
Create, Update, Filter, Group, Sort

**Description**
The resource who is assigned to the service appointment.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource


You can assign multiple service resources to a service appointment. Service resources who are assigned to service appointments cannot
be deactivated until they are removed from the appointments.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AssignedResourceChangeEvent (API version 48.0)**
Change events are available for the object.

**AssignedResourceHistory on page 62(API version 61.0)**
History is available for tracked fields of the object.

**AssignedResourceFeed**

Feed tracking is available for the object.
