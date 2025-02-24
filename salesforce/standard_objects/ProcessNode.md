#### ProcessNode

Describes a step in a process definition. Compare to ProcessInstanceNode, which describes a step in a running process. This object is
available in API version 31.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field**
```
Description
DeveloperName
Name
ProcessDefinitionId

##### Usage

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A description of this node, no longer than 3,000 bytes.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The external name of the node that’s seen by users.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique node name.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the object affected by this approval instance.

A relationship field.

**Relationship Name**
ProcessDefinition

**Relationship Type**
Lookup

**Refers To**
ProcessDefinition


Use this object to get details about the process node or the process definition that it's associated with.


-----
