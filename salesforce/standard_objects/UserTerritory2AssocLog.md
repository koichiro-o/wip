#### UserTerritory2AssocLog

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is active (true) or inactive (false) in the given
territory.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The role of the user in a territory. Possible values are: Owner, Administrator, Sales
Rep. Label is `Role in Territory.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory that the user is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user who is assigned to the territory.


Represents a log of when a user is assigned and unassigned from a territory. This object is available in API version 57.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

```

-----

##### Special Access Rules

To see this object, enable Sales Territory and User Tracking on the Territory Settings page. Activate a territory model to start the tracking.

##### Fields

```
CurrencyIsoCode
EndDate
Name
RoleInTerritory2

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code of currency.

Possible values are:

**•** `EUR—Euro`

**•** `INR—Indian Rupee`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the user is unassigned from a territory. If the end date is empty, the user is still
assigned.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Auto-generated unique name of the log.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
User’s role in the territory between the start and end date. The picklist is, by default, empty.
Add values to this field using Object Manager.


-----

```
StartDate
Territory2Id
Territory2ModelId
UserId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the user is assigned to the territory.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the territory associated with the log.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the territory model associated with the log.

This field is a relationship field.

**Relationship Name**
Territory2Model

**Refers To**
Territory2Model

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user associated with the log.

This field is a relationship field.

**Relationship Name**
User


-----

**Refers To**
User
