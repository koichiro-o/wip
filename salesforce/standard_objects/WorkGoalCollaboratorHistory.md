#### WorkGoalCollaboratorHistory

Represents the history of changes to the values in the fields in a WorkGoalCollaborator object. Access is read-only.

Note: This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals in API
version 35.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


-----

##### Fields

**Field Name**
```
DataType
Field
NewValue
OldValue
WorkGoalCollaboratorId

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

Name of the standard or custom field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**

New value of the modified field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**

Previous value of the modified field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the WorkGoalCollaborator object that is associated with this history entry.


-----
