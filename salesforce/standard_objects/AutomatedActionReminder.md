#### AutomatedActionReminder

Represents a reminder to the end user to take an action in the future. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
ActionTakenDateTime
AutomatedActionId
IsLocked
IsValidForUser

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Timestamp of when the user took the action suggested by the reminder.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action reminder record is locked or not.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action is active and accessible to the user who owns the
record (true) or not (false).

The default value is `false.`


-----

```
MayEdit
ReferenceRecordId
StartDateTime
State

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action reminder record can be edited or not.

The default value is `false.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that triggered the reminder. For example, when a rule is set to Case, the value of
this field is `CaseId.`

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact, Invoice, Lead, Opportunity

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time this reminder is scheduled to be displayed to the user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the reminder.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Disabled`


-----

```
Type

##### Associated Objects

```


**•** `Dismissed`

**•** `Expired`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of automated action reminder.

Possible values are:

**•** `Reminder`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionReminderOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AutomatedActionReminderShare on page 66**
Sharing is available for the object.
