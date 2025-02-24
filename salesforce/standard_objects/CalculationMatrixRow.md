#### CalculationMatrixRow

Defines a row in a Decision Matrix. The label for this object is Decision Matrix Row. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Decision Matrices requires OmniStudio licenses.

##### Fields

```
CalculationMatrixVersionId
EndDateTime

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Decision Matrix Version to which this row belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrixVersion

**Relationship Type**
Lookup

**Refers To**
CalculationMatrixVersion

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
InputData
IsVersionEnabled
Name
OutputData
StartDateTime

```

**Description**
The last date on which this row version is active. Applicable if `IsVersionEnabled` is
```
  true.

```
**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input columns and associated values for this row of the matrix.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the associated matrix version is active. Derived from the associated Decision
Matrix Version (CalculationMatrixVersion object).

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The row name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The output columns and associated values for this row of the matrix.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first date on which this row version is active. Applicable if `IsVersionEnabled` is
```
  true.

```

-----
