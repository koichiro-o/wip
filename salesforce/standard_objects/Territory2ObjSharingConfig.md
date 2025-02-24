#### Territory2ObjSharingConfig

Represents the sharing access level of objects assigned to a particular territory. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update()

 Special Access Rules

```
Only standard and partner users can access this object. Any standard or partner user can view object sharing configuration records in
an active model. Users without the Manage Territories permission can’t view territory records in the `Planning` or `Archived state.`


-----

##### Fields

**Field**
```
AccessLevel
Territory2Id
TerritoryMgmtObjectConfigId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The access level of the object for the particular territory.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The territory on which the access level is defined.

This field is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The object configuration record the territory access level is related to.

This field is a relationship field.

**Relationship Name**
TerritoryMgmtObjectConfig

**Relationship Type**
Lookup

**Refers To**
TerritoryMgmtObjectConfig


-----
