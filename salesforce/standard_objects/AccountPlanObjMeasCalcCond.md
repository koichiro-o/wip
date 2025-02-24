#### AccountPlanObjMeasCalcCond

Represents a field and value combination for filtering records to include in the calculation of a sales account plan objective measure’s
current value. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is available if sales account plans are turned on.

##### Fields

```
AccountPlanObjMeasCalcDefId
FieldName

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan objective measure calculation definition where this criteria is used.

This field is a relationship field.

**Relationship Name**
AccountPlanObjMeasCalcDef

**Relationship Type**
Master-detail

**Refers To**
AccountPlanObjMeasCalcDef

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A field on the calculation definition’s TargetObject that you want to filter by. Fields on
the Campaign, Case, Contact, or Opportunity objects are supported.


-----

```
Operation
Value

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The logical operator for matching records with the specified field value.

Possible values are:

**•** `Contains`

**•** `Equals`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`

**•** `NotContain`

**•** `NotEqual`

**•** `StartsWith`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value to match for the specified field.


Let’s say that a calculation definition tracks the currency amount on Closed Won opportunities. The calculation definition’s
`TargetObject` is `Opportunity, and the condition further specifies these values.`

**•** `FieldName` is `StageName.`

**•** `Operation` is `Equals.`

**•** `Value` is `ClosedWon.`
