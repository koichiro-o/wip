#### ObjectTerritory2Association

Represents an association (by assignment) between a territory and an object record such as an account or a lead.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available after enabling Sales Territories.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your sharing settings.

If you delete associations, you can query them for up to 12 hours. Keep in mind that deleted associations bypass the recycle bin.

##### Fields

```
AssociationCause
ObjectId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The means by which the record was associated with the territory. User interface
field label is `Method.`

Possible values are:

**•** `Territory2AssignmentRule—Territory assignment rule association`

**•** `Territory2Manual—Manual association`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the object assigned to the territory.

|Object|Availability|
|---|---|
|Account|API version 30.0 and later|
|Lead|API version 55.0 and later|


-----

```
SobjectType
Territory2Id
