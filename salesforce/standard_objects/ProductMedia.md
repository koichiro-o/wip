#### ProductMedia

Represents the rich media, including images and attachments, that can be added to products.This object is available in API version 49.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access product media.


-----

##### Fields

**Field**
```
CurrencyIsoCode
ElectronicMediaGroupId
ElectronicMediaId
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD. Possible values are:`

**•** `USD—U.S. Dollar`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique ID of the media group.

This field is a relationship field.

**Relationship Name**
ElectronicMediaGroup

**Relationship Type**
Lookup

**Refers To**
ElectronicMediaGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique ID of the media record.

This field is a polymorphic relationship field.

**Relationship Name**
ElectronicMedia

**Relationship Type**
Lookup

**Refers To**
ManagedContent, ManagedContentInfo

**Type**
dateTime


-----

```
LastViewedDate
Name
ProductId
SortOrder

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the media.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product that the media is associated with.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The order that product media is displayed in.


-----

##### Associated Objects

**ProductMediaChangeEvent (API version 57.0)**
Change events are available for the object.

**ProductMediaHistory on page 62**
History is available for tracked fields of the object.

**ProductMediaOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ProductMediaShare on page 66**
Sharing is available for the object.
