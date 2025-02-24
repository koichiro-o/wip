#### FlowOrchestrationVersion

Represents the version of an orchestration. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

```

-----

##### Fields

**Field**
```
ActivatedById
ActivatedDate
ApiVersion
Description
FlowOrchestrationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that activated the orchestration.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the orchestration was activated.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version of this orchestration record version.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow orchestration version.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent orchestration running this version.


-----

```
IsOverridable
IsTemplate
LastReferencedDate
LastViewedDate
Name

```

This field is a relationship field.

**Relationship Name**
FlowOrchestration

**Relationship Type**
Master-detail

**Refers To**
FlowOrchestration

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration that's part of a managed package is overridable.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration record version is a template.

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
string


-----

```
OrchestrationType
OverriddenById
OverriddenOrchestrationId

```

**Properties**
Filter, Group, idLookup, Sort

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

**•** `OrchRecTrigAftSave—Record-Triggered After Save Orchestration: Launches`
when a record is created or updated. An orchestration lets you create a multi-step,
multi-user process. This type of flow runs in the background without user interaction.

**•** `CmsOrchAutolnch—CMS Workflow Orchestration Autolaunched: Launches when`
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


-----

```
RunInMode
SourceTemplateId
Status

```

**Description**
The ID of the orchestration that the current orchestration is overriding.

This field is a relationship field.

**Relationship Name**
OverriddenOrchestration

**Refers To**
FlowOrchestration

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the orchestration runs in.

Possible values are:

**•** `DefaultMode—The orchestration version runs in system or user context, depending`
on how the orchestration is launched.

**•** `SystemModeWithSharing—The orchestration version always runs in system`
mode with sharing. The orchestration respects org-wide default settings, role hierarchies,
sharing rules, manual sharing, teams, and territories. But it doesn’t respect object
permissions, field-level access, or other permissions of the running user.

**•** `SystemModeWithoutSharing—The orchestration version can access all data.`
In the UI, this value appears as System Context without Sharing—Access All Data.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Refers To**
FlowOrchestration

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
TriggerObjectOrEventLabel
VersionNumber

##### Associated Objects

```

**Description**
The ID of the template that the orchestration was created from. This is a relationship
field.(Refers to Orchestration Record).

Possible values are:

**•** `Active—Active`

**•** `Draft—Inactive`

**•** `InvalidDraft—Draft`

**•** `Obsolete—Inactive`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the orchestration version.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationVersionChangeEvent on page 67**
Change events are available for the object.
