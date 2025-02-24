#### FlowInterview

Represents a flow interview. A flow interview is a running instance of a flow. This object is available in API version 32.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To delete a flow interview, you must have the “Manage Flow” user permission. All other calls require the “Run Flows” user permission or
the `Flow User field enabled on the user detail page. If Override default behavior and restrict access to enabled profiles or`
**permission sets is selected for an individual flow, access to that specific flow and its interviews is given to users by profile or permission**
set.

##### Fields

```
CurrentElement

```

**Type**
string


-----

```
FlowVersionViewId
Guid
InterviewLabel
InterviewStatus

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow element at which the interview is paused.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
This field is a relationship field. This field is available in API version 51.0 and later.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Globally unique identifier for the interview.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Label for the interview. This label helps users and administrators differentiate
interviews from the same flow.

In the user interface, this label appears in the Paused Flow Interviews component
on the user’s Home tab and in the list of paused flow interviews in Setup.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the interview. Valid values are:


-----

```
Name
OwnerId
PauseLabel

```


**•** `Completed—This flow is complete. There are no more records to process.`

**•** `Error—This flow has one or more errors. To resolve each error, check the`
error code for instructions.

**•** `Paused—This flow is paused. No new processes are added until the flow`
is resumed.

**•** `Running—This flow is running or is ready to run.`

**•** `VersionPaused—This flow version is paused. No more records are`
processed until the flow is resumed. This value is available in API version 60.0
and later.

This field is available in API version 50.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the interview.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the interview. Only this user or an admin can resume
the interview.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Information about why the interview was paused. This string is entered by the
user who paused the flow interview. The label is Why Paused.


-----

```
WasPausedFromScreen

##### Associated Objects

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the flow interview was paused by a user from a flow Screen element
(true ) or not (false ). This field is available in API version 46.0 and later.


This object has these associated objects. Unless noted, these objects are available in the same API version as this object.

**FlowInterviewOwnerSharingRule**

Sharing rules are available for the object.

**FlowInterviewShare**

Sharing is available for the object.
