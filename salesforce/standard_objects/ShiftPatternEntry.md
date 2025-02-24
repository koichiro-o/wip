#### ShiftPatternEntry

ShiftPatternEntry links a shift template to a shift pattern. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled. Users must have Field Service permission.


-----

##### Fields

**Field**
```
DayOrder
LastReferencedDate
LastViewedDate
Name
ShiftPatternId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
`DayOrder` links the shift template to the specific day within the shift pattern duration that
the template. For example, if the DayOrder is 2 then a shift from the associated template is
created on the second day of the pattern.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern entry was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern entry was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated reference number for the shift pattern entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the shift pattern that the shift pattern entry is linked to.

This is a relationship field.

**Relationship Name**
ShiftPattern


-----

```
ShiftTemplateId

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
ShiftPattern

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the shift template that’s used to create shifts for this shift pattern entry.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShiftPatternEntryChangeEvent (API version 54.0)**
Change events are available for the object.

SEE ALSO:

ShiftPattern
