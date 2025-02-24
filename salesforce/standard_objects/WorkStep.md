#### WorkStep

Represents a work step in a work plan. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
ActionDefinition
ActionType
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The platform action that the work step executes. The possible values are the names of the
flow and quick actions configured in your org. To launch Lightning Web Components from
Work Steps, you must use `QuickAction` on the action definition.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of platform action that the work step is associated with.

Possible values are:

**•** `Flow`

**•** `QuickAction`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the work step.


-----

```
EndTime
ExecutionOrder
LastReferencedDate
LastViewedDate
Name
PausedFlowInterviewId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the work step ends. The value must be greater than or equal to
```
  StartTime.

```
**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the work step is executed. Only positive integer values or null are
supported.

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
Required. The user-defined name of the work step.

**Type**
reference


-----

```
StartTime
Status
StatusCategory

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated ID of the flow interview paused by a user.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time the work step starts.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The customizable status of the work order. Every status must be mapped to a status category,
but there can be status categories not mapped to a status.

Possible values are:

**•** `Completed`

**•** `In Progress`

**•** `New`

**•** `Not Applicable`

**•** `Paused`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each status value belongs to. Each default status category is mapped to
the corresponding default status. If you create a custom status, you must indicate which
[status category it belongs to. To learn which processes reference StatusCategory, see How](https://help.salesforce.com/articleView?id=sf.fs_status_categories.htm&language=en_US)
[are Status Categories Used?.](https://help.salesforce.com/articleView?id=sf.fs_status_categories.htm&language=en_US)

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `NotApplicable`


-----

```
WorkOrderId
WorkOrderLineItemId
WorkPlanExecutionOrder
WorkPlanId

##### Associated Objects

```


**•** `Paused`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the work order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the work order line item.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the plan execution order.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the work plan.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkStepChangeEvent**

Change events are available for the object.

**WorkStepFeed**

Feed tracking is available for the object.

**WorkStepHistory**

History is available for tracked fields of the object.


-----
