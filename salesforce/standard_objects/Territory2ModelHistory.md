#### Territory2ModelHistory

Represents the history of changes to the values in the fields on a territory model. Available if Sales Territories has been enabled.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Fields

```
DataType
Field
NewValue
OldValue
Territory2ModelId

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
The name of the field whose value was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
The ID of the territory model whose history is tracked.

##### Usage

This object is automatically generated whenever any field value changes on a territory model record. Use this object it to identify those
changes.
