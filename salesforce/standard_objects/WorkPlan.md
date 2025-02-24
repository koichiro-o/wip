#### WorkPlan

Represents a work plan for a work order or work order line item. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
Description
ExecutionOrder

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work plan.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the work plan is executed. Only positive values or null are supported.


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
ParentRecordId

```

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

**Description**
The name of the work plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the work plan.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
ParentRecordType
WorkOrderId
WorkOrderLineItemId

```

**Description**
The ID of the work order, work order line item, or change request that the work plan is
associated with. Available in API version 54.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
ChangeRequest, WorkOrder, WorkOrderLineItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes whether the parent record is a work order, work order line item, or change request.
Available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the work order.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work order line item.

**Relationship Name**
WorkOrderLineItem


-----

```
WorkPlanTemplateId

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the work plan template record. Available in API version 54.0 and later.

This field is a relationship field.

**Relationship Name**
WorkPlanTemplate

**Relationship Type**
Lookup

**Refers To**
WorkPlanTemplate


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanChangeEvent on page 67**
Change events are available for the object. Available in API version 54.0 and later.

**WorkPlanFeed on page 54**
Feed tracking is available for the object.

**WorkPlanHistory on page 62**
History is available for tracked fields of the object.

**WorkPlanOwnerSharingRule on page 64**
Sharing rules are available for the object.

**WorkPlanShare on page 66**
Sharing is available for the object.
