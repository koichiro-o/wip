#### UnitOfMeasure

```


**•** `Organizer`

**•** `To`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the person participating in the voice call.

This field is a polymorphic relationship field.

**Relationship Name**
Person

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
double

**Properties**
Filter, Nillable

**Description**
Ratio of time the participant was talking versus listening in the voice call.


Defines the units and systems of units used to express and account for quantities. This object is available in API version 61.0 and later.

Examples of units of measure include Litre (for volume), Kilogram (for weight), and single units (such as Can, sachet, and packet).

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ConversionFactor

```

**Type**
double


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The factor or rate that's used to convert this unit of measurement to the base unit. For
example, if the base unit is

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

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the unit of measure.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user or group that owns the job.,

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


-----

```
Sequence
Status
UnitCode
