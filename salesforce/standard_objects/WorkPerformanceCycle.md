#### WorkPerformanceCycle

Represents feedback that is gathered to assess the performance of a specific set of employees.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActivityFrom
ActivityTo
CurrentTask
LastManagerRequestsSharedDate
LastReferencedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date that you want to start filtering the WDC objects to help requesters create
accurate summaries. The start of the evaluation period.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date that you want to stop filtering the WDC objects to help requesters create
accurate summaries. The end of the evaluation period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The current task that the performance summary cycle is engaged in, including
deploying and sharing.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when all manager requests are set to be shared.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId
State

```

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkPerformanceCycle.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkPerformanceCycle. If this value is null, this record might have been only
referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the performance summary cycle that employees will participate in.
This name is created by the administrator and is visible on all respective
notifications and in the UI.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkPerformanceCycle.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state that the performance summary cycle is in. Available pick list values:

**•** Setup: The summary is in draft.

**•** In Progress: The summary is deployed and people are answering the questions
that were created.

**•** Finished: The summary is no longer in progress.

**•** Error: The summary encountered an error.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkPerformanceCycleFeed**

Feed tracking is available for the object.

**WorkPerformanceCycleHistory**

History is available for tracked fields of the object.

**WorkPerformanceCycleOwnerSharingRule**

Sharing rules are available for the object.

**WorkPerformanceCycleShare**

Sharing is available for the object.
