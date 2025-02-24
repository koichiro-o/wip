#### LocationWaitlist

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the queue.

Possible values are:

**•** `approaching—In Progress`

**•** `confirmation—Confirmed`

**•** `inactive—Inactive`

**•** `ready—Ready`

**•** `removed—Removed`


Represents a queue created for a specific location. Multiple queues can be created for a single location. For example, you can have a
queue for each sales agent or a standard queue and a queue for vulnerable groups. The specific party of people in a queue is represented
by LocationWaitlistedParty. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
BusinessHoursId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ClosedDateTime
CumulativeGuestCount
CumulativeGuestGroupCount
CurrentGuestCount
Description
GuestCapacity

```

**Description**
A reference to the BusinessHours record that contains the hours the business is open.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time a queue is closed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of guests allowed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of groups allowed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current number of guests.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
MaxPartySize
MessagingChannelId
Name
OpenDateTime

```

**Description**
The total capacity of guests.

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
The date on which the record was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum size of a group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The messaging channel ID.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

**Type**
dateTime


-----

```
OwnerId
PartyReminderDelayMinutes
PlaceId
ResourceCapacity
ResourceOccupancyCount
Status

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time a queue is open.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of minutes between when a party is notified and when they receive a reminder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location ID for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The capacity for this resource.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The occupancy count for this resource.

**Type**
picklist


-----

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the queue.

Possible values are:

**•** `closed`

**•** `open`

**•** `paused`
