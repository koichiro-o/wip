#### ApexTestResultLimits

Captures the Apex test limits used for a particular test method execution. An instance of this object is associated with each ApexTestResult
record. This object is available in API version 37.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

##### Fields

```
ApexTestResultId
AsyncCalls

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the associated ApexTestResult object.

This is a relationship field.

**Relationship Name**
ApexTestResult

**Relationship Type**
Lookup

**Refers To**
ApexTestResult

**Type**
int


-----

```
Callouts
Cpu
Dml
DmlRows
Email

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of asynchronous calls made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of callouts made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The amount of CPU used during the test run, in milliseconds.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of DML statements made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of rows accessed by DML statements during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of email invocations made during the test run.


-----

```
LimitContext
LimitExceptions
MobilePush
QueryRows
Soql
Sosl

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether the test run was synchronous or asynchronous.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether your org has any limits that differ from the default limits.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of mobile push calls made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of rows queried during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The number of SOQL queries made during the test run.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


-----

**Description**

The number of SOSL queries made during the test run.

##### Usage

The ApexTestResultLimits object is populated for each test method execution, and it captures the limits used between the Test.startTest()
and Test.stopTest() methods. If startTest() and stopTest() aren’t called, limits usage isn’t captured. Note the following:

**•** The associated test method must be run asynchronously.

**•** Limits for asynchronous Apex operations (batch, scheduled, future, and queueable) that are called within test methods aren’t
captured.

**•** Limits are captured only for the default namespace.
