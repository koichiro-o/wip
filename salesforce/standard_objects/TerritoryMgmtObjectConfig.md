#### TerritoryMgmtObjectConfig

Represents territory management settings and defaults for a particular object. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

Only standard and partner users can access this object.

##### Fields

```
DefaultAccessLevel
DeveloperName
Language
MasterLabel
Object

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The default access level of the defined object for all territories.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the org where the territory model was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The readable label for this entity.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The name of the Enterprise Territory Management object.

Possible values are:


-----

```
State
