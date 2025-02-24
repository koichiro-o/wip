#### MaintenanceWorkRule

Represents the recurrence pattern for a maintenance record. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
DoesFloatingWorkOrder

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the maintenance plan uses the floating work order adjustment. The default is
false.


-----

```
LastReferencedDate
LastViewedDate
Name
NextSuggestedMaintenanceDate
OwnerId
ParentMaintenancePlanId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last modified. Its label in the user interface is `Last`
```
  Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this maintenance work rule.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next date on which this rule will generate maintenance items.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The assigned owner of the maintenance work rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ParentMaintenanceRecordId
RecordsetFilterCriteriaId
RecurrencePattern
SortOrder
Title
Type

```

**Description**
The maintenance plan associated with the maintenance work rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance record this work rule applies to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recordset filter criteria associated with this maintenance work rule. Available in API
version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The RRULE that defines the pattern of recurrence for this work order rule.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The sort order that applies to this work order rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The title of this work order rule.

**Type**
picklist


-----

```
WorkTypeId

##### Associated Objects

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of maintenance work rule. Available values are:

**•** `Criteria-based`

**•** `Calendar-based` (default)

Available in API version 52.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work type that this work order rule generates.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MaintenanceWorkRuleChangeEvent**

Change events are available for the object.

**MaintenanceWorkRuleFeed**

Feed tracking is available for the object.

**MaintenanceWorkRuleHistory**

History is available for tracked fields of the object.

**MaintenanceWorkRuleOwnerSharingRule**

Sharing rules are available for the object.

**MaintenanceWorkRuleShare**

Sharing is available for the object.
