#### Shift

```

**Type**
picklist

**Properties**
Read, Edit

**Description**
The access level on the related record collection.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user or group with access to the record collection.


Represents a shift for service resource scheduling. Available in API versions 46.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), upsert()

 Special Access Rules

```
Field Service, Service Engagement, or Workforce Engagement must be enabled. For Field Service, users must have Field Service permissions.
For Service Engagement, users must have the Service Engagement Planner permission set. For Workforce Engagement, users must have
the Workforce Engagement Admin or Planner permission set.


-----

##### Fields

**Field**
```
BackgroundColor
EndTime
IsHolidayShift
IsNonStandard
JobProfileId
Label

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates a shift that overlaps with holiday hours. The default value is false. Available in API
version 55.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is nonstandard, such as overtime or on-call shifts.

The default value is false. Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The job profile associated with the shift. Available in API versions 47.0 and later.

**Type**
string


-----

```
LastReferencedDate
LastViewedDate
OwnerId
RecordsetFilterCriteriaId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The label that a shift is given.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed a related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shift.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria selected for the shift. Available in API version 49.0 and
later.

This is a relationship field.


-----

```
ServiceResourceId
ServiceTerritoryId
ShiftNumber

```

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service resource the shift belongs to. Available in API versions 47.0 and later.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory the shift belongs to. Available in API versions 47.0 and later.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number automatically given to the shift upon creation.


-----

```
ShiftTemplateId
StartTime
Status
StatusCategory

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The shift template ID, if the shift was created from a shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift starts.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the status of the shift. Users can create custom values. Default values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the status of the shift using static values. This field is derived from Status using
the mapping defined in setup.

Possible values are:


-----

```
TimeSlotType

##### Usage

```


**•** `Tentative`

**•** `Published`

**•** `Confirmed`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of time slot for the shift. The same setup values as the `TimeSlot` field in the
OperatingHours object.

Possible values are:

**•** `Normal (default value)`

**•** `Extended`


Scheduling and dispatching service resources using shift data is not supported in API version 46.0, and is a pilot feature in API version
47.0.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ShiftChangeEvent (API version 54.0)**
Change events are available for the object.

**ShiftFeed**

Feed tracking is available for the object.

**ShiftHistory**

History is available for tracked fields of the object.

**ShiftOwnerSharingRule**

Sharing rules are available for the object.

**ShiftShare**

Sharing is available for the object.
