#### VoiceCallListItem

Represents a single phone number in a prioritized call list.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
CallListId
Ordinal
RelatedRecordId
State

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related call list.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order of the item in the overall call list.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the related record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Whether the call list item is not called, called, or skipped.


-----
