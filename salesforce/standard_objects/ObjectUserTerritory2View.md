#### ObjectUserTerritory2View

```

This is a polymorphic relationship field.

**Relationship Name**
Object

**Relationship Type**
Lookup

**Refers To**
Account

Lead

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the object.

Possible values are:

**•** `Account`

**•** `Lead`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory that the record is assigned to.

This is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2


Represents a user and object, such as an account or lead, assigned to a territory. This object is available in API version 58.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To see this object, enable Sales Territories.

##### Fields

```
ObjectId
RoleInTerritory2
Territory2Id

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object that the territory user is assigned to.

This field is a polymorphic relationship field.

**Relationship Name**
Object

**Refers To**
Account, Lead

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Role of the user assigned to the territory.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the territory to which the object and user are assigned.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2


-----

```
UserId
