#### WorkCapacityAvailability

Represents the available work capacity for a specific time and service territory. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AvailCapacityHours
AvailCapacityMinutes
EndDate
LastReferencedDate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of available capacity in hours in the time frame the user defined for a service
territory.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of available capacity in minutes in the time frame the user defined for a service
territory.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the total available capacity.

**Type**
dateTime


-----

```
LastViewedDate
OwnerId
ServiceTerritoryId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this object.

This field is a polymorphic relationship field.

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
The ID of the service territory of the work capacity availability calculation.

This field is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory


-----

```
StartDate
TimePeriod

##### Associated Objects

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the total available capacity.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period the user selected when creating the work capacity limit. The value is copied
from the TimePeriod field of the WorkCapacityLimit object.

Possible values are:

**•** `Day`

The default value is `Day.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkCapacityAvailabilityFeed on page 54**
Feed tracking is available for the object.

**WorkCapacityAvailabilityShare on page 66**
Sharing is available for the object.
