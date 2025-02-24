#### WaveAutoInstallRequest

Provides access to the concrete object that represents a CRM Analytics auto-install request. The auto-install request tracks the progress
of CRM Analytics applications created from CRM Analytics templates by the automated process user. This object is available in API version
38.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
CRM Analytics must be enabled in your org. A user must have the Auto Install permission enabled.


-----

##### Fields

**Field**
```
 Configuration
 FailedReason

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**
CRM Analytics application configuration for the auto-install request.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the CRM Analytics application fails to complete successfully, this value indicates why the
failure occurred. Values can be:

**•** `OrganizationIncompatible: the org didn't pass the template compatibility`
checks.

**•** `AppInstallationSkipped: the org didn't pass the template compatibility checks`
and was skipped.

**•** `RetriesExhausted: the request exhausted the maximum number of retries.`

**•** `RequestCancelled: the user canceled the request.`

**•** `AppCreateFailure: the app or folder creation failed. Check the request log and`
try again.

**•** `AppUpdateFailure: the app or folder update failed. Check the request log and try`
again.

**•** `AppConstructionFailure: the app or folder construction failed. Check the`
request log and try again.

**•** `WaveDisabled: the org doesn't have the Wave org permission or preference enabled.`
Check the licenses for CRM Analytics and try again.

**•** `CancelFailed: canceling an in-progress app failed. Check the request log and try`
again.

**•** `DeleteFailed: deleting an app failed. Check the request log and try again.`

**•** `DependencyFailure: a dependent auto-install request failed. Check App Install`
History and try again.

**•** `DependencyCancelled: the user canceled a dependent auto-install request. Check`
App Install History and try again.

**•** `FailedToEnqueue: the request failed to enqueue. Check the request log and try`
again.

**•** `FailedOther: the request failed for another reason. Check the request log and try`
again.


-----

```
FolderId
IsLocked
MayEdit
Name
RequestLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the CRM Analytics application created by the auto-install request.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the auto-install request is locked or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the auto-install request can be edited or not.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the auto-install request, provided at creation by the user.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A log of the auto-install progress and completion results.


-----

```
 RequestStatus
 RequestType
 TemplateApiName
 TemplateVersion

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the auto-install request. Values can be `New,` `Enqueued,` `Cancelled,` `In`
```
  Progress, AppInProgress, Failed, and Success.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of auto-install request. Values can be `WaveEnable,`
```
  OrgCompatibilityCheck, WaveAppCreate, WaveAppUpdate,
  WaveAppDelete, and StartDataflow.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The API name of the CRM Analytics template to create the CRM Analytics app from.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The version of the CRM Analytics template to create the CRM Analytics app from.


Use this object to query and create auto-install requests for CRM Analytics applications in your org. This object is useful to troubleshoot
issues with templated applications that the automated process user creates.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WaveAutoInstallRequestChangeEvent (API version 62.0)**
Change events are available for the object.


-----
