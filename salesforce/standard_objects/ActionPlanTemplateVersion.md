#### ActionPlanTemplateVersion

Represents the version of an action plan template. This object is available in API version 44.0 and later.


-----

##### Supported Calls
```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search
( )undelete()update()upsert()

 Fields

```
```
ActionPlanTemplateId
ActivationDateTime
InactivationDateTime
IsLocked
LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Filter, Group, Sort

**Description**

The ID of the action plan template this version represents.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort,

**Description**

The date and time at which this version became active.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

The date and time at which this version became inactive.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template version is locked or not. The default
value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort,, Sort


-----

```
LastViewedDate
MayEdit
Name
Status
Version

```

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template version can be edited. The default
value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update,

**Description**

The name of this version item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action plan template version’s state. Possible values are:

**•** `Draft`

**•** `Final – Published`

**•** `Obsolete`

**•** `ReadOnly`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort


-----

**Description**

The index number of this action plan template version.
