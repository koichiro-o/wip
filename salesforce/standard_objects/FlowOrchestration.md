#### FlowOrchestration

```


**•** `UserProvisioningFlow`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier. For example:`
```
  TID:000000000000c00fff.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time that the flow was executed in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```
**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in milliseconds to start and finish all flow interviews.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who executed the flow through the UI or the API. For example:
```
  00530000009M943.

```

Represents the details of an orchestration definition. This object is available in API version 62.0 and later.


-----

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), update()

 Fields

```
```
ActiveVersionId
ApiName
ApiVersion
AverageRunTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active orchestration version. This field is a relationship field.

This field is a relationship field.

**Relationship Name**
ActiveVersion

**Refers To**
FlowOrchestrationVersion

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the the orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the active orchestration or the last saved orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The average duration of an orchestration run that has completed without error.


-----

```
CompletionRate
Description
FailedRunCount
InstalledPackageName
IsCitizenEnabled
IsOverridable

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the total number of orchestration runs that have completed without error.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The description of the flow orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of orchestration runs that have failed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the installed package that the orchestration is a part of.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration can be modified by non-admins. Valid value is False.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsTemplate
LastReferencedDate
LastViewedDate
ManageableState

```

**Description**
Indicates whether the orchestration that's part of a managed package is overridable.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration record is a template.

The default value is `false.`

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
The timestamp for when the current user last viewed this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the managable state of the orchestration that's contained in a package.

Valid values are:

**•** `beta—Managed-Beta`

**•** `deleted—Managed-Proposed-Deleted`

**•** `deprecated—Managed-Proposed-Deprecated`

**•** `deprecatedEditable—SecondGen-Installed-Deprecated`

**•** `installed—Managed-Installed`

**•** `installedEditable—SecondGen-Installed-Editable`

**•** `released—Managed-Released`


-----

```
Name
NamespacePrefix
OrchestrationDefinition
OrchestrationLabel
OrchestrationType

```


**•** `unmanaged—Unmanaged`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The label of the orchestration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the orchestration record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the orchestration definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The label of the orchestration.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The orchestration's flow type. FlowType consolidates ProcessType and TriggerType into one
field. FlowType is used with permissions, so admins can control access to each flow type.

Valid values are:

**•** `OrchAutolnch—Autolaunched No Trigger Orchestration: Launches when invoked`
by Apex, REST API, custom buttons, or custom links. An orchestration lets you create a
multi-step, multi-user process.


-----

```
OverriddenById
OverriddenOrchestrationId
RunCount
SourceTemplateId

```


**•** `OrchRecTrigAftSave—Record-Triggered After Save Orchestration: Launches`
when a record is created or updated. An orchestration lets you create a multi-step,
multi-user process. This type of flow runs in the background without user interaction.

**•** `CmsOrchAutolnch —CMS Workflow Orchestration Autolaunched: Launches when`
invoked from the Workflows component in a CMS workspace. This type of orchestration
lets you create a multi-step, multi-user process to create, edit, organize, and manage
digital content from a centralized location

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that's overriding the current orchestration.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Refers To**
FlowOrchestration

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that the current orchestration is overriding.

This field is a relationship field.

**Relationship Name**
OverriddenOrchestration

**Refers To**
FlowOrchestration

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of orchestration runs that have been started across all orchestration versions.

**Type**
reference


-----

```
Status
TriggerType

##### Associated Objects

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template that the orchestration was created from.

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Refers To**
FlowOrchestration

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the record.

Valid values are:

**•** `Active—Active`

**•** `Draft—Inactive`

**•** `InvalidDraft—Draft`

**•** `Obsolete—Inactive`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the trigger type for a record-triggered orchestration.

Valid values are:

**•** `RecordAfterSave—Record—Run After Save`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationChangeEvent on page 67**
Change events are available for the object.


-----
