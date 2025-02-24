#### ShiftStatus

Represents a shift, such as Tentative, Published, or Confirmed. Available in API versions 46.0 and later.

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
Indicates whether this is the default shift status value (true) or not (false) in the picklist.
Only one value can be the default value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this shift status value. This display value is the internal label that does not
get translated. Limit: 255 characters.


-----

```
SortOrder
StatusCode

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the shift status picklist. These numbers are not guaranteed
to be sequential, as some previous shift status values might have been deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the status of the shift using static values. Possible values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`


Scheduling and dispatching service resources using shift data is not supported in API version 46.0.
