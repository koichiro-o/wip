#### UserDefinedLabelAssignment

Represents a relationship between a record label and the item the user assigned it to. This object is available in API version 61.0 and
later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
EntityType
ItemId
LabelId
OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Object label of the Item record derived from ItemId. Available in API version 62.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Item record added to the UserDefinedLabel record.

This field is a polymorphic relationship field.

**Relationship Name**
Item

**Refers To**
Account, ActionCadence, ActionCadenceStepTracker, CallTemplate, Case, Contact,
EmailTemplate, FlowOrchestrationWorkItem, Lead, Opportunity, Task

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the UserDefinedLabel record that the Item record is assigned to.

This field is a relationship field.

**Relationship Name**
Label

**Refers To**
UserDefinedLabel

**Type**
reference


-----

```
SortOrder
SubjectOrName

##### Associated Objects

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Order of the assigned items for a given UserDefinedLabel record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the Item record. If it's a task, the value is the subject of the Item record.


This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**UserDefinedLabelAssignmentOwnerSharingRule on page 64**
Sharing rules are available for the object.

**UserDefinedLabelAssignmentShare on page 66**
Sharing is available for the object.
