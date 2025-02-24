#### CalculationProcedureVariable

Defines a variable in an Expression Set. The label for this object is Expression Set Variable. This object is available in API version 53.0 and
later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

##### Fields

```
ApiName
CalculationMatrixName
CalculationProcedureVersionId
DataType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of this variable.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Decision Matrix to which this variable belongs. Applicable only if this variable
references a Decision Matrix column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set Version to which this variable belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedureVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of this variable.


-----

```
DefaultValue
DisplayName
IsEditable
IsUserDefined
Name

```

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Number`

**•** `Percent`

**•** `Text`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default value of this variable.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user-readable name of this variable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, specifies that a variable is NOT auto-imported from a step that calls a Decision`
Matrix or a child Expression Set.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a variable is defined by the user.

The default value is `false.`

**Type**
string


-----

```
Precision
UiDisplayOrder

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this variable.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of decimal places. Applicable if the DataType is Currency, Number, or Percent.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The display order of the variable in the UI.

