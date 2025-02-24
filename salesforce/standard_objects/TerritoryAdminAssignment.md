#### TerritoryAdminAssignment

Represents designated team members who can administer specific territories and their descendants. This object is available in API version
63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
To designate team members, assign them the Administer Territory Operations permission.


-----

##### Fields

**Field**
```
CanManageHierarchy
CanManageMembers
CanManageRecordAssociations
Territory2Id

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user update and delete the territory and its descendants, and create descendants.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user assign other team members to the territory and its descendants. Also lets the
user update the user territory association log.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Lets the user add and remove assignments for records, author rules, and assign and run rules
for the territory and its descendants.

The default value is `false.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the territory you’re letting the user administer. The user can also administer this
territory’s descendants.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2


-----

```
Territory2ModelId
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the territory model that includes the territory you’re letting the user administer.

This field is a relationship field.

**Relationship Name**
Territory2Model

**Refers To**
Territory2Model

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID for the user you’re letting administer the territory and its descendants. Requires that
the user is assigned the Administer Territory Operations permission set.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Refers To**
Group, User

