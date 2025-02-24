#### SharingRecordCollection

Represents a collection of records. This object is available in API version 51.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

```
Record collections are limited to 100 items and 100 members for each record collection.

##### Fields

```
Description
GroupId
LastAdded
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the record collection.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The group ID of the record collection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when an item was last added to the record collection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
NumberOfRecords
OwnerId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the record collection.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of records in the record collection. The limit is 100.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record collection owner.

