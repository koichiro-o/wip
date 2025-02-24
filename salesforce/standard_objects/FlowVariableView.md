#### FlowVariableView

Represents a variable within the flow version. This object is available in API version 46.0 and later.

##### Supported Calls
```
describeSObjects(), query()

```
|StageLabel|StageType|StageOrder|
|---|---|---|
|Review Cart|Active|0|
|Shipping Details|Active|1|
|Billing Details|Active|2|
|Payment Details|Active|3|
|Order Confirmation|Active|4|
|Shipping Details|Current|1|


-----

##### Fields

**Field**
```
ApiName
DataType
Description
DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow variable.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data type of the flow variable. Valid values are:

**•** `Apex—This value is available in API version 46.0 and later.`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime—This value is available in API version 30.0 and later.`

**•** `Number`

**•** `Multipicklist—This value is available in API version 34.0 and later.`

**•** `Picklist—This value is available in API version 34.0 and later.`

**•** `String`

**•** `sObject`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow variable information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Id of the flow variable.


-----

```
FlowVersionViewId
IsCollection
IsInput
IsOutput
ObjectType

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The Id of the flow version.

This is a relationship field.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether or not the flow variable is a collection of values.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicated whether or not the flow variable is available for input.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether or not the flow variable is available for output.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the data type is sObject, this field indicates which object.


-----

##### Usage

Use this object to query information about flow variables. A query must be filtered by `FlowVersionViewId` to get results. Only
variables with IsInput or IsOutput marked as true are visible.
