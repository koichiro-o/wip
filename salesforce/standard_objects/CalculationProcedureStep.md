#### CalculationProcedureStep

Defines a step in an Expression Set. The label for this object is Expression Set Step. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Expression Sets requires OmniStudio licenses.

##### Fields

```
CalculationMatrixId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Decision Matrix this step calls. Applicable only if the `StepType` is
```
  MatrixLookupor GroupMatrixLookup.

```
This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup


-----

```
CalculationMatrixType
CalculationProcedure
CalculationProcedureVersionId
ConditionsConvertedText

```

**Refers To**
CalculationMatrix

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the Decision Matrix this step calls. Applicable only if this step calls a Decision
Matrix. If the `StepType` is `MatrixLookup, the value of this field is` `Standard. If the`
`StepType` is `GroupMatrixLookup, the value of this field is` `Grouped.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Expression Set to which this step belongs.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set Version to which this step belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedureVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression converted to postfix notation. Applicable only if the `StepType`
is `Condition.`


-----

```
ConditionsExpressionText
ConditionsUiFormattedText
Description
FormulaConvertedText
FormulaExpressionText
FormulaUiFormattedText

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression as the user entered it. Applicable only if the `StepType` is
```
  Condition.

```
**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression converted to JSON format for UI display. Applicable only if the
`StepType` is `Condition.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set Step.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression converted to postfix notation. Applicable only if the `StepType` is
```
  Calculation.

```
**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression as the user entered it. Applicable only if the `StepType` is
```
  Calculation.

```
**Type**
textarea


-----

```
InputVariablesFormatText
IsConditionalStep
IsResultIncluded
Name
OutputVariablesFormatText

```

**Properties**
Create, Nillable, Update

**Description**
The formula expression converted to JSON format for UI display. Applicable only if the
`StepType` is `Calculation.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of the input matrix columns or procedure variables applicable to the step.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that this step is conditional.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that the result of this step is included in the Expression Set output.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The step name.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
OutputVariablesMappingText
ReferenceProcedureId
ReturnMessageValueSet
Stage

```

**Description**
A list of the output matrix columns or procedure variables applicable to the step. Applicable
only if the `StepType` is `MatrixLookup,` `GroupMatrixLookup, or`
```
  ReferenceProcedure.

```
**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Maps Decision Matrix output variables to Expression Set variables. Applicable only if the
`StepType` is `MatrixLookupor` `GroupMatrixLookup.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the child Expression Set this step calls. Applicable only if the `StepType` is
```
  ReferenceProcedure.

```
This is a relationship field.

**Relationship Name**
ReferenceProcedure

**Relationship Type**
Lookup

**Refers To**
CalculationProcedure

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A set of messages to return based on the result of a step with a StepType of Condition.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The stage of Expression Set invocation. The `Aggregation` stage applies only to steps
with a `StepType` of `Aggregation.`


-----

```
StageStepSequence
StepType

```

Possible values are:

**•** `Aggregation`

**•** `Calculation`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sequence order of the step within the Expression Set. Used only for Expression Sets migrated
from a Salesforce Industries package. New Expression Sets use Expression Set Step Relationship
objects to order their steps.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of action this step performs.

Possible values are:

**•** `Aggregation—Returns an average, maximum, minimum, or sum of a list of values.`

**•** `Calculation—Performs a mathematical operation, which can include variables and`
constants.

**•** `Condition—Defines a condition that determines whether other steps are invoked.`

**•** `GroupMatrixLookup—Calls a Grouped Decision Matrix.`

**•** `MatrixLookup—Calls a Standard Decision Matrix.`

**•** `ReferenceProcedure—Calls a child Expression Set.`

