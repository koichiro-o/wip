#### CalculationProcedureVersion

Defines a version of an Expression Set. The label for this object is Expression Set Version. This object is available in API version 53.0 and
later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Expression Sets requires OmniStudio licenses.


-----

##### Fields

**Field**
```
CalculationProcedureId
Constants
Description
EndDateTime
IsEnabled

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set to which this version belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedure

**Relationship Type**
Lookup

**Refers To**
CalculationProcedure

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A serialized JSON object containing information about each constant. This information
includes the name, data type, alias, and precision.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set Version.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this Expression Set Version is active.

**Type**
boolean


-----

```
IsLoopingEnabled
LastSimulatedVariablesInput
LoopEnd
LoopIncrement
LoopStart

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether this Expression Set Version is active.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether looping is enabled in this Expression Set Version.

The default value is `false.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input variables and results of the most recent simulation.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the end variable for looping.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the interval variable for looping.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the start variable for looping.


-----

```
Name
Rank
StartDateTime
VersionNumber
