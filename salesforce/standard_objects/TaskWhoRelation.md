#### TaskWhoRelation

Represents the relationship between a task and a lead or contacts. This object is available in API version 29.0 and later.

TaskWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared
Activities for your organization.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field Name**
```
AccountId
RelationId
TaskId
Type

##### Usage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the Account ID of the relation.

For information on IDs, see ID Field Type.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the contacts or lead related to the task.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the person related to the task is a lead or contact.


**Apex example that queries contacts associated with a task**


-----

SEE ALSO:

Task

TaskRelation
