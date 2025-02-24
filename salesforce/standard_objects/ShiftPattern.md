#### ShiftPattern

Represents a pattern of templates for creating shifts. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled. Users must have Field Service permission.

##### Fields

```
Description
IsActive

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A short description of the shift pattern to help users identify the pattern.

**Type**
boolean


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the shift pattern can be used to create shifts.

The default value is ‘false’.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A short, descriptive name of the shift pattern.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the shift pattern. Default is the user who creates the shift pattern.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
PatternLength

##### Associated Objects

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration in days of the shift pattern.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftPatternChangeEvent (API version 54.0)**
Change events are available for the object.

**ShiftPatternFeed on page 54**
Feed tracking is available for the object.

**ShiftPatternHistory on page 62**
History is available for tracked fields of the object.

**ShiftPatternShare on page 66**
Sharing is available for the object.

SEE ALSO:

ShiftPatternEntry

[Shift Patterns](https://help.salesforce.com/articleView?id=fs_shift_patterns.htm&language=en_US)
