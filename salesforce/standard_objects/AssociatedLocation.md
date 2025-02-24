#### AssociatedLocation

Represents a link between an account and a location in Field Service. You can associate multiple accounts with one location. For example,
a shopping center location may have multiple customer accounts.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
ActiveFrom
ActiveTo
AssociatedLocationNumber
LastReferencedDate
LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the associated location is active.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the associated location stops being active.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number identifying the associated location.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date the associated location was last modified.

**Type**
dateTime


-----

```
LocationId
ParentRecordId
Type

```

**Properties**
Filter, Nillable, Sort

**Description**
The date the associated location was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location associated with the address.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account associated with the location.

This is a relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Picklist of address types. The values are:

**•** Bill To


-----

**•** Ship To

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AssociatedLocationChangeEvent (API version 62.0)**
Change events are available for the object.

**AssociatedLocationHistory**

History is available for tracked fields of the object.
