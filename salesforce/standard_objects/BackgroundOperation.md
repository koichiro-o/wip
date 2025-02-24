#### BackgroundOperation

Represents a background operation in an asynchronous job queue. This object is available in API version 35.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), retrieve()

 Special Access Rules

```
**•** BackgroundOperation doesn’t support search.

##### Fields

```
Error

```

**Type**
string


-----

```
ExecutionGroup
ExpiresAt
FinishedAt
GroupLeaderId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message for the operation. Applies only if the operation has an error
status.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Identifies the execution group.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
After this time, the operation is removed from the asynchronous job queue.
Applies only if the operation has a status of complete, canceled, error, or merged.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the operation reached the status of completed or error.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Identifies the operation that’s selected as the
leader of the execution group.

This is a relationship field.

**Relationship Name**
GroupLeader

**Relationship Type**
Lookup


-----

```
Name
NumFollowers
ParentKey
ProcessAfter
RetryBackoff

```

**Refers To**
BackgroundOperation

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Identifies the background operation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation is merged with other operations into an execution
group to be processed in bulk. Number of other operations that are in the
execution group.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Tag that identifies related sets of operations, if any.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The operation is scheduled to be processed after this time.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only if the operation has an error status. The first retry is attempted
immediately. Each subsequent retry is increasingly delayed according to an
exponential expression that’s multiplied by the RetryBackoff, in milliseconds.


-----

```
RetryCount
RetryLimit
SequenceGroup
SequenceNumber

```

Specifically, the delay time is (2[n]-1)×R, where `n` is the RetryCount, and
`R` is the RetryBackoff.

The default value for `RetryBackoff depends on the type of operation. For`
example, the RetryBackoff default for write operations on external objects
is 1,000 milliseconds. For write operations, retries are attempted immediately,
after 3 seconds, after 7 seconds, after 15 seconds, and so on.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Number of attempted retries. Applies only if the operation has an error status.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Maximum number of retries to attempt. Applies only if the operation has an error
status.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence group. Applies only if the operation is merged with other
operations into an execution group to be processed in bulk. Within an execution
group, operations can be placed into a sequence group to be executed in a
specific order.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Order position within the sequence group. Applies only if the operation is merged
with other operations into an execution group to be processed in bulk. Within
an execution group, operations can be placed into a sequence group to be
executed in a specific order.


-----

```
StartedAt
Status
SubmittedAt
Timeout
Type

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

When the operation started running.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the background operation. The options are:

**•** `New`

**•** `Scheduled`

**•** `Canceled`

**•** `Merged`

**•** `Waiting`

**•** `Running`

**•** `Error`

**•** `Complete`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
When the operation was added to the job queue.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Maximum time in milliseconds to wait for results after the operation started
running.

**Type**
picklist


-----

```
WorkerUri

##### Usage

```
The BackgroundOperation object lets you:


**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the background operation. The options are:

**•** `BlockchainEventPoller`

**•** `CdpMetadataDeploy`

**•** `ExternalChangeDataCapture`

**•** `ExternalConnectivityPoller—Reserved for future use.`

**•** `ExternalObject`

**•** `ExternalObjectSync`

**•** `ExternalServiceCallback`

**•** `SiteTaskCreate`

**•** `SiteTaskPublish`

**•** `Sweeper`

**•** `WebCart`

**•** `XClean`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
URI of the worker that performed the operation.

Example for a Salesforce Connect OData operation:



**•** Monitor the job status of asynchronous operations.

**•** View errors that are related to the asynchronous operations.

**•** Extract statistics for the asynchronous job queue.
