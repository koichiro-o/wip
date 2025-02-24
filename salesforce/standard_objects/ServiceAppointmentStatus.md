#### ServiceAppointmentStatus

Represents a possible status of a service appointment in field service.

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

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean


-----

```
MasterLabel
SortOrder
StatusCode

##### Usage

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on service appointments. Only
one status value can be the default.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

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


The Status field on service appointments comes with the following values:

**•** None—Default value.

**•** Scheduled—Appointment has been assigned to a service resource.

**•** Dispatched—Assigned service resource has been notified about their assignment.

**•** In Progress—Work has begun.

**•** Completed—Work is complete.

**•** Cannot Complete—Work could not be completed.

**•** Canceled—Work is canceled, typically before any work began

**•** CheckedIn—The customer has arrived for their scheduled appointment.


-----

Important: While you can set the status to null via the API, setting the status to null returns an error. To prevent errors, use one
of the documented picklist values.

The ServiceAppointmentStatus object corresponds to the Status field. Adding a value to the Status field—for example, Waiting—creates
a service appointment status record, and vice versa.

Note: Service appointments also come with a StatusCategory field whose values are identical to the default Status values. If you
create custom Status values, you must indicate which category it belongs to. For example, if you create a `Customer Absent`
value, you may decide that it belongs in the Cannot Complete category. To learn which processes reference StatusCategory,
[see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
