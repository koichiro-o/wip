#### WorkOrderHistory

Represents the history of changes made to tracked fields on a work order. This object is available in API version 36.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

Work orders or Field Service must be enabled in your organization, and field tracking for work order fields must be configured.

##### Fields

```
DataType
Field

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


-----

```
NewValue
OldValue
WorkOrderId
