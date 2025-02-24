#### WorkGoalHistory

Represents the history of changes to the values in the fields of a WorkGoal. Access is read-only. This object has been deprecated as of
API version 35.0. Use the GoalHistory object to query historical information for WDC goals.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Fields

```
Field
NewValue
OldValue
WorkGoalId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The name of the field that was changed.

**Type**
Any Type

**Properties**
Nillable, Sort

**Description**

The new value of the field that was changed.

**Type**
Any Type

**Properties**
Nillable, Sort

**Description**

The latest value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

**Description**

ID of the Goal. Label is Goal ID.
