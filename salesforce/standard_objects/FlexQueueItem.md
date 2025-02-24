#### FlexQueueItem

Represents an asynchronous Apex job in the Apex flex queue. Provides information about the job type and flex queue position of the
AsyncApexJob. This object is available in API version 36.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

##### Fields

```
AsyncApexJobId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of an AsyncApexJob that’s waiting in the flex queue.


-----

```
FlexQueueItemId
JobPosition
JobType

```

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary key for this FlexQueueItem.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The position in the flex queue of the waiting job. The highest-priority job in the
queue is at position 0.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of the job. Valid values are:

**•** `ApexToken`

**•** `BatchApex`

**•** `BatchApexWorker`

**•** `Future`

**•** `Queueable`

**•** `ScheduledApex`

**•** `SharingRecalculation`

**•** `TestRequest`

**•** `TestWorker`

Currently, queries are supported only on `BatchApex` jobs.


-----

##### Usage

To find the position of an AsyncApexJob in the flex queue, query `JobPosition. For example:`
```
SELECT JobPosition FROM FlexQueueItem WHERE JobType = 'BatchApex' AND AsyncApexJobId =
'707xx000000DABC'

```
To find the job at a given position, query `AsyncApexJobId. For example:`
```
SELECT AsyncApexJobId FROM FlexQueueItem WHERE JobType = 'BatchApex' AND JobPosition = '2'

```
To find all batch jobs in the flex queue, query `JobType. To get other information about the jobs, include AsyncApexJob in your query.`
For example:
```
SELECT JobType, JobPosition, AsyncApexJob.ApexClass.Name, AsyncApexJob.CreatedDate,
   AsyncApexJob.CreatedById FROM FlexQueueItem WHERE JobType='BatchApex' AND
   AsyncApexJob.ApexClass.Name LIKE '%BatchAJob%' ORDER BY JobPosition DESC
