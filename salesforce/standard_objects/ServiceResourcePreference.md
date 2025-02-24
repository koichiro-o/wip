#### ServiceResourcePreference

Represents the service resource scheduling preferences that are considered as a business objective in the scheduling logic engine. This
object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
The org must have the Workforce Engagement license. To view, create, edit, and delete records, the user must have the Workforce
Engagement Agent or Workforce Engagement Planner permission set.


-----

##### Fields

**Field**
```
EndDate
LastReferencedDate
LastViewedDate
Name
OperatingHoursId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date period that this preference is effective.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource preference was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service resource preference was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The service resource preference record name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The operating hours associated with the service resource preference.

This is a relationship field.

**Relationship Name**
OperatingHours


-----

```
OwnerId
ServiceResourceId
StartDate

```

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service resource preference.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource associated with the service resource preference.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The start date period that this preference is effective.


-----
