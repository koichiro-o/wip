#### EmpUserProvisionProcessErr

Represents an employee-user provisioning process error. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object requires a Workplace Command Center add-on license, or an Employee Experience add-on license.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Person Account linked to the employee record associated with the error.

This is a relationship field.

**Relationship Name**
Account

**Refers To**
Account


-----

```
EmployeeId
ErrorCode
ErrorMessage
LastReferencedDate
LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the employee record associated with the error.

This is a relationship field.

**Relationship Name**
Employee

**Relationship Type**
Lookup

**Refers To**
Employee

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the provisioning isn’t successful.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If an error occurred, this field contains the error message.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the error was last referenced, with a precision of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the error was last viewed, with a precision of one second.


-----

```
Name
ProvisioningProcessId

##### Usage

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the error.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated user provisioning process.

This is a relationship field.

**Relationship Name**
ProvisioningProcess

**Relationship Type**
Lookup

**Refers To**
EmpUserProvisioningProcess


Use the EmpUserProvisionProcessErr to view the errors for an employee-user provisioning process.
