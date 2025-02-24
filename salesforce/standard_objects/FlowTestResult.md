#### FlowTestResult

```

**Type**
dateTime

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The scheduled time and date of the occurrence.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of flows that were stopped for this occurrence.


Represents the results for a flow test associated with a flow version. This object is available in API version 55.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To view test run details, you must have the View All Data user permission. You can view flow tests and test results without the View All
Data permission.

##### Fields

```
FlowDefinitionViewId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowDefinitionView


-----

```
FlowTestViewId
FlowVersionNumber
FlowVersionViewId

```

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow test associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowTestView

**Relationship Type**
Lookup

**Refers To**
FlowTestView

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number for the flow.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow version associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView


-----

```
Name
OwnerId
Result
TestEndDateTime
TestStartDateTime

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the flow test result.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns this test result.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the flow test result.

Possible values are:

**•** `Error`

**•** `Fail`

**•** `Pass`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow test ended.

**Type**
dateTime


-----

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow test started.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowTestResultShare**

Sharing is available for the object.
