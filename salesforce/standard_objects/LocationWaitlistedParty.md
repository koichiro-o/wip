#### LocationWaitlistedParty

Represents a specific party of people waiting in a queue. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
Description
EntryDateTime
EstimatedWaitHours

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this queue.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time a party is added to the queue.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
EstimatedWaitMinutes
LastReferencedDate
LastViewedDate
Name
OwnerId
PartySize

```

**Description**
The estimated hours of wait time for a party.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated minutes of wait time for a party.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the group.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int


-----

```
PartyStatus
SignUpDateTime
WaitlistId
