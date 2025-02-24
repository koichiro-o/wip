#### ServiceSetupProvisioning

Represents a task completed by the Service Setup Assistant. This object is available in API version 52.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
ServiceSetupProvisioning is accessible only if the Service Setup Assistant is turned on. Users need the Customize Application permission
to access it.


-----

##### Fields

**Field**
```
JobName
Name
Status
TaskAction

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of a group of tasks completed by the Service Setup Assistant.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the task being completed by the Service Setup Assistant.

Possible values are:

**•** `

**•** `Completed—The task completed successfully.`

**•** `ExistingSetup—The task couldn’t be completed due to conflicting configurations.`

**•** `FailedFatalError—The task couldn’t be completed.`

**•** `InProgress—The task is in progress.`

**•** `PRE_CONDITION_NOT_MET—The task couldn’t be completed because one or more`
prerequisites weren’t met.

**•** `VALIDATION_NOT_MET—The task is considered as completed but the condition`
defined in the implementation was not true. No retry will be executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action taken by the task.

Possible values are:


-----

```
TaskActionContext
TaskContext
TaskName
