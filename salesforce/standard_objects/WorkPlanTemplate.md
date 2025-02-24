#### WorkPlanTemplate

Represents a template for a work plan. This object is available in API version 52.0 and later.

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
Description
IsActive
LastReferencedDate
LastViewedDate
Name

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work plan template.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether the specific template is available for application (true) or not (false).
Default is `false. Label is Active.`

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
Create, Filter, Group, idLookup, Sort, Update


-----

```
OwnerId
RelativeExecutionOrder

##### Associated Objects

```

**Description**
The user-defined name of the work plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner who created the work plan template.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The relative execution order for sorting the work plan when it’s applied to the work order or
work order line item. Only positive integers are supported.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanTemplateChangeEvent**

Change events are available for the object.

**WorkPlanTemplateFeed**

Feed tracking is available for the object.

**WorkPlanTemplateHistory**

History is available for tracked fields of the object.

**WorkPlanTemplateOwnerSharingRule**

Sharing rules are available for the object.

**WorkPlanTemplateShare**

Sharing is available for the object.
