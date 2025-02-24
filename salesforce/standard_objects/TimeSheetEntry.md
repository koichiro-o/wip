#### TimeSheetEntry

Represents a span of time that a service resource spends on a field service task. This object is available in API version 47.0 and later.

Time sheets are composed of time sheet entries. Time sheet entries typically track individual tasks like travel or asset repair.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
CurrencyIsoCode
Description
DurationInMinutes

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
```
  Currency ISO Code.

```
Time sheet entries inherit their time sheet’s currency code. Updates to a time
sheet’s currency code aren’t reflected in existing time sheet entries’ currency
code.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes on how the time was spent. For example, “This service took longer than
normal because the machine was jammed.”

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Minutes recorded on the time sheet entry.


-----

```
EndTime
LastReferencedDate
LastViewedDate
LocationTimeZone
StartTime
Status

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the activity finished.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the location where the activity occurred.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the activity began.

**Type**
picklist


-----

```
Subject
TimeSheetEntryNumber
TimeSheetId
Type

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the time sheet entry. The picklist includes the following values,
which can be customized:

**•** New

**•** Submitted

**•** Approved

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Activity performed; for example, repair, lunch, or travel.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the time sheet entry.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The time sheet associated with the time sheet entry.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of work performed. The picklist includes the following values, which
can be customized:

**•** Direct

**•** Indirect


-----

```
WorkOrderId
WorkOrderLineItemId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order related to the time sheet entry. Work orders are searchable by
their content.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order line item related to the time sheet entry. Work order line items
are searchable by their content.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TimeSheetEntryChangeEvent (API version 48.0)**
Change events are available for the object.

**TimeSheetEntryFeed**

Feed tracking is available for the object.

**TimeSheetEntryHistory**

History is available for tracked fields of the object.
