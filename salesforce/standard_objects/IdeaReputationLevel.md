#### IdeaReputationLevel

Represents a reputation level within an Ideas zone or internal organization and is used by the system to calculate reputation. You can
create up to 25 levels per zone or internal organization. This object is available in API version 28.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ContextId
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Namepointing, Sort, Update

**Description**

The ID of the zone or internal organization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Threshold

##### Usage

```

**Description**

Name of the reputation level. The name must be unique within the zone or
internal organization. Maximum size is 50 characters.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level. The threshold must be unique within
the zone or internal organization and must be greater than or equal to zero.


Use to create or edit reputation levels for an Ideas zone or internal organization.
