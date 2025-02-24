#### Territory2ObjectExclusion

Represents the objects that aren’t included in territory assignment rule runs, even when they meet assignment rule criteria. This object
is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
Available if Sales Territories has been enabled.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your org’s sharing settings. Users can’t view territory models in other states (such as `Planning`
or `Archived).`

##### Fields

```
Note
ObjectId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Territory2Id

```

**Description**
The ID of the Account object to exclude from the territory assignment rule.

This is a polymorphic relationship field.

**Relationship Name**
Object

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory to exclude from the territory model assignment rule.

This is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

