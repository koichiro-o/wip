#### WorkTypeGroup

Represents a grouping of work types used to categorize types of appointments available in Lightning Scheduler, or to define scheduling
limits in Field Service. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdditionalInformation
Description

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Additional information about the types of appointments this work type group represents.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of this work type group.


-----

```
GroupType
IsActive
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The category of this work type group. Possible values are:

**•** `Capacity—A group of work types used to define a work capacity limit in Field Service.`

**•** `Default—A non-capacity group of work types used in Lightning Scheduler.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this work type group can be used for appointment scheduling or work
capacity limits. A work type can belong to only one active work type group of type Capacity.

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this work type group.

**Type**
reference


-----

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created this record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkTypeGroupFeed**

Feed tracking is available for the object.

**WorkTypeGroupHistory**

History is available for tracked fields of the object.

**WorkTypeGroupOwnerSharingRule**

Sharing rules are available for the object.

**WorkTypeGroupShare**

Sharing is available for the object.
