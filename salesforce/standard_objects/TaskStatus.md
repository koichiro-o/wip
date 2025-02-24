#### TaskStatus

Represents the status of a task, such as Not Started, Completed, or Closed.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
ApiName
IsClosed
IsDefault
MasterLabel

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this task status value represents a closed task (true) or not (false).
Multiple task status values can represent a closed task.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task status value (true) or not (false) in the
picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task status value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.


-----

```
 SortOrder

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the task status picklist. These numbers aren’t guaranteed
to be sequential, as some previous task status values might have been deleted.


This object represents a value in the task status picklist. The task status picklist provides additional information about the status of a task
, such as whether a given status value represents an open or closed task. Your client application can query this object to retrieve the set
of values in the task status picklist, and then use that information while processing task records to determine more information about
a given task. For example, the application could test whether a given task is open or closed based on the task `Status` value and the
value of the `IsClosed` property in the associated TaskStatus record.

SEE ALSO:

Overview of Salesforce Objects and Fields
