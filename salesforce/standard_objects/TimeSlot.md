#### TimeSlot

Represents a period of time on a specified day of the week during which work can be performed in Field Service, Salesforce Scheduler,
or Workforce Engagement. Operating hours consist of one or more time slots. This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
DayOfWeek
EndTime
LastReferencedDate
LastViewedDate
MaxAppointments

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The day of the week when the time slot takes place.

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time when the time slot ends.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced (LastReferencedDate)
and not viewed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum number of appointments for a single time slot. Available in API version
47.0 and later.


-----

```
OperatingHoursId
StartTime
RecordSetFilterCriteriaId
TimeSlotNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The operating hours that the time slot belongs to. An operating hours’ time slots
appear in the Operating Hours related list.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time when the time slot starts.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria selected for the time slot.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
Type
WorkTypeGroupId

##### Usage

```

**Description**
The name of the time slot. The name is auto-populated to a day and time
format—for example, `Monday 9:00 AM - 10:00 PM—but you can`
manually update it if you wish.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of time slot. Possible values are `Normal` and `Extended. You may`
choose to use `Extended to represent overtime shifts.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Work type group assigned to the time slot. Available in API version 47.0 and later.

This is a relationship field.

**Relationship Name**
WorkTypeGroup

**Relationship Type**
Lookup

**Refers To**
WorkTypeGroup


Operating hours are composed of time slots, which indicate the hours of operation for a particular day. After you create operating hours,
create time slots for each day. For example, if the operating hours should be 8 AM to 5 PM Monday through Friday, create five time slots,
one per day. To reflect breaks such as lunch hours, create multiple time slots in a day: for example, `Monday 8:00 AM – 12:00`
`PM` and `Monday 1:00 PM – 5:00 PM.`

Tip: Time slots don’t come with any built-in rules, but you can create Apex triggers that limit time slot settings in your org. For
example, you may want to restrict the start and end times on time slots to half-hour increments, or to prohibit end times later
than 8 PM.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**[TimeSlotChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[TimeSlotHistory (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_associated_objects_history.htm;)**
History is available for tracked fields of the object.
