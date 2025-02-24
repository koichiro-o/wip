#### ContentDocumentListViewMapping

Represents an association between a ListView and a Quip ContentDocument. Applies to Quip file types only. Maintains the mapping
between a list view and Quip document when the list view is exported to a newly created Quip document. This object is available in API
version 44.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To use this object, the Files Connect and Quip permissions must be enabled in the org.

To insert and update this object through the API, the QuipMassAction gater permission must also be enabled.


-----

##### Fields

**Field**
```
ContentDocumentId
LastReferencedDate
LastViewedDate
ListViewId
Name

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this document.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the list view associated with the document.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the document.


ContentDocumentListViewMapping is used primarily by the Quip list view integration feature. Only Quip file types (Quip sheets and
docs) are supported. The ContentDocumentId field must point to a Quip file.


-----
