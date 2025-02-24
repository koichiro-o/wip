#### AppointmentTopicTimeSlot

Represents a lookup to a work type or a work type group for a time slot This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AppointmentTopicTimeSlotKey

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
Name
OperatingHoursId
TimeSlotId
WorkTypeGroupId

```

**Description**
Non-editable validating field used to ensure no two rows have the same time slot and work
type or work type group values in an instance.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name or ID of the AppointmentTopicTimeSlot object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operating hours that contain the time slot.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the time slot.

This is a relationship field.

**Relationship Name**
TimeSlot

**Relationship Type**
Lookup

**Refers To**
TimeSlot

**Type**
reference


-----

```
WorkTypeId

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type group associated with this time slot.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with this time slot.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AppointmentTopicTimeSlotChangeEvent on page 67**
Change events are available for the object.

**AppointmentTopicTimeSlotFeed on page 54**
Feed tracking is available for the object.

**AppointmentTopicTimeSlotHistory on page 62**
History is available for tracked fields of the object.

**AppointmentTopicTimeSlotOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AppointmentTopicTimeSlotShare on page 66**
Sharing is available for the object.


-----
