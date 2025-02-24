#### AutomatedAction

Represents the configuration of an automated action, such as a workflow rule. This object is available in API version 57.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ApiVersion
Description
ErrorDetail
ErrorMessage

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. API version to use for executing the automated action.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the automated action.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The source of the error encountered when executing the automated action.

Possible values are:

**•** `invalidCondition`

**•** `invalidConditionReference`

**•** `invalidConditionValue`

**•** `invalidInvocableAction`

**•** `invalidInvocableActionParam`

**•** `invalidReferenceEntity`

**•** `unknownError`

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
EvalType
ExecutionType
ExtraFilterExpression
ExtraFilterType

```

**Description**
A description of the error encountered when executing the automated action.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
When the automated action runs.

Possible values are:

**•** `OnCreate`

**•** `OnCreateAndUpdate`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Whether the action runs automatically or generates a reminder.

Possible values are:

**•** `Automatic`

**•** `Reminder`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional condition logic for cross-object filters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Additional criteria for cross-object filters.

Possible values are:

**•** `Advanced`

**•** `And`

**•** `Or`


-----

```
FilterExpression
FilterType
InvocationName
IsLocked
LastEditedDateTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If `FilterType` is `Advanced, this field contains the condition logic.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Criteria for filters.

Possible values are:

**•** `Advanced`

**•** `And`

**•** `Or`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Invocable action to execute.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action record is locked or not.

The default value is `false.`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the automated action had a change that impacted rule evaluation.


-----

```
LastReferencedDate
LastViewedDate
MayEdit
Name
ReferenceEntity
RuleType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record was likely referenced (LastReferencedDate) and not viewed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action record can be edited or not.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the automated action.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Entity on which the automated action operates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
State
SubscriptionState
Summary

##### Associated Objects

```

**Description**
The type of workflow rule.

Possible values are:

**•** `ManagerAssigned`

**•** `ManagerSubscribed`

**•** `Personal`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the alert.

Possible values are:

**•** `Active`

**•** `Error`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
For users who don’t have an override, the default value of the subscription.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
A human-readable explanation of the automated action, its conditions, and its parameters.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**AutomatedActionOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AutomatedActionShare on page 66**
Sharing is available for the object.
