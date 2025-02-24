#### WorkStepStatus

Represents a picklist for a status category on a work step. This object is available in API version 52.0 and later.

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
SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The name of the work step status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Controls whether this status is the default value of the picklist of the corresponding status
category (true) or not (false). Default is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. The label of the work step status.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
StatusCode
