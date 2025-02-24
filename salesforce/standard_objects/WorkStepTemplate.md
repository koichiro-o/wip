#### WorkStepTemplate

```

**Description**
Required. The order in which the work step statuses are displayed in the status category's
picklist.

**Type**
picklist

**Properties**
Required. Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that this status belongs to.

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `NotApplicable`

**•** `Paused`


Represents a template for a work step. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
ActionDefinition

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
ActionType
Description
IsActive
LastReferencedDate
LastViewedDate

```

**Description**
The platform action that the work step executes. The possible values are the names of the
flow and quick actions configured in your org.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of platform action that the work step is associated with.

Possible values are:

**•** `Flow`

**•** `QuickAction`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the work step template.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether this work step template is active true or not false. Default is false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId

##### Associated Objects

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the work step template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner who created the work step template.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkStepTemplateChangeEvent**

Change events are available for the object.

**WorkStepTemplateFeed**

Feed tracking is available for the object.

**WorkStepTemplateHistory**

History is available for tracked fields of the object.

**WorkStepTemplateOwnerSharingRule**

Sharing rules are available for the object.

**WorkStepTemplateShare**

Sharing is available for the object.
