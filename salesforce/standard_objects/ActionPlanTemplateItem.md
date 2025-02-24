#### ActionPlanTemplateItem

Represents the instance of an item on an action plan template version. This object is available in API version 44.0 and later.

##### Supported Calls
```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search()undelete()update()upsert()

 Fields

```
```
ActionPlanTemplateVersionId
DisplayOrder
IsActive

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**

The version of the action plan template this item is for.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The order in which this item is displayed within the action plan template version.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is active. The default
value is `false.`


-----

```
IsLocked
IsRequired
ItemEntityType
LastReferencedDate
LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item is locked or not. The default
value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is required. The default
value is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The type of action plan template item entity..

Possible values are:

**•** `Document Checklist Item`

**•** `Event—This value is available in API version 63.0.`

**•** `RecordAction`

**•** `Task`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
MayEdit
Name
UniqueName

```

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item can be edited or not. The default
value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, idLookup, Update

**Description**

The unique identifier for this action plan template item record.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this action plan template item. This field is unique within
your organization.

