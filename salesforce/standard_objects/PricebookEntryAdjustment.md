#### PricebookEntryAdjustment

Read-only junction object created when you associate a price adjustment schedule with a price book entry. This object is available in
API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the B2B Commerce license is enabled.

##### Fields

```
Name
PriceAdjustmentScheduleId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book entry adjustment.


-----

```
PricebookEntryId

```
SEE ALSO:

PriceAdjustmentSchedule
