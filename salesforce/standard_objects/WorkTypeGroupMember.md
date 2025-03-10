#### WorkTypeGroupMember

Represents the relationship between a work type and the work type group it belongs to. This object is available in API version 45.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
LastReferencedDate

```

**Type**
dateTime


-----

```
LastViewedDate
Name
WorkTypeGroupId
WorkTypeId

```

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
Autogenerated number identifying the work type group membership. It uses the format
########.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type group that this record belongs to.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work type that this record corresponds to.

This is a relationship field.


-----

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkTypeGroupMemberFeed**

Feed tracking is available for the object.

**WorkTypeGroupMemberHistory**

History is available for tracked fields of the object.


-----
