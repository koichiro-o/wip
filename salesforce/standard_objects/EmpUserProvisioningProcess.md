#### EmpUserProvisioningProcess

Represents an employee-user provisioning process. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object requires a Workplace Command Center add-on license, or an Employee Experience add-on license.

##### Fields

```
EndTime
ErrorRecordCount
LastReferencedDate
LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the user provisioning process ended.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of records that encountered an error during the user provisioning process.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user provisioning process was last referenced, with a precision
of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
ProcessStatus
StartTime
SuccessRecordCount

```

**Description**
The date and time when the user provisioning process was last viewed, with a precision of
one second.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the user provisioning process.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the user provisioning process.

Possible values are:

**•** `Aborted`

**•** `Cancelled`

**•** `Failed`

**•** `Finished`

**•** `Initializing`

**•** `Processing`

**•** `Queued`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the user provisioning process started.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of records that were successfully provisioned during the user provisioning
process.


-----

```
TotalRecordCount

##### Usage

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of records in the user provisioning process.


Use the EmpUserProvisioningProcess to view the status of an employee-user provisioning process.
