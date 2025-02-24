#### ExpenseReportEntry

Represents an entry in an expense report. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Amount
CurrencyIsoCode
ExpenseId
ExpenseReportEntryNumber

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the expense.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The expense that corresponds to the expense report entry.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the expense report entry.


-----

```
ExpenseReportId
ExpenseType
LastReferencedDate
LastViewedDate
Title
TransactionDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The expense report that’s associated with the expense report entry.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The type of expense. Possible values are:

**•** `Billable`

**•** `Non-Billable`

The default value is `Billable.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A title that identifies the expense.

**Type**
date


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
The day that the expense was incurred, or the payment date for the expense.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseReportEntryFeed**

Feed tracking is available for the object.

**ExpenseReportEntryHistory**

History is available for tracked fields of the object.
