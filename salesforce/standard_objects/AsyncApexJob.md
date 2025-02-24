#### AsyncApexJob

Represents an individual Apex sharing recalculation job, a batch Apex job, a method with the `future` annotation, or a job that
implements `Queueable` or `Schedulable. Use this object to query Apex batch jobs in your organization.`

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
If Apex isn’t running in system mode, users must have the View Setup and Configuration permission to access this object and to enqueue
asynchronous Apex jobs.

##### Fields

```
ApexClassId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex class executing the job. Label is `Class ID.`

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass


-----

```
CompletedDate
CronTriggerId
ExtendedStatus
JobItemsProcessed
JobType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the job was completed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CronTrigger for the AsyncApexJob. This field only applies to ScheduledApex
job type. This field is available in API version 53.0 and later. For scheduled jobs created before
version 53.0, this field is populated on subsequent execution.

This is a relationship field.

**Relationship Name**
CronTrigger

**Relationship Type**
Lookup

**Refers To**
CronTrigger

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If one or more errors occurred during the batch processing, this field contains a short
description of the first error. A more detailed description of that error, along with any
subsequent errors, is emailed to the last user who modified the batch class. This field is
available in API version 19.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of job items processed. Label is `Batches Processed.`

**Type**
picklist


-----

```
LastProcessed
LastProcessedOffset
MethodName
NumberOfErrors

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of job being processed. Valid values are:

**•** `ApexToken`

**•** `BatchApex`

**•** `BatchApexWorker`

**•** `Future`

**•** `Queueable`

**•** `ScheduledApex`

**•** `SharingRecalculation`

**•** `TestRequest`

**•** `TestWorker`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Last ID that was processed and committed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Offset of the last ID that was processed and committed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Apex method being executed. Label is `Apex Method.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ParentJobId
Status
TotalJobItems

##### Usage

```

**Description**
Total number of batches with a failure. A batch is considered transactional, so any unhandled
exceptions constitute an entire failure of the batch. Label is `Failures.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
For batch Apex jobs that run using chunking implementation, multiple child jobs of type
`BatchApexWorker` are created. Each of these child job records contains the job Id of
the parent Apex job that started their execution. For batch Apex jobs that run using a
non-chunking implementation, child jobs aren’t created.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the job. Valid values are:

**•** `Aborted`

**•** `Completed`

**•** `Failed`

**•** `Holding[1]`

**•** `Preparing`

**•** `Processing`

**•** `Queued`

1 This status applies to batch jobs in the Apex flex queue.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of batches processed. Each batch contains a set of records. Label is `Total`
```
  Batches.

```

Use this object to query Apex batch jobs in your organization.


-----
