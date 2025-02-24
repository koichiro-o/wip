#### ChannelProgram

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique label name for this rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of object to link to the channel interaction.

Possible values are:

**•** `Contact`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the rule as it appears in the UI. Maximum length is 80 characters.


Represents a channel program that vendors use to market and sell their products through channel partners. This object is available in
API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Fields

```
```
Category

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Description
IsActive
LastReferencedDate
LastViewedDate
Name

```

**Description**
Category of the channel program. Categories group channel programs by type.
For example, a reseller category would include all the different regional reseller
channel programs.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the channel program is active. New channel programs are
inactive by default.

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
Create, Filter, Group, Sort, Update


-----

```
OwnerId

##### Associated Objects

```

**Description**
Name of the channel program.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the channel program.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramFeed**

Feed tracking is available for the object.

**ChannelProgramHistory**

History is available for tracked fields of the object.

**ChannelProgramOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramShare**

Sharing is available for the object.
