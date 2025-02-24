#### ActionPlanTemplateItemValue

Represents the value associated with an action plan template item. This object is available in API version 44.0 and later.

##### Supported Calls
```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()search()undelete()update()upsert()

 Fields

```
```
ActionPlanTemplateItemId

```

**Type**
reference


-----

```
IsActive
IsLocked
ItemEntityFieldName

```

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the action plan template item that this value relates to.

**Relationship Name**
ActionPlanTemplateItem

**Relationship Type**
Master-detail

**Refers To**
ActionPlanTemplateItem (the master object)

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the task created from this template item is active. The default
value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item value is locked or not. The
default value is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The name of the field on the action plan template item that this value is for.
Available fields include:

**•** `AssessmentTask.AssignedToId`

**•** `AssessmentTask.AssessmentTaskDefinitionId`

**•** `AssessmentTask.Description`

**•** `AssessmentTask.EndTime`

**•** `AssessmentTask.IsRequired`

**•** `AssessmentTask.Name`


-----

**•** `AssessmentTask.OwnerId`

**•** `AssessmentTask.ParentId` (Visit ID)

**•** `AssessmentTask.ReferenceRecordId`

**•** `AssessmentTask.SequenceNumber`

**•** `AssessmentTask.StartTime`

**•** `AssessmentTask.Status`

**•** `AssessmentTask.TaskDefinitionId`

**•** `AssessmentTask.TaskType`

**•** `DocumentChecklistItem.DocumentTypeId`

**•** `DocumentChecklistItem.Instruction`

**•** `DocumentChecklistItem.IsAccepted`

**•** `DocumentChecklistItem.IsFrozen`

**•** `DocumentChecklistItem.IsRequired`

**•** `DocumentChecklistItem.Name`

**•** `DocumentChecklistItem.OwnerId`

**•** `DocumentChecklistItem.ParentRecordId`

**•** `DocumentChecklistItem.Status`

**•** `DocumentChecklistItem.WhoId`

**•** `Event`

**•** `Event.ActivityDate`

**•** `Event.ActivityDateTime`

**•** `Event.Description`

**•** `Event.DurationInMinutes`

**•** `Event.EndDateTime`

**•** `Event.EventSubtype`

**•** `Event.IsAllDayEvent`

**•** `Event.IsPrivate`

**•** `Event.IsRecurrence`

**•** `Event.IsReminderSet`

**•** `Event.IsVisibleInSelfService`

**•** `Event.Location`

**•** `Event.OwnerId`

**•** `Event.Recurrence2PatternText`

**•** `Event.RecurrenceDayOfWeekMask`

**•** `Event.RecurrenceDayOfMonth`

**•** `Event.RecurrenceEndDateOnly`

**•** `Event.RecurrenceInterval`

**•** `Event.RecurrenceInstance`


-----

**•** `Event.RecurrenceMonthOfYear`

**•** `Event.RecurrenceStartDateTime`

**•** `Event.RecurrenceTimeZoneSidKey`

**•** `Event.RecurrenceType`

**•** `Event.ReminderDateTime`

**•** `Event.StartDateTime`

**•** `Event.ShowAs`

**•** `Event.Subject`

**•** `Event.Type`

**•** `Event.WhatId`

**•** `Event.WhoId`

**•** `IndividualApplicationTask.Description This value is`
available in API version 62.0 and later.

**•** `IndividualApplicationTask.IsSubmitted`

**•** `IndividualApplicationTask.Name`

**•** `IndividualApplicationTask.SavedApplicationUrl`

**•** `OtherComponentTask.ParticipantRoleId`

**•** `RecordAction.ActionDefinition`

**•** `RecordAction.ActionType`

**•** `RecordAction.FlowDefinition` (Interaction Definition ID)

**•** `RecordAction.FlowInterviewId`

**•** `RecordAction.IsMandatory`

**•** `RecordAction.IsUiRemoveHidden` (Hide Remove Action in UI)

**•** `RecordAction.Order`

**•** `RecordAction.Pinned`

**•** `RecordAction.ParticipantRoleId`

**•** `RecordAction.RecordId(Parent Record ID)`

**•** `RecordAction.Status`

**•** `Task.ActivityDate` (Due Date Only)

**•** `Task.CallDisposition`

**•** `Task.CallDurationInSeconds`

**•** `Task.CallObject`

**•** `Task.CallType`

**•** `Task.Description`

**•** `Task.IsRecurrence`

**•** `Task.IsReminderSet`

**•** `Task.OwnerId` (Assigned To ID)

**•** `Task.Priority`


-----

```
ItemEntityType
LastReferencedDate
LastViewedDate

```


**•** `Task.RecurrenceDayOfMonth`

**•** `Task.RecurrenceDayOfWeekMask`

**•** `Task.RecurrenceEndDateOnly`

**•** `Task.RecurrenceInstance`

**•** `Task.RecurrenceInterval`

**•** `Task.RecurrenceMonthOfYear`

**•** `Task.RecurrenceRegeneratedType`

**•** `Task.RecurrenceStartDateOnly`

**•** `Task.RecurrenceTimeZoneSidKey`

**•** `Task.RecurrenceType`

**•** `Task.ReminderDateTime`

**•** `Task.Status`

**•** `Task.Subject`

**•** `Task.TaskSubtype`

**•** `Task.WhatId (Related To ID)`

**•** `Task.WhoId`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of action plan template item.

Possible values are:

**•** `Document Checklist Item`

**•** `Event—Available in API version 63.0 and later with the Sales Action Plans`
add-on license and the Sales Action Plans default permission set.

**•** `RecordAction`

**•** `Task`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime


-----

```
MayEdit
Name
ValueFormula
ValueLiteral

```

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template item value can be edited or not. The
default value is false.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The unique identifier for this record.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A formula used to calculate the value for this action plan template item.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**

The value for this action plan template item.

