#### AccountPlanObjectiveMeasure

Represents the performance of target metrics for an objective associated with the account plan. This object is available in API version
62.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if sales account plans are turned on.

##### Fields


AccountPlanObjMeasCalcDefId


**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account plan objective calculation definition associated with the measure.

This field is a relationship field. Available in API version 63.0 and later.


-----

```
AccountPlanObjectiveId
CurrentCurrencyValue
CurrentNumberValue
CurrentPercentValue

```

**Relationship Name**
AccountPlanObjMeasCalcDef

**Refers To**
AccountPlanObjMeasCalcDef

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan objective associated with the measure.

This field is a relationship field.

**Relationship Name**
AccountPlanObjective

**Relationship Type**
Master-detail

**Refers To**
AccountPlanObjective

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The current value in currency for a measure associated with the account plan objective.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The current numerical value for a measure associated with the account plan objective.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The current value in percentage for a measure associated with the account plan objective.


-----

```
CurrentValue

```
CurrentValueTimestamp
```
LastReferencedDate
LastViewedDate
Name
TargetCurrencyValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current value for a measure associated with the account plan objective.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current value was last updated. This field is available in API version
63.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record. If this value is null, it’s possible
that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the account plan objective measure.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TargetNumberValue
TargetPercentValue
TargetValue
ValueType

##### Associated Objects

```

**Description**
The target value in currency for a measure associated with the account plan objective.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The target numerical value for a measure associated with the account plan objective.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The target value in percentage for a measure associated with the account plan objective.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The target value for a measure associated with the account plan objective.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of value that's measured.

Possible values are:

**•** `Currency`

**•** `Number`

**•** `Percent`


This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.


-----

**AccountPlanObjectiveMeasureChangeEvent on page 67**
Change events are available for the object.

**AccountPlanObjectiveMeasureHistory on page 62**
History is available for tracked fields of the object.
