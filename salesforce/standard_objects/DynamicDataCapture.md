#### DynamicDataCapture

DynamicDataCapture is a junction object that adds a Form tab to Work Order Overview, and to the related list of a work order, work
order line item, or service appointment in the Field Service mobile app. This object is available in API version 62.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActionDefinition
ActionType
Description
ExecutionOrder
IsRequired

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The associated Data Capture Flow to execute.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of platform action that the form is associated with. Possible values are:

Possible values are:

**•** `Flow`

The default value is `Flow.`

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the form.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the Data Capture flow is executed. Positive integer values or null are
supported.

**Type**
boolean


-----

```
LastReferencedDate
Name
ParentRecordId
ParentRecordType

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Boolean value that specifies if this form needs to be completed before moving on to the
next form.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The order in which the Data Capture flow is executed. Positive integer values or null are
supported.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the form.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID that refers to a work order, work order line item, or service appointment that serves
as the parent record for junction object.

This field is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Parent-child

**Refers To**
ServiceAppointment, WorkOrder, WorkOrderLineItem (the parent object)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
PausedFlowInterviewId
ProcessType
StatusCategory

```

**Description**
The type of parent object associated with the junction object.

Possible values are:

**•** `Work Order`

**•** `Work Order Line Item`

**•** `Service Appointment`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the flow interview that has been paused by a user.

This field is a relationship field.

**Relationship Name**
PausedFlowInterview

**Refers To**
FlowInterview

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow process type for the form.

Possible values are:

**•** `DataCaptureFlow—Data Capture Flow`

The default value is `DataCaptureFlow.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The category that each status value belongs to.

Possible values are:

**•** `Completed`

**•** `InProgress—In Progress`

**•** `New`


-----

**•** `NotApplicable—Not Applicable`

**•** `Paused`

The default value is `New.`
