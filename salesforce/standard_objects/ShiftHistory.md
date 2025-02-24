#### ShiftHistory

Represents the history of changes made to tracked fields on a time sheet. Available in API versions 46.0 and later.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

Field Service must be enabled in your organization, and field tracking for shift fields must be configured.

##### Fields

```
DataType
Field
NewValue
OldValue
ShiftId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
ID of the shift being tracked. The history is displayed on the detail page for this record.

This is a relationship field.

**Relationship Name**
Shift

**Relationship Type**
Lookup

**Refers To**
Shift

##### Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.
