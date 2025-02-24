#### ApexTestRunResult

Contains summary information about all the test methods that were run in a particular Apex job. This object is available in API version
37.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

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
Create, Filter, Group, Nillable, Sort, Update

**Description**

The parent Apex job ID for the result.

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup


-----

```
ClassesCompleted
ClassesEnqueued
EndTime
IsAllTests
JobName
MethodsCompleted

```

**Refers To**
AsyncApexJob

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The total number of classes executed during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The total number of classes enqueued during the test run.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The time at which the test run ended.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether all Apex test classes were run.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Reserved for future use.

**Type**
int


-----

```
MethodsEnqueued
MethodsFailed
Source
StartTime
Status

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods completed during the test run. This value is updated
after each class is run.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods enqueued for the test run. This value is initialized
before the test runs.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of methods that failed during this test run. This value is updated
after each class is run.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The source of the test run, such as the Developer Console.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**

The time at which the test run started.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
TestSetupTime
TestTime
UserId

```

**Description**

The status of the test run. Values include:

**•** Queued

**•** Preparing

**•** Processing

**•** Aborted

**•** Completed

**•** Failed

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the setup methods to run, in milliseconds.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The time it took the test to run, in milliseconds.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The user who ran the test run.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


-----
