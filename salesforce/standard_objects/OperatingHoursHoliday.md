#### OperatingHoursHoliday

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the operating hours record being tracked. The history is displayed on the
detail page for this record.


Represents the day or hours for which a service territory and service resources exclusive to the service territory are unavailable in Salesforce
Scheduler. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
Salesforce Scheduler must be enabled.


-----

##### Fields

**Field**
```
DateAndTime
HolidayId
LastReferencedDate
LastViewedDate
OperatingHoursHolidayNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read-Only) The date or time for the holiday.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the holiday that’s related to the operating hours indicated in the OperatingHoursId
field.

This is a relationship field.

**Relationship Name**
Holiday

**Relationship Type**
Lookup

**Refers To**
Holiday

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this object.

**Type**
string


-----

```
OperatingHoursId
