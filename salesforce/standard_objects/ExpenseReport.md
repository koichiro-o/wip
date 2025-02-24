#### ExpenseReport

Represents a report that summarizes expenses. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CurrencyIsoCode
Description
ExpenseReportNumber
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description for the expense report.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the expense report.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


-----

```
LastViewedDate
OwnerId
Title
TotalExpenseAmount

##### Associated Objects

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the expense report record.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A title that identifies the expense report.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all expense entries in the report.

This is a calculated field.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseReportFeed**

Feed tracking is available for the object.

**ExpenseReportHistory**

History is available for tracked fields of the object.

**ExpenseReportShare**

Sharing is available for the object.


-----
