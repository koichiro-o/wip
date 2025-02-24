#### ServiceTerritoryLocation

Represents a location associated with a particular service territory in field service.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
LocationId
ServiceTerritoryId
ServiceTerritoryLocationNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location that is associated with the service territory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated service territory.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read only) Auto-generated number identifying the service territory location.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceTerritoryLocationChangeEvent (API version 55.0)**
Change events are available for the object.

**ServiceTerritoryLocationFeed**

Feed tracking is available for the object.

**ServiceTerritoryLocationHistory**

History is available for tracked fields of the object.
