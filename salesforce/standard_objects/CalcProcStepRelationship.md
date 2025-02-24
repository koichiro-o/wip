#### CalcProcStepRelationship

Defines a parent-child relationship between two Expression Set Steps in an Expression Set Version. The label for this object is Expression
Set Step Relationship. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Parent-child step relationships collectively determine the step order.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Expression Sets requires OmniStudio licenses.

##### Fields

```
CalcProcStepId
CalcProcVersionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the child Expression Set Step.

This is a relationship field.

**Relationship Name**
CalcProcStep

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureStep

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related Expression Set Version.

This is a relationship field.


-----

```
Name
ParentCalcProcStepId
RelationshipType

```

**Relationship Name**
CalcProcVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Expression Set Step Relationship name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent Expression Set Step.

This is a relationship field.

**Relationship Name**
ParentCalcProcStep

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureStep

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of relationship between the parent and child steps.

Possible values are:

**•** `Bypass—The parent is a condition step. If the condition is false, the child is the next`
step.

**•** `ParentChild—The child is the next step after the parent.`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalcProcStepRelationshipFeed on page 54**
Feed tracking is available for the object.

**CalcProcStepRelationshipHistory on page 62**
History is available for tracked fields of the object.
