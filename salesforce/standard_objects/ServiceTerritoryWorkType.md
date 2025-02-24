#### ServiceTerritoryWorkType

Represents the relationship between a ServiceTerritory object and a WorkType object for Salesforce Scheduler appointments. This object
is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
IsSlotPublished

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicate whether records in the Shift object are created for the selected Service Territory and
Work Type.

The default value is `false.`


-----

```
LastReferencedDate
LastViewedDate
Name
ServiceTerritoryId
TeamId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this object.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of this service territory-work type relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service territory that’s related to the work type indicated in the WorkTypeId
field.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
WorkTypeId

##### Associated Objects

```

**Description**
Represents the team associated with the service territory for a specific work type.

This field is a relationship field and is available in API version 58.0 and later.

**Relationship Name**
Team

**Relationship Type**
Lookup

**Refers To**
Team

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type that’s related to the service territory indicated in the
`ServiceTerritoryId` field.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceTerritoryWorkTypeFeed**

Feed tracking is available for the object.

**ServiceTerritoryWorkTypeHistory**

History is available for tracked fields of the object.
