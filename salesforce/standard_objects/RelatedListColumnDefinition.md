#### RelatedListColumnDefinition

Represents information about a column in a related list. A related list specifies a set of records for a related object, based on specific
criteria. This object is available in API version 55.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Alias
ColumnSoql
DataType
DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique alias of the column in the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SOQL query string used in a SELECT clause for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The field type of the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
FieldDefinitionId
IsDefault
IsDescribable
Label

```

**Description**
The unique identifier for the related list. Always retrieve this value before using it, as the value
can change from one release to the next. Simplify queries by using this field instead of making
multiple queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FieldDefinition associated with the column, if applicable.

This is a relationship field.

**Relationship Name**
FieldDefinition

**Relationship Type**
Lookup

**Refers To**
FieldDefinition

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the column appears on the related list by default `(true)` or not
```
  (false).

```
The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can appear in describeLayout call results (true)
or not `(false).`

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
LookupId
RelatedListDefinitionId

##### Usage

```

**Description**
The label for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lookup ID for the column.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the RelatedListDefinition that contains the column.

This is a relationship field.

**Relationship Name**
RelatedListDefinition

**Relationship Type**
Lookup

**Refers To**
RelatedListDefinition


**Find all available columns on a related list definition.**
```
  SELECT Alias, ColumnSoql, DurableId FROM RelatedListColumnDefinition WHERE
  RelatedListDefinitionId = 'Account.Opportunities'
