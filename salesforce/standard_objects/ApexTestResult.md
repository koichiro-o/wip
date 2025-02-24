#### ApexTestResult

Represents the result of an Apex test method execution. This object is available in API version 23.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

##### Fields

```
ApexClassId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The Apex class whose test methods were executed.

This is a relationship field.


-----

```
ApexLogId
ApexTestRunResultId
AsyncApexJobId

```

**Relationship Name**
ApexClass

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the ApexLog for this test method execution if debug logging is enabled;
otherwise, `null.`

This is a relationship field.

**Relationship Name**
ApexLog

**Relationship Type**
Lookup

**Refers To**
ApexLog

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the ApexTestRunResult that represents the entire test run.

This is a relationship field.

**Relationship Name**
ApexTestRunResult

**Relationship Type**
Lookup

**Refers To**
ApexTestRunResult

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
IsTestSetup
Message
MethodName
Outcome

```

**Description**

Points to the AsyncApexJob that represents the entire test run.

This field points to the same object as
```
  ApexTestQueueItem.ParentJobId.

```
This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates if the results are for a test setup method. The default is false.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The exception error message if a test failure occurs; otherwise, `null.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The test method name.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The result of the test method execution. Can be one of these values:


-----

```
QueueItemId
RunTime
StackTrace
TestTimestamp

```


**•** Pass

**•** Fail

**•** CompileFail

**•** Skip

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Points to the ApexTestQueueItem which is the class that this test method is part
of.

This is a relationship field.

**Relationship Name**
QueueItem

**Relationship Type**
Lookup

**Refers To**
ApexTestQueueItem

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the test method to run, in milliseconds.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The Apex stack trace if the test failed; otherwise, `null.`

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**

The start time of the test method.


-----

##### Usage

You can query the fields of the `ApexTestResult` record that corresponds to a test method executed as part of an Apex class
execution.

Each test method execution is represented by a single `ApexTestResult` record. For example, if an Apex test class contains six test
methods, six `ApexTestResult` records are created. These records are in addition to the `ApexTestQueueItem` record that
represents the Apex class.

Each ApexTestResult record has an associated ApexTestResultLimits on page 651 record, which captures the Apex limits used during
execution of the test method.
