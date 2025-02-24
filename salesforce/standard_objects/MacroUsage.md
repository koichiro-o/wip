#### MacroUsage

Represents macro usage on a record, including which macro was used, who used it, and how they used it. This object is available in API
version 47.0 and later.

##### Supported Calls

describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

delete() is supported in API version 55.0 and later.

##### Special Access Rules

This object is always read-only. Only users with “Modify All Data” permission can delete MacroUsage records.


-----

##### Fields

**Field**
```
AppContext
ConditionCount
ContextRecord
DurationInMs
ExecutedInstructionCount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Context in which the macro was run. Possible values are:

**•** `Aloha—Salesforce Classic`

**•** `Lightning—Lightning Experience`

**•** `Unknown`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of conditional instructions contained in the macro at execution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the record on which the macro was run.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The execution time, in milliseconds, for the macro.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of macro instructions that ran successfully. If the macro completed successfully,
this value is the same as InstructionCount.


-----

```
ExecutionEndTime
ExecutionState
FailureReason
FolderId
InstructionCount

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time at which macro execution completed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The end state of macro execution. Possible values are

**•** `SUCCESS`

**•** `FAILURE`

**•** `CANCELED`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If `ExecutionState` is failure, this field stores the reason for the failure. Possible values
are:

**•** `ACCESS`

**•** `GENERIC`

**•** `TIMEOUT`

**•** `UNSUPPORTED`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the folder containing the macro at the time it was used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
IsFromBulk
MacroID
Name
OwnerId
UserId

```

**Description**
The number of instructions in the macro at the start of execution.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the macro was run as a bulk macro. When a bulk macro is run on multiple records,
usage is recorded per record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the macro.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the macro.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the group or user that owns the macro.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user that ran the macro.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MacroUsageOwnerSharingRule**

Sharing rules are available for the object.

**MacroUsageShare**

Sharing is available for the object.
