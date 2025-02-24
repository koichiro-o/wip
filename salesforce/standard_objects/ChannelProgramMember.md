#### ChannelProgramMember

Represents a partner who is a member of a channel program. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
LastReferencedDate
LastViewedDate
LevelId
Name
OwnerId
PartnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date referenced. This field is available in API version 45.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed. This field is available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the channel program level.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the channel program member.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
ProgramId

##### Associated Objects

```

**Description**
ID of the partner.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramMemberFeed (API version 46.0)**
Feed tracking is available for the object.

**ChannelProgramMemberHistory (API version 46.0)**
History is available for tracked fields of the object.

**ChannelProgramMemberOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramMemberShare (API version 43.0)**
Sharing is available for the object.
