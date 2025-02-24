#### CalculationMatrixVersion

Defines a version of a Decision Matrix. The label for this object is Decision Matrix Version. This object is available in API version 53.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Decision Matrices requires OmniStudio licenses.

##### Fields

```
ApiName
CalculationMatrixId
DecisionMatrixDefinitionVerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the decision matrix version. This field is available in API version 56.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Decision Matrix to which this version belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

**Type**
reference


-----

```
DscnModelNoteExportStatus
EndDateTime
GroupKey

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The decision matrix definition version associated with this calculation matrix version.

This field is a relationship field.

**Relationship Name**
DecisionMatrixDefinitionVer

**Relationship Type**
Lookup

**Refers To**
DecisionMatrixDefinitionVersion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the export status of a decision matrix version in the Decision Model and Notation
(DMN) format.

Possible values are:

**•** `Initiated`

**•** `InProgress`

**•** `Complete`

**•** `Failed`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this matrix version is active.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A key for grouping matrix rows in different versions, such as geographic region or product
code. Derived from the associated Decision Matrix (CalculationMatrix object).


-----

```
GroupKeyValue
IsEnabled
LoadProcessStatus
MatrixType
Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the GroupKey for this version. For example, if the GroupKey is Country,
the `GroupKeyValue` can be `United States.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether this version is active.

The default value is `false.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of a data upload from a `.csv file.`

Possible values are:

**•** `Completed`

**•** `CompletedWithErrors`

**•** `Failed`

**•** `InProgress`

**•** `Pending`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The matrix type, either Standard or Grouped. A Grouped Decision Matrix groups rows
in different Decision Matrix Versions by one or two keys such as geographic region or product
code. Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string


-----

```
Rank
StartDateTime
SubGroupKey
SubGroupKeyValue
VersionNumber

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The matrix version name.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When the invocation time of a matrix call is between the `StartDateTime` and
`EndDateTime` of more than one enabled matrix version, the version with the highest
`Rank` is chosen.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first date on which this matrix version is active.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A subkey for grouping matrix rows in different versions, such as geographic region or product
code. For example, if the `GroupKey` is `Country, the` `SubGroupKey` can be `State`
```
  or Province. Derived from the associated Decision Matrix (CalculationMatrix object).

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `SubGroupKey` for this version. For example, if the `SubGroupKey` is
`State or Province, the` `SubGroupKeyValue` can be `California.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
The version number.
