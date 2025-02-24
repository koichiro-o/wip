#### LinkedArticleHistory

```
Represents the history of changes made to tracked fields on a linked article. This object is available in API version 37.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

Knowledge must be enabled in your org.

##### Fields

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.


-----

```
Field
LinkedArticleId
NewValue
OldValue
