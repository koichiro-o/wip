#### ChannelProgramLevel

Represents a level, based on member experience, in a channel program. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
ProgramId

```

**Description**
Description of the channel program level.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the channel program level.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.


-----

```
Rank
RecordTypeId

##### Associated Objects

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An integer associated with the level. For example, 1 represents the lowest level,
2 the next level up, etc.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramLevelFeed**

Feed tracking is available for the object.

**ChannelProgramLevelHistory**

History is available for tracked fields of the object.

**ChannelProgramLevelOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramLevelShare (API version 43.0)**
Sharing is available for the object.
