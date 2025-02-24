#### ActionPlanItem

Represents the instance of an action plan item.This object is available in API version 44.0 and later.

##### Supported Calls
```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()undelete()update()upsert()

 Fields

```
```
ActionPlanId
ActionPlanTemplateItemId
IsLocked
IsRequired

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the action plan that this item belongs to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the action plan template item this item was created from.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan item is locked or not. The default value is
```
  false.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan item is required or not.


-----

```
ItemEntityType
ItemId
ItemState

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of object used with the item. This field is available in API version 61.0
and later.

Possible values are:

**•** `Document Checklist Item`

**•** `Event—Available only with sales action plans in API version 63.0 and later`
with the Sales Action Plans add-on license and the Sales Action Plans default
permission set.

**•** `RecordAction`

**•** `Task`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the record created by this action plan item. This field is a polymorphic
relationship field.

**Relationship Name**
Item

**Refers To**
DocumentChecklistItem, Event, RecordAction, Task

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action plan item’s work state.

Possible values are:

**•** `Canceled`

**•** `Completed`

**•** `Deleted`

**•** `In Progress`

**•** `Pending`


-----

```
Name
