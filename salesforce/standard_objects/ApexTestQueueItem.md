#### ApexTestQueueItem

Represents a single Apex class in the Apex job queue. This object is available in API version 23.0 and later.

This object is available in API version 23.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

##### Fields

```
ApexClassId
ExtendedStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The Apex class whose tests are to be executed.

This is a relationship field.

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Filter, Nillable, Sort


-----

```
ParentJobId
ShouldSkipCodeCoverage
Status

```

**Description**

The pass rate of the test run.

For example: “(4/6)”. This means that four out of a total of six tests passed.

If the class fails to execute, this field contains the cause of the failure.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Points to the AsyncApexJob that represents the entire test run.

If you insert multiple Apex test queue items in a single bulk operation, the queue
items share the same parent job. This means that a test run can consist of the
execution of the tests of several classes if all the test queue items are inserted in
the same bulk operation.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether to opt out of collecting code coverage information during
Apex test runs. Available in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the job. Valid values are:

**•** `Holding[1]`

**•** `Queued`

**•** `Preparing`

**•** `Processing`

**•** `Aborted`

**•** `Completed`

**•** `Failed`

1 This status applies to batch jobs in the Apex flex queue.


-----

```
TestRunResultId

##### Usage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the associated ApexTestRunResult object.


Insert an `ApexTestQueueItem` object to place its corresponding Apex class in the Apex job queue for execution. The Apex job
executes the test methods in the class.

To abort a class that is in the Apex job queue, perform an update operation on the ApexTestQueueItem object and set its `Status`
field to `Aborted.`

If you insert multiple Apex test queue items in a single bulk operation, the queue items share the same parent job. This means that a
test run can consist of the execution of the tests of several classes if all the test queue items are inserted in the same bulk operation.
