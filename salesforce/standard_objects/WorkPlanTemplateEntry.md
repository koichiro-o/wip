#### WorkPlanTemplateEntry

Represents an object that associates a work step template with a work plan template. This object is available in API version 52.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

Field Service must be enabled.

##### Fields

**Field**
```
ExecutionOrder
LastReferencedDate
LastViewedDate
WorkPlanTemplateEntryNumber
WorkPlanTemplateId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequence number of when this entry is executed. Only positive values are supported.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number of the work plan template entry, for example, WPTE-0001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
WorkStepTemplateId

##### Associated Objects

```

**Description**
Required. The ID of the work plan template.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the work step template.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanTemplateEntryChangeEvent**

Change events are available for the object.

**WorkPlanTemplateEntryFeed**

Feed tracking is available for the object.

**WorkPlanTemplateEntryHistory**

History is available for tracked fields of the object.
