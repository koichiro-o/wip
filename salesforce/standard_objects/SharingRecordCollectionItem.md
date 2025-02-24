#### SharingRecordCollectionItem

Represents a single record in a collection of records. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```
Record collections are limited to 100 items for each record collection.


-----

##### Fields

**Field**
```
CollectionId
Description
ItemId
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the record collection item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record collection item.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the record collection item.

