#### TimeSheet

Represents a schedule of a service resource’s time in Field Service or Workforce Engagement. This object is available in API v47.0 and
later.

Time sheets are composed of time sheet entries, which typically track individual tasks like travel or asset repair.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service or Workforce Engagement must be enabled.

##### Fields

```
CurrencyIsoCode
EndDate
LastReferencedDate
LastViewedDate

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
**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The last day the time sheet covers.

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


-----

```
OwnerId
ServiceResourceId
StartDate
Status
TimeSheetEntryCount

```

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the time sheet.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource whose time is being tracked with the time sheet.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The first day the time sheet covers.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the time sheet. The picklist includes the following values, which
can be customized:

**•** New

**•** Submitted

**•** Approved

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
TimeSheetNumber
TotalDurationInHours
TotalDurationInMinutes

##### Associated Objects

```

**Description**
(Read Only) The number of related time sheet entries.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the time sheet.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the sum total of the duration field of all the time sheet entries related
to the time sheet object in hours.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the sum total of the duration field of all the time sheet entries related
to the time sheet object in minutes.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TimeSheetChangeEvent (API version 48.0)**
Change events are available for the object.

**TimeSheetFeed**

Feed tracking is available for the object.

**TimeSheetHistory**

History is available for tracked fields of the object.

**TimeSheetOwnerSharingRule**

Sharing rules are available for the object.

**TimeSheetShare**

Sharing is available for the object.


-----
