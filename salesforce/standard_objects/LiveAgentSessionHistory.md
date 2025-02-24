#### LiveAgentSessionHistory

This object is automatically created for each Chat session and stores information about changes made to the session. This object is
available in API versions 28.0 and later.

Note: Standard fields for the LiveAgentSession object can only be modified if your administrator has given you editing permissions
for these records.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Fields

```
DataType
Field
LiveAgentSessionId

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
The name of the field that was changed in a session record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the session record that was changed.


-----

```
NewValue
OldValue

##### Usage

```

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
The original value of the field that was changed.


Use this object to identify changes to chat session records.
