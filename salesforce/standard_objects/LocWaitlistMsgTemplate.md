#### LocWaitlistMsgTemplate

Represents a junction object connecting LocationWaitlist to MessagingTemplate. This object is available in API version 50.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
LastReferencedDate
LastViewedDate
LocationWaitlistId
MessagingTemplateId
Name

```

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
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the LocationWaitlist record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to the MessagingTemplate record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this record.


-----

```
OwnerId
Type
