#### WorkOrderStatus

Represents a possible status of a work order in field service.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
ApiName
IsDefault
MasterLabel

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on work orders. Only one status
value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
SortOrder
StatusCode

##### Usage

```

**Description**
The label for the picklist value that appears in the UI.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the drop-down list of values in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has
seven values which are identical to the default Status values.


The Status field on work orders comes with the following values:

**•** New—Work order was created, but there hasn’t yet been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The WorkOrderStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled By
Customer—creates a work order status record, and vice versa.

Note: Work orders also come with a StatusCategory field whose values are identical to the default Status values. If you create
custom Status values, you must indicate which category it belongs to. For example, if you create a `Customer Absent` value,
you may decide that it belongs in the `Cannot Complete category. To learn which processes reference StatusCategory, see`
[How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
