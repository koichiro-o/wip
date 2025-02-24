#### TaskPriority

Represents the importance or urgency of a task, such as High, Normal, or Low.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Customer and Partner Portal users can’t access this object.

##### Fields

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.


-----

```
IsDefault
 IsHighPriority
 MasterLabel
 SortOrder

##### Usage

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the status is the default task priority value (true) or not (false) in the
picklist. Only one value in the picklist can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this task priority value represents a high priority task (true) or not
(false). Multiple task priority values can represent a high-priority task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this task priority value. This display value is the internal label that doesn’t get
translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
Number used to sort this value in the task priority picklist. These numbers aren’t guaranteed
to be sequential, as some previous task priority values might have been deleted.


This object represents a value in the task priority picklist. The task priority picklist provides additional information about the importance
of a task, such as whether a given priority value represents a high priority. Your client application can query on this object to retrieve
the set of values in the task priority picklist, and then use that information while processing task objects to determine more information
about a given task. For example, the application could test whether a given task is high priority based on its `Priority` value and the
value of the `IsHighPriority field in the associated TaskPriority object.`

SEE ALSO:

Overview of Salesforce Objects and Fields


-----
