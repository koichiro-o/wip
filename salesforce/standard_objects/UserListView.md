#### UserListView

Represents the customizations a user made to a list view. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Name**
```
LastViewedChart
ListViewId
SobjectType
UserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The last chart a user viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the list view.

This is a relationship field.

**Relationship Name**
ListView

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The API name of the sObject for the user list view.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


-----

**Refers To**
User
