#### WebCartHistory

WebCartHistory represents the history of changes to the values in the fields of the `WebCart` object.

For specific version information, see the documentation for WebCart.


-----

##### Supported Calls
```
describeSObjects(), query, replicate, retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

For specific special access rules, if any, see the documentation for `WebCart.`

##### Fields

```
DataType
Field
NewValue
OldValue
WebCartId

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
Name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Old value of the field that was changed.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the `WebCart.`
