#### EnblProgramTaskMeasure

Represents the connection between an Enablement measure and a specific milestone or outcome in an Enablement program. This
object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

##### Fields

```
EnablementMeasureDefinitionId
EnblProgramTaskDefinitionId
SequenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Enablement measure to use with a milestone or outcome.

This field is a relationship field.

**Relationship Name**
EnablementMeasureDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementMeasureDefinition

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the outcome or milestone that uses the Enablement measure.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskDefinition

**Relationship Type**
Master-detail

**Refers To**
EnblProgramTaskDefinition (the master object)

**Type**
int


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
A number that specifies the order of the Enablement measure when multiple measures are
used with one outcome or milestone, starting at 0. For example, in a composite milestone
that uses the Percentage function, the measure that provides the numerator value is sequence
0 and the measure that provides the denominator value is sequence 1.
