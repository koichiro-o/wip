#### CalculationMatrixColumn

Defines a column in a Decision Matrix. The label for this object is Decision Matrix Column. This object is available in API version 53.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Decision Matrices requires OmniStudio licenses.


-----

##### Fields

**Field**
```
ApiName
CalculationMatrixId
ColumnType
DataType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Decision Matrix to which this column belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the column matches matrix input or is returned as output.

Possible values are:

**•** `Input`

**•** `Output`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data in the column.

Possible values are:


-----

```
DisplaySequence
IsWildcardColumn
Name
RangeValues
WildcardColumnValue

```


**•** `Boolean`

**•** `Currency`

**•** `Number`

**•** `NumberRange`

**•** `Percent`

**•** `Text`

**•** `TextRange`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The position of this column in the column order.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that this column can contain a wildcard value such as `ALL.`

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The column name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of values that define range boundaries.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
The value that indicates a wildcard, for example ALL. Applicable if IsWildcardColumn
is `true.`
