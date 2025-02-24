#### LocationGroupAssignment

Represents the assignment of a location to a location group. This object is available in API version 51.0 and later.

You can assign a location to multiple location groups, which associates it with one location group assignment for each location group
that it’s assigned to. Each location group assignment represents the relationship between one location and one location group, so a
location or location group can be associated with multiple location group assignments.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Omnichannel Inventory orgs.

##### Fields

```
LastReferencedDate
LastViewedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LocationExternalReference
LocationGroupAssignment
LocationGroupExternalReference
LocationGroupId
LocationGroupName
LocationId

```

**Description**
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external reference of the associated location.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the location group assignment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external reference of the associated location group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The associated location group.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location group name of the associated location group.

**Type**
reference


-----

```
LocationName

##### Associated Objects

```

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The associated location.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated location.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LocationGroupAssignmentChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

Location

LocationGroup
